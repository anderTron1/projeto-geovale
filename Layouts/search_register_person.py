#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:39:48 2021

@author: andre
"""
from elementsAdditional import ElementsAdditional

import PySimpleGUI as sg

#--------------------------KEY TABLES-------------------------------------
DEFAULT_KEY_TABLE_SEARCH_REGISTRATION = '-SEARCH_REGISTRATION-'

DEFAULT_KEY_BTN_SEARCH = '-BTN_SEARCH-'
DEFAULT_KEY_TXT_SEARCH_REGISTRATION_CPF = '-SEARCH_REGISTRATION_CPF-'
DEFAULT_KEY_TXT_SEARCH_REGISTRATION_NAME = '-SEARCH_REGISTRATION_NAME-'

class Search_register_person:
    def __init__(self, sg, conectionDB=None):
        self._conn = conectionDB
        self.elem = ElementsAdditional()
        self._datas = None
        self._id_to_name = 0
        self._window = self._layout()
        
    
    def _databases_db(self):
        return self._conn.select_register([self._conn.id_register_people,'name', 'cpf'], self._conn.register_people, self._conn.id_register_people)
    
    def _table_search(self):
        headings = ['ID','Nome', 'CPF']
        self._datas = self._databases_db()
        table = self.elem.Table(sg, headings, DEFAULT_KEY_TABLE_SEARCH_REGISTRATION, dados = self._datas , col_width=15)
        return table
    
    def _layout(self):
        self._search = [[sg.T('Nome:', size=(5,1)), sg.Input(size=(25), key=DEFAULT_KEY_TXT_SEARCH_REGISTRATION_NAME)],
                  [sg.T('CPF:', size=(5,1)), sg.Input(size=(25), key=DEFAULT_KEY_TXT_SEARCH_REGISTRATION_CPF)],
                  [sg.Button('Procurar', key=DEFAULT_KEY_BTN_SEARCH)]
                  ]
        
        layout = [[sg.Frame('Procurar cliente por:', self._search)], [self._table_search()]]
        windows = sg.Window('Procurar cliente', layout, element_justification='center', default_element_size=(40,1), keep_on_top=True, modal=True)
        return windows
    
    def _search_event(self, id_table, key, window, value, is_cpf = False):
        not_found = False
        id_to = 0
        for cont in range(len(self._datas)):
            if str(self._datas[cont][id_table]) == value[key]:
                if is_cpf != True:
                    id_to += cont+1
                else:
                    self._id_to_name += cont+1
                not_found = True
                break
        if not_found:
            window.Element(DEFAULT_KEY_TABLE_SEARCH_REGISTRATION).TKTreeview.selection_set(id_to)
        else:
            sg.popup(f'ERRO!\nO registro {value[key]} não foi encontrado', keep_on_top=True)

    def _event_btn(self, window, event, value):
        if event == DEFAULT_KEY_BTN_SEARCH:
            if value[DEFAULT_KEY_TXT_SEARCH_REGISTRATION_NAME] != '':
                self._search_event(1,DEFAULT_KEY_TXT_SEARCH_REGISTRATION_NAME, window, value)
            elif value[DEFAULT_KEY_TXT_SEARCH_REGISTRATION_CPF] != '':
                self._search_event(2,DEFAULT_KEY_TXT_SEARCH_REGISTRATION_CPF, window, value)
    
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
                if len(self._window.Element(DEFAULT_KEY_TABLE_SEARCH_REGISTRATION).TKTreeview.selection()) > 0:
                    rows = self._window.Element(DEFAULT_KEY_TABLE_SEARCH_REGISTRATION).SelectedRows[0]
                    id = self._window.Element(DEFAULT_KEY_TABLE_SEARCH_REGISTRATION).Values[int(rows)][0]
                    closed = True
                    break
            self._event_btn(self._window, event, value)
            
        if closed is True:
            self._window.close()
            return None, id
        return self._window, None