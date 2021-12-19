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
from collections import defaultdict

import openpyxl
from string import ascii_uppercase

from Layouts.registration import Get_projects

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
            [sg.Button('Gerar planilha', key=DEFAULT_KEY_BTN_EXPORT)]
            ]
        return layout
    
    def get_datas(self, value):
        name_db_people = self.__conn.register_people
        name_db_spouse = self.__conn.register_spouse
        
        columns = ['NOME', 'ENQUADRAMENTO','RENDA R$',
                   'IMÓVEL  RURAL', 
                   'LOTE', 'QUADRA', 'BAIRRO DO IMOVÉL', 
                   'RUA', 'NÚMERO', 'BAIRRO', 
                   'CPF /CNPJ','RG', 'ORGÃO EMISSOR', 
                   'TITULO DE ELEITOR', 'IDADE', 'PROFISÃO',
                   'ESTADO  CIVIL', 'FILHOS', 'ESCOLARIDADE', 
                   
                   'NOME DO CONJUGE', 'CPF - CONJUGE', 'RG - CONJUGE',
                   'TITULO DE ELEITOR - CONJUGE','REGIME DE UNIÃO']
        
        fields_db = ['name', 'type_reurb', 'income_between', 'has_rural_property', 
                     'num_bach_regu', 'num_block_regu', 'district_regu', 'address', 
                     'address_number', 'district', 'cpf', 'rg', 'issuing_agency', 
                     'voter_title', 'age', 'profession', 'marital_status', 'how_many_children', 'schooling', 'name_spouse', 'cpf_spouse','rg_spouse', 'issuing_agency_spouse', 'union_regime_spouse']
        
        

        dict_datas = defaultdict(list)

        value_project = value[DEFAULT_KEY_PROJECT]
        value_framework = value[DEFAULT_KEY_FRAMEWORK]
        if value_project == 'Todos' and value_framework == 'Todos':
            busca = name_db_people  +", " + name_db_spouse+ " WHERE (" + name_db_people + '.id_register_people = ' + name_db_spouse + '.id_to_register_people OR ' + name_db_spouse + '.id_to_register_people IS NOT NULL)'
        else:
            value_project = self.__get_projects.get_id(value[DEFAULT_KEY_PROJECT])
            print(value_project)
            busca = name_db_people  +", " + name_db_spouse+ " WHERE (" + name_db_people + '.id_register_people = ' + name_db_spouse + '.id_to_register_people AND ' + name_db_people+'.id_to_projects_service = '+ value_project +' OR ' + name_db_spouse + '.id_to_register_people IS NOT NULL)'
            
        datas_regist = self.__conn.select_register(fields_db, busca)
        
        print(datas_regist)
        
        new_datas = []
        stato = 'Casado'
        for cont, val in enumerate(datas_regist):
            new = []
            if val[16] !=  stato:
                for cont in range(len(val)):   
                    if cont > 18:
                        new.append(None)
                    else:
                        new.append(val[cont])
            else:
                for elem in val:
                    new.append(elem)
            new_datas.append(new)
            
        
        #print(new_datas)
        
        
        df = pd.DataFrame(new_datas, columns=columns)
        
        dict_save = value[DEFAULT_KEY_PATH_TO_EXPORT]
        dict_save += '/' +value[DEFAULT_KEY_NAME_FILE_TO_EXPORT] +'.xlsx'
        
        writer = pd.ExcelWriter(dict_save)
        df.to_excel(writer, sheet_name='teste', index=False)
        writer.save()
        
        wb = openpyxl.load_workbook(filename = dict_save)        
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
                    
        wb.save(dict_save)
        
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
                self.get_datas(value)
                
        window.close()