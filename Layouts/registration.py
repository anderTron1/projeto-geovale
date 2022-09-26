#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 13:57:29 2021

@author: André Luiz Pires Guimarães
"""


import PySimpleGUI as sg
import numpy as np

import re

from elementsAdditional import ElementsAdditional
from Layouts.search_register_person import Search_register_person
from Layouts.keys_names.keys_to_registration import *

import time

from decimal import Decimal
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

#--------------------------key to buttons personal data-------------------
DEFAULT_KEY_BTN_NEW = '-BUTTONNEW-'
DEFAULT_KEY_BTN_CANCEL = '-BUTONCANCEL-'
DEFAULT_KEY_BTN_SAVE = '-BUTTONSAVE-'
DEFAULT_KEY_BTN_EDIT = '-BUTTONEDIT-'
DEFAULT_KEY_BTN_DELETE = '-BUTTONDELETE-'

#--------------------------key to buttons registration selection------------------------
DEFAULT_KEY_BTN_SEARCH = '-BUTTONSEARCH-'

#--------------------------key buttons registration residents-------------------
DEFAULT_KEY_BTN_NEW_REGIST_RESID = '-BTN_NOVO_CADASTRO_MORADORES-'
DEFAULT_KEY_BTN_CANCEL_REGIST_RESID = '-BTN_CANCELAR_CADASTRO_MORADORES-'
DEFAULT_KEY_BTN_SAVE_REGIST_RESID = '-BTN_SALVAR_CADASTRO_MORADORES-'
DEFAULT_KEY_BTN_EDIT_REGIST_RESID = '-BTN_EDITAR_CADASTRO_MORADORES-'
DEFAULT_KEY_BTN_DEL_REGIST_RESID = '-BTN_EXCLUIR_CADASTRO_MORADORES-'
DEFAULT_BTN_VALIDATE_INCOME = '-VALIDATE_INCOME-'

DEFAULT_KEY_BTN_UPDATE_TYPE = '<<BTN_ATUALIZAR_TIPO_REURB>>'

def rangeArray(init, size):
    return [num for num in range(init, size)]

class Get_projects:
    def __init__(self, database):
        self.__conn = database
        self.__name_db = database.projects_service
        self.__id_of_db = database.id_projects_service
        
        self.__datas_db = self.get_list_db()
        
    def get_list_db(self):
        return self.__conn.select_all(self.__name_db)
    
    def get_list(self):
        return self.__datas_db
    
    def get_id(self, name_projet):
        register = self.__datas_db 
        id_table = None
        #self.__list_datas_projetcs[:,1].tolist()
        
        for datas in register:
            if datas[1] == name_projet:
                id_table = datas[0]
                break
            
        return id_table
    
    def get_name(self, id):
        register = self.__datas_db 
        name_project = None
        #self.__list_datas_projetcs[:,1].tolist()
        
        for datas in register:
            if datas[0] == id:
                name_project = datas[1]
                break
            
        return name_project
                
#############################################################################
#                                                                           #
#                           FIST RECORD TAB class                           #
#                                                                           #
#############################################################################
class register_personal_data:
    
    def __init__(self, database):
        self.__conn = database
        self._marital_status = 'Casado'
        self._cohabitant = 'Amasiado/Convivente'
        self.elemAdditional = ElementsAdditional()
        self.datas_register_residents_new = []
        self.datas_register_residents = []
        self.datas_register_residents_edit = []
        
        self.table_index_deleted = []
        
        self.projetcs = None
        self.list_datas_projetcs = None
        
        
    def load_window_layout(self):
        
        self.projetcs = Get_projects(self.__conn)
        self.list_datas_projetcs = np.array(self.projetcs.get_list())        
        
        listEstadoCivil = [self._marital_status, 'Solteiro', 'Divorciado', self._cohabitant, 'Viúvo']
        
        schooling_list = ['Não Alfabetizado', 'Ensino Fundamental Incompleto', 'Ensino Fundamental Completo', 'Ensino Médio Incompleto', 
                                     'Ensino Médio Completo', 'Ensino Técnico', 'Ensino Superior']
        
        spouse_frame = [
            [sg.T('Nome:',size=(5)), sg.Input(size=(60,1), key=DEFAULT_KEY_NAME_SPOUSE)],
            [sg.Text('Sexo:',size=(5)), sg.Combo(['F', 'M'], key=DEFAULT_KEY_SEX_SPOUSE, readonly=True),
             sg.Text('Data de Nascimento:'), sg.Input(size=(12,1), key=DEFAULT_KEY_BIRTHDATE_SPOUSE), sg.Text('Idade'), sg.Spin(rangeArray(0, 120), initial_value='', key=DEFAULT_KEY_AGE_SPOUSE),
             sg.T('Naturalidade:'), sg.Input(size=(20,1), key=DEFAULT_KEY_NATURALNESS_SPOUSE)],
            [sg.T('Tel.:', size=(10, 1)), sg.Input(size=(20,1), key=DEFAULT_KEY_TEL_SPOUSE), 
             sg.T('Cel.:'), sg.Input(size=(20,1),  key=DEFAULT_KEY_CEL_SPOUSE)],
            [sg.T('RG:', size=(10, 1)), sg.Input(size=(15,1),  key=DEFAULT_KEY_RG_SPOUSE), sg.T('órgão Emissor:'), sg.Input(size=(5,1), key=DEFAULT_KEY_ISSUING_BODY_SPOUSE), 
             sg.T('CPF:',), sg.Input(size=(15,1), key=DEFAULT_KEY_CPF_SPOUSE),
             sg.T('CNH'), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_CNH_SPOUSE, readonly=True)],
            [sg.T('Titulo de Eleitor:', size=(18)), sg.Input(size=(20,1), key=DEFAULT_KEY_VOTER_TITLE_SPOUSE), sg.T('Renda:'),sg.Input(size=(15,1), key=DEFAULT_KEY_INCOME_SPOUSE), sg.T('Profissão:'), sg.Input(size=(25,1), key=DEFAULT_KEY_PROFESSION_SPOUSE)],
            [sg.T('Escolaridade:', size=(18)), sg.Combo(['Não Alfabetizado', 'Ensino Fundamental Incompleto', 'Ensino Fundamental Completo', 'Ensino Médio Incompleto', 
                                             'Ensino Médio Completo', 'Ensino Técnico', 'Ensino Superior'], key=DEFAULT_KEY_SCHOOLING_SPOUSE, readonly=True),
             sg.T('Regime de União'), sg.Combo(['Comunhão parcial de bens','Comunhão Universal de Bens','Separação de bens', 'Participação final nos Aquestos'],key=DEFAULT_KEY_UNION_REGIME, readonly=True)]   
            ]
        
        batch_to_be_regularized = [
            [sg.T('Lote nº:', size=15), sg.Input(size=(10,1), k=DEFAULT_KEY_BATCH_REGU_BATCH, disabled=True), sg.T('Quadra nº:', size=20), sg.Input(size=(10,1), k=DEFAULT_KEY_BATCH_REGU_BLOCK, disabled=True)],
            [sg.T('Bairro:', size=15), sg.Input(size=(20,1), k=DEFAULT_KEY_BATCH_REGU_BATCH_REGULARIZAR_DISTRICT, disabled=True), sg.T('Área (m²):', size=10), sg.Input(size=(15,1), k=DEFAULT_KEY_BATCH_REGU_AREA, disabled=True)],
            [sg.T('Rua do Lote:', size=15), sg.Input(size=(20,1), k=DEFAULT_KEY_BATCH_REGU_STREET_LOTE, disabled=True)]
        ]
        
        personal_data_tab = [
            [sg.Text('Nome:',size=(5)), sg.Input(size=(60,1), disabled=True, key=DEFAULT_KEY_NOME_PERSONAL_DATA),
             sg.Text('Sexo:',size=(5)), sg.Combo(['F', 'M'], key=DEFAULT_KEY_SEX_PERSONAL_DATA, readonly=True),
             sg.Text('Data de Nascimento:'), sg.Input(size=(12,1), disabled=True, key=DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA)], 
            [sg.Text('Idade',size=(5)), sg.Spin(rangeArray(0, 120),initial_value='', disabled=True, key=DEFAULT_KEY_AGE_PERSONAL_DATA),
             sg.Text('Naturalidade'), sg.Input(size=(30,1), disabled=True,key=DEFAULT_KEY_NATURALNESS_PERSONAL_DATA), sg.Text('UF:'), sg.Input(size=(15,1), disabled=True, key=DEFAULT_KEY_UF_PERSONAL_DATA)],
            [sg.Text('Tel.:',size=(5)), sg.Input(size=(20,1), disabled=True,key=DEFAULT_KEY_TEL_PERSONAL_DATA), 
             sg.Text('Cel.:',size=(5)), sg.Input(size=(20,1), disabled=True,key=DEFAULT_KEY_CEL_PERSONAL_DATA)],
            [sg.HorizontalSeparator()],
            [sg.Text('Email:', size=(10)), sg.Input(size=(40,1), disabled=True,key=DEFAULT_KEY_EMAIL_PERSONAL_DATA)],
            [sg.Text('Cidade', size=(10)), sg.Input(size=40, key= DEFAULT_KEY_CITY, disabled=True), sg.T('Estado'), sg.Input(size=25, key=DEFAULT_KEY_STATE, disabled=True), 
             sg.T('CEP'), sg.Input(size=10, key=DEFAULT_KEY_CEP, disabled=True)],
            [sg.Text('Endereço:', size=(10)), sg.Input(size=(40,1), disabled=True,key=DEFAULT_KEY_ADDRESS_PERSONAL_DATA),
             sg.Text('Bairro:'), sg.Input(size=(40,1), disabled=True,key=DEFAULT_KEY_DISTRICT_PERSONAL_DATA), sg.Text('Nº:'), sg.Input(size=(5,), disabled=True, key=DEFAULT_KEY_HOUSE_NUMBER_PERSONAL_DATA)],
            [sg.Text('RG:', size=(10)), sg.Input(size=(15,1), disabled=True,key=DEFAULT_KEY_RG_PERSONAL_DATA), sg.Text('Órgão Emissor:'), sg.Input(size=(5,1), disabled=True, key=DEFAULT_KEY_ISSUING_BODY_PERSONAL_DATA), 
             sg.Text('CPF:', size=(10)), sg.Input(size=(15,1), disabled=True,key=DEFAULT_KEY_CPF_PERSONAL_DATA),
             sg.Text('CNH:', size=(10)), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_CNH_PERSONAL_DATA, readonly=True)], 
            [sg.Text('Titulo de Eleitor:'), sg.Input(size=(20,1), disabled=True, key=DEFAULT_KEY_VOTER_TITLE_PERSONAL_DATA),
             sg.T('Considera-se'),sg.Combo(['Branco','Negro', 'Pardo', 'Amarelo', 'Indígena'], key=DEFAULT_KEY_CONSIDER_PERSONAL_DATA, readonly=True), sg.T('Estado Civil:'), 
             sg.Combo(listEstadoCivil, key=DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA, readonly=True)],
            [sg.T('Escolaridade', size=(18)), sg.Combo(schooling_list, key=DEFAULT_KEY_SCHOOLING_PERSONAL_DATA, readonly=True)],
            [sg.Frame('Dados do Cônjuge', spouse_frame)],
            [sg.Frame('Lote a regularizar', batch_to_be_regularized)]
            ]

        frameConfImovel = [
            [sg.T('Frente:', size=(10)), sg.Input(size=(25,1), disabled=True,  key=DEFAULT_KEY_TXT_FRONT),
             sg.T('Direita:', size=(10)), sg.Input(size=(25,1), disabled=True,  key=DEFAULT_KEY_TXT_RIGHT)],
            [sg.T('Esquerda:', size=(10)), sg.Input(size=(25,1), disabled=True,  key=DEFAULT_KEY_TXT_LEFT),
             sg.T('Fundos:', size=(10)), sg.Input(size=(25,1), disabled=True,  key=DEFAULT_KEY_TXT_FUNDS)],
            ]

        frameCondImoveis = [
            [sg.T('Tem outro dono?', size=(32)), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_COMB_ONLY_OWNER, readonly=True), sg.T('Nome do outro Dono:'), sg.Input(size=(25,1), disabled=True,  key=DEFAULT_KEY_TXT_ANOTHER_OWNER)],
            [sg.T('O imóvel é quitado?'),sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_TXT_PROPERTY_IS_PAID_OFF, readonly=True), sg.T('A quanto tempo possui o Imóvel?'), sg.Input(size=(15,1), disabled=True,  key=DEFAULT_KEY_TXT_HOW_LONG_HAS_THE_PROPERTY)],
            [sg.T('Possui Outro Imóvel Urbano?', size=(32)), sg.Combo([KEY_YES, KEY_NOT],  key=DEFAULT_KEY_COMB_HAVE_ANOTHER_URBAN_PROPERTY, readonly=True), sg.T('Quantos?'), 
             sg.Spin(rangeArray(0, 11), disabled=True,  key=DEFAULT_KEY_ANOTHER_PROPERTY_HOW_MANY, initial_value=(''), readonly=True), sg.T('Onde?'), sg.Input(size=(20,1), disabled=True,  key=DEFAULT_KEY_TXT_ANOTHER_PROPERTY_WHERE)],
            [sg.T('Tem Edificação no Imóvel?', size=(32)), sg.Combo([KEY_YES, KEY_NOT],  key=DEFAULT_KEY_COMB_REAL_ESTATE_CONSTRUC, readonly=True), sg.T('Utiliza o imóvel para:'), 
             sg.Combo(['Moradia', 'Comércio'], key=DEFAULT_KEY_PROPERTY_USED_FOR, readonly=True)],
            [sg.Frame('Confrontantes do imóvel, Vizinhos, Nº:', frameConfImovel)],
            
            [sg.T('Tipo do Imóvel:', size=(25)), sg.Combo(['Casa', 'Sobrado', 'Apartamento', 'Ponto de comércio'], key=DEFAULT_KEY_COMB_TYPE, readonly=True), 
             sg.T('É murado?', size=(11)), sg.Combo([KEY_YES, KEY_NOT],   key=DEFAULT_KEY_COMB_IS_WALLED, readonly=True),
             sg.T('Posição no lote:'), sg.Combo(['Frente', 'Fundos', 'Centro'],  key=DEFAULT_KEY_COMB_BATCH_POSITION, readonly=True)], 
            [sg.T('Estado das edificações:', size=(25)), sg.Combo(['Muito bom', 'Bom', 'Regular', 'Ruim', 'Péssimo'],  key=DEFAULT_KEY_COMB_STATE_BUILDINGS, readonly=True),
             sg.T('Tipo de construção:', size=(19)), sg.Combo(['Alvenaria', 'Madeira', 'Estuque', 'Mista', 'Outros'], key=DEFAULT_KEY_COMB_BUILDING_TYPE, readonly=True)], 
            [sg.T('Tem Acabamento?', size=(25)), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_COMB_IS_BEDRIDDEN, readonly=True),
             sg.T('Numero de pavimentos?', size=(25)), sg.Spin(rangeArray(0, 11), initial_value='', disabled=True, key=DEFAULT_KEY_NUMB_FLOORS, readonly=True),
             sg.T('Cômodos?'),sg.Spin(rangeArray(0, 11),  initial_value='', disabled=True, key=DEFAULT_KEY_ROOMS, readonly=True),sg.T('e Banheiros?'), sg.Spin(rangeArray(0, 11), initial_value='', disabled=True, key=DEFAULT_KEY_BATHROOMS, readonly=True)]
            ]

        tab_other_infor = [
            [sg.T('Trabalha?'), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_COMB_WORKS, readonly=True),sg.T('Onde:'), sg.Input(size=(25,1), disabled=True,  key=DEFAULT_KEY_INP_WHERE),
             sg.T('Profissão:'), sg.Input(size=(25,1), disabled=True,   key=DEFAULT_KEY_TXT_PROFESSION), sg.T('É aposentado?'), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_COMB_RETIREE, readonly=True)],
            [sg.T('Beneficiário de algum programa social?'), sg.Combo([KEY_YES, KEY_NOT],  key=DEFAULT_KEY_BENEF_CAMB_SOCI_PROG, readonly=True),
             sg.T('Renda:'), sg.Input(size=(15,1),  key=DEFAULT_KEY_INCOME_COMB_INCOME),
             sg.T('Tem Filhos?'), sg.Combo([KEY_YES, KEY_NOT],  key=DEFAULT_KEY_COMB_HAVE_CHILDREM, readonly=True), 
             sg.T('Quantos?'), sg.Spin(values=(rangeArray(0,20)), disabled=True, key=DEFAULT_KEY_HOW_MANY_CHILDREM, initial_value=(''), readonly=True)],
            [sg.T('Mora Algum deficiente ou idoso?', size=(38)), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_LIVES_DISABLED_OR_ELDERLY, readonly=True), 
             sg.T('Quantos?'), sg.Spin(values=(rangeArray(0,10)), disabled=True,  key=DEFAULT_KEY_DISABLED_ELDERLY_HOW_MANY, initial_value='', readonly=True)],
            [sg.T('Possui imóvel rural?'), sg.Combo([KEY_YES, KEY_NOT],  key=DEFAULT_KEY_COMB_OWN_RURAL_PROPERTY, readonly=True)],
            [sg.HorizontalSeparator()],
            
            [sg.T('Possui Automóvel?', size=(30)), sg.Combo([KEY_YES, KEY_NOT],   key=DEFAULT_KEY__COMB_OWNS_CAR, readonly=True), sg.T('Quantas?'),sg.Spin(rangeArray(0,11), disabled=True,  key=DEFAULT_KEY_OWNS_CAR_HOW_MANY, initial_value=(''), readonly=True),
             sg.T('Possui Motos?', size=(25)), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY__COMB_HAS_MOTORCICLE, readonly=True), sg.T('Quantas?'),sg.Spin(rangeArray(0,11), disabled=True,  key=DEFAULT_KEY_HAS_MOTORCICLE_HOW_MANY, initial_value=(''), readonly=True)],
            
            [sg.T('Tem Geladeira em casa?', size=(30)), sg.Combo([KEY_YES, KEY_NOT],  key=DEFAULT_KEY_COMB__HAVE_FRIDGE, readonly=True), sg.T('Quantas?'), 
             sg.Spin(rangeArray(0,11), disabled=True,  key=DEFAULT_KEY_HAVE_FRIDGE_HOW_MANY, initial_value=(''), readonly=True),
             sg.T('Tem Televisão em casa?', size=(25)), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_COMB__HAVE_TELEVI, readonly=True), sg.T('Quantas?'), 
             sg.Spin(rangeArray(0, 11), disabled=True, key=DEFAULT_KEY_HAVE_TELEVI_HOW_MANY, initial_value=(''), readonly=True)],
            [sg.T('Tem Computador em casa?', size=(30)), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_COMB__HAVE_COMPUTER, readonly=True), sg.T('Quantos?'), 
             sg.Spin(rangeArray(0, 11), disabled=True, key=DEFAULT_KEY_HAVE_COMPUTER_HOW_MANY, initial_value=(''), readonly=True),
             sg.T('Tem acesso a internet?', size=(25)), sg.Combo([KEY_YES, KEY_NOT],  key=DEFAULT_KEY_COMB__HAVE_INTERNET, readonly=True)],
            [sg.T('Tem acesso a Energia Elétrica?', size=(30)), sg.Combo(['Sim', 'Não'],  key=DEFAULT_KEY_COMB__HAVE_ACESS_ELECTRI, readonly=True),
             sg.T('Tem acesso a Água Encanada?'), sg.Combo([KEY_YES, KEY_NOT],  key=DEFAULT_KEY_COMB__HAVE_DRAINAG_WATER, readonly=True)],
            [sg.Frame('Condições do Imóvel', frameCondImoveis)],
            [sg.T('Projetos/serviços'), sg.Combo(self.list_datas_projetcs[:,1].tolist(), key=DEFAULT_KEY_PROJECT_SERVICES, readonly=True)]
            ]
        
        
        headings = ['id','Nome:', 'Paren.', 'Idade', 'Sexo', 'Est. Civil', 'Ocupação', 'Renda']
        table = self.elemAdditional.Table(sg, headings, DEFAULT_KEY_TABLE_RESIDENTS, col_width=12)
        tab_residents = [
            [sg.Frame('Informações', [
                [sg.T('ID:', size=(15,1)), sg.Input(size=(20,1), key=DEFAULT_KEY_INPUT_ID_REGIST_RESID, disabled=True)],
                [sg.T('Nome:', size=(15,1)), sg.Input(size=(25,1), disabled=True, key=DEFAULT_KEY_TXT_NOME_REGIST_RESID)],
                [sg.T('Parentesco',size=(15,1)), sg.Input(size=(20,1),disabled=True, key=DEFAULT_KEY_SPIN_KINSHIP_REGIST_RESID), sg.T('Sexo'), 
                 sg.Combo(['M', 'F'], disabled=True, key=DEFAULT_KEY_COMB_SEX_REGIST_RESID, readonly=True), sg.T('Idade'), sg.Spin(rangeArray(0, 120), disabled=True,initial_value='', key=DEFAULT_KEY_SPIN_AGE, readonly=True)],
                [sg.T('Estado Civil:', size=(15,1)),sg.Combo(['Casado', 'Solteiro', 'Divorciado', 'Amasiado/Convivente', 'Viúvo'], disabled=True,  key=DEFAULT_KEY_COMB_MARITAL_STATUS_REGIST_RESID, readonly=True)],
                [sg.T('Ocupação:', size=(15,1)), sg.Input(size=(20,1),disabled=True, key=DEFAULT_KEY_TXT_OCCUPATION_REGIST_RESID)],
                [sg.T('Renda:', size=(15,1)), sg.Input(size=(15,1), disabled=True, key=DEFAULT_KEY_TXT_INCOME_REGIST_RESID), sg.Button('Validar', disabled=True, key=DEFAULT_BTN_VALIDATE_INCOME)],
                [sg.Button('Novo', disabled=True, key=DEFAULT_KEY_BTN_NEW_REGIST_RESID), sg.Button('Cancelar', disabled=True, key=DEFAULT_KEY_BTN_CANCEL_REGIST_RESID),
                 sg.T(' '*5), sg.Button('Salvar', disabled=True, key=DEFAULT_KEY_BTN_SAVE_REGIST_RESID), 
                 sg.Button('Editar', disabled=True, key=DEFAULT_KEY_BTN_EDIT_REGIST_RESID), sg.Button('Excluir',disabled=True, key=DEFAULT_KEY_BTN_DEL_REGIST_RESID)]
                ])],
            [sg.Column([table])],
            [sg.T('Renda Familiar Total:'), sg.Input(size=(25,1), disabled=True, key=DEFAULT_KEY_TXT_FAMILY_INCOME_REGIST_RESID)]
            ]

        layout = [
            [sg.TabGroup([ 
                [sg.Tab('Dados Pessoais', personal_data_tab, key=DEFAULT_KEY_PERSONAL_DATA_TABGROUP)],
                [sg.Tab('Outras Inforamções', tab_other_infor, key=DEFAULT_KEY_OTHER_INFOR_TABGROUP)],
                [sg.Tab('Cadastro de Moradores', tab_residents, element_justification='center', key=DEFAULT_KEY_RESIDENTS_REGIST_TABGROUP)]
                ], key=DEFAULT_KEY_TABGROUP, enable_events=True)],
            ]

        return layout
        #return sg.Window('Cadastro',self._layout, default_element_size=(40, 1),return_keyboard_events=False, grab_anywhere=False)

    def disable_objts(self,list_key, window, disable, closeValue=True):
        for key in list_key:
            if closeValue == True:
                window.Element(key).update(disabled=disable, value='')
            else:
                window.Element(key).update(disabled=disable)
                
        window.Element(DEFAULT_KEY_INPUT_ID_REGIST_RESID).update(disabled=True)
        #window.Element(DEFAULT_KEY_TYPE_FRAMEWORK).update(disabled=True)

        
    def disable_input_conjuge(self,window, value, keys, estadCivil):
        if value[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == estadCivil or value[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == self._cohabitant and window.Element(DEFAULT_KEY_BTN_NEW).TKButton['state'] == 'disabled':# and value[DEFAULT_KEY_NAME_SPOUSE] != '':# and window.Element(DEFAULT_KEY_BTN_SAVE).TKButton['state'] == 'normal':
            if window.Element(DEFAULT_KEY_NAME_SPOUSE).TKEntry['state'] == 'readonly':
                self.disable_objts(keys,window, False, False)
                                
        elif  window.Element(DEFAULT_KEY_NAME_SPOUSE).TKEntry['state'] == 'normal':
            self.disable_objts(keys,window, True)
   
    '''
    get the data from the fields of the layouts
    valuer         = inform variable of own PySimpleGui generated by windows
    key            = inform layout keys
    keys_numeric   = all keys here will be formatted to leave only the numbers
    '''
    def get_key_values(self, valuer, keys):
        register = []
        for key in keys:
            if valuer[key] == '':
                register.append(None)
            else:
                
                '''key_found = False
                for key_number in keys_numeric:
                    if key == key_number:
                        num = re.sub('[^0-9]', '', valuer[key])
                        register.append(num)
                        key_found = True
                        break'''

                if key == DEFAULT_KEY_PROJECT_SERVICES:
                        register.append(self.projetcs.get_id(valuer[key]))
                else:
                    register.append(valuer[key])
        
        return register
            
    '''def _change_fields_color(self, window, key, color):
        if window.Element(key).Type == 'input':
            window.Element(key).TKEntry.configure(background=color)
                    
        elif window.Element(key).Type == 'spind':
            window.Element(key).TKSpinBox.configure(background=color)
                    
        elif window.Element(key).Type == 'combo':
            #active, disabled, focus, pressed, selected, background, readonly, alternate, invalid
            style = sg.ttk.Style()
            if color == 'red':
                style.map('TCombobox', fieldbackground=[('active',color)])
                window.Element(key).Widget['state'] = 'active'
            else:
                style.map('TCombobox', fieldbackground=[('selected',color)])
                window.Element(key).Widget['state'] = 'selected'
                
            window.Element(key).Widget.configure(style='TCombobox')
    
    def required_fields(self,window,event, value):
        filled_fields = True        
        key_to_check = [DEFAULT_KEY_NOME_PERSONAL_DATA,           DEFAULT_KEY_SEX_PERSONAL_DATA,
                        DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA,      DEFAULT_KEY_AGE_PERSONAL_DATA,
                        DEFAULT_KEY_NATURALNESS_PERSONAL_DATA,    DEFAULT_KEY_UF_PERSONAL_DATA,
                        DEFAULT_KEY_EMAIL_PERSONAL_DATA,          DEFAULT_KEY_ADDRESS_PERSONAL_DATA,
                        DEFAULT_KEY_DISTRICT_PERSONAL_DATA,       DEFAULT_KEY_RG_PERSONAL_DATA,
                        DEFAULT_KEY_CPF_PERSONAL_DATA,            DEFAULT_KEY_ISSUING_BODY_PERSONAL_DATA,
                        DEFAULT_KEY_CONSIDER_PERSONAL_DATA,       DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA,
                        DEFAULT_KEY_SCHOOLING_PERSONAL_DATA,      DEFAULT_KEY_CNH_PERSONAL_DATA,
                        #Tab outras informações 
                        DEFAULT_KEY_COMB_WORKS,                   DEFAULT_KEY_INP_WHERE,
                        DEFAULT_KEY_TXT_PROFESSION,               DEFAULT_KEY_COMB_RETIREE,
                        DEFAULT_KEY_BENEF_CAMB_SOCI_PROG,
                        DEFAULT_KEY_INCOME_COMB_INCOME,           DEFAULT_KEY_COMB_HAVE_CHILDREM,
                        DEFAULT_KEY_HOW_MANY_CHILDREM,
                        DEFAULT_KEY_LIVES_DISABLED_OR_ELDERLY,    DEFAULT_KEY_DISABLED_ELDERLY_HOW_MANY,
                        DEFAULT_KEY_COMB_OWN_RURAL_PROPERTY,
                        DEFAULT_KEY__COMB_OWNS_CAR,               DEFAULT_KEY_OWNS_CAR_HOW_MANY,
                        DEFAULT_KEY__COMB_HAS_MOTORCICLE,         DEFAULT_KEY_HAS_MOTORCICLE_HOW_MANY,
                        DEFAULT_KEY_COMB__HAVE_FRIDGE,            DEFAULT_KEY_HAVE_FRIDGE_HOW_MANY,
                        DEFAULT_KEY_COMB__HAVE_TELEVI,            DEFAULT_KEY_HAVE_TELEVI_HOW_MANY,
                        DEFAULT_KEY_COMB__HAVE_COMPUTER,          DEFAULT_KEY_HAVE_COMPUTER_HOW_MANY,
                        DEFAULT_KEY_COMB__HAVE_INTERNET,
                        DEFAULT_KEY_COMB__HAVE_ACESS_ELECTRI,     DEFAULT_KEY_COMB__HAVE_DRAINAG_WATER,
                        DEFAULT_KEY_COMB_ONLY_OWNER,              DEFAULT_KEY_TXT_ANOTHER_OWNER,
                        DEFAULT_KEY_TXT_STILL_TIME,               DEFAULT_KEY_COMB_HAVE_ANOTHER_URBAN_PROPERTY,
                        DEFAULT_KEY_ANOTHER_PROPERTY_HOW_MANY,    DEFAULT_KEY_TXT_ANOTHER_PROPERTY_WHERE,
                        DEFAULT_KEY_COMB_REAL_ESTATE_CONSTRUC,    DEFAULT_KEY_PROPERTY_USED_FOR,
                        DEFAULT_KEY_TXT_FRONT,                    DEFAULT_KEY_TXT_RIGHT,
                        DEFAULT_KEY_TXT_LEFT,                     DEFAULT_KEY_TXT_FUNDS,
                        DEFAULT_KEY_COMB_TYPE,                    DEFAULT_KEY_COMB_IS_WALLED,
                        DEFAULT_KEY_COMB_BATCH_POSITION,          DEFAULT_KEY_COMB_STATE_BUILDINGS,
                        DEFAULT_KEY_COMB_BUILDING_TYPE,           DEFAULT_KEY_ROOMS,
                        DEFAULT_KEY_NUMB_FLOORS,                  DEFAULT_KEY_COMB_IS_BEDRIDDEN,
                        DEFAULT_KEY_BATHROOMS,                      
                        ]
        
        key_to_check_spouse = {
                        DEFAULT_KEY_NAME_SPOUSE,
                        DEFAULT_KEY_BIRTHDATE_SPOUSE,
                        DEFAULT_KEY_NATURALNESS_SPOUSE,
                        DEFAULT_KEY_RG_SPOUSE,
                        DEFAULT_KEY_ISSUING_BODY_SPOUSE,
                        DEFAULT_KEY_CPF_SPOUSE,
                        DEFAULT_KEY_SCHOOLING_SPOUSE,
                        DEFAULT_KEY_CNH_SPOUSE,
                        DEFAULT_KEY_SEX_SPOUSE
                        }
        
        for key_check in key_to_check:
            if value[key_check] == '':
                if window.find_element(key_check).Widget['state'] != 'disabled' and window.find_element(key_check).Widget['state'] != 'readonly':
                    self._change_fields_color(window,key_check, 'red')
                    filled_fields = False
                else:
                    self._change_fields_color(window, key_check, "white")
            else: 
                self._change_fields_color(window, key_check, "white")
                
        for key_check in key_to_check_spouse:
            if value[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == self._marital_status:
                if value[key_check] == '':
                    self._change_fields_color(window,key_check, 'red')
                    filled_fields = False
                else: 
                    self._change_fields_color(window, key_check, "white")
                    
        return filled_fields
    '''
    
    def event_other_infor(self,window,value):
        dict_key_Comb = {
            DEFAULT_KEY_DISABLED_ELDERLY_HOW_MANY: DEFAULT_KEY_LIVES_DISABLED_OR_ELDERLY,
            DEFAULT_KEY_HOW_MANY_CHILDREM: DEFAULT_KEY_COMB_HAVE_CHILDREM,
            DEFAULT_KEY_INP_WHERE: DEFAULT_KEY_COMB_WORKS,
            DEFAULT_KEY_OWNS_CAR_HOW_MANY: DEFAULT_KEY__COMB_OWNS_CAR,
            DEFAULT_KEY_HAS_MOTORCICLE_HOW_MANY: DEFAULT_KEY__COMB_HAS_MOTORCICLE,
            DEFAULT_KEY_HAVE_FRIDGE_HOW_MANY: DEFAULT_KEY_COMB__HAVE_FRIDGE,
            DEFAULT_KEY_HAVE_TELEVI_HOW_MANY: DEFAULT_KEY_COMB__HAVE_TELEVI,
            DEFAULT_KEY_HAVE_COMPUTER_HOW_MANY: DEFAULT_KEY_COMB__HAVE_COMPUTER,
            DEFAULT_KEY_TXT_ANOTHER_OWNER: DEFAULT_KEY_COMB_ONLY_OWNER,
            DEFAULT_KEY_ANOTHER_PROPERTY_HOW_MANY: DEFAULT_KEY_COMB_HAVE_ANOTHER_URBAN_PROPERTY,
            DEFAULT_KEY_TXT_ANOTHER_PROPERTY_WHERE :DEFAULT_KEY_COMB_HAVE_ANOTHER_URBAN_PROPERTY
            }
        
        if window.Element(DEFAULT_KEY_BTN_SAVE).TKButton['state'] == 'normal':#or window.Element(DEFAULT_KEY_COMB_WORKS).TKCombo['state'] == 'selected':
            for key_disabled, keys_itens in dict_key_Comb.items():
                    if value[keys_itens] == KEY_YES:
                        window.Element(key_disabled).update(disabled=False)
                    elif value[keys_itens] == KEY_NOT:
                        if window.Element(key_disabled).Type == 'spind':
                            window.Element(key_disabled).update(value = '--',disabled=True)
                        elif window.Element(key_disabled).Type == 'input':
                            window.Element(key_disabled).update(value = '--',disabled=True)
                    elif value[keys_itens] == '':
                        window.Element(key_disabled).update(value = '',disabled=True)
   
    def event_buttons_residents(self,window, btnValid, btnNew,btnCancel, btnSave, btnEdit, btnDel):
        window.Element(DEFAULT_BTN_VALIDATE_INCOME).update(disabled=btnValid)
        window.Element(DEFAULT_KEY_BTN_NEW_REGIST_RESID).update(disabled=btnNew)
        window.Element(DEFAULT_KEY_BTN_CANCEL_REGIST_RESID).update(disabled=btnCancel)    
        window.Element(DEFAULT_KEY_BTN_SAVE_REGIST_RESID).update(disabled=btnSave)
        window.Element(DEFAULT_KEY_BTN_EDIT_REGIST_RESID).update(disabled=btnEdit)
        window.Element(DEFAULT_KEY_BTN_DEL_REGIST_RESID).update(disabled=btnDel)
    
    def _event_have_information(self,window, result, key, msg):
        if result != -1:
            window.Element(key).update(result)
        else:
            window.Element(key).update('')
            window.Element(key).set_focus(False)
            sg.popup_error(msg, keep_on_top=True)
            
     
    def _select_rows_table_residents(self, window):
        if len(window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.selection()) > 0:
            rows = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).SelectedRows[0]
            dados = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values[int(rows)]
            
            for id, key in enumerate(key_fields_residents()):
                window.Element(key).update(dados[id])
            
    def _edit_table(self, window, value, data, keys, indice_table):
        data_new = data[indice_table] = [value[keys[indice]] for indice in range(len(keys))]
        data_new.append(self.update_register_txt_income(window, value))
        
        window.Element(DEFAULT_KEY_TABLE_RESIDENTS).update(values=data, num_rows=20,select_rows=[indice_table])
    
        return data_new
    
    def __save_regist_table(self, window, count_rows, list_record, alternating_row_color, background_color):
        window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.tag_configure('oddrow', background=alternating_row_color)
        window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.tag_configure('evenrow', background=background_color)
        if count_rows % 2 == 0:
            id = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.insert(parent='',index='end',iid=count_rows+1, values=list_record, tags=('oddrow'))
        else:
            id = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.insert(parent='',index='end',iid=count_rows+1, values=list_record, tags=('evenrow'))
        window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values.append(list_record)
                
        window.Element(DEFAULT_KEY_TABLE_RESIDENTS).update(select_rows=[int(id)-1])
        
    def delete_table(self, window, key, id = None):
        if id == None:
            rows = window.Element(key).TKTreeview.get_children()
            if len(rows) > 0:
                for row in rows:
                    window.Element(key).TKTreeview.delete(row)
        else:
            if id > 0:
                window.Element(key).TKTreeview.delete(id)
        
    
    def save_record_regist_resid(self, window, value, keys, alternating_row_color='DimGray', background_color='Gray'):
        datas = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values
        count_rows = len(datas)
        list_record = [value[key] for key in keys]
        self.__save_regist_table(window, count_rows, list_record, alternating_row_color, background_color)
        return list_record
        
    
    def save_regist_table(self, window, datas, alternating_row_color='DimGray', background_color='Gray'):
        #list_record = [key for key in datas]
        elem = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values
        count_rows = len(elem)
                
        self.__save_regist_table(window, count_rows, datas, alternating_row_color, background_color)
    
    def update_register_txt_income(self, window, value):
        #if len(window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.get_children()) > 0:
            datas = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values
            #update valuer to family income
            total_income = 0
            income = 0
            income_spouse = 0
            if value[DEFAULT_KEY_INCOME_COMB_INCOME] != '':
                try:
                    income = value[DEFAULT_KEY_INCOME_COMB_INCOME].replace('.', '')
                    income = float(re.sub('([^0-9].[^0-9]{1,2})', '',income.replace(',','.')))
                except:
                    print('ERRO para alterar a renda total familiar com o valor da renda pessoal')
            
            if value[DEFAULT_KEY_INCOME_SPOUSE] != '':
                try:
                    income_spouse = value[DEFAULT_KEY_INCOME_SPOUSE].replace('.', '')
                    income_spouse = float(re.sub('([^0-9].[^0-9]{1,2})', '',income_spouse.replace(',','.')))
                except:
                    print('ERRO para alterar a renda total familiar com o valor da renda do cônjuge')
                
            total_income = (income+income_spouse)
            if len(datas) != 0:
                total_income += [sum(float(re.sub('([^0-9].[^0-9]{1,2})', '', str(i[7]).replace('.', '').replace(',','.'))) for i in datas)][0]
            income = Decimal(total_income)
            income = locale.currency(income, grouping=True)
            
            window.Element(DEFAULT_KEY_TXT_FAMILY_INCOME_REGIST_RESID).update(income)
            return income
    
    def _event_table_regist_resid(self, window, event, value):
        if len(window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.get_children()) > 0:
            dados = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values
            
        if event == DEFAULT_KEY_TABLE_RESIDENTS:
            if len(window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.selection()) > 0 and window.Element(DEFAULT_KEY_BTN_CANCEL).TKButton['state'] != 'disabled':
                self._select_rows_table_residents(window)
                self.disable_objts(key_fields_residents(), window,True,closeValue=False)
                self.event_buttons_residents(window,True, False,True, True, False, False)
        
        if event == DEFAULT_BTN_VALIDATE_INCOME:
            try:
                money = value[DEFAULT_KEY_TXT_INCOME_REGIST_RESID].replace('.', '')
                money = re.sub('([^0-9].[^0-9]{1,2})', '',money.replace(',','.'))
                income = Decimal(money)
                income = locale.currency(income, grouping=True)
                window.Element(DEFAULT_KEY_TXT_INCOME_REGIST_RESID).update(income)
                
                window.Element(DEFAULT_KEY_BTN_SAVE_REGIST_RESID).update(disabled=False)
            except:
                sg.popup_error('Erro\n, O tipo de texto deve ser numérico',keep_on_top=True)
                
        if event == DEFAULT_KEY_BTN_NEW_REGIST_RESID:
            self.disable_objts(key_fields_residents(), window,False,closeValue=True)
            self.event_buttons_residents(window=window, btnValid=False, btnNew=True, btnCancel=False, btnSave=True, btnEdit=True, btnDel=True)
            #window.Element(DEFAULT_KEY_TABLE_RESIDENTS).focus()
            
        if event == DEFAULT_KEY_BTN_CANCEL_REGIST_RESID:
            self.disable_objts(key_fields_residents(), window,True,closeValue=True)
            self.event_buttons_residents(window, True, True, True, True, True, True)
            
        if event == DEFAULT_KEY_BTN_SAVE_REGIST_RESID:            
            element_nane = False
            for key in key_fields_residents():
                if key != DEFAULT_KEY_INPUT_ID_REGIST_RESID:
                    if value[key] == '':
                        element_nane = True
                    
            if element_nane == False:
                
                if value[DEFAULT_KEY_INPUT_ID_REGIST_RESID] != '' or window.Element(DEFAULT_KEY_BTN_EDIT_REGIST_RESID).TKButton['state'] != 'disabled':
                    print('Salvar Ediãço')
                    regist = self._edit_table(window, value, dados, key_fields_residents(), window.Element(DEFAULT_KEY_TABLE_RESIDENTS).SelectedRows[0])
                    
                    regist_exist = False
                    for cont in range(len(self.datas_register_residents_edit)):
                        indix_column_table_id = 0
                        if self.datas_register_residents_edit[cont][indix_column_table_id] == regist[indix_column_table_id]:
                            self.datas_register_residents_edit[cont] = regist
                            regist_exist = True
                            
                    if regist_exist == False:
                        self.datas_register_residents_edit.append(regist)
                        
                else:
                    print('Salvar Novo registro')
                    regist = self.save_record_regist_resid(window, value,key_fields_residents()) 
                    self.datas_register_residents_new.append(regist)
    
                self.update_register_txt_income(window, value)
                
                self.disable_objts(key_fields_residents(),window,True,closeValue=False)
                self.event_buttons_residents(window, True, False, True, True, True, True)
            else:
                sg.popup('ERRO!\nTodos os campos devem ser preenchidos', keep_on_top=True)
            
        if event == DEFAULT_KEY_BTN_EDIT_REGIST_RESID:
            self.disable_objts(key_fields_residents(),window,False,closeValue=False)
            self.event_buttons_residents(window=window, btnValid=False, btnNew=True, btnCancel=False, btnSave=True, btnEdit=False, btnDel=True)
                
        if event == DEFAULT_KEY_BTN_DEL_REGIST_RESID:
            id = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.selection()[0]
            self.table_index_deleted.append(value[DEFAULT_KEY_INPUT_ID_REGIST_RESID])
            self.delete_table(window, DEFAULT_KEY_TABLE_RESIDENTS, int(id))
            self.disable_objts(key_fields_residents(),window,True,closeValue=True)
                  
    def update_income(self,element_event, window, event,value, key):
        if element_event.event_keyboard_enter(window, event, key):
            try:
                money = value[key].replace('.', '')
                money = re.sub('([^0-9].[^0-9]{1,2})', '',money.replace(',','.'))
                income = Decimal(money)
                income = locale.currency(income, grouping=True)
                window.Element(key).update(income)
                
                self.update_register_txt_income(window, value)
            except:
                window.Element(key).update('')
        
    def event_inputs(self,sg, window, event, value):
        elemAdditional = ElementsAdditional()
        #----------------------------EVENTOS DO CAMPO DE tabDadosPessoal-------------------------
               
        if elemAdditional.event_keyboard_enter(window, event,DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA):
            result = elemAdditional.valid_birth( value[DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA])
            self._event_have_information(window, result, DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA, 'Data incorreta!')
                
        if elemAdditional.event_keyboard_enter(window, event,DEFAULT_KEY_TEL_PERSONAL_DATA):
            result = elemAdditional.valid_cell_number( value[DEFAULT_KEY_TEL_PERSONAL_DATA])
            self._event_have_information(window, result, DEFAULT_KEY_TEL_PERSONAL_DATA, 'quantidade de digitos incorreta!')
            
        if elemAdditional.event_keyboard_enter(window, event,DEFAULT_KEY_CEL_PERSONAL_DATA):
            result = elemAdditional.valid_cell_number( value[DEFAULT_KEY_CEL_PERSONAL_DATA])
            self._event_have_information(window, result, DEFAULT_KEY_CEL_PERSONAL_DATA, 'quantidade de digitos incorreta!')
        
        if elemAdditional.event_keyboard_enter(window, event,DEFAULT_KEY_EMAIL_PERSONAL_DATA):
            result = elemAdditional.valid_email( value[DEFAULT_KEY_EMAIL_PERSONAL_DATA])
            self._event_have_information(window, result, DEFAULT_KEY_EMAIL_PERSONAL_DATA, 'formato do email incorreta!')
                
        if elemAdditional.event_keyboard_enter(window, event,DEFAULT_KEY_HOUSE_NUMBER_PERSONAL_DATA):
            result = elemAdditional.valid_just_number(sg, value[DEFAULT_KEY_HOUSE_NUMBER_PERSONAL_DATA])
            self._event_have_information(window, result, DEFAULT_KEY_HOUSE_NUMBER_PERSONAL_DATA, 'Apenas valor númerico!')
                
        if elemAdditional.event_keyboard_enter(window, event,DEFAULT_KEY_CPF_PERSONAL_DATA):
            result = elemAdditional.valid_cpf(value[DEFAULT_KEY_CPF_PERSONAL_DATA])
            self._event_have_information(window, result, DEFAULT_KEY_CPF_PERSONAL_DATA, 'quantidades de digítos do CPF incorreta!')
            
        '''if elemAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_VOTER_TITLE_PERSONAL_DATA):
            result = elemAdditional.valid_titulo_eleitor(value[DEFAULT_KEY_VOTER_TITLE_PERSONAL_DATA])
            self._event_have_information(window, result, DEFAULT_KEY_VOTER_TITLE_PERSONAL_DATA, 'quantidade de digitos incorreta!')'''
                
        '''if elemAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_RG_PERSONAL_DATA):
            result = elemAdditional.valid_rg( value[DEFAULT_KEY_RG_PERSONAL_DATA])
            self._event_have_information(window, result, DEFAULT_KEY_RG_PERSONAL_DATA, 'Número de RG incorreto!')'''
            
        if elemAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_INCOME_COMB_INCOME):
            try:
                money = value[DEFAULT_KEY_INCOME_COMB_INCOME].replace('.', '')
                money = re.sub('([^0-9].[^0-9]{1,2})', '',money.replace(',','.'))
                income = Decimal(money)
                income = locale.currency(income, grouping=True)
                window.Element(DEFAULT_KEY_INCOME_COMB_INCOME).update(income)
                
                self.update_register_txt_income(window, value)
            except:
                window.Element(DEFAULT_KEY_INCOME_COMB_INCOME).update('')
        
        self.update_income(elemAdditional, window, event,value, DEFAULT_KEY_INCOME_SPOUSE)
                
            

        #----------------------------EVENTOS DO CAMPO DE frameConjuge-------------------------

        if elemAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_BIRTHDATE_SPOUSE):
            result = elemAdditional.valid_birth( value[DEFAULT_KEY_BIRTHDATE_SPOUSE])
            self._event_have_information(window, result, DEFAULT_KEY_BIRTHDATE_SPOUSE, 'Data incorreta!')
                
        if elemAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_TEL_SPOUSE):
            result = elemAdditional.valid_cell_number( value[DEFAULT_KEY_TEL_SPOUSE])
            self._event_have_information(window, result, DEFAULT_KEY_TEL_SPOUSE, 'Número de telefone incorreto!')
                
        if elemAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_CEL_SPOUSE):
            result = elemAdditional.valid_cell_number( value[DEFAULT_KEY_CEL_SPOUSE])
            self._event_have_information(window, result, DEFAULT_KEY_CEL_SPOUSE, 'Número de celular incorreto!')
                
        '''if elemAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_RG_SPOUSE):
            result = elemAdditional.valid_rg( value[DEFAULT_KEY_RG_SPOUSE])
            self._event_have_information(window, result, DEFAULT_KEY_RG_SPOUSE, 'Número de RG incorreto!')'''
        
        if elemAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_CPF_SPOUSE):
            result = elemAdditional.valid_cpf(value[DEFAULT_KEY_CPF_SPOUSE])
            self._event_have_information(window, result, DEFAULT_KEY_CPF_SPOUSE, 'Número de CPF incorreto!')
                
        '''if elemAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_VOTER_TITLE_SPOUSE):
            result = elemAdditional.valid_titulo_eleitor( value[DEFAULT_KEY_VOTER_TITLE_SPOUSE])
            self._event_have_information(window, result, DEFAULT_KEY_VOTER_TITLE_SPOUSE, 'Número do Titulo de Eleitor incorreto!')'''
        del elemAdditional
        
    def exec_layout(self, window, event, value):
       self.event_inputs(sg, window, event, value)
       self.event_other_infor(window, value)
       self.disable_input_conjuge(window, value, keys_fields_spouse(), self._marital_status)
       self._event_table_regist_resid(window, event, value)


class Registration:
    def __init__(self, conectionDB = None):
        self._conn = conectionDB
        self.elemAdditional = ElementsAdditional()
        self._class_register = register_personal_data(self._conn)
        self._window_button_search = None
        self._btn_edit_clicked = False
        self._id_register_db = None
        
        self.window_regitration = None
        
    def _load_layout(self):
        layout = [
             self._class_register.load_window_layout(),
            [sg.T('O cadastro em questão se enquadra como:'), sg.Button('Atualizar REURB',key=DEFAULT_KEY_BTN_UPDATE_TYPE, disabled=True), 
             sg.Combo(['REURB-E', 'REURB-S'],disabled=True, k=DEFAULT_KEY_TYPE_FRAMEWORK), 
             sg.Button('Editar', k=DEFAULT_KEY_EDIT_TYPE_FRAMEWORK), sg.Button('Salvar', k=DEFAULT_KEY_SAVE_TYPE_FRAMEWORK)],
            
            [sg.Button('Novo', key=DEFAULT_KEY_BTN_NEW), sg.Button('Cancelar', disabled=True, key=DEFAULT_KEY_BTN_CANCEL),sg.Button('Salvar',disabled=True, key=DEFAULT_KEY_BTN_SAVE), 
             sg.Button('Editar', disabled=True, key=DEFAULT_KEY_BTN_EDIT), sg.Button('Excluir', disabled=True, key=DEFAULT_KEY_BTN_DELETE)],
            [sg.HorizontalSeparator()],
            [sg.Button('Procurar', key=DEFAULT_KEY_BTN_SEARCH),sg.T(size=(5,1))]
            ]
            
        return layout
    
    def _loard_records_into_fields(self,window, name_table, keys_fields, name_id_table, id_register, is_table = False, key_table = None, get_new_id=None):
        fileds_and_field_db = self._conn._take_fields_records(name_table, keys_fields, is_pass_to_id = get_new_id)
        if is_table:
            keys_new = []
            keys_new.append(self._conn.id_register_residents)
            for k in fileds_and_field_db.keys():
                keys_new.append(k)
            
            self._class_register.datas_register_residents = self._conn.select_register(keys_new, name_table, name_id_table, id_register)
        else:
            self._class_register.datas_register_residents = self._conn.select_register(fileds_and_field_db.keys(), name_table, name_id_table, id_register)[0]
            
        datas = np.array(self._class_register.datas_register_residents)
        if key_table == None:
            for cont, key in enumerate(fileds_and_field_db.values()):
                if datas[cont] != None:
                    if window.Element(key).Type == 'input':
                        window.Element(key).Update(datas[cont])
                    elif window.Element(key).Type == 'combo':
                        if key == DEFAULT_KEY_PROJECT_SERVICES:
                            name_project = self._class_register.projetcs.get_name(datas[cont])
                            window.Element(key).TKCombo.set(name_project)
                        else:
                            window.Element(key).TKCombo.set(datas[cont])
                    elif window.Element(key).Type == 'spind':
                        window.Element(key).TKStringVar.set(datas[cont])
        else:
            window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values = []
            for row in datas:
                val = [i for i in row]
                self._class_register.save_regist_table(window, val)
        
        if len(datas) > 0:
            return True
        return False
    
    def _activate_registration_buttons(self,window, btnNew, btnCancel, btnSave, btnEdit, btnDel, btnUpdataType):
        window.Element(DEFAULT_KEY_BTN_NEW).update(disabled=btnNew)
        window.Element(DEFAULT_KEY_BTN_CANCEL).update(disabled=btnCancel)
        window.Element(DEFAULT_KEY_BTN_SAVE).update(disabled=btnSave)
        window.Element(DEFAULT_KEY_BTN_EDIT).update(disabled=btnEdit)
        window.Element(DEFAULT_KEY_BTN_DELETE).update(disabled=btnDel)
        
        window.Element(DEFAULT_KEY_BTN_UPDATE_TYPE).update(disabled=btnUpdataType)

    def _activate_search_buttons(self, window, buttons):
        window.Element(DEFAULT_KEY_BTN_SEARCH).update(disabled=buttons)
    
    '''
    CONFIGURATION TO DEFINE REGISTRATION AS REURB-S/E 
    '''    
    def if_framing_as(self, value):
        name_db = self._conn.basic_settings
        id_db = self._conn.id_basic_settings
        
        family_income = None
        lot_area = None
        how_many_urban_property = None
        own_rural_property = None
        
        family_income = value[DEFAULT_KEY_INCOME_COMB_INCOME].replace('.', '')
        family_income = re.sub('([^0-9].[^0-9]{1,2})', '',family_income.replace(',','.'))
        if family_income != '':
            family_income = float(family_income)
        if value[DEFAULT_KEY_BATCH_REGU_AREA] != '':
            lot_area = float(value[DEFAULT_KEY_BATCH_REGU_AREA])
        if value[DEFAULT_KEY_ANOTHER_PROPERTY_HOW_MANY] != '':
            how_many_urban_property = int(value[DEFAULT_KEY_ANOTHER_PROPERTY_HOW_MANY])
        own_rural_property = value[DEFAULT_KEY_COMB_OWN_RURAL_PROPERTY]
        
        '''
        values database
        '''
        keys = ['minimum_wage', 'family_income', 'lot_area', 'how_many_urban_property', 'own_rural_property', 'REURB']
        dict_value = dict()
        
        select_tupla = 0
        elements_after_id = 1
        database = self._conn.select_all(name_db)[select_tupla]
        database = database[elements_after_id::]
        for cont in range(len(keys)):
            dict_value[keys[cont]] = database[cont]
            
        income_family_total = dict_value['family_income'] * dict_value['minimum_wage']
        reurb = 'REURB-S'  if dict_value['REURB'] == 'REURB-S' else 'REURB-E'
        fits_how = ''
        
        if family_income != '' and lot_area != '' and how_many_urban_property != '' and own_rural_property != '':
            if family_income < income_family_total and lot_area <= dict_value['lot_area'] and how_many_urban_property == dict_value['how_many_urban_property'] \
                and own_rural_property == dict_value['own_rural_property']:
                    fits_how = reurb

        if fits_how == '':
            fits_how = 'REURB-E' if reurb == 'REURB-S' else 'REURB-S'
                        
        return fits_how
        
    def fill_records_in_fields(self, window, window_button_search, id_register):
        if window_button_search != None or id_register != None:
            #remove data if any existing
            window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values = []
                    
            #event to residents
            self._class_register.disable_objts(key_fields_residents(), window,True,closeValue=True)
            self._class_register.event_buttons_residents(window,True, True, True, True, True, True)
            self._class_register.delete_table(window, DEFAULT_KEY_TABLE_RESIDENTS)
                    
            self._class_register.disable_objts(keys_fields(), window, True,True)
            self._class_register.disable_objts(keys_fields_spouse(), window, True)
                
            register_ok = self._loard_records_into_fields(window, self._conn.register_people, keys_fields(), self._conn.id_register_people, id_register, get_new_id=self._conn.id_to_projects_service)
            register_spouse_exist = self._conn.query_record(self._conn.register_spouse, self._conn.name_id_to_table_register, id_register)
            register_residents_exist = self._conn.query_record(self._conn.register_residents, self._conn.name_id_to_table_register, id_register)
                    
            if register_spouse_exist is True:
                self._loard_records_into_fields(window, self._conn.register_spouse, keys_fields_spouse(), self._conn.name_id_to_table_register, id_register)
                
            if register_residents_exist is True:
                self._loard_records_into_fields(window, self._conn.register_residents, key_fields_residents(),  self._conn.name_id_to_table_register, 
                                                id_register, is_table=True, key_table=DEFAULT_KEY_TABLE_RESIDENTS)
                                    
            if register_ok:
                self._activate_registration_buttons(window, btnNew=False, btnCancel=True, btnSave=True, btnEdit=False, btnDel=False,btnUpdataType=True)
    
    def _input_event_buttons(self, window, event, value):

        if event == DEFAULT_KEY_BTN_NEW:
            self._id_register_db = None
            window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values = []
            
            self._class_register.disable_objts(key_fields_residents(), window, True, closeValue=True)
            self._class_register.disable_objts(keys_fields(),window, False, True)
            
            self._activate_registration_buttons(window, btnNew=True, btnCancel=False, btnSave=False, btnEdit=True, btnDel=True, btnUpdataType=False)
            self._activate_search_buttons(window, buttons=True)
            #event buttons registration residents
            self._class_register.event_buttons_residents(window, True, False, True, True, True, True)
            
            self._class_register.delete_table(window, DEFAULT_KEY_TABLE_RESIDENTS)
            
        elif event == DEFAULT_KEY_BTN_CANCEL:
            self._btn_edit_clicked = False
                        
            if self._id_register_db != None:
                self.fill_records_in_fields(window, self._window_button_search, self._id_register_db)
                self._activate_registration_buttons(window, btnNew=False, btnCancel=True, btnSave=True, btnEdit=False, btnDel=False, btnUpdataType=True)
            else:
                self._activate_registration_buttons(window, btnNew=False, btnCancel=True, btnSave=True, btnEdit=True, btnDel=True, btnUpdataType=True)
                
            self._activate_search_buttons(window, buttons=False)
            #event buttons registration residents
            #self._class_register.event_buttons_residents(window, True, True, True, True, True, False)
            
            #disable functions to register residents tab
            self._class_register.disable_objts(key_fields_residents(), window,True,True)
            self._class_register.event_buttons_residents(window, True, True, True, True, True, True)
            
            #for item in window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.get_children():
            #    window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.delete(item)
                
            #for key in self._class_register.keys_fields():
            #   self._class_register._change_fields_color(window, key, "white")
                
            self._class_register.disable_objts(keys_fields(), window, True,False)
            self._class_register.disable_objts(keys_fields_spouse(), window, True, False)
            
        if event == DEFAULT_KEY_BTN_SAVE:
            '''resultFields = self._class_register.required_fields(window, event,value)
                        
            if  resultFields == False:
                #window[DEFAULT_KEY_PERSONAL_DATA_TABGROUP].select()
                sg.popup_error('ERRO!\ntodos os campos em vermelho são obrigatorios.\n', keep_on_top=True) 
                
            else:
            '''
            field_name = value[DEFAULT_KEY_NOME_PERSONAL_DATA]
            field_cpf = value[DEFAULT_KEY_CPF_PERSONAL_DATA]
            combo_project_services = value[DEFAULT_KEY_PROJECT_SERVICES]
            
            find_name_spouse = value[DEFAULT_KEY_NAME_SPOUSE]
            find_cpf_spouse = value[DEFAULT_KEY_CPF_SPOUSE]
            
            if value[DEFAULT_KEY_TYPE_FRAMEWORK] != '':
                mandatory_spouse_fields_has_been_filled = True
                if value[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == self._class_register._marital_status or value[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == self._class_register._cohabitant:
                    if find_name_spouse != '' and find_cpf_spouse != '':
                        mandatory_spouse_fields_has_been_filled = True
                    else:
                        mandatory_spouse_fields_has_been_filled = False                     
                
                if field_name != '' and field_cpf != '' and combo_project_services != '' and mandatory_spouse_fields_has_been_filled != False:
                    #keys_numeric_fields = [DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA, DEFAULT_KEY_TEL_PERSONAL_DATA, DEFAULT_KEY_CEL_PERSONAL_DATA,
                    #                       DEFAULT_KEY_RG_PERSONAL_DATA, DEFAULT_KEY_CPF_PERSONAL_DATA]
                    #keys_numeric = [DEFAULT_KEY_BIRTHDATE_SPOUSE, DEFAULT_KEY_CEL_SPOUSE, DEFAULT_KEY_TEL_SPOUSE, DEFAULT_KEY_RG_SPOUSE, DEFAULT_KEY_CPF_SPOUSE]
                    register_exist_db = False
                    change_events_fields  = False
        
                    if self._btn_edit_clicked == False:  # Save register
    
                        register_exist_db = self._conn.query_record(self._conn.register_people, 'cpf', re.sub(
                            '[^0-9]', '', value[DEFAULT_KEY_CPF_PERSONAL_DATA]))
                        if register_exist_db != True:
                            self._id_register_db = self._conn.insert_register(self._class_register.get_key_values(value, keys_fields()), 
                                                                              self._conn.register_people, self._conn.id_register_people, self._conn.id_to_projects_service)
    
                            if value[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == self._class_register._marital_status or value[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == self._class_register._cohabitant:
                                self._conn.insert_register(self._class_register.get_key_values(value, keys_fields_spouse()),
                                                           self._conn.register_spouse, self._conn.id_register_spouse, insert_id=self._id_register_db)
    
                            if len(value[DEFAULT_KEY_TABLE_RESIDENTS]) > 0:
                                datas = window.Element(
                                    DEFAULT_KEY_TABLE_RESIDENTS).Values
                                datas = datas[1:]
                                for register in datas:
                                    self._conn.insert_register(
                                        register, self._conn.register_residents, self._conn.id_register_residents, insert_id=self._id_register_db)
                        else:
                            sg.popup('ERRO!\n  cadastro do titular do CPF: {0} já existente na base de dados.'.format(
                                value[DEFAULT_KEY_CPF_PERSONAL_DATA]), keep_on_top=True)
    
                    else:  # save edition register
                        change_events_fields = True
    
                        self._conn.update_register(self._class_register.get_key_values(value, keys_fields()),
                                                   self._conn.register_people, self._conn.id_register_people, self._id_register_db, self._conn.id_to_projects_service)
                        
                        register_exist = self._conn.query_record(
                            self._conn.register_spouse, self._conn.name_id_to_table_register, self._id_register_db)
                        
                        if value[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == self._class_register._marital_status or value[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == self._class_register._cohabitant:
                            
                            if register_exist:
                                self._conn.update_register(self._class_register.get_key_values(value, keys_fields_spouse()), 
                                                           self._conn.register_spouse, self._conn.name_id_to_table_register, self._id_register_db)
                            else:
                                self._conn.insert_register(self._class_register.get_key_values(value, keys_fields_spouse()),
                                                           self._conn.register_spouse, self._conn.id_register_people, insert_id=self._id_register_db)
                        else:
                            self._conn.delete_register(self._conn.register_spouse, self._conn.name_id_to_table_register, self._id_register_db)
                            
                        if len(value[DEFAULT_KEY_TABLE_RESIDENTS]) > 0:
                            index_column_name_table = 1
                            index_column_income_table = 8
                            #when a new record is inserted into the table
                            if (len(self._class_register.datas_register_residents_new)) > 0:
                                for cont in range(len(self._class_register.datas_register_residents_new)):
                                    for register in [self._class_register.datas_register_residents_new[cont][index_column_name_table:]]:
                                        self._conn.insert_register(
                                            register, self._conn.register_residents, self._conn.id_register_residents, insert_id=self._id_register_db)
                                        
                                self._class_register.datas_register_residents_new = []
    
                            #when a record is edited, it will save only the record that was edited.
                            if(len(self._class_register.datas_register_residents_edit)) > 0:
    
                                for register in self._class_register.datas_register_residents_edit:
                                    self._conn.update_register(register[index_column_name_table:index_column_income_table],
                                                               self._conn.register_residents, self._conn.id_register_residents, register[0:1][0])
                                self._class_register.datas_register_residents_edit = []
                                
                        #Delete Elements database
                        if len(self._class_register.table_index_deleted) > 0:
                            for id_register in self._class_register.table_index_deleted:
                                self._conn.delete_register(self._conn.register_residents, self._conn.id_register_residents, id_register)
                                
                    if register_exist_db != True or change_events_fields:
                        self._class_register.disable_objts(keys_fields(), window, True, False)
                        self._class_register.disable_objts(keys_fields_spouse(), window, True, False)
    
                        self._activate_registration_buttons(
                            window, btnNew=False, btnCancel=True, btnSave=True, btnEdit=False, btnDel=False, btnUpdataType=True)
                        self._activate_search_buttons(window, buttons=False)
                        #event buttons registration residents
                        self._class_register.event_buttons_residents(
                            window, True, False, True, True, True, False)
                else:
                    sg.popup_error('ERRO!\nCampos Nome, CPF e Projetos/serviços são campos obrigatorios!\nSe a opção [Casado] ou [amasiado] foi selecionada da opeção [Estado Civil] os campos:\n Nome e CPF do cônjuge são obrigatorios  ', keep_on_top=True)
            else:
                sg.popup_error('Clique no botão [Atualizar REURB] antes de salvar!', keep_on_top=True)

        elif event == DEFAULT_KEY_BTN_EDIT:
            self._btn_edit_clicked = True
            self._class_register.disable_objts(keys_fields(),window, False,False)
            self._activate_registration_buttons(window, btnNew=True, btnCancel=False, btnSave=False, btnEdit=True, btnDel=True,btnUpdataType=False)
            self._activate_search_buttons(window, buttons=True)
            #event buttons registration residents
            self._class_register.event_buttons_residents(window, True, False, True, True, True, True)
        
        elif event == DEFAULT_KEY_BTN_DELETE:              
            deleta = sg.popup_ok_cancel('Deseja realmente Excluir esse registro ?\n\nOK=SIM\nCancel=Não', keep_on_top=True)
            if deleta == 'OK':
                self._class_register.delete_table(window, DEFAULT_KEY_TABLE_RESIDENTS)
                self._conn.delete_register(self._conn.register_residents, self._conn.name_id_to_table_register, self._id_register_db)
                self._conn.delete_register(self._conn.register_spouse, self._conn.name_id_to_table_register, self._id_register_db)
                self._conn.delete_register(self._conn.register_people, self._conn.id_register_people, self._id_register_db)
            
                self._class_register.disable_objts(keys_fields(), window, True,True)
                self._activate_registration_buttons(window, btnNew=False, btnCancel=True, btnSave=True, btnEdit=True, btnDel=True,btnUpdataType=True)
                self._activate_search_buttons(window, buttons=False)
                self._class_register.event_buttons_residents(window, True, True, True, True, True, True)
                
        if event == DEFAULT_KEY_BTN_UPDATE_TYPE:
            window.Element(DEFAULT_KEY_TYPE_FRAMEWORK).update(self.if_framing_as(value))
        
        if event == DEFAULT_KEY_BTN_SEARCH:
            
            search = Search_register_person(self._conn)
            self._window_button_search, self._id_register_db = search.window_button_search()
            
            self.fill_records_in_fields(window, self._window_button_search, self._id_register_db)
                    
                    
        if event == DEFAULT_KEY_EDIT_TYPE_FRAMEWORK:
            window.Element(DEFAULT_KEY_TYPE_FRAMEWORK).update(disabled=False)
        if event == DEFAULT_KEY_SAVE_TYPE_FRAMEWORK:
            dict_regist = dict()
            dict_regist['type_reurb'] = value[DEFAULT_KEY_TYPE_FRAMEWORK]
            self._conn.update_record_by(registers = dict_regist, name_table=self._conn.register_people , name_id = self._conn.id_register_people, id_register = self._id_register_db)
            
            window.Element(DEFAULT_KEY_TYPE_FRAMEWORK).update(disabled=True)
            
        #if event == DEFAULT_KEY_TABGROUP:
        if value[DEFAULT_KEY_TABGROUP] == DEFAULT_KEY_RESIDENTS_REGIST_TABGROUP:
                self._class_register.update_register_txt_income(window, value)
            
    def exec_class(self):
        self.window_regitration = sg.Window('Cadastro', self._load_layout(),icon=r'image/iconLogo.ico',keep_on_top=True, modal=True)
        event, value = None, None
        while(True):
            event, value = self.window_regitration.read(timeout=100)  
                
            if event == sg.WINDOW_CLOSED:
                break
            
            self._input_event_buttons(self.window_regitration, event, value)
            self._class_register.exec_layout(self.window_regitration, event, value)
            
        if self._window_button_search != None:
            self._window_button_search.close()
        
        self.window_regitration.close()
