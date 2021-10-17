#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 13:47:57 2021

@author: andre
"""


from elementsAdditional import ElementsAdditional     
import PySimpleGUI as sg

import os
import shutil
import subprocess

#--------------------------KEYS TABLE IMPORT CONTRACT----------------------
DEFAULT_KEY_BTN_OPEN = '-ABRIR-'
DEFAULT_KEY_BTN_DELET = '-DELETE-'
DEFAULT_KEY_BTN_SELECT = '-SELECIONAR-'
DEFAULT_KEY_INP_PATH = '-CAMINHO_ARQUIVO-'
DEFAULT_KEY_BTN_IMPORT = '-BTN_IMPORTAR-'
DEFAULT_KEY_INPUT_SEARCH_SELECT = '-PROCURAR_REGISTRO_SELECIONADO-'


DEFAULT_KEY_TABLE_INPORT_CONTRACT = '-INPORT_CONTRACT-'

class Import_contract:
        
    def __init__(self):
        self.elem = ElementsAdditional()
        self.path_docs = 'database/imported_documents'
        self.rows_table = None
        
    def _table_search(self):
        headings = ['Contratos salvos']
        self.rows_table = self.files_to_table(self.path_docs)
        table = None
        if self.rows_table != None:

            table = self.elem.Table(sg, headings, DEFAULT_KEY_TABLE_INPORT_CONTRACT,  dados=self.rows_table, col_width=70, justification='left')
        else:
            table = self.elem.Table(sg, headings, DEFAULT_KEY_TABLE_INPORT_CONTRACT, col_width=70)
        return table
    
    def _delete_regist(self, window, key, element_table, id_selection):
        if id_selection != -1:
            name = element_table
            confirm = sg.popup_ok_cancel('Realmente deseja excluir esse arquivo?', keep_on_top=True)
            if confirm == 'OK':
                window.Element(key).TKTreeview.delete(id_selection)
            
                arq = self.path_docs + '/' + name[0]
                #del(self.rows_table[id_selection])
                os.remove(arq)
                sg.popup('Arquivo deletado', keep_on_top=True)
    
    def _search_register(self, window, record_to_select):
        datas = window.Element(DEFAULT_KEY_TABLE_INPORT_CONTRACT).Values

        print(datas)

        id_table = -1

        print(datas)
        for cont, element in reversed(list(enumerate(datas))):
            print(element, 'selec: ', record_to_select)
            print(element[0].find(str(record_to_select)))
            if element[0].find(str(record_to_select)) != -1:
                id_table = cont+1
                break
        
        return id_table
        
    
    def layout(self):
        layout = [
                    [sg.T('Contrato'), sg.Input(key=DEFAULT_KEY_INPUT_SEARCH_SELECT), sg.Button('Selecionar', key=DEFAULT_KEY_BTN_SELECT)],
                    [self._table_search()],
                    [sg.Button('Abrir', key=DEFAULT_KEY_BTN_OPEN, disabled=True), sg.Button('Excluir', key=DEFAULT_KEY_BTN_DELET, disabled=True)],
                    [sg.Input(key=DEFAULT_KEY_INP_PATH, disabled=True, size=55), sg.Button('Importar', key=DEFAULT_KEY_BTN_IMPORT)],
                    [sg.FileBrowse(button_text= 'Importar Contrato', target=DEFAULT_KEY_INP_PATH,tooltip='Importar novo contrato para o sistema', file_types=(('Arquivo no Formato', "*.docx"),))]
                ]
        return layout
    
    def path_exist(self, path):
        if not os.path.exists(path):
            return False
        else:
            return True
            
    def import_file(self,window, event, key, pathFile, alternating_row_color='DimGray', background_color='Gray'):
        if not self.path_exist(self.path_docs):
            os.makedirs(self.path_docs)      
        
        datas = self.files_to_table(self.path_docs)
        exist = False
        for row in datas:
            if pathFile.find(row[0]) != -1:
                exist = True
        if not exist:
            file = shutil.copy(pathFile, self.path_docs)
            
            count_rows  = len(window.Element(DEFAULT_KEY_TABLE_INPORT_CONTRACT).Values)
            elem = [file[file.rindex('/')+1:len(file)]]
            
            window.Element(key).TKTreeview.tag_configure('oddrow', background=alternating_row_color)
            window.Element(key).TKTreeview.tag_configure('evenrow', background=background_color)
            if count_rows % 2 == 0:
                id = window.Element(key).TKTreeview.insert(parent='',index='end',iid=count_rows+1, values=elem, tags=('evenrow'))
            else:
                id = window.Element(key).TKTreeview.insert(parent='',index='end',iid=count_rows+1, values=elem, tags=('oddrow'))
            window.Element(key).Values.append(elem)
                    
            window.Element(key).update(select_rows=[int(id)-1])
        else:
            sg.popup('Contrato já existe na base de dados!', keep_on_top=True)
    
    def files_to_table(self, path):
        rows_table = None
        if self.path_exist(path):
           for root, dirs, files in os.walk(path, topdown=True):
               rows_table = files
               
           for cont in range(len(rows_table)):
                   rows_table[cont] = [str(rows_table[cont])]
                   
        if rows_table == None:
            return None
        return rows_table
        
    
    def _selected_element_table(self, window):
        if len(window.Element(DEFAULT_KEY_TABLE_INPORT_CONTRACT).TKTreeview.selection()) > 0:
            id_table_select = window.Element(DEFAULT_KEY_TABLE_INPORT_CONTRACT).TKTreeview.selection()[0]
            name = window.Element(DEFAULT_KEY_TABLE_INPORT_CONTRACT).Values[int(id_table_select)-1]
            
            if len(name) > 0:
                return name, int(id_table_select)
            return -1
    
    def _disable_btns(self, window, btn_open = True, btn_del = True):
        window.Element(DEFAULT_KEY_BTN_OPEN).update(disabled=btn_open)
        window.Element(DEFAULT_KEY_BTN_DELET).update(disabled=btn_del)
        
    
    def exec_classes(self):
        window_input_layout = sg.Window('Modelos de Contratos', self.layout(), keep_on_top=True, modal=True)
        while(True):
            event, value = window_input_layout.read(timeout=100)  
            
            if event == DEFAULT_KEY_TABLE_INPORT_CONTRACT:
                if len(window_input_layout.Element(DEFAULT_KEY_TABLE_INPORT_CONTRACT).TKTreeview.get_children()) > 0 and len(window_input_layout.Element(DEFAULT_KEY_TABLE_INPORT_CONTRACT).TKTreeview.selection()) > 0:
                        self._disable_btns(window_input_layout,False, False)
                else:
                    self._disable_btns(window_input_layout,True, True)
                    
            if event == sg.WINDOW_CLOSED:
                break
            if event == DEFAULT_KEY_BTN_IMPORT:
                if value[DEFAULT_KEY_INP_PATH] != '':
                    self.import_file(window_input_layout, event,  DEFAULT_KEY_TABLE_INPORT_CONTRACT, value[DEFAULT_KEY_INP_PATH])
                    
                else:
                    sg.popup('Selecione um arquivo para importar', keep_on_top=True)
            
            if event == DEFAULT_KEY_BTN_SELECT:
                id_regist_table = self._search_register(window_input_layout, value[DEFAULT_KEY_INPUT_SEARCH_SELECT])
                try:
                    window_input_layout.Element(DEFAULT_KEY_TABLE_INPORT_CONTRACT).TKTreeview.selection_set(id_regist_table)
                except sg.ttk.tkinter.TclError as err:
                    sg.popup(f'Registro não existe na base de dados\n{err}', keep_on_top=True)
            
            if event == DEFAULT_KEY_BTN_OPEN:
                name, _ =self._selected_element_table(window_input_layout)
                arq = self.path_docs + '/' + name[0]
                os.system('libreoffice --writer '+ "'"+arq+"'")
                
            if event == DEFAULT_KEY_BTN_DELET:
                element_selection, id_selection_table = self._selected_element_table(window_input_layout)
                self._delete_regist(window_input_layout, DEFAULT_KEY_TABLE_INPORT_CONTRACT, element_selection, id_selection_table)
                
        window_input_layout.close()