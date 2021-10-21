# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:41:31 2021

@author: André luiz Pires Guimarães
"""
from elementsAdditional import ElementsAdditional
from Layouts.search_register_person import Search_register_person
from Layouts.import_contract import Import_contract
import PySimpleGUI as sg

DEFAULT_KEY_INPUT_ID = '-ID_DO_REGISTRO_DA_BASE_DE_DADOS-'
DEFAULT_KEY_INPUT_NAME = '-NOME-'
DEFAULT_KEY_INPUT_CPF = '-CPF-'
DEFAULT_KEY_INPUT_CONTRACT = '-CONTRATO-'

DEFAULT_KEY_BTN_SEARCH_RECORD = '-PESQUISAR_REGISTRO-'
DEFAULT_KEY_BTN_SEARCH_CONTRACT = '-PESQUISAR_CONTRATO-'
DEFAULT_KEY_BTN_GENERATE = '-GERAR_CONTRATO-'
DEFAULT_KEY_BTN_CANCEL = '-CANCELAR_INFORMACOES-'

class Generate_contract:
    def __init__(self, conectionDB):
        self._conn = conectionDB
        self._class_search_register_person = Search_register_person(conectionDB)
        self._class_import_contract = Import_contract(return_only_the_path=True)
        
        self.elemAdditional = ElementsAdditional()
        
        self._path_contract = None
        self._id_register_db = None
        
    def layout(self):
        construct_layout = [
                        [sg.T('ID:', size=(5)), sg.Input(size=(10),key=DEFAULT_KEY_INPUT_ID, disabled=True)],
                        [sg.T('Nome:', size=(5)), sg.Input(key=DEFAULT_KEY_INPUT_NAME, disabled=True)],
                        [sg.T('CPF:', size=(5)), sg.Input(size=(15),key=DEFAULT_KEY_INPUT_CPF, disabled=True)],
                        [sg.Button('Pesquisar', key=DEFAULT_KEY_BTN_SEARCH_RECORD)],
                        [sg.HorizontalSeparator()],
                        [sg.T('Contrato:'), sg.Input(key=DEFAULT_KEY_INPUT_CONTRACT, disabled=True)],
                        [sg.Button('Pesquisar', key=DEFAULT_KEY_BTN_SEARCH_CONTRACT)],
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
        
    def __contract_files(self, window):
        path = self._class_import_contract.exec_classes()
        
        if path != -1:
            self._path_contract = path
            window.Element(DEFAULT_KEY_INPUT_CONTRACT).update(self._path_contract[self._path_contract.rindex('/')+1:len(self._path_contract)])
            
    def __enabled_btns(self, window, disabled):
        window.Element(DEFAULT_KEY_BTN_GENERATE).update(disabled=disabled)
        window.Element(DEFAULT_KEY_BTN_CANCEL).update(disabled=disabled)
        
    def __clear_inputs(self, window, is_to_clean = True):
        window.Element(DEFAULT_KEY_INPUT_ID).update('')
        window.Element(DEFAULT_KEY_INPUT_NAME).update('')
        window.Element(DEFAULT_KEY_INPUT_CPF).update('')
        window.Element(DEFAULT_KEY_INPUT_CONTRACT).update('')
    
    def exec_class(self):
        window = sg.Window('Gerar contrato para registros', self.layout(),icon=r'image/iconLogo.ico', keep_on_top=True, modal=True)
        while(True):
            event, value = window.read(timeout=100)
            
            if event == sg.WINDOW_CLOSED:
                break
            
            if event == DEFAULT_KEY_BTN_SEARCH_RECORD:
                self.__database_records(window)
                
            if event == DEFAULT_KEY_BTN_SEARCH_CONTRACT:
                self.__contract_files(window)
                
            if value[DEFAULT_KEY_INPUT_NAME] != '' and value[DEFAULT_KEY_INPUT_CONTRACT] != '':
                self.__enabled_btns(window, False)
            else:
                self.__enabled_btns(window, True)
            
            if event == DEFAULT_KEY_BTN_CANCEL:
                self.__clear_inputs(window, True)
            
        window.close()
