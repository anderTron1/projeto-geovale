# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:41:31 2021

@author: André luiz Pires Guimarães
"""

from Layouts.search_register_person import Search_register_person

import PySimpleGUI as sg

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
        
        self._window_button_search = None
        self._id_register_db = None
        
    def layout(self):
        construct_layout = [
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
    
    def exec_class(self):
        window = sg.Window('Gerar contrato para registros', self.layout(),icon=r'image/iconLogo.ico', keep_on_top=True, modal=True)
        while(True):
            event, value = window.read(timeout=100)
            
            if event == DEFAULT_KEY_BTN_SEARCH_RECORD:
                search = Search_register_person(self._conn)
                self._window_button_search, self._id_register_db = search.window_button_search()
            
            if event == sg.WINDOW_CLOSED:
                break
        window.close()
