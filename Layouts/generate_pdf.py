#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:07:25 2021

@author: andre
"""
from Layouts.keys_names.keys_to_registration import *

from reportlab.pdfgen import canvas
import shutil
import os

import pandas as pd

import PySimpleGUI as sg

DEFAULT_KEY_BTN_GENERATE_PDF = '<<-GERAR_PDF->>'
DEFAULT_KEY_BTN_EXPORT_FILE = '<<-EXPORTAR_ARQUIVO->>'
DEFAULT_KEY_BTN_SAVE_IN = '<<-SALVAR_EM->>'

DEFAULT_KEY_GENERATED_PDF_FILE = '<<-ARQUIVO_PDF_GERADO->>'
DEFAULT_KEY_PATH_TO_SAVE_PDF = '<<-CAMINHO_PARA_SALVAR_PDF->>'

DEFAULT_KEY_INPUT_EXPORT_FILE_EXCEL = 'EXPORTAR_ARQUIVO_EXCEL'
DEFAULT_KEY_BTN_EXPORT_FILE_EXCEL = 'BTN_EXPORTAR_ARQUIVO_EXCEL'

class Tags:
    def __init__(self):
        
        self.path = 'database/files_pdf_excel'
        
        self.name_file = 'tags_para_cadastro'
        self.path_file = 'database/files_pdf_excel/' + self.name_file + '.pdf'
        
        self.name_file_excel = 'database_keys'
        self.path_file_excel = 'database/files_pdf_excel/' + self.name_file_excel + '.xlsx'
        
        self.space = '<<space>>'
        self.list_tags = {
        '1-': 'DADOS PESSOAIS',
        'Nome':DEFAULT_KEY_NOME_PERSONAL_DATA,
        'Sexo':DEFAULT_KEY_SEX_PERSONAL_DATA,
        'Data de Nascimento':DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA,
        'Idade':DEFAULT_KEY_AGE_PERSONAL_DATA,
        'Naturalidade':DEFAULT_KEY_NATURALNESS_PERSONAL_DATA,
        'UF':DEFAULT_KEY_UF_PERSONAL_DATA,
        'Telefone':DEFAULT_KEY_TEL_PERSONAL_DATA,
        'Celular':DEFAULT_KEY_CEL_PERSONAL_DATA,
        'Email':DEFAULT_KEY_EMAIL_PERSONAL_DATA,
        'Endereço':DEFAULT_KEY_ADDRESS_PERSONAL_DATA,
        'Bairro':DEFAULT_KEY_DISTRICT_PERSONAL_DATA ,
        'Numero do estabelecimento':DEFAULT_KEY_HOUSE_NUMBER_PERSONAL_DATA,
        'RG':DEFAULT_KEY_RG_PERSONAL_DATA,
        'Orgão emissor':DEFAULT_KEY_ISSUING_BODY_PERSONAL_DATA,
        'CPF':DEFAULT_KEY_CPF_PERSONAL_DATA,
        'Possui CNH':DEFAULT_KEY_CNH_PERSONAL_DATA,
        'Titulo eleitoral':DEFAULT_KEY_VOTER_TITLE_PERSONAL_DATA,
        'Considera-se':DEFAULT_KEY_CONSIDER_PERSONAL_DATA,
        'Estado Civil':DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA,
        'Escolaridade':DEFAULT_KEY_SCHOOLING_PERSONAL_DATA,
        
        #-----------------------------keys batch to be regularized--------------------#

        '2':self.space,
        '2-': 'DADOS PARA REGULARIZAÇÃO DO LOTE',
        'Lote': DEFAULT_KEY_BATCH_REGU_BATCH,
        'Quadra': DEFAULT_KEY_BATCH_REGU_BLOCK,
        'Bairro':DEFAULT_KEY_BATCH_REGU_BATCH_REGULARIZAR_DISTRICT,
        'Área':DEFAULT_KEY_BATCH_REGU_AREA,
        'Rua':DEFAULT_KEY_BATCH_REGU_STREET_LOTE,
        
        '3':self.space,
        '3-': 'DADOS DO CÔNJUGE',
        'Nome Conjuge': DEFAULT_KEY_NAME_SPOUSE,
        'Sexo Conjuge': DEFAULT_KEY_SEX_SPOUSE,
        'Data de Nascimento Conjuge': DEFAULT_KEY_BIRTHDATE_SPOUSE,
        'Idade Conjuge': DEFAULT_KEY_AGE_SPOUSE,
        'Naturalidade Conjuge': DEFAULT_KEY_NATURALNESS_SPOUSE,
        'Telefone Conjuge':DEFAULT_KEY_TEL_SPOUSE,
        'Celular Conjuge': DEFAULT_KEY_CEL_SPOUSE,
        'RG Conjuge':DEFAULT_KEY_RG_SPOUSE,
        'Orgão Emissor Conjuge':DEFAULT_KEY_ISSUING_BODY_SPOUSE,
        'CPF Conjuge':DEFAULT_KEY_CPF_SPOUSE,
        'CNH Conjuge':DEFAULT_KEY_CNH_SPOUSE,
        'Titulo de eleitor Conjuge':DEFAULT_KEY_VOTER_TITLE_SPOUSE,
        'Escolaridade Conjuge':DEFAULT_KEY_SCHOOLING_SPOUSE,
        'Regime de União':DEFAULT_KEY_UNION_REGIME,
        
        #-------------------------KEY to tab other_information----------------------
        '4':self.space,
        '4-': 'OUTRAS INFORMAÇÕES',
        'Trabalha':DEFAULT_KEY_COMB_WORKS,
        'Onde Trabalha':DEFAULT_KEY_INP_WHERE,
        'Profissão':DEFAULT_KEY_TXT_PROFESSION,
        'É aposentado':DEFAULT_KEY_COMB_RETIREE,
        'Beneficiario de algum programa social':DEFAULT_KEY_BENEF_CAMB_SOCI_PROG,
        'Renda':DEFAULT_KEY_INCOME_COMB_INCOME,
        'Tem Filhos':DEFAULT_KEY_COMB_HAVE_CHILDREM,
        'Quantos Filhos':DEFAULT_KEY_HOW_MANY_CHILDREM,
        'Mora algum deficiente ou idoso':DEFAULT_KEY_LIVES_DISABLED_OR_ELDERLY,
        'Quantos deficentes ou idosos':DEFAULT_KEY_DISABLED_ELDERLY_HOW_MANY,
        'Possui outro Imóvel Rural':DEFAULT_KEY_COMB_OWN_RURAL_PROPERTY,
        
        'Tem Automovel':DEFAULT_KEY__COMB_OWNS_CAR,
        'Quantos Automoveis':DEFAULT_KEY_OWNS_CAR_HOW_MANY,
        'Tem Moto':DEFAULT_KEY__COMB_HAS_MOTORCICLE,
        'Quantas Motos':DEFAULT_KEY_HAS_MOTORCICLE_HOW_MANY,
        'Tem geladeira':DEFAULT_KEY_COMB__HAVE_FRIDGE,
        'Quantas Geladeiras':DEFAULT_KEY_HAVE_FRIDGE_HOW_MANY,
        'Tem televisão':DEFAULT_KEY_COMB__HAVE_TELEVI,
        'Quantas Televisões':DEFAULT_KEY_HAVE_TELEVI_HOW_MANY,
        'Tem Computador':DEFAULT_KEY_COMB__HAVE_COMPUTER,
        'Quantos Computadores':DEFAULT_KEY_HAVE_COMPUTER_HOW_MANY,
        'Tem Acesso a Internet':DEFAULT_KEY_COMB__HAVE_INTERNET,
        'Tem Energia Eletrica':DEFAULT_KEY_COMB__HAVE_ACESS_ELECTRI,
        'Tem Água Encanada':DEFAULT_KEY_COMB__HAVE_DRAINAG_WATER,
        
        '5':self.space,
        '4.1-': 'CONDIÇÕES DO IMÓVEL',
        'Tem Outro Dono':DEFAULT_KEY_COMB_ONLY_OWNER,
        'Nome do Outro Dono': DEFAULT_KEY_TXT_ANOTHER_OWNER,
        'O imóvel é quitado': DEFAULT_KEY_TXT_PROPERTY_IS_PAID_OFF,
        'A quanto tempo Possui o Imóvel':DEFAULT_KEY_TXT_HOW_LONG_HAS_THE_PROPERTY,
        'Possui Outro Imóvel Urbano':DEFAULT_KEY_COMB_HAVE_ANOTHER_URBAN_PROPERTY,    
        'Quanto Tempo Possui o Imóvel Urbano':DEFAULT_KEY_ANOTHER_PROPERTY_HOW_MANY,
        'Onde Possui o Imóvel Urbano':DEFAULT_KEY_TXT_ANOTHER_PROPERTY_WHERE,
        'Tem Edificação no Imóvel':DEFAULT_KEY_COMB_REAL_ESTATE_CONSTRUC,
        'Utiliza o Imóvel Para':DEFAULT_KEY_PROPERTY_USED_FOR,
        
        '6':self.space,
        '4.2-': 'CONFRONTANTES DO IMÓVEL, Vizinhos, Nº',
        'Frente':DEFAULT_KEY_TXT_FRONT,
        'Direita':DEFAULT_KEY_TXT_RIGHT,
        'Esquerda':DEFAULT_KEY_TXT_LEFT,
        'Fundos':DEFAULT_KEY_TXT_FUNDS,
        
        'Tipo do Imóvel':DEFAULT_KEY_COMB_TYPE,
        'É Murada':DEFAULT_KEY_COMB_IS_WALLED,
        'Posição no Lote':DEFAULT_KEY_COMB_BATCH_POSITION,
        'Estado das Edificações':DEFAULT_KEY_COMB_STATE_BUILDINGS,
        'Tipo de Construção':DEFAULT_KEY_COMB_BUILDING_TYPE,
        'Tem Acabamento':DEFAULT_KEY_COMB_IS_BEDRIDDEN,
        'Numero de Pavimentos':DEFAULT_KEY_NUMB_FLOORS,
        'Cômodos':DEFAULT_KEY_ROOMS,
        'Banheiros':DEFAULT_KEY_BATHROOMS,
        
        '7':self.space,
        'COLOCAR NO CABEÇALHO DA TABELA DE CADASTRO DE MORADORES':DEFAULT_KEY_TABLE_RESIDENTS,
        'Renda Familiar total':DEFAULT_KEY_TXT_FAMILY_INCOME_REGIST_RESID,
        '8':self.space,
        'Projetos/Serviçõs':DEFAULT_KEY_PROJECT_SERVICES,
        'Tipo de Enquadramento (REURB-S/E)':DEFAULT_KEY_TYPE_FRAMEWORK,
        }
        
    def get_list_gats(self):
        return self.list_tags

class Generate_pdf:
    def __init__(self):
        self.__tags = Tags()
        self.__path_to_save = None
        
    def layout(self):
        menu = [
                [sg.T('Arquivo pdf gerado:'), sg.Input(size=25, key=DEFAULT_KEY_GENERATED_PDF_FILE)],
                [sg.Button('Gerar pdf', key=DEFAULT_KEY_BTN_GENERATE_PDF)],
                [sg.HorizontalSeparator()],
                [sg.T('Caminho'),sg.Input(size=25, key=DEFAULT_KEY_PATH_TO_SAVE_PDF, disabled=True), sg.Button('Salva em', key=DEFAULT_KEY_BTN_SAVE_IN)],
                [sg.Button('Exportar arquivo', key=DEFAULT_KEY_BTN_EXPORT_FILE, disabled=True)],
                [sg.HorizontalSeparator()],
                [sg.T('Caminho'),sg.Input(size=25, key=DEFAULT_KEY_INPUT_EXPORT_FILE_EXCEL, disabled=True)],
                [sg.Button('Exportar arq. excel', key=DEFAULT_KEY_BTN_EXPORT_FILE_EXCEL, disabled=True)]
            ]
        
        layout = [
                 [sg.Frame('Gerar pdf com tags do cadastro de clientes', menu)]
            ]
        return layout
    
    def checke_file_existance(self, path):
        try:
            with open(path, 'r') as f:
                return True
        except FileNotFoundError as e:
            return False
        except IOError as e:
            return False

    def GeneratePDF(self, list_tags):
        path_file = self.__tags.path_file
        
        try:
            nome_pdf = self.__tags.name_file
            pdf = canvas.Canvas(path_file)
            #pdf.setTitle(nome_pdf)
            pdf.setFont("Helvetica-Oblique", 14)
            pdf.drawString(170,750, 'Lista de tags para')
            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(245,724, 'Cadastro Socioeconômico')
            pdf.setFont("Helvetica-Oblique", 12)
            
            x = 720
            for key,value in list_tags.items():
                x -= 20
                if x <= 80:
                    pdf.showPage()
                    x = 720
                
                if value == self.__tags.space:
                    pdf.drawString(40,x, ' ')
                else:
                    pdf.drawString(40,x, '{} : {}'.format(key,value))
                
            
            pdf.save()
            
            sg.popup('{}.pdf criado com sucesso!'.format(nome_pdf))
        except:
            sg.popup_error('ERRO!\nErro ao gerar {}.pdf'.format(nome_pdf))
    
    '''def generateExcel(self):
        
        data_new = []
        
        for key in key_fields_spouse():
            data_new.append(key)
        
        for key in keys_fields():
            data_new.append(key)
        data_new.append(DEFAULT_KEY_TABLE_RESIDENTS)
        data_new.append(DEFAULT_KEY_TABLE_RESIDENTS)
        data_new.append(DEFAULT_KEY_TXT_FAMILY_INCOME_REGIST_RESID)
        data_new.append(DEFAULT_KEY_PROJECT_SERVICES)
        data_new.append(DEFAULT_KEY_TYPE_FRAMEWORK)
        
        if len(data_new) > 0:
            df = pd.DataFrame(columns=data_new)
            
            save_file = self.path
            save_file += '/' +self.name_file_excel  +'.ods'

            #Save file .xlsx
            writer = pd.ExcelWriter(save_file)
            df.to_excel(writer, sheet_name='teste', index=False)
            writer.save()'''
    
    def event_elements(self, window, event, value):
        if event == DEFAULT_KEY_BTN_GENERATE_PDF:
            self.GeneratePDF(self.__tags.list_tags)
            
            if self.checke_file_existance(self.__tags.path_file):
                window.Element(DEFAULT_KEY_GENERATED_PDF_FILE).update(self.__tags.name_file)
        if event == DEFAULT_KEY_BTN_SAVE_IN:
            self.__path_to_save = sg.tk.filedialog.askdirectory(initialdir=os.path.abspath(os.sep))
            
            if self.__path_to_save != None and self.__path_to_save != '':
                window.Element(DEFAULT_KEY_PATH_TO_SAVE_PDF).update(self.__path_to_save)
        
        if event == DEFAULT_KEY_BTN_EXPORT_FILE:
            if value[DEFAULT_KEY_PATH_TO_SAVE_PDF] != '':
                shutil.copy(self.__tags.path_file, value[DEFAULT_KEY_PATH_TO_SAVE_PDF])
                
        if self.checke_file_existance(self.__tags.path_file):
            window.Element(DEFAULT_KEY_BTN_GENERATE_PDF).update(disabled=True)
            window.Element(DEFAULT_KEY_GENERATED_PDF_FILE).update(self.__tags.name_file)
            
        if value[DEFAULT_KEY_PATH_TO_SAVE_PDF] != '':
            window.Element(DEFAULT_KEY_BTN_EXPORT_FILE).update(disabled=False)     
            window.Element(DEFAULT_KEY_BTN_EXPORT_FILE_EXCEL).update(disabled=False)
                
        if self.checke_file_existance(self.__tags.path_file_excel):
            abspath_arq = os.path.abspath(self.__tags.path_file_excel)
            window.Element(DEFAULT_KEY_INPUT_EXPORT_FILE_EXCEL).update(abspath_arq)
                
        if event == DEFAULT_KEY_BTN_EXPORT_FILE_EXCEL:
            shutil.copy(self.__tags.path_file_excel, value[DEFAULT_KEY_PATH_TO_SAVE_PDF])
            
    def exec_class(self):
        window = sg.Window('PDF para tags', self.layout(), icon=r'image/iconLogo.ico', modal=True)
            
        while(True):
            event, value = window.read(timeout=100)
            
            if event == sg.WINDOW_CLOSED:
                break
            
            self.event_elements(window, event, value) 
            
        window.close()
