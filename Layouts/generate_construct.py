# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:41:31 2021

@author: André luiz Pires Guimarães
"""
from elementsAdditional import ElementsAdditional
from Layouts.keys_names.keys_to_registration import *
from Layouts.search_register_person import Search_register_person
from Layouts.import_contract import Import_contract
import PySimpleGUI as sg
import os

from docx import Document

DEFAULT_KEY_INPUT_ID = '-ID_DO_REGISTRO_DA_BASE_DE_DADOS-'
DEFAULT_KEY_INPUT_NAME = '-NOME-'
DEFAULT_KEY_INPUT_CPF = '-CPF-'
DEFAULT_KEY_INPUT_CONTRACT = '-CONTRATO-'
DEFAULT_KEY_INPUT_NAME_FILE_TO_SAVE = '<<-NOME_DO_ARQUIVO_PARA_SARVAR->>'

DEFAULT_KEY_BTN_SEARCH_RECORD = '-PESQUISAR_REGISTRO-'
DEFAULT_KEY_BTN_SEARCH_CONTRACT = '-PESQUISAR_CONTRATO-'
DEFAULT_KEY_BTN_GENERATE = '-GERAR_CONTRATO-'
DEFAULT_KEY_BTN_CANCEL = '-CANCELAR_INFORMACOES-'


class Generate:
    def __init__(self):
        super()
        
    def lines(self,inline, dict_sub):
        for i in range(len(inline)):
            paragr = inline[i].text
            for text in dict_sub.keys():
                if paragr.find(text) != -1:
                    texto = paragr.replace(text, str(dict_sub[text]))
                    inline[i].text = texto
                    paragr = texto
    
    def update_docx(self, name, dict_save, save_as, dict_sub):
        save = True
        if name.find('.docx') == -1:
            sg.popup_error('O arquivo não é um formato docx')
        else:
            document = Document(name)
            
            #atualizando paragrafos
            for paragraph in document.paragraphs:
                self.lines(paragraph.runs, dict_sub)
                
            #atualizar tabelas
            for table in document.tables:
                for i, line in enumerate(table.rows):
                    for cell in line.cells:
                        for paragraph in cell.paragraphs:
                            self.lines(paragraph.runs, dict_sub)
            
            try:
                document.save(dict_save+'/'+save_as+'.docx')
            except:
                save = False
        return save
        
        
#nomes = {'ACADÊMICO': 'to nem ai', 'serem': 'ja foram', '27':'12345'}
#update_docx('testttt.dss', nomes)

        

class Generate_contract:
    def __init__(self, conectionDB):
        self._conn = conectionDB
        self._class_search_register_person = Search_register_person(conectionDB)
        self._class_import_contract = Import_contract(return_only_the_path=True)
        
        self.elemAdditional = ElementsAdditional()
        
        self._path_contract = None
        self._id_register_db = None
        
        self.__generate = Generate()
        
    def layout(self):
        construct_layout = [
                        [sg.T('ID:', size=(5)), sg.Input(size=(10),key=DEFAULT_KEY_INPUT_ID, disabled=True)],
                        [sg.T('Nome:', size=(5)), sg.Input(key=DEFAULT_KEY_INPUT_NAME, disabled=True)],
                        [sg.T('CPF:', size=(5)), sg.Input(size=(15),key=DEFAULT_KEY_INPUT_CPF, disabled=True)],
                        [sg.Button('Pesquisar', key=DEFAULT_KEY_BTN_SEARCH_RECORD)],
                        [sg.HorizontalSeparator()],
                        [sg.T('Contrato:'), sg.Input(key=DEFAULT_KEY_INPUT_CONTRACT, disabled=True)],
                        [sg.Button('Pesquisar', key=DEFAULT_KEY_BTN_SEARCH_CONTRACT, disabled=True)],
                        [sg.T('Salvar como:'), sg.Input(size=30, key=DEFAULT_KEY_INPUT_NAME_FILE_TO_SAVE, disabled=True), sg.T('.docx')],
                        [sg.Button('Gerar', key=DEFAULT_KEY_BTN_GENERATE, disabled=True),
                         sg.Button('Cancelar', key=DEFAULT_KEY_BTN_CANCEL, disabled=True)]
                    ]
        return construct_layout
    
    def __database_records(self, window):
        KEY_ID = 0
        KEY_NAME = 1
        KEY_CPF = 2
        
        search = Search_register_person(self._conn)
        _, self._id_register_db = search.window_button_search()
            
        register_database = self._conn.select_register([self._conn.id_register_people,'name', 'cpf'], self._conn.register_people, self._conn.id_register_people, self._id_register_db)
        
        if len(register_database) > 0:
            window.Element(DEFAULT_KEY_INPUT_ID).update(register_database[0][KEY_ID])
            window.Element(DEFAULT_KEY_INPUT_NAME).update(register_database[0][KEY_NAME])
            window.Element(DEFAULT_KEY_INPUT_CPF).update(self.elemAdditional.valid_cpf(str(register_database[0][KEY_CPF])))
        
    def __contract_files(self, window, value):
        path = self._class_import_contract.exec_classes()
        
        if path != -1:
            self._path_contract = path
            window.Element(DEFAULT_KEY_INPUT_CONTRACT).update(self._path_contract[self._path_contract.rindex('/')+1:len(self._path_contract)])
            window.Element(DEFAULT_KEY_INPUT_NAME_FILE_TO_SAVE).update(value[DEFAULT_KEY_INPUT_NAME])
            
    def __enabled_btns(self, window, disabled):
        window.Element(DEFAULT_KEY_BTN_GENERATE).update(disabled=disabled)
        window.Element(DEFAULT_KEY_BTN_CANCEL).update(disabled=disabled)
        
    def __clear_inputs(self, window, is_to_clean = True):
        window.Element(DEFAULT_KEY_INPUT_ID).update('')
        window.Element(DEFAULT_KEY_INPUT_NAME).update('')
        window.Element(DEFAULT_KEY_INPUT_CPF).update('')
        window.Element(DEFAULT_KEY_INPUT_CONTRACT).update('')
        window.Element(DEFAULT_KEY_INPUT_NAME_FILE_TO_SAVE).update('')
    
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
                DEFAULT_KEY_BATCH_REGU_BATCH,           DEFAULT_KEY_BATCH_REGU_BLOCK,
                DEFAULT_KEY_BATCH_REGU_BATCH_REGULARIZAR_DISTRICT, DEFAULT_KEY_BATCH_REGU_AREA,
                DEFAULT_KEY_BATCH_REGU_STREET_LOTE,
                
                #-------------------------KEY to tab other_information----------------------------
                DEFAULT_KEY_COMB_WORKS,                 DEFAULT_KEY_INP_WHERE,
                DEFAULT_KEY_TXT_PROFESSION,             DEFAULT_KEY_COMB_RETIREE,
                DEFAULT_KEY_BENEF_CAMB_SOCI_PROG,       DEFAULT_KEY_INCOME_COMB_INCOME,
                DEFAULT_KEY_COMB_HAVE_CHILDREM,         DEFAULT_KEY_HOW_MANY_CHILDREM,
                DEFAULT_KEY_LIVES_DISABLED_OR_ELDERLY,  DEFAULT_KEY_DISABLED_ELDERLY_HOW_MANY,
                DEFAULT_KEY_COMB_OWN_RURAL_PROPERTY, 
                
                DEFAULT_KEY__COMB_OWNS_CAR,         DEFAULT_KEY_OWNS_CAR_HOW_MANY,
                DEFAULT_KEY__COMB_HAS_MOTORCICLE,   DEFAULT_KEY_HAS_MOTORCICLE_HOW_MANY,
                DEFAULT_KEY_COMB__HAVE_FRIDGE,      DEFAULT_KEY_HAVE_FRIDGE_HOW_MANY,
                DEFAULT_KEY_COMB__HAVE_TELEVI,      DEFAULT_KEY_HAVE_TELEVI_HOW_MANY,
                DEFAULT_KEY_COMB__HAVE_COMPUTER,    DEFAULT_KEY_HAVE_COMPUTER_HOW_MANY,
                DEFAULT_KEY_COMB__HAVE_INTERNET,    DEFAULT_KEY_COMB__HAVE_ACESS_ELECTRI,
                DEFAULT_KEY_COMB__HAVE_DRAINAG_WATER, 
                
                #--------------------------KEY FRAME PROPERTY CONDITIONS---------------------------
                DEFAULT_KEY_COMB_ONLY_OWNER,             DEFAULT_KEY_TXT_ANOTHER_OWNER,
                DEFAULT_KEY_TXT_STILL_TIME,              DEFAULT_KEY_COMB_HAVE_ANOTHER_URBAN_PROPERTY,
                DEFAULT_KEY_ANOTHER_PROPERTY_HOW_MANY,   DEFAULT_KEY_TXT_ANOTHER_PROPERTY_WHERE,
                DEFAULT_KEY_COMB_REAL_ESTATE_CONSTRUC,   DEFAULT_KEY_PROPERTY_USED_FOR,
                
                DEFAULT_KEY_TXT_FRONT,   DEFAULT_KEY_TXT_RIGHT,
                DEFAULT_KEY_TXT_LEFT,    DEFAULT_KEY_TXT_FUNDS,
                
                DEFAULT_KEY_COMB_TYPE,               DEFAULT_KEY_COMB_IS_WALLED,
                DEFAULT_KEY_COMB_BATCH_POSITION,     DEFAULT_KEY_COMB_STATE_BUILDINGS,
                DEFAULT_KEY_COMB_BUILDING_TYPE,      DEFAULT_KEY_COMB_IS_BEDRIDDEN,
                DEFAULT_KEY_NUMB_FLOORS,             DEFAULT_KEY_ROOMS,
                DEFAULT_KEY_BATHROOMS,               DEFAULT_KEY_PROJECT_SERVICES,
                DEFAULT_KEY_TYPE_FRAMEWORK]
        return keys
    
    def get_datas_db(self, value):
        name_register = self._conn.register_people
        name_id_register = self._conn.id_register_people
        id_register = int(value[DEFAULT_KEY_INPUT_ID])
        
        key_value = dict()
        
        fileds_and_field_db = self._conn._take_fields_records(name_register, self.keys_fields_tab())
        
        register_db = self._conn.select_register(fileds_and_field_db.keys(), name_register,name_id_register, id_register)[0]
        
        for cont, key in enumerate(fileds_and_field_db.values()):
            if register_db[cont] != None:
                key_value[key] = register_db[cont]

        save_in_directory = sg.tk.filedialog.askdirectory(initialdir=os.path.abspath(os.sep))
        
        save = self.__generate.update_docx(self._path_contract, save_in_directory, value[DEFAULT_KEY_INPUT_NAME_FILE_TO_SAVE], key_value)
        if save:
            sg.popup('Arquivo gerado e salvo com sucesso!', keep_on_top=True)
        
    def exec_class(self):
        window = sg.Window('Gerar contrato para registros', self.layout(),icon=r'image/iconLogo.ico', keep_on_top=False, modal=True)
        while(True):
            event, value = window.read(timeout=100)
            
            if event == sg.WINDOW_CLOSED:
                break
            
            if event == DEFAULT_KEY_BTN_SEARCH_RECORD:
                self.__database_records(window)
                
            if event == DEFAULT_KEY_BTN_SEARCH_CONTRACT:
                self.__contract_files(window, value)
                
            if value[DEFAULT_KEY_INPUT_NAME] == '':
                window.Element(DEFAULT_KEY_BTN_SEARCH_CONTRACT).update(disabled=True)
                window.Element(DEFAULT_KEY_INPUT_NAME_FILE_TO_SAVE).update(disabled=True)
            else:
                window.Element(DEFAULT_KEY_BTN_SEARCH_CONTRACT).update(disabled=False)
                window.Element(DEFAULT_KEY_INPUT_NAME_FILE_TO_SAVE).update(disabled=False)
                
            if value[DEFAULT_KEY_INPUT_NAME] != '' and value[DEFAULT_KEY_INPUT_CONTRACT] != '' and value[DEFAULT_KEY_INPUT_NAME_FILE_TO_SAVE] != '':
                self.__enabled_btns(window, False)
            else:
                self.__enabled_btns(window, True)
            
            if event == DEFAULT_KEY_BTN_GENERATE:
                self.get_datas_db(value)
                self.__clear_inputs(window, True)
                
            if event == DEFAULT_KEY_BTN_CANCEL:
                self.__clear_inputs(window, True)
            
        window.close()
