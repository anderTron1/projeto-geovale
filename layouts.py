#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 00:20:07 2021

@author: andre
"""
from elementsAdditional import ElementsAdditional
from databaseConection import Database

import PySimpleGUI as sg
import numpy as np

import re

import screeninfo

#sg.ChangeLookAndFeel('DarkTeal10')

#-------------------------------BOOLEAN KEYS------------------------------
KEY_YES = 'Sim' 
KEY_NOT = 'Não'

#-------------------------------KEYS FOR THE spouse_frame------------------

DEFAULT_KEY_NAME_SPOUSE = '-NOMECONJ-'
DEFAULT_KEY_SEX_SPOUSE = '-SEXCONJ-'
DEFAULT_KEY_BIRTHDATE_SPOUSE = '-DATANASCICONJ-'
DEFAULT_KEY_AGE_SPOUSE = '-IDADECONJ-'
DEFAULT_KEY_NATURALNESS_SPOUSE = '-NATURALICONJ-'
DEFAULT_KEY_TEL_SPOUSE = '-TELCONJUGE-'
DEFAULT_KEY_CEL_SPOUSE = '-CELCONJUGE-'
DEFAULT_KEY_RG_SPOUSE = '-RGCONJ-'
DEFAULT_KEY_ISSUING_BODY_SPOUSE = '-ORGEMICONJ-'
DEFAULT_KEY_CPF_SPOUSE = '-CPFCONJUGE-'
DEFAULT_KEY_CNH_SPOUSE = '-CNHCONJ-'
DEFAULT_KEY_VOTER_TITLE_SPOUSE = '-TITELEITORCONJU-'
DEFAULT_KEY_SCHOOLING_SPOUSE = '-COMBOESCOLACONJ-'

#------------------------------KEYS TO personal_data_tab-------------------

DEFAULT_KEY_NOME_PERSONAL_DATA = '-NOMEDADOSPESSOAL-'
DEFAULT_KEY_SEX_PERSONAL_DATA = '-SEXPERSONALDATA-'
DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA = '-DATNACIPESSOAL-'
DEFAULT_KEY_AGE_PERSONAL_DATA = '-IDADEDADOPESSOAL-'
DEFAULT_KEY_NATURALNESS_PERSONAL_DATA = '-NATURALDADOSPESSOAL-'
DEFAULT_KEY_UF_PERSONAL_DATA = '-UFDADOSPESSOAL-'
DEFAULT_KEY_TEL_PERSONAL_DATA = '-TELDADOSPESSOAL-'
DEFAULT_KEY_CEL_PERSONAL_DATA = '-CELDADOSPESSOAL-'
DEFAULT_KEY_EMAIL_PERSONAL_DATA = '-EMAILDADOSPESSOAL-'
DEFAULT_KEY_ADDRESS_PERSONAL_DATA = '-ENDDADOSPESSOAL-'
DEFAULT_KEY_DISTRICT_PERSONAL_DATA = '-BAIRDADOSPESSOAL-'
DEFAULT_KEY_HOUSE_NUMBER_PERSONAL_DATA = '-NCASADADOPESSOAL-'
DEFAULT_KEY_RG_PERSONAL_DATA = '-RGDADOPESSOAL-'
DEFAULT_KEY_ISSUING_BODY_PERSONAL_DATA = '-ORGAOEMIDADOSPESSOAL-'
DEFAULT_KEY_CPF_PERSONAL_DATA = '-CPFDADOSPESSOAL-'
DEFAULT_KEY_CNH_PERSONAL_DATA = '-CNHPERSONALDATA-'
DEFAULT_KEY_VOTER_TITLE_PERSONAL_DATA = '-TITELEITORPESSOAL-'
DEFAULT_KEY_CONSIDER_PERSONAL_DATA = '-CONSIDEDADOSPESSOAL-'
DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA = '-ESTACIVILDADPESSOAL-'
DEFAULT_KEY_SCHOOLING_PERSONAL_DATA = '-COMBOESCOLA-'

#----------------------------keys to TabGroup------------------------

DEFAULT_KEY_PERSONAL_DATA_TABGROUP = '-TABDADOSPESSOAL-'
DEFAULT_KEY_OTHER_INFOR_TABGROUP = '-TABOUTRASINFOR-'
DEFAULT_KEY_RESIDENTS_REGIST_TABGROUP = '-TABCADASMORA-'
DEFAULT_KEY_TABGROUP = '-TABGROUDADOPESSOAL-'

#--------------------------key to buttons personal data-------------------
DEFAULT_KEY_BTN_NEW = '-BUTTONNEW-'
DEFAULT_KEY_BTN_CANCEL = '-BUTONCANCEL-'
DEFAULT_KEY_BTN_SAVE = '-BUTTONSAVE-'
DEFAULT_KEY_BTN_EDIT = '-BUTTONEDIT-'
DEFAULT_KEY_BTN_DELETE = '-BUTTONDELETE-'

#--------------------------key to buttons registration selection------------------------
DEFAULT_KEY_BTN_SEARCH = '-BUTTONSEARCH-'
DEFAULT_KEY_BTN_BACK_OFF_LAST = '-BUTTONBACKOFFLAST-'
DEFAULT_KEY_BTN_BACK_ONE = '-BUTTONBACKONE-'
DEFAULT_KEY_BTN_ADVANCE_LAST = '-BUTTONADVANCELAST-'
DEFAULT_KEY_BTN_ADVANCE_ONE = '-BUTTONADVANCEONE-'


#-------------------------KEY to tab other_information----------------------
DEFAULT_KEY_COMB_WORKS = '-RADIOWORKS-'
DEFAULT_KEY_INP_WHERE = '-INPUTWHERE-'
DEFAULT_KEY_TXT_PROFESSION = '-PROFESSION-'
DEFAULT_KEY_COMB_RETIREE = '-RETIREEY-'
DEFAULT_KEY_BENEF_CAMB_SOCI_PROG = '-BENEFICIARYSOCIALPROGRAM-'
DEFAULT_KEY_INCOME_COMB_INCOME = '-INCOME-'
DEFAULT_KEY_COMB_HAVE_CHILDREM = '-HAVECHILDREN-'
DEFAULT_KEY_HOW_MANY_CHILDREM = '-HOWMANYCRILDREN-'
DEFAULT_KEY_LIVES_DISABLED_OR_ELDERLY = '-LIVESDISABLEDORELDERLY-'
DEFAULT_KEY_DISABLED_ELDERLY_HOW_MANY = '-DISABLEDELDERLYHOWMANY-'
DEFAULT_KEY_COMB_RURAL_URBAN_BENEFICIARY = '-RURALURBANPROPERTYBENEFICIARY-'

DEFAULT_KEY__COMB_OWNS_CAR = '-OWNSACAR-'
DEFAULT_KEY_OWNS_CAR_HOW_MANY = '-OWNSCARHOWMANY-'
DEFAULT_KEY__COMB_HAS_MOTORCICLE = '-HASMOTORCICLE-'
DEFAULT_KEY_HAS_MOTORCICLE_HOW_MANY = '-HASMOTORCICLEHOWMANY-'
DEFAULT_KEY_COMB__HAVE_FRIDGE = '-HAVEFRIDGE-'
DEFAULT_KEY_HAVE_FRIDGE_HOW_MANY = '-HAVEFRIDGEHOWMANY-'
DEFAULT_KEY_COMB__HAVE_TELEVI = '-HAVETELEVISION-'
DEFAULT_KEY_HAVE_TELEVI_HOW_MANY = '-HAVETELEVISIONHOWMANY-'
DEFAULT_KEY_COMB__HAVE_COMPUTER = '-HAVECOMPUTER-'
DEFAULT_KEY_HAVE_COMPUTER_HOW_MANY = '-HAVECOMPUTERHOWMANY-'
DEFAULT_KEY_COMB__HAVE_INTERNET = '-HAVEINTERNET-'
DEFAULT_KEY_COMB__HAVE_ACESS_ELECTRI = '-HASACCESSELECTRICITY-'
DEFAULT_KEY_COMB__HAVE_DRAINAG_WATER = '-ACESSODRAINAGEWATER-'

#--------------------------KEY FRAME PROPERTY CONDITIONS-----------------
DEFAULT_KEY_COMB_ONLY_OWNER = '-ONLYOWNER-'
DEFAULT_KEY_TXT_ANOTHER_OWNER = '-ANOTHEROWNER-'
DEFAULT_KEY_TXT_STILL_TIME = '-TIMEYOUOWNTHEPROPERTY-'
DEFAULT_KEY_COMB_ANOTHER_PROPERTY = '-HASANOTHERPROPERTY-'
DEFAULT_KEY_ANOTHER_PROPERTY_HOW_MANY = '-ANOTHERPROPERTYHOWMANY-'
DEFAULT_KEY_TXT_ANOTHER_PROPERTY_WHERE = '-ANOTHERPROPERTYWHERE-'
DEFAULT_KEY_COMB_REAL_ESTATE_CONSTRUC = '-REALESTATECONSTRUCTION-'
DEFAULT_KEY_PROPERTY_USED_FOR = '-PROPERTYUSEDFOR-'

DEFAULT_KEY_TXT_FRONT = '-INPUTFRONT-'
DEFAULT_KEY_TXT_RIGHT = '-INPUTRIGHT-'
DEFAULT_KEY_TXT_LEFT = '-INPUTLEFT-'
DEFAULT_KEY_TXT_FUNDS = '-INPUTFUNDS-'

DEFAULT_KEY_COMB_TYPE = '-TYPEOFPROPERTY-'
DEFAULT_KEY_COMB_IS_WALLED = '-ISWALLED-'
DEFAULT_KEY_COMB_BATCH_POSITION = '-BATCHPOSITION-'
DEFAULT_KEY_COMB_STATE_BUILDINGS = '-STATEOFBUILDINGS-'
DEFAULT_KEY_COMB_BUILDING_TYPE = '-BUILDINGTYPE-'
DEFAULT_KEY_COMB_IS_BEDRIDDEN = '-ISBEDRIDDEN-'
DEFAULT_KEY_NUMB_FLOORS = '-NUMBEROFFLOORS-'
DEFAULT_KEY_ROOMS = '-ROOMS-'
DEFAULT_KEY_BATHROOMS = '-BATHROOMS-'

#-------------------------key registration residents--------------------
DEFAULT_KEY_TXT_NOME_REGIST_RESID = '-NOME_CADASTRO_MORADORES-'
DEFAULT_KEY_SPIN_KINSHIP_REGIST_RESID = '-PARENTESCO_CADASTRO_MORADORES-'
DEFAULT_KEY_COMB_SEX_REGIST_RESID = '-SEXO_CADASTRO_MORADORES-'
DEFAULT_KEY_COMB_MARITAL_STATUS_REGIST_RESID = '-ESTADO_CIVIL_CADASTRO_MORADORES-'
DEFAULT_KEY_TXT_OCCUPATION_REGIST_RESID = '-OCUPAÇÃO_CADASTRO_MORADORES-'
DEFAULT_KEY_TXT_INCOME_REGIST_RESID = '-RENDA_CADASTRO_MORADORES-'

DEFAULT_KEY_TXT_FAMILY_INCOME_REGIST_RESID = '-RENDA_FAMILIAR_TOTAL_CADASTRO_MORADORES-'

#--------------------------key buttons registration residents-------------------
DEFAULT_KEY_BTN_NEW_REGIST_RESID = '-BTN_NOVO_CADASTRO_MORADORES-'
DEFAULT_KEY_BTN_CANCEL_REGIST_RESID = '-BTN_CANCELAR_CADASTRO_MORADORES-'
DEFAULT_KEY_BTN_SAVE_REGIST_RESID = '-BTN_SALVAR_CADASTRO_MORADORES-'
DEFAULT_KEY_BTN_EDIT_REGIST_RESID = '-BTN_EDITAR_CADASTRO_MORADORES-'
DEFAULT_KEY_BTN_DEL_REGIST_RESID = '-BTN_EXCLUIR_CADASTRO_MORADORES-'

#--------------------------KEY TABLES-------------------------------------
DEFAULT_KEY_TABLE_RESIDENTS = '-RESIDENTS-'
DEFAULT_KEY_TABLE_SEARCH_REGISTRATION = '-SEARCH_REGISTRATION-'

def rangeArray(init, size):
    return [num for num in range(init, size)]

class button_search:
    def __init__(self, sg, conectionDB=None):
        self._DEFAULT_KEY_BTN_SEARCH_NOME = '-SEARCHNOME-'
        self._DEFAULT_KEY_BTN_SEARCH_CPF = '-SEARCHCPF-'   
        self._conn = conectionDB
        
        self._window = self._layout()
        
    
    def _databases_db(self):
        return self._conn.select_register([self._conn.id_register_people,'name', 'cpf'], self._conn.register_people, self._conn.id_register_people)
    
    def _table_search(self):
        headings = ['ID','Nome', 'CPF']
        NUM_ROWS = 30
        
        dados = [i for i in range(NUM_ROWS)]
        table = ElementsAdditional.Table(sg, headings, DEFAULT_KEY_TABLE_SEARCH_REGISTRATION, dados = self._databases_db(), col_width=15)
        
        return table
    
    def _layout(self):
        self._search = [[sg.T('Nome:', size=(5,1)), sg.Input(size=(25)), sg.Button('Procurar', key=self._DEFAULT_KEY_BTN_SEARCH_NOME)],
                  [sg.T('CPF:', size=(5,1)), sg.Input(size=(25)), sg.Button('Procurar', key=self._DEFAULT_KEY_BTN_SEARCH_CPF)]
                  ]
        
        layout = [[sg.Frame('Procurar cliente por:', self._search)], [self._table_search()]]
        windows = sg.Window('Procurar cliente', layout, element_justification='center', default_element_size=(40,1), keep_on_top=True, modal=True)
        return windows
        
    def window_button_search(self):
        closed = False
        id = None
        while True:
            event, value = self._window.read(timeout=100)
            
            if event == sg.WIN_CLOSED:
                closed = True
                break
            
            self._window[DEFAULT_KEY_TABLE_SEARCH_REGISTRATION].bind('<Double-Button-1>', '_dublo')
            if event == DEFAULT_KEY_TABLE_SEARCH_REGISTRATION + '_dublo':
                rows = self._window.Element(DEFAULT_KEY_TABLE_SEARCH_REGISTRATION).SelectedRows[0]
                id = self._window.Element(DEFAULT_KEY_TABLE_SEARCH_REGISTRATION).Values[int(rows)][0]
                closed = True
                break
            
        if closed is True:
            self._window.close()
            return None, id
        return self._window, None
#############################################################################
#                                                                           #
#                           FIST RECORD TAB class                           #
#                                                                           #
#############################################################################
class register_personal_data:
    
    def __init__(self):
        self._marital_status = 'Casado'
        #self._style = sg.ttk.Style()
        #self._style.configure('TCombobox', fieldbackground='red')
        
    def load_window_layout(self):
        listEstadoCivil = [self._marital_status, 'Solteiro', 'Divorciado', 'Amasiado/Convivente', 'Viúvo']
        
        schooling_list = ['Não Alfabetizado', 'Ensino Fundamental Incompleto', 'Ensino Fundamental Completo', 'Ensino Médio Incompleto', 
                                     'Ensino Médio Completo', 'Ensino Técnico', 'Ensino Superior']
        
        spouse_frame = [
            [sg.T('Nome:'), sg.Input(size=(60,1), key=DEFAULT_KEY_NAME_SPOUSE)],
            [sg.Text('Sexo:'), sg.Combo(['F', 'M'], key=DEFAULT_KEY_SEX_SPOUSE),
             sg.Text('Data de Nascimento:'), sg.Input(size=(12,1), key=DEFAULT_KEY_BIRTHDATE_SPOUSE), sg.Text('Idade'), sg.Spin(rangeArray(1, 120), initial_value='', key=DEFAULT_KEY_AGE_SPOUSE)],
            [sg.T('Naturalidade:'), sg.Input(size=(20,1), key=DEFAULT_KEY_NATURALNESS_SPOUSE)],
            [sg.T('Tel.:', size=(10, 1)), sg.Input(size=(20,1), key=DEFAULT_KEY_TEL_SPOUSE)], 
            [sg.T('Cel.:', size=(10, 1)), sg.Input(size=(20,1),  key=DEFAULT_KEY_CEL_SPOUSE)],
            [sg.T('RG:', size=(10, 1)), sg.Input(size=(15,1),  key=DEFAULT_KEY_RG_SPOUSE), sg.T('órgão Emissor:'), sg.Input(size=(5,1), key=DEFAULT_KEY_ISSUING_BODY_SPOUSE)], 
            [sg.T('CPF:', size=(10, 1)), sg.Input(size=(15,1), key=DEFAULT_KEY_CPF_SPOUSE)],
            [sg.T('CNH'), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_CNH_SPOUSE)],
            [sg.T('Titulo de Eleitor:'), sg.Input(size=(20,1), key=DEFAULT_KEY_VOTER_TITLE_SPOUSE)],
            [sg.T('Escolaridade'), sg.Combo(['Não Alfabetizado', 'Ensino Fundamental Incompleto', 'Ensino Fundamental Completo', 'Ensino Médio Incompleto', 
                                             'Ensino Médio Completo', 'Ensino Técnico', 'Ensino Superior'], key=DEFAULT_KEY_SCHOOLING_SPOUSE)]   
            ]

        personal_data_tab = [
            [sg.Text('Nome:'), sg.Input(size=(60,1), disabled=True, key=DEFAULT_KEY_NOME_PERSONAL_DATA)],
            [sg.Text('Sexo:'), sg.Combo(['F', 'M'], key=DEFAULT_KEY_SEX_PERSONAL_DATA)],
            [sg.Text('Data de Nascimento:'), sg.Input(size=(12,1), disabled=True, key=DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA)], 
            [sg.Text('Idade'), sg.Spin(rangeArray(1, 120),initial_value='', disabled=True, key=DEFAULT_KEY_AGE_PERSONAL_DATA)],
            [sg.Text('Naturalidade'), sg.Input(size=(30,1), disabled=True,key=DEFAULT_KEY_NATURALNESS_PERSONAL_DATA), sg.Text('UF:'), sg.Input(size=(15,1), disabled=True, key=DEFAULT_KEY_UF_PERSONAL_DATA)],
            [sg.Text('Tel.:'), sg.Input(size=(20,1), disabled=True,key=DEFAULT_KEY_TEL_PERSONAL_DATA)], 
            [sg.Text('Cel.:'), sg.Input(size=(20,1), disabled=True,key=DEFAULT_KEY_CEL_PERSONAL_DATA)],
            [sg.HorizontalSeparator()],
            [sg.Text('Email:   '), sg.Input(size=(40,1), disabled=True,key=DEFAULT_KEY_EMAIL_PERSONAL_DATA)],
            [sg.Text('Endereço:'), sg.Input(size=(40,1), disabled=True,key=DEFAULT_KEY_ADDRESS_PERSONAL_DATA)],
            [sg.Text('Bairro:  '), sg.Input(size=(40,1), disabled=True,key=DEFAULT_KEY_DISTRICT_PERSONAL_DATA), sg.Text('Nº:'), sg.Input(size=(5,), disabled=True, key=DEFAULT_KEY_HOUSE_NUMBER_PERSONAL_DATA)],
            [sg.Text('RG:      '), sg.Input(size=(15,1), disabled=True,key=DEFAULT_KEY_RG_PERSONAL_DATA), sg.Text('Órgão Emissor:'), sg.Input(size=(5,1), disabled=True, key=DEFAULT_KEY_ISSUING_BODY_PERSONAL_DATA)], 
            [sg.Text('CPF:     '), sg.Input(size=(15,1), disabled=True,key=DEFAULT_KEY_CPF_PERSONAL_DATA)],
            [sg.Text('CNH:     '), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_CNH_PERSONAL_DATA)], 
            [sg.Text('Titulo de Eleitor:'), sg.Input(size=(20,1), disabled=True, key=DEFAULT_KEY_VOTER_TITLE_PERSONAL_DATA)],
            [sg.T('Considera-se'),sg.Combo(['Branco','Negro', 'Pardo', 'Amarelo', 'Indígena'], key=DEFAULT_KEY_CONSIDER_PERSONAL_DATA), sg.T('Estado Civil:'), 
             sg.Combo(listEstadoCivil, key=DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA)],
            [sg.T('Escolaridade'), sg.Combo(schooling_list, key=DEFAULT_KEY_SCHOOLING_PERSONAL_DATA)],
            [sg.Frame('Dados do Cônjuge', spouse_frame)]
            ]

        frameConfImovel = [
            [sg.T('Frente:  '), sg.Input(size=(25,1), disabled=True,  key=DEFAULT_KEY_TXT_FRONT)],
            [sg.T('Direita: '), sg.Input(size=(25,1), disabled=True,  key=DEFAULT_KEY_TXT_RIGHT)],
            [sg.T('Esquerda:'), sg.Input(size=(25,1), disabled=True,  key=DEFAULT_KEY_TXT_LEFT)],
            [sg.T('Fundos:  '), sg.Input(size=(25,1), disabled=True,  key=DEFAULT_KEY_TXT_FUNDS)],
            ]

        frameCondImoveis = [
            [sg.T('É o único dono?'), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_COMB_ONLY_OWNER), sg.T('Outro Dono?'), sg.Input(size=(25,1), disabled=True,  key=DEFAULT_KEY_TXT_ANOTHER_OWNER)],
            [sg.T('A quanto tempo spossui o Imóvel?'), sg.Input(size=(15,1), disabled=True,  key=DEFAULT_KEY_TXT_STILL_TIME)],
            [sg.T('Possui Outro Imóvel?'), sg.Combo([KEY_YES, KEY_NOT],  key=DEFAULT_KEY_COMB_ANOTHER_PROPERTY), sg.T('Quantos?'),
             sg.Spin(rangeArray(1, 11), disabled=True,  key=DEFAULT_KEY_ANOTHER_PROPERTY_HOW_MANY, initial_value=('')), sg.T('Onde?'), sg.Input(size=(20,1), disabled=True,  key=DEFAULT_KEY_TXT_ANOTHER_PROPERTY_WHERE)],
            [sg.T('Tem Edificação no Imóvel?'), sg.Combo([KEY_YES, KEY_NOT],  key=DEFAULT_KEY_COMB_REAL_ESTATE_CONSTRUC), sg.T('Utiliza o imóvel para:'), 
             sg.Combo(['Moradia', 'Comércio'], key=DEFAULT_KEY_PROPERTY_USED_FOR)],
            [sg.Frame('Confrontantes do imóvel, Vizinhos, Nº:', frameConfImovel)],
            
            [sg.T('Tipo do Imóvel:', size=(22)), sg.Combo(['Casa', 'Sobrado', 'Apartamento', 'Ponto de comércio'], key=DEFAULT_KEY_COMB_TYPE), 
             sg.T('É murado?'), sg.Combo([KEY_YES, KEY_NOT],   key=DEFAULT_KEY_COMB_IS_WALLED)],
            
            [sg.T('Posição no lote:',size=(22)), sg.Combo(['Frente', 'Fundos', 'Centro'],  key=DEFAULT_KEY_COMB_BATCH_POSITION), 
             sg.T('Estado das edificações:',size=(22)), sg.Combo(['Muito bom', 'Bom', 'Regular', 'Ruim', 'Péssimo'],  key=DEFAULT_KEY_COMB_STATE_BUILDINGS)],
            
            [sg.T('Tipo de construção:',size=(22)), sg.Combo(['Alvenaria', 'Madeira', 'Estuque', 'Mista', 'Outros'], key=DEFAULT_KEY_COMB_BUILDING_TYPE), 
             sg.T('Tem Acabamento?'), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_COMB_IS_BEDRIDDEN)],
            
            [sg.T('Numero de pavimentos?',size=(22)), sg.Spin(rangeArray(1, 11), initial_value='', disabled=True, key=DEFAULT_KEY_NUMB_FLOORS), sg.T('Cômodos?'), 
             sg.Spin(rangeArray(1, 11),  initial_value='', disabled=True, key=DEFAULT_KEY_ROOMS),sg.T('e Banheiros?'), sg.Spin(rangeArray(1, 11), initial_value='', disabled=True, key=DEFAULT_KEY_BATHROOMS)]
            ]

        tab_other_infor = [
            [sg.T('Trabalha?'), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_COMB_WORKS),sg.T('Onde:'), sg.Input(size=(25,1), disabled=True,  key=DEFAULT_KEY_INP_WHERE)],
            [sg.T('Profissão:'), sg.Input(size=(25,1), disabled=True,   key=DEFAULT_KEY_TXT_PROFESSION), sg.T('É aposentado?'), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_COMB_RETIREE)],
            [sg.T('Beneficiário de algum programa social?'), sg.Combo([KEY_YES, KEY_NOT],  key=DEFAULT_KEY_BENEF_CAMB_SOCI_PROG)],
            [sg.T('Renda:'), sg.Combo(['Até 1 Salário Mínimo', 'De 1 a 3 Salários mínimos', 'De 3 a 5 Salários Mínimos', 'Mais de 5 Salários mínimos'],  key=DEFAULT_KEY_INCOME_COMB_INCOME)],
            [sg.T('Tem Filhos?'), sg.Combo([KEY_YES, KEY_NOT],  key=DEFAULT_KEY_COMB_HAVE_CHILDREM), 
             sg.T('Quantos?'), sg.Spin(values=(rangeArray(1,20)), disabled=True, key=DEFAULT_KEY_HOW_MANY_CHILDREM, initial_value=(''))],
            [sg.T('Mora Algum deficiente ou idoso?'), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_LIVES_DISABLED_OR_ELDERLY), 
             sg.T('Quantos?'), sg.Spin(values=(rangeArray(1,10)), disabled=True,  key=DEFAULT_KEY_DISABLED_ELDERLY_HOW_MANY, initial_value='')],
            [sg.T('É beneficiário Concessionário de alguma imóvel Urbano ou Rural?'), sg.Combo([KEY_YES, KEY_NOT],  key=DEFAULT_KEY_COMB_RURAL_URBAN_BENEFICIARY)],
            [sg.HorizontalSeparator()],
            
            [sg.T('Possui Automóvel?'), sg.Combo([KEY_YES, KEY_NOT],   key=DEFAULT_KEY__COMB_OWNS_CAR), sg.T('Quantas'),sg.Spin(rangeArray(1,11), disabled=True,  key=DEFAULT_KEY_OWNS_CAR_HOW_MANY, initial_value=('')),
             sg.T('Possui Motos?'), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY__COMB_HAS_MOTORCICLE), sg.T('Quantas'),sg.Spin(rangeArray(1,11), disabled=True,  key=DEFAULT_KEY_HAS_MOTORCICLE_HOW_MANY, initial_value=(''))],
            
            [sg.T('Tem Geladeira em casa?', size=(27)), sg.Combo([KEY_YES, KEY_NOT],  key=DEFAULT_KEY_COMB__HAVE_FRIDGE), sg.T('Quantas?'), 
             sg.Spin(rangeArray(1,11), disabled=True,  key=DEFAULT_KEY_HAVE_FRIDGE_HOW_MANY, initial_value=(''))],
            [sg.T('Tem Televisão em casa?', size=(27)), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_COMB__HAVE_TELEVI), sg.T('Quantas '), 
             sg.Spin(rangeArray(1, 11), disabled=True, key=DEFAULT_KEY_HAVE_TELEVI_HOW_MANY, initial_value=(''))],
            [sg.T('Tem Computador em casa?', size=(27)), sg.Combo([KEY_YES, KEY_NOT], key=DEFAULT_KEY_COMB__HAVE_COMPUTER), sg.T('Quantos?'), 
             sg.Spin(rangeArray(1, 11), disabled=True, key=DEFAULT_KEY_HAVE_COMPUTER_HOW_MANY, initial_value=(''))],
            [sg.T('Tem acesso a internet?', size=(27)), sg.Combo([KEY_YES, KEY_NOT],  key=DEFAULT_KEY_COMB__HAVE_INTERNET),sg.T('Tem acesso a Energia Elétrica?'), 
             sg.Combo(['Sim', 'Não'],  key=DEFAULT_KEY_COMB__HAVE_ACESS_ELECTRI)],
            [sg.T('Tem acesso a Água Encanada?', size=(27)), sg.Combo([KEY_YES, KEY_NOT],  key=DEFAULT_KEY_COMB__HAVE_DRAINAG_WATER)],
            [sg.Frame('Condições do Imóvel', frameCondImoveis)]
            ]

        headings = ['Nome:', 'Paren.', 'Sexo', 'Est. Civil', 'Ocupação', 'Renda']

        sg.Table
        table = ElementsAdditional.Table(sg, headings, DEFAULT_KEY_TABLE_RESIDENTS, col_width=12)
        tab_residents = [
            [sg.Frame('Informações', [
                [sg.T('Nome:', size=(15,1)), sg.Input(size=(25,1), disabled=True, key=DEFAULT_KEY_TXT_NOME_REGIST_RESID)],
                [sg.T('Parentesco',size=(15,1)), sg.Spin(rangeArray(1, 120), disabled=True,initial_value='', key=DEFAULT_KEY_SPIN_KINSHIP_REGIST_RESID), sg.T('Sexo'), 
                 sg.Combo(['M', 'F'], disabled=True, key=DEFAULT_KEY_COMB_SEX_REGIST_RESID)],
                [sg.T('Estado Civil:', size=(15,1)),sg.Combo(['Casado', 'Solteiro', 'Divorciado', 'Amasiado/Convivente', 'Viúvo'], disabled=True,  key=DEFAULT_KEY_COMB_MARITAL_STATUS_REGIST_RESID)],
                [sg.T('Ocupação:', size=(15,1)), sg.Input(size=(20,1),disabled=True, key=DEFAULT_KEY_TXT_OCCUPATION_REGIST_RESID), sg.T('Renda:'), sg.Input(size=(15,1), disabled=True, key=DEFAULT_KEY_TXT_INCOME_REGIST_RESID)],
                [sg.Button('Novo', disabled=False, key=DEFAULT_KEY_BTN_NEW_REGIST_RESID), sg.Button('Cancelar', disabled=True, key=DEFAULT_KEY_BTN_CANCEL_REGIST_RESID),
                 sg.T(' '*5), sg.Button('Salvar', disabled=True, key=DEFAULT_KEY_BTN_SAVE_REGIST_RESID), 
                 sg.Button('Editar', disabled=True, key=DEFAULT_KEY_BTN_EDIT_REGIST_RESID), sg.Button('Excluir',disabled=True, key=DEFAULT_KEY_BTN_DEL_REGIST_RESID)]
                ])],
            [sg.Column([table])],
            [sg.T('Renda Familiar Total:'), sg.Input(size=(15,1), disabled=True, key=DEFAULT_KEY_TXT_FAMILY_INCOME_REGIST_RESID)]
            ]

        layout = [
            [sg.TabGroup([ 
                [sg.Tab('Dados Pessoais', personal_data_tab, key=DEFAULT_KEY_PERSONAL_DATA_TABGROUP)],
                [sg.Tab('Outras Inforamções', tab_other_infor, key=DEFAULT_KEY_OTHER_INFOR_TABGROUP)],
                [sg.Tab('Cadastro de Moradores', tab_residents, element_justification='center', key=DEFAULT_KEY_RESIDENTS_REGIST_TABGROUP)]
                ], key=DEFAULT_KEY_TABGROUP)],
            ]

        return layout
        #return sg.Window('Cadastro',self._layout, default_element_size=(40, 1),return_keyboard_events=False, grab_anywhere=False)

    def disable_objts(self,list_key, window, disable, closeValue=True):
        for key in list_key:
            if closeValue == True:
                window.Element(key).update(disabled=disable, value='')
            else:
                window.Element(key).update(disabled=disable)
                #self._change_fields_color(window, key, "white")

        
    def disable_input_conjuge(self,window, velue, estadCivil):
        key_to_disable = [DEFAULT_KEY_NAME_SPOUSE,  DEFAULT_KEY_SEX_SPOUSE,
                          DEFAULT_KEY_BIRTHDATE_SPOUSE, DEFAULT_KEY_AGE_SPOUSE,
                          DEFAULT_KEY_NATURALNESS_SPOUSE, DEFAULT_KEY_TEL_SPOUSE,
                          DEFAULT_KEY_CEL_SPOUSE, DEFAULT_KEY_RG_SPOUSE,
                          DEFAULT_KEY_ISSUING_BODY_SPOUSE, DEFAULT_KEY_CPF_SPOUSE,
                          DEFAULT_KEY_CNH_SPOUSE, DEFAULT_KEY_VOTER_TITLE_SPOUSE,
                          DEFAULT_KEY_SCHOOLING_SPOUSE]
        
        if velue[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == estadCivil and window.Element(DEFAULT_KEY_BTN_NEW).TKButton['state'] == 'disabled':# and velue[DEFAULT_KEY_NAME_SPOUSE] != '':# and window.Element(DEFAULT_KEY_BTN_SAVE).TKButton['state'] == 'normal':
            if window.Element(DEFAULT_KEY_NAME_SPOUSE).TKEntry['state'] == 'readonly':
                self.disable_objts(key_to_disable,window, False)
                
        elif  window.Element(DEFAULT_KEY_NAME_SPOUSE).TKEntry['state'] == 'normal':
                self.disable_objts(key_to_disable,window, True)

    def _change_fields_color(self, window, key, color):
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
    
    def keys_fields_spouse(self):
        keys = [DEFAULT_KEY_NAME_SPOUSE,          DEFAULT_KEY_SEX_SPOUSE,
                DEFAULT_KEY_BIRTHDATE_SPOUSE,     DEFAULT_KEY_AGE_SPOUSE,
                DEFAULT_KEY_NATURALNESS_SPOUSE,   DEFAULT_KEY_TEL_SPOUSE,
                DEFAULT_KEY_CEL_SPOUSE,           DEFAULT_KEY_RG_SPOUSE,
                DEFAULT_KEY_ISSUING_BODY_SPOUSE,  DEFAULT_KEY_CPF_SPOUSE,
                DEFAULT_KEY_CNH_SPOUSE,           DEFAULT_KEY_VOTER_TITLE_SPOUSE,
                DEFAULT_KEY_SCHOOLING_SPOUSE]
        
        return keys
    

    def keys_fields_tab(self):
        keys = [               
                #-------------------------KEYS TO personal_data_tab------------------------------
                DEFAULT_KEY_NOME_PERSONAL_DATA,         DEFAULT_KEY_SEX_PERSONAL_DATA,
                DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA,    DEFAULT_KEY_AGE_PERSONAL_DATA,
                DEFAULT_KEY_NATURALNESS_PERSONAL_DATA,  DEFAULT_KEY_UF_PERSONAL_DATA,
                DEFAULT_KEY_TEL_PERSONAL_DATA,          DEFAULT_KEY_CEL_PERSONAL_DATA,
                DEFAULT_KEY_EMAIL_PERSONAL_DATA,        DEFAULT_KEY_ADDRESS_PERSONAL_DATA,
                DEFAULT_KEY_DISTRICT_PERSONAL_DATA,     DEFAULT_KEY_HOUSE_NUMBER_PERSONAL_DATA,
                DEFAULT_KEY_RG_PERSONAL_DATA,           DEFAULT_KEY_ISSUING_BODY_PERSONAL_DATA,
                DEFAULT_KEY_CPF_PERSONAL_DATA,          DEFAULT_KEY_CNH_PERSONAL_DATA,
                DEFAULT_KEY_VOTER_TITLE_PERSONAL_DATA,  DEFAULT_KEY_CONSIDER_PERSONAL_DATA,
                DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA, DEFAULT_KEY_SCHOOLING_PERSONAL_DATA,
                
                #-------------------------KEY to tab other_information----------------------------
                DEFAULT_KEY_COMB_WORKS,                 DEFAULT_KEY_INP_WHERE,
                DEFAULT_KEY_TXT_PROFESSION,             DEFAULT_KEY_COMB_RETIREE,
                DEFAULT_KEY_BENEF_CAMB_SOCI_PROG,       DEFAULT_KEY_INCOME_COMB_INCOME,
                DEFAULT_KEY_COMB_HAVE_CHILDREM,         DEFAULT_KEY_HOW_MANY_CHILDREM,
                DEFAULT_KEY_LIVES_DISABLED_OR_ELDERLY,  DEFAULT_KEY_DISABLED_ELDERLY_HOW_MANY,
                DEFAULT_KEY_COMB_RURAL_URBAN_BENEFICIARY, 
                
                DEFAULT_KEY__COMB_OWNS_CAR,         DEFAULT_KEY_OWNS_CAR_HOW_MANY,
                DEFAULT_KEY__COMB_HAS_MOTORCICLE,   DEFAULT_KEY_HAS_MOTORCICLE_HOW_MANY,
                DEFAULT_KEY_COMB__HAVE_FRIDGE,      DEFAULT_KEY_HAVE_FRIDGE_HOW_MANY,
                DEFAULT_KEY_COMB__HAVE_TELEVI,      DEFAULT_KEY_HAVE_TELEVI_HOW_MANY,
                DEFAULT_KEY_COMB__HAVE_COMPUTER,    DEFAULT_KEY_HAVE_COMPUTER_HOW_MANY,
                DEFAULT_KEY_COMB__HAVE_INTERNET,    DEFAULT_KEY_COMB__HAVE_ACESS_ELECTRI,
                DEFAULT_KEY_COMB__HAVE_DRAINAG_WATER, 
                
                #--------------------------KEY FRAME PROPERTY CONDITIONS---------------------------
                DEFAULT_KEY_COMB_ONLY_OWNER,             DEFAULT_KEY_TXT_ANOTHER_OWNER,
                DEFAULT_KEY_TXT_STILL_TIME,              DEFAULT_KEY_COMB_ANOTHER_PROPERTY,
                DEFAULT_KEY_ANOTHER_PROPERTY_HOW_MANY,   DEFAULT_KEY_TXT_ANOTHER_PROPERTY_WHERE,
                DEFAULT_KEY_COMB_REAL_ESTATE_CONSTRUC,   DEFAULT_KEY_PROPERTY_USED_FOR,
                
                DEFAULT_KEY_TXT_FRONT,   DEFAULT_KEY_TXT_RIGHT,
                DEFAULT_KEY_TXT_LEFT,    DEFAULT_KEY_TXT_FUNDS,
                
                DEFAULT_KEY_COMB_TYPE,               DEFAULT_KEY_COMB_IS_WALLED,
                DEFAULT_KEY_COMB_BATCH_POSITION,     DEFAULT_KEY_COMB_STATE_BUILDINGS,
                DEFAULT_KEY_COMB_BUILDING_TYPE,      DEFAULT_KEY_COMB_IS_BEDRIDDEN,
                DEFAULT_KEY_NUMB_FLOORS,             DEFAULT_KEY_ROOMS,
                DEFAULT_KEY_BATHROOMS]
        return keys
        
    def get_key_values(self, valuer, keys, keys_numeric):
        register = []
        for key in keys:
            if valuer[key] == '':
                register.append(None)
            else:
                
                key_found = False
                for key_number in keys_numeric:
                    if key == key_number:
                        num = re.sub('[^0-9]', '', valuer[key])
                        register.append(num)
                        key_found = True
                        break
                    
                if key_found == False:
                    register.append(valuer[key])
        
        return register
            
    def required_fields(self,window,event, velue):
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
                        DEFAULT_KEY_COMB_RURAL_URBAN_BENEFICIARY,
                        DEFAULT_KEY__COMB_OWNS_CAR,               DEFAULT_KEY_OWNS_CAR_HOW_MANY,
                        DEFAULT_KEY__COMB_HAS_MOTORCICLE,         DEFAULT_KEY_HAS_MOTORCICLE_HOW_MANY,
                        DEFAULT_KEY_COMB__HAVE_FRIDGE,            DEFAULT_KEY_HAVE_FRIDGE_HOW_MANY,
                        DEFAULT_KEY_COMB__HAVE_TELEVI,            DEFAULT_KEY_HAVE_TELEVI_HOW_MANY,
                        DEFAULT_KEY_COMB__HAVE_COMPUTER,          DEFAULT_KEY_HAVE_COMPUTER_HOW_MANY,
                        DEFAULT_KEY_COMB__HAVE_INTERNET,
                        DEFAULT_KEY_COMB__HAVE_ACESS_ELECTRI,     DEFAULT_KEY_COMB__HAVE_DRAINAG_WATER,
                        DEFAULT_KEY_COMB_ONLY_OWNER,              DEFAULT_KEY_TXT_ANOTHER_OWNER,
                        DEFAULT_KEY_TXT_STILL_TIME,               DEFAULT_KEY_COMB_ANOTHER_PROPERTY,
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
            if velue[key_check] == '':
                if window.find_element(key_check).Widget['state'] != 'disabled' and window.find_element(key_check).Widget['state'] != 'readonly':
                    self._change_fields_color(window,key_check, 'red')
                    filled_fields = False
                else:
                    self._change_fields_color(window, key_check, "white")
            else: 
                self._change_fields_color(window, key_check, "white")
                
        for key_check in key_to_check_spouse:
            if velue[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == self._marital_status:
                if velue[key_check] == '':
                    self._change_fields_color(window,key_check, 'red')
                    filled_fields = False
                else: 
                    self._change_fields_color(window, key_check, "white")
                    
        return filled_fields
    
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
            DEFAULT_KEY_ANOTHER_PROPERTY_HOW_MANY: DEFAULT_KEY_COMB_ANOTHER_PROPERTY,
            DEFAULT_KEY_TXT_ANOTHER_PROPERTY_WHERE :DEFAULT_KEY_COMB_ANOTHER_PROPERTY
            }
        
        if window.Element(DEFAULT_KEY_DISABLED_ELDERLY_HOW_MANY).Widget['state'] == 'disable':
            for key_disabled, keys_itens in dict_key_Comb.items():
                if value[keys_itens] == KEY_YES:
                    window.Element(key_disabled).update(disabled=False)
                elif value[keys_itens] == KEY_NOT or value[keys_itens] == '':
                    window.Element(key_disabled).update(disabled=True)
   
    def event_buttons_residents(self,window, btnNew,btnCancel, btnSave, btnEdit, btnDel):
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
            sg.popup_error(msg)
            
     
    def _select_rows_table_residents(self, window):
        if len(window.Element(DEFAULT_KEY_TABLE_RESIDENTS).SelectedRows) > 0:
            rows = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).SelectedRows[0]
            dados = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values[int(rows)]
                
            window.Element(DEFAULT_KEY_TXT_NOME_REGIST_RESID).update(dados[0])
            window.Element(DEFAULT_KEY_TXT_OCCUPATION_REGIST_RESID).update(dados[4])
            window.Element(DEFAULT_KEY_TXT_INCOME_REGIST_RESID).update(dados[5])
            
            select_sex = window.Element(DEFAULT_KEY_COMB_SEX_REGIST_RESID).Values.index(dados[2])
            window.Element(DEFAULT_KEY_COMB_SEX_REGIST_RESID).update(set_to_index=select_sex)
            
            window.Element(DEFAULT_KEY_SPIN_KINSHIP_REGIST_RESID).update(value=dados[1])
                
            select_marital_status = window.Element(DEFAULT_KEY_COMB_MARITAL_STATUS_REGIST_RESID).Values.index(dados[3])
            window.Element(DEFAULT_KEY_COMB_MARITAL_STATUS_REGIST_RESID).update(set_to_index = select_marital_status)
            
    def _edit_table(self, window, value, data, keys, indice_table):
        data[indice_table] = [value[keys[indice]] for indice in range(len(keys))]
        
        window.Element(DEFAULT_KEY_TABLE_RESIDENTS).update(values=data, num_rows=20,select_rows=[indice_table])
    
    def _save_record_regist_resid(self, window, value, keys, alternating_row_color='DimGray', background_color='Gray'):
        datas = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values
        count_rows = len(datas)
        list_record = [value[key] for key in keys]
                
        window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.tag_configure('oddrow', background=alternating_row_color)
        window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.tag_configure('evenrow', background=background_color)
        if count_rows % 2 == 0:
            id = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.insert(parent='',index='end',iid=count_rows+1, values=list_record, tags=('oddrow'))
        else:
            id = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.insert(parent='',index='end',iid=count_rows+1, values=list_record, tags=('evenrow'))
        window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values.append(list_record)
                
        window.Element(DEFAULT_KEY_TABLE_RESIDENTS).update(select_rows=[int(id)-1])
    
    def key_to_disable_regist(self):
        key_to_disable_regist = [DEFAULT_KEY_TXT_NOME_REGIST_RESID,
                                         DEFAULT_KEY_SPIN_KINSHIP_REGIST_RESID,
                                         DEFAULT_KEY_COMB_SEX_REGIST_RESID,
                                         DEFAULT_KEY_COMB_MARITAL_STATUS_REGIST_RESID,
                                         DEFAULT_KEY_TXT_OCCUPATION_REGIST_RESID,
                                         DEFAULT_KEY_TXT_INCOME_REGIST_RESID]
        return key_to_disable_regist
    
    def _event_table_regist_resid(self, window, event, valuer):
        dados = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values
                
        if event == DEFAULT_KEY_TABLE_RESIDENTS:
            if len(dados) > 0:
                self._select_rows_table_residents(window)
                self.disable_objts(self.key_to_disable_regist(), window,True,closeValue=False)
                self.event_buttons_residents(window, False,True, True, False, False)
                     
        if event == DEFAULT_KEY_BTN_NEW_REGIST_RESID:
            self.disable_objts(self.key_to_disable_regist(), window,False,closeValue=True)
            self.event_buttons_residents(window, False, False, False, True, True)
            #window.Element(DEFAULT_KEY_TABLE_RESIDENTS).focus()
            
        if event == DEFAULT_KEY_BTN_CANCEL_REGIST_RESID:
            self.disable_objts(self.key_to_disable_regist(), window,True,closeValue=True)
            self.event_buttons_residents(window, True, True, True, True, True)
            
        if event == DEFAULT_KEY_BTN_SAVE_REGIST_RESID:

            
            if window.Element(DEFAULT_KEY_BTN_EDIT_REGIST_RESID).Disabled == False:
                self._edit_table(window, valuer, dados, self.key_to_disable_regist(), window.Element(DEFAULT_KEY_TABLE_RESIDENTS).SelectedRows[0])
                
            elif window.Element(DEFAULT_KEY_BTN_NEW_REGIST_RESID).Disabled == False:
                self._save_record_regist_resid(window, valuer,self.key_to_disable_regist()) 

            #update valuer to family income
            total_income = [sum(int(i[5]) for i in dados)][0]
            window.Element(DEFAULT_KEY_TXT_FAMILY_INCOME_REGIST_RESID).update(ElementsAdditional.money_validation(sg,str(total_income)))
            
            self.disable_objts(self.key_to_disable_regist(),window,True,closeValue=False)
            self.event_buttons_residents(window, False, True, True, True, True)
            
        if event == DEFAULT_KEY_BTN_EDIT_REGIST_RESID:
            self.disable_objts(self.key_to_disable_regist(),window,False,closeValue=False)
            self.event_buttons_residents(window, True, False, False, False, True)
                
        if event == DEFAULT_KEY_BTN_DEL_REGIST_RESID:
            self.disable_objts(self.key_to_disable_regist(),window,True,closeValue=False)
            
            
    def event_inputs(self,sg, window, event, velue):
        #----------------------------EVENTOS DO CAMPO DE tabDadosPessoal-------------------------
               
        if ElementsAdditional.event_keyboard_enter(window, event,DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA):
            result = ElementsAdditional.valid_birth(sg, velue[DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA])
            self._event_have_information(window, result, DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA, 'Data incorreta!')
                
        if ElementsAdditional.event_keyboard_enter(window, event,DEFAULT_KEY_TEL_PERSONAL_DATA):
            result = ElementsAdditional.valid_cell_number(sg, velue[DEFAULT_KEY_TEL_PERSONAL_DATA])
            self._event_have_information(window, result, DEFAULT_KEY_TEL_PERSONAL_DATA, 'quantidade de digitos incorreta!')
            
        if ElementsAdditional.event_keyboard_enter(window, event,DEFAULT_KEY_CEL_PERSONAL_DATA):
            result = ElementsAdditional.valid_cell_number(sg, velue[DEFAULT_KEY_CEL_PERSONAL_DATA])
            self._event_have_information(window, result, DEFAULT_KEY_CEL_PERSONAL_DATA, 'quantidade de digitos incorreta!')
        
        if ElementsAdditional.event_keyboard_enter(window, event,DEFAULT_KEY_EMAIL_PERSONAL_DATA):
            result = ElementsAdditional.valid_email(sg, velue[DEFAULT_KEY_EMAIL_PERSONAL_DATA])
            self._event_have_information(window, result, DEFAULT_KEY_EMAIL_PERSONAL_DATA, 'formato do email incorreta!')
                
        if ElementsAdditional.event_keyboard_enter(window, event,DEFAULT_KEY_HOUSE_NUMBER_PERSONAL_DATA):
            result = ElementsAdditional.valid_just_number(sg, velue[DEFAULT_KEY_HOUSE_NUMBER_PERSONAL_DATA])
            self._event_have_information(window, result, DEFAULT_KEY_HOUSE_NUMBER_PERSONAL_DATA, 'Apenas valor númerico!')
                
        if ElementsAdditional.event_keyboard_enter(window, event,DEFAULT_KEY_CPF_PERSONAL_DATA):
            result = ElementsAdditional.valid_cpf(sg, velue[DEFAULT_KEY_CPF_PERSONAL_DATA])
            self._event_have_information(window, result, DEFAULT_KEY_CPF_PERSONAL_DATA, 'quantidades de digítos do CPF incorreta!')
            
        if ElementsAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_VOTER_TITLE_PERSONAL_DATA):
            result = ElementsAdditional.valid_titulo_eleitor(sg, velue[DEFAULT_KEY_VOTER_TITLE_PERSONAL_DATA])
            self._event_have_information(window, result, DEFAULT_KEY_VOTER_TITLE_PERSONAL_DATA, 'quantidade de digitos incorreta!')
                
        if ElementsAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_RG_PERSONAL_DATA):
            result = ElementsAdditional.valid_rg(sg, velue[DEFAULT_KEY_RG_PERSONAL_DATA])
            self._event_have_information(window, result, DEFAULT_KEY_RG_PERSONAL_DATA, 'Quantidade de digitos incorreta!')
        
        #----------------------------EVENTOS DO CAMPO DE frameConjuge-------------------------

        if ElementsAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_BIRTHDATE_SPOUSE):
            result = ElementsAdditional.valid_birth(sg, velue[DEFAULT_KEY_BIRTHDATE_SPOUSE])
            self._event_have_information(window, result, DEFAULT_KEY_BIRTHDATE_SPOUSE, 'Data incorreta!')
                
        if ElementsAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_TEL_SPOUSE):
            result = ElementsAdditional.valid_cell_number(sg, velue[DEFAULT_KEY_TEL_SPOUSE])
            self._event_have_information(window, result, DEFAULT_KEY_TEL_SPOUSE, 'Número de telefone incorreto!')
                
        if ElementsAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_CEL_SPOUSE):
            result = ElementsAdditional.valid_cell_number(sg, velue[DEFAULT_KEY_CEL_SPOUSE])
            self._event_have_information(window, result, DEFAULT_KEY_CEL_SPOUSE, 'Número de celular incorreto!')
                
        if ElementsAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_RG_SPOUSE):
            result = ElementsAdditional.valid_rg(sg, velue[DEFAULT_KEY_RG_SPOUSE])
            self._event_have_information(window, result, DEFAULT_KEY_RG_SPOUSE, 'Número de RG incorreto!')
        
        if ElementsAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_CPF_SPOUSE):
            result = ElementsAdditional.valid_cpf(sg, velue[DEFAULT_KEY_CPF_SPOUSE])
            self._event_have_information(window, result, DEFAULT_KEY_CPF_SPOUSE, 'Número de CPF incorreto!')
                
        if ElementsAdditional.event_keyboard_enter(window, event, DEFAULT_KEY_VOTER_TITLE_SPOUSE):
            result = ElementsAdditional.valid_titulo_eleitor(sg, velue[DEFAULT_KEY_VOTER_TITLE_SPOUSE])
            self._event_have_information(window, result, DEFAULT_KEY_VOTER_TITLE_SPOUSE, 'Número do Titulo de Eleitor incorreto!')

           
    def exec_layout(self, window, event, valuer):
       self.event_inputs(sg, window, event, valuer)
       self.event_other_infor(window, valuer)
       self.disable_input_conjuge(window, valuer, self._marital_status)
       self._event_table_regist_resid(window, event, valuer)
                


class registration:
    def __init__(self, conectionDB = None):
        self._conn = conectionDB
        self._class_register = register_personal_data()
        self._window_button_search = None
        self._btn_edit_clicked = False
        self._id_register_db = None
        
    def _load_layout(self):
        layout = [self._class_register.load_window_layout(),
            [sg.Button('Novo', key=DEFAULT_KEY_BTN_NEW), sg.Button('Cancelar', disabled=True, key=DEFAULT_KEY_BTN_CANCEL),sg.Button('Salvar',disabled=True, key=DEFAULT_KEY_BTN_SAVE), 
             sg.Button('Editar', disabled=True, key=DEFAULT_KEY_BTN_EDIT), sg.Button('Excluir', disabled=True, key=DEFAULT_KEY_BTN_DELETE)],
            [sg.HorizontalSeparator()],
            [sg.Button('Procurar', key=DEFAULT_KEY_BTN_SEARCH),sg.T(size=(5,1)), sg.Button('<<', key=DEFAULT_KEY_BTN_BACK_OFF_LAST), 
             sg.Button('<', key=DEFAULT_KEY_BTN_BACK_ONE),sg.Button('>', key=DEFAULT_KEY_BTN_ADVANCE_LAST), sg.Button('>>', key=DEFAULT_KEY_BTN_ADVANCE_ONE)]
            ]
            
        return layout
    
    def _loard_records_into_fields(self,window, name_table, keys_fields, name_id_table, id_register):
        fileds_and_field_db = self._conn._take_fields_records(name_table, keys_fields)      
        datas = self._conn.select_register(fileds_and_field_db.keys(), name_table, name_id_table, id_register)[0]
        datas = np.array(datas)

        for cont, key in enumerate(fileds_and_field_db.values()):
            if datas[cont] != None:
                if window.Element(key).Type == 'input':
                    window.Element(key).Update(datas[cont])
                elif window.Element(key).Type == 'combo':
                    window.Element(key).TKCombo.set(datas[cont])
                elif window.Element(key).Type == 'spind':
                    window.Element(key).TKStringVar.set(datas[cont])
        if len(datas) > 0:
            return True
        return False
    
    def _activate_registration_buttons(self,window, btnNew, btnCancel, btnSave, btnEdit, btnDel):
        window.Element(DEFAULT_KEY_BTN_NEW).update(disabled=btnNew)
        window.Element(DEFAULT_KEY_BTN_CANCEL).update(disabled=btnCancel)
        window.Element(DEFAULT_KEY_BTN_SAVE).update(disabled=btnSave)
        window.Element(DEFAULT_KEY_BTN_EDIT).update(disabled=btnEdit)
        window.Element(DEFAULT_KEY_BTN_DELETE).update(disabled=btnDel)

    def _activate_search_buttons(self, window, buttons):
        window.Element(DEFAULT_KEY_BTN_SEARCH).update(disabled=buttons)
        window.Element(DEFAULT_KEY_BTN_BACK_OFF_LAST).update(disabled=buttons)
        window.Element(DEFAULT_KEY_BTN_BACK_ONE).update(disabled=buttons)
        window.Element(DEFAULT_KEY_BTN_ADVANCE_LAST).update(disabled=buttons)
        window.Element(DEFAULT_KEY_BTN_ADVANCE_ONE).update(disabled=buttons)
    
    def _input_event_buttons(self, window, event, value):
        key_to_update = [DEFAULT_KEY_NOME_PERSONAL_DATA, DEFAULT_KEY_SEX_PERSONAL_DATA,
                         DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA, DEFAULT_KEY_AGE_PERSONAL_DATA,
                         DEFAULT_KEY_NATURALNESS_PERSONAL_DATA, DEFAULT_KEY_UF_PERSONAL_DATA,
                         DEFAULT_KEY_TEL_PERSONAL_DATA, DEFAULT_KEY_CEL_PERSONAL_DATA,
                         DEFAULT_KEY_EMAIL_PERSONAL_DATA, DEFAULT_KEY_ADDRESS_PERSONAL_DATA,
                         DEFAULT_KEY_DISTRICT_PERSONAL_DATA, DEFAULT_KEY_RG_PERSONAL_DATA,
                         DEFAULT_KEY_HOUSE_NUMBER_PERSONAL_DATA, DEFAULT_KEY_ISSUING_BODY_PERSONAL_DATA,
                         DEFAULT_KEY_CPF_PERSONAL_DATA, DEFAULT_KEY_CNH_PERSONAL_DATA, 
                         DEFAULT_KEY_VOTER_TITLE_PERSONAL_DATA, DEFAULT_KEY_CONSIDER_PERSONAL_DATA,
                         DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA, DEFAULT_KEY_SCHOOLING_PERSONAL_DATA,
                         #-----------------------key tab other_information------------------------------
                         DEFAULT_KEY_COMB_WORKS, DEFAULT_KEY_INP_WHERE,DEFAULT_KEY_TXT_PROFESSION,
                         DEFAULT_KEY_COMB_RETIREE, DEFAULT_KEY_BENEF_CAMB_SOCI_PROG,
                         DEFAULT_KEY_INCOME_COMB_INCOME, DEFAULT_KEY_COMB_HAVE_CHILDREM, 
                         DEFAULT_KEY_HOW_MANY_CHILDREM,DEFAULT_KEY_LIVES_DISABLED_OR_ELDERLY,
                         DEFAULT_KEY_DISABLED_ELDERLY_HOW_MANY, DEFAULT_KEY_COMB_RURAL_URBAN_BENEFICIARY,
                         DEFAULT_KEY__COMB_OWNS_CAR,DEFAULT_KEY_OWNS_CAR_HOW_MANY, 
                         DEFAULT_KEY__COMB_HAS_MOTORCICLE, DEFAULT_KEY_HAS_MOTORCICLE_HOW_MANY,
                         DEFAULT_KEY_COMB__HAVE_FRIDGE, DEFAULT_KEY_HAVE_FRIDGE_HOW_MANY,
                         DEFAULT_KEY_COMB__HAVE_TELEVI,DEFAULT_KEY_HAVE_TELEVI_HOW_MANY,
                         DEFAULT_KEY_COMB__HAVE_COMPUTER, DEFAULT_KEY_HAVE_COMPUTER_HOW_MANY,
                         DEFAULT_KEY_COMB__HAVE_INTERNET, 
                         DEFAULT_KEY_COMB__HAVE_ACESS_ELECTRI,DEFAULT_KEY_COMB__HAVE_DRAINAG_WATER, 
                         DEFAULT_KEY_COMB_ONLY_OWNER, DEFAULT_KEY_TXT_ANOTHER_OWNER, DEFAULT_KEY_TXT_STILL_TIME,
                         DEFAULT_KEY_COMB_ANOTHER_PROPERTY, DEFAULT_KEY_ANOTHER_PROPERTY_HOW_MANY,
                         DEFAULT_KEY_TXT_ANOTHER_PROPERTY_WHERE, DEFAULT_KEY_COMB_REAL_ESTATE_CONSTRUC,
                         DEFAULT_KEY_PROPERTY_USED_FOR, DEFAULT_KEY_TXT_FRONT, 
                         DEFAULT_KEY_TXT_RIGHT, DEFAULT_KEY_TXT_LEFT, 
                         DEFAULT_KEY_TXT_FUNDS, DEFAULT_KEY_COMB_TYPE, 
                         DEFAULT_KEY_COMB_IS_WALLED, DEFAULT_KEY_COMB_BATCH_POSITION, 
                         DEFAULT_KEY_COMB_STATE_BUILDINGS, DEFAULT_KEY_COMB_BUILDING_TYPE, DEFAULT_KEY_COMB_IS_BEDRIDDEN,
                         DEFAULT_KEY_NUMB_FLOORS, DEFAULT_KEY_ROOMS,
                         DEFAULT_KEY_BATHROOMS
                         ]
        
        if event == DEFAULT_KEY_BTN_NEW:
            self._class_register.disable_objts(key_to_update,window, False, True)
            self._activate_registration_buttons(window, btnNew=True, btnCancel=False, btnSave=False, btnEdit=True, btnDel=True)
            self._activate_search_buttons(window, buttons=True)
            #event buttons registration residents
            self._class_register.event_buttons_residents(window, False, True, True, True, True)            
            
        elif event == DEFAULT_KEY_BTN_CANCEL:
            self._btn_edit_clicked = False
            self._class_register.disable_objts(key_to_update,window, True,False)
            
            if value[DEFAULT_KEY_NOME_PERSONAL_DATA] != '':
                self._activate_registration_buttons(window, btnNew=False, btnCancel=True, btnSave=True, btnEdit=False, btnDel=False)
            else:
                self._activate_registration_buttons(window, btnNew=False, btnCancel=True, btnSave=True, btnEdit=True, btnDel=True)
                
            self._activate_search_buttons(window, buttons=False)
            #event buttons registration residents
            self._class_register.event_buttons_residents(window, True, True, True, True, False)
            
            #disable functions to register residents tab
            self._class_register.disable_objts(self._class_register.key_to_disable_regist(), window,True,closeValue=True)
            self._class_register.event_buttons_residents(window, True, True, True, True, True)
            
            for item in window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.get_children():
                window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.delete(item)
                
            for key in key_to_update:
                self._class_register._change_fields_color(window, key, "white")
            
        elif event == DEFAULT_KEY_BTN_SAVE:
            resultFields = self._class_register.required_fields(window, event,value)
            
            
            if  resultFields == False:
                #window[DEFAULT_KEY_PERSONAL_DATA_TABGROUP].select()
                sg.popup_error('ERRO!\ntodos os campos em vermelho são obrigatorios.\n', keep_on_top=True) 
            else:
                keys_numeric_fields = [DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA, DEFAULT_KEY_TEL_PERSONAL_DATA,DEFAULT_KEY_CEL_PERSONAL_DATA,
                                           DEFAULT_KEY_RG_PERSONAL_DATA, DEFAULT_KEY_CPF_PERSONAL_DATA]
                keys_numeric = [DEFAULT_KEY_BIRTHDATE_SPOUSE, DEFAULT_KEY_CEL_SPOUSE,DEFAULT_KEY_TEL_SPOUSE, DEFAULT_KEY_RG_SPOUSE,DEFAULT_KEY_CPF_SPOUSE]
                
                if self._btn_edit_clicked == False: #Save register
                    
                    self._id_register_db = self._conn.insert_register(self._class_register.get_key_values(value,self._class_register.keys_fields_tab(), keys_numeric_fields), self._conn.register_people, self._conn.id_register_people)
                
                    if value[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == self._class_register._marital_status:
                        self._conn.insert_register(self._class_register.get_key_values(value,self._class_register.keys_fields_spouse(), keys_numeric) , self._conn.register_spouse, self._conn.id_register_spouse, self._id_register_db)
                    
                    if len(value[DEFAULT_KEY_TABLE_RESIDENTS]) > 0:
                        datas = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values
                        
                        for register in datas:
                            self._conn.insert_register(register, self._conn.register_residents, self._conn.id_register_residents, self._id_register_db)
                    
                else: #save edition register
                    self._conn.update_register(self._class_register.get_key_values(value,self._class_register.keys_fields_tab(), keys_numeric_fields), self._conn.register_people, self._conn.id_register_people, self._id_register_db)
                    
                    register_exist = self._conn.query_record(self._conn.register_spouse, self._conn.id_to_table_register_spouse, self._id_register_db)
                    
                    if value[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == self._class_register._marital_status:
                        if register_exist:
                            self._conn.update_register(self._class_register.get_key_values(value,self._class_register.keys_fields_spouse(), keys_numeric), self._conn.register_spouse, self._conn.id_register_spouse, self._id_register_db)
                        else:
                            self._conn.insert_register(self._class_register.get_key_values(value,self._class_register.keys_fields_spouse(), keys_numeric) , self._conn.register_spouse, self._conn.id_register_spouse, self._id_register_db)
                    
                    self._conn.commit()
                    
                    #if len(value[DEFAULT_KEY_TABLE_RESIDENTS]) > 0:
                    #    datas = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values
                        
                    
                self._class_register.disable_objts(key_to_update, window, True,False)
                self._class_register.disable_objts(self._class_register.keys_fields_spouse(), window, True, False)
                
                self._activate_registration_buttons(window, btnNew=False, btnCancel=True, btnSave=True, btnEdit=False, btnDel=False)
                self._activate_search_buttons(window, buttons=False)
                #event buttons registration residents
                self._class_register.event_buttons_residents(window, False, True, True, True, False)
            
        elif event == DEFAULT_KEY_BTN_EDIT:
            self._btn_edit_clicked = True
            self._class_register.disable_objts(key_to_update,window, False,False)
            self._activate_registration_buttons(window, btnNew=True, btnCancel=False, btnSave=False, btnEdit=True, btnDel=True)
            self._activate_search_buttons(window, buttons=True)
            #event buttons registration residents
            self._class_register.event_buttons_residents(window, False, True, True, True, True)
        
        elif event == DEFAULT_KEY_BTN_DELETE:  
            self._class_register.disable_objts(key_to_update, window, True,True)
            self._activate_registration_buttons(window, btnNew=False, btnCancel=True, btnSave=True, btnEdit=False, btnDel=False)
            self._activate_search_buttons(window, buttons=False)
            self._class_register.event_buttons_residents(window, True, True, True, True, True)
        
        if event == DEFAULT_KEY_BTN_SEARCH:
            self._class_register.disable_objts(key_to_update, window, True,True)
            self._class_register.disable_objts(self._class_register.keys_fields_spouse(), window, True)
            
            search = button_search(sg, self._conn)
            self._window_button_search, self._id_register_db = search.window_button_search()
                        
            register_ok = self._loard_records_into_fields(window, self._conn.register_people, self._class_register.keys_fields_tab(), self._conn.id_register_people, self._id_register_db)
        
            register_spouse_exist = self._conn.query_record(self._conn.register_spouse, self._conn.id_to_table_register_spouse, self._id_register_db)
            
            if register_spouse_exist is True:
                self._loard_records_into_fields(window, self._conn.register_spouse, self._class_register.keys_fields_spouse(), self._conn.id_to_table_register_spouse, self._id_register_db)
        
            if register_ok:
                self._activate_registration_buttons(window, btnNew=False, btnCancel=True, btnSave=True, btnEdit=False, btnDel=False)
            
    def exec_classes(self):
        window_regitration = sg.Window('Cadastro', self._load_layout(),icon=r'image/iconLogo.ico',keep_on_top=True, modal=True)
        while(True):
            event, value = window_regitration.read(timeout=100)  

            if event == sg.WINDOW_CLOSED:
                break;
                
            self._input_event_buttons(window_regitration, event, value)
            self._class_register.exec_layout(window_regitration, event, value)
            
        if self._window_button_search != None:
            self._window_button_search.close()
            
        window_regitration.close()
        
        
class main_layout: 
    def __init__(self):
        self._conn = Database()
        self._class_registration = registration(self._conn)
        self._current_screen = self.get_monitor_from_coord(200, 200)
        
    def get_monitor_from_coord(self, x, y):
        monitors = screeninfo.get_monitors()
    
        for m in reversed(monitors):
            if m.x <= x <= m.width + m.x and m.y <= y <= m.height + m.y:
                return m
        return monitors[0]
        
    def layout(self):
        image = 'image/temaLogo.png'
        menu = [ [sg.Menu(
                [   ['&Menu', ['&Cadastros', '&Registros', 'E&xit']],
                    ['C&ontratos', ['&Gerar Tegs', 'Lista Contratos', '&Importar contrato', 'G&erar contrato']],
                    ['Sobre', ['Dados desenvolvedor']]
                ], background_color='#176d81')]]
        layout = [menu,
                  [sg.Image(image,  background_color='white', size=(self._current_screen.width, self._current_screen.height))]
                  ]
        return layout
    
    def exec_classes(self):
        window = sg.Window('Janela Principal', self.layout(),icon=r'image/iconLogo.ico',default_button_element_size=(25,1), background_color='white', resizable=True, size=(self._current_screen.width, self._current_screen.height))
        
        while(True):
            event, valuer = window.read(timeout=100)
            
            if event == 'Cadastros':
                self._class_registration.exec_classes()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Exit':
                break
        window.close()
        
if __name__ == '__main__':
    
    app = main_layout()
    app.exec_classes()
























