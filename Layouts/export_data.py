#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 12:30:07 2021

@author: andre
"""

import PySimpleGUI as sg
import pandas as pd
import numpy as np
import os
import time
from collections import defaultdict

import openpyxl
from string import ascii_uppercase

from Layouts.registration import Get_projects
import re
from decimal import Decimal
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

import threading

DEFAULT_KEY_PROJECT = '<<BUSCA_POR_PROJETO>>'
DEFAULT_KEY_FRAMEWORK = '<<ENQUADRAMENTO_PARA_EXPORTAR>>'
DEFAULT_KEY_PATH_TO_EXPORT = '<<EXPORTAR_PARA_O_CAMINHO>>'
DEFAULT_KEY_NAME_FILE_TO_EXPORT = '<<NOME_DO_ARQUIVO_PARA_EXPORTAR>>'

DEFAULT_KEY_SEARCH_THE_WAY_TO_EXPORT = '<<BTN_BUSCAR_CAMINHO_PARA_EXPORTAR>>'
DEFAULT_KEY_BTN_EXPORT = '<<EXPORTAR_PLANILHA>>'

class Export_data:
    def __init__(self, database):
        self.__conn = database
        self.__get_projects = Get_projects(database)
        self.list_datas_projetcs = None
        
    def layout(self):
        
        self.list_datas_projetcs = np.array(self.__get_projects.get_list())  
        list_project = ['Todos']
        for val in self.list_datas_projetcs[:,1].tolist():
            list_project.append(val)
            
        menu = [
                [sg.T('Projetos'), sg.Combo(list_project, key=DEFAULT_KEY_PROJECT, readonly=True), sg.T('Enquadramento'), sg.Combo(['Todos','REURB-S', 'REURB-E'], key=DEFAULT_KEY_FRAMEWORK, readonly=True)],
                [sg.T('Caminho para salvar'), sg.Input(size=20, disabled=True, key=DEFAULT_KEY_PATH_TO_EXPORT), sg.Button('Busca pasta', key=DEFAULT_KEY_SEARCH_THE_WAY_TO_EXPORT)],
                [sg.T('Nome do arquivo'), sg.Input(size=15, key=DEFAULT_KEY_NAME_FILE_TO_EXPORT), sg.T('.xlsx')]
            ]
        layout = [
            [sg.Frame('Gerar planilha excel de todos os dados', menu)],
            [sg.Button('Gerar planilha', key=DEFAULT_KEY_BTN_EXPORT, disabled=True)],
            [sg.ProgressBar(1, orientation='h', size=(20,20), key='progress'), sg.T('', key='SAVE_PLANILHA')]
            ]
        return layout
    
    def event_disable(self,window, btn_export):
        window.Element(DEFAULT_KEY_BTN_EXPORT).update(disabled=btn_export)
    
    def format_income(self, income):
        total_income = 0
        try:
            total_income = income.replace('.', '')
            total_income = float(re.sub('([^0-9].[^0-9]{1,2})', '',total_income.replace(',','.')))
        except Exception as err:
            total_income = -1
            sg.popup_error('ERRO para inserir a renda familiar\n' + str(err))
        return total_income
            
    
    def get_income_residents(self,name_db_people, name_db_residents, list_data):
        '''
        search for income and create a new list of records
        '''
        fields_db_residents = 'income'
        datas_regist_new = []
        
        if list_data != '':
            for rows in list_data: 
                new_elements = []
                for cont, elem in enumerate(rows):
                    new_elements.append(elem)
                    if cont == 9:#index for the list cpf 
                    
                        sql = name_db_people + " WHERE cpf = '" + elem + "'"
                        register = self.__conn.select_register([self.__conn.id_register_people, 'income_between'], sql)
                        
                        '''
                        if there is an income in the personal record, start the data_income_residents with it
                        '''
                        if register[0][1] != None:
                            datas_income_residents = self.format_income(register[0][1])
                        else:
                            datas_income_residents = 0
                        
                        if len(register) != 0:
                            #search current record id
                            sql = name_db_residents + " WHERE " + self.__conn.name_id_to_table_register + ' = ' + str(register[0][0])

                            #search all income values
                            incomes_residents = self.__conn.select_register([fields_db_residents], sql)
                            
                            if incomes_residents != '':
                                for values in incomes_residents:
                                    income = self.format_income(values[0])
                                    if income != -1:
                                        datas_income_residents += income
                                    else:
                                        break
                                    
                                datas_income_residents = Decimal(datas_income_residents)
                                datas_income_residents = locale.currency(datas_income_residents, grouping=True)
                                
                            new_elements.append(datas_income_residents)
                            
            datas_regist_new.append(new_elements)
        return datas_regist_new
    
    def get_datas(self,window, value):
        progress_bar = window.Element('progress')

        name_db_people = self.__conn.register_people
        name_db_spouse = self.__conn.register_spouse
        name_db_residents = self.__conn.register_residents
        
        spouse = ['NOME DO CONJUGE', 'CPF - CONJUGE', 'RG - CONJUGE',
                   'TITULO DE ELEITOR - CONJUGE','REGIME DE UNIÃO']
        
        columns = ['NOME', 'ENQUADRAMENTO',
                   'IMÓVEL  RURAL', 
                   'LOTE', 'QUADRA', 'BAIRRO DO IMOVÉL', 
                   'RUA', 'NÚMERO', 'BAIRRO', 
                   'CPF /CNPJ','RENDA R$','RG', 'ORGÃO EMISSOR', 
                   'TITULO DE ELEITOR', 'IDADE', 'PROFISÃO',
                   'ESTADO  CIVIL', 'FILHOS', 'ESCOLARIDADE'
                   ]
        for i in spouse:
            columns.append(i)
        
        fields_db = ['name', 'type_reurb', 'has_rural_property', 
                     'num_bach_regu', 'num_block_regu', 'district_regu', 'address', 
                     'address_number', 'district', 'cpf', 'rg', 'issuing_agency', 
                     'voter_title', 'age', 'profession', 'marital_status', 'how_many_children', 'schooling', 'name_spouse', 'cpf_spouse','rg_spouse', 'issuing_agency_spouse', 'union_regime_spouse']
        
        value_project = value[DEFAULT_KEY_PROJECT]
        value_framework = value[DEFAULT_KEY_FRAMEWORK]
        
        if value_project == 'Todos' and value_framework == 'Todos':
            search_all = name_db_people  +", " + name_db_spouse+ " WHERE (" + name_db_people + '.id_register_people = ' + name_db_spouse + '.id_to_register_people)'
            
            search_singles = name_db_people +" WHERE marital_status <> 'Casado'"
            
            datas_regist_singles = self.__conn.select_register(fields_db[0:18], search_singles)
            datas_regist_all = self.__conn.select_register(fields_db, search_all)
            
        else:
            if value_project == 'Todos':
                search_all = name_db_people + ", " + name_db_spouse + " WHERE (" + name_db_people + '.id_register_people = ' + name_db_spouse + '.id_to_register_people) AND '+ \
                    name_db_people + ".type_reurb = '" + value_framework+"'"
                
                search_singles = name_db_people +" WHERE marital_status <> 'Casado' " + ' AND '+name_db_people + ".type_reurb = '" + value_framework+"'"
                
            elif value_framework == 'Todos':
                value_project = self.__get_projects.get_id(value[DEFAULT_KEY_PROJECT])
                search_all = name_db_people + ", " + name_db_spouse + " WHERE (" + name_db_people + '.id_register_people = ' + name_db_spouse + '.id_to_register_people) AND ' + \
                    name_db_people+'.id_to_projects_service = ' + str(value_project)
                
                search_singles = name_db_people +" WHERE marital_status <> 'Casado' AND "+name_db_people+'.id_to_projects_service =' + str(value_project)
            else:
                value_project = self.__get_projects.get_id(value[DEFAULT_KEY_PROJECT])
                
                search_all = name_db_people + ", " + name_db_spouse + " WHERE (" + name_db_people + '.id_register_people = ' + name_db_spouse + '.id_to_register_people) AND ' + \
                    name_db_people+'.id_to_projects_service = ' + \
                    str(value_project) + ' AND '+name_db_people + ".type_reurb = '" + value_framework+"'"
                
                search_singles = name_db_people +" WHERE marital_status <> 'Casado' AND " +name_db_people+'.id_to_projects_service = ' + str(value_project) + ' AND '+name_db_people + ".type_reurb = '" + value_framework+"'"
                
            datas_regist_all = self.__conn.select_register(fields_db, search_all)
            datas_regist_singles = self.__conn.select_register(fields_db[0:18], search_singles)

        '''
        search for income and create a new list of records to datas_regist_new
        '''
        datas_regist_new = self.get_income_residents(name_db_people, name_db_residents, datas_regist_all)
        
        '''
        search for income and create a new list of records to datas_regist_singles
        '''
        datas_regist_singles = self.get_income_residents(name_db_people, name_db_residents, datas_regist_singles)

        progress_bar.UpdateBar(0,4)
        time.sleep(.5)
        
        new_datas = []
        if datas_regist_new != '':
            for rows in datas_regist_new:
                new_datas.append(rows)
                
        progress_bar.UpdateBar(1,4)
        time.sleep(.5)
        
        if datas_regist_singles != '':
            for rows in datas_regist_singles:
                new = []
                for elem in rows:
                    new.append(elem)
                    
                for cont in range(len(spouse)):
                    new.append(None)
                new_datas.append(new)
                
        progress_bar.UpdateBar(2,4)
        time.sleep(.5)  
        
        if len(new_datas) > 0:
            df = pd.DataFrame(new_datas, columns=columns)
            
            save_file = value[DEFAULT_KEY_PATH_TO_EXPORT]
            save_file += '/' +value[DEFAULT_KEY_NAME_FILE_TO_EXPORT] +'.xlsx'

            #Save file .xlsx
            writer = pd.ExcelWriter(save_file)
            df.to_excel(writer, sheet_name='teste', index=False)
            writer.save()
            
            progress_bar.UpdateBar(3,4)
            time.sleep(.5)
            
            #open file.xlsx to increase column size
            wb = openpyxl.load_workbook(filename = save_file)        
            worksheet = wb.active
            
            letas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            cont = 0
            for column in ascii_uppercase:
                    if cont < len(columns):
                        if columns[cont] == 'NOME':
                            size = 20
                        elif columns[cont] == 'RUA':
                            size = 15
                        elif columns[cont] == 'RG':
                            size = 10
                        else:
                            size = len(columns[cont])
                            
                        if (column==letas[cont]):
                            worksheet.column_dimensions[column].width = size*2
                    cont+= 1
            #save file with enlarged column 
            wb.save(save_file)
            progress_bar.UpdateBar(4,4)
            time.sleep(.5)
            
            window.Element('SAVE_PLANILHA').update('Registro salvo!',text_color='white')
        else:
            window.Element('SAVE_PLANILHA').update('Registro não foi encontrato',text_color='red')
        
    def exec_class(self):
        window = sg.Window('Gerar planilha', self.layout(), icon=r'image/iconLogo.ico', modal=True)
        
        while(True):
            event, value = window.read(timeout=100)
            
            if event == sg.WINDOW_CLOSED:
                break

            if event == DEFAULT_KEY_SEARCH_THE_WAY_TO_EXPORT:
                save_in_directory = sg.tk.filedialog.askdirectory(initialdir=os.path.abspath(os.sep))
                window.Element(DEFAULT_KEY_PATH_TO_EXPORT).update(save_in_directory)
            if event == DEFAULT_KEY_BTN_EXPORT:
                try:
                    self.get_datas(window,value)
                except Exception as inst:
                    sg.popup_error('ERRO!\n'+ str(inst.args))
            if value[DEFAULT_KEY_PROJECT] != '' and value[DEFAULT_KEY_FRAMEWORK] and value[DEFAULT_KEY_PATH_TO_EXPORT] != '' and value[DEFAULT_KEY_NAME_FILE_TO_EXPORT] != '':
                self.event_disable(window,False)
            else:
                self.event_disable(window,True)
                
        window.close()
