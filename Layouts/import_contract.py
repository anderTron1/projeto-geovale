#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 13:47:57 2021

@author: André Luiz Pires Guimarães
"""


from elementsAdditional import ElementsAdditional     
import PySimpleGUI as sg

import os
import shutil
import subprocess
from sys import platform

#--------------------------KEYS TABLE IMPORT CONTRACT----------------------
DEFAULT_KEY_BTN_OPEN = '-ABRIR-'
DEFAULT_KEY_BTN_DELET = '-DELETE-'
DEFAULT_KEY_BTN_SELECT = '-SELECIONAR-'
DEFAULT_KEY_INP_PATH = '-CAMINHO_ARQUIVO-'
DEFAULT_KEY_BTN_IMPORT = '-BTN_IMPORTAR-'
DEFAULT_KEY_INPUT_SEARCH_SELECT = '-PROCURAR_REGISTRO_SELECIONADO-'


DEFAULT_KEY_TABLE_INPORT_CONTRACT = '-INPORT_CONTRACT-'

class Import_contract:
        
    def __init__(self, return_only_the_path = False):
        self.elem = ElementsAdditional()
        self.path_docs = 'database/imported_documents'
        self.rows_table = None
        self.table_elements = dict()
        self.__return_only_the_path = return_only_the_path
        
    def _table_search(self):
        headings = ['Contratos salvos']
        self.rows_table = self.files_to_table(self.path_docs)
        
        for cont, elem in enumerate(self.rows_table):
            self.table_elements[cont+1] = elem
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
                
                print(self.table_elements)
                for key, value in self.table_elements.items():
                    if value[0] == name[0]:
                        self.table_elements.pop(key)
                        break
                print('Depois: ',self.table_elements)
                sg.popup('Arquivo deletado', keep_on_top=True)
    
    def _search_register(self, window, record_to_select):
        for key, item in self.table_elements.items():
            if item[0].find(record_to_select) != -1:
                return key
        return -1
    
    def layout(self):
        if self.__return_only_the_path != True:
            layout = [
                        [sg.T('Contrato'), sg.Input(key=DEFAULT_KEY_INPUT_SEARCH_SELECT), sg.Button('Selecionar', key=DEFAULT_KEY_BTN_SELECT)],
                        [self._table_search()],
                            
                        [sg.Button('Abrir', key=DEFAULT_KEY_BTN_OPEN, disabled=True), sg.Button('Excluir', key=DEFAULT_KEY_BTN_DELET, disabled=True)],
                        [sg.Input(key=DEFAULT_KEY_INP_PATH, disabled=True, size=55), sg.Button('Importar', key=DEFAULT_KEY_BTN_IMPORT)],
                        [sg.FileBrowse(button_text= 'Importar Contrato', target=DEFAULT_KEY_INP_PATH,tooltip='Importar novo contrato para o sistema', file_types=(('Arquivo no Formato', "*.docx"),))]
                      ]
        else:
            layout = [
                        [sg.T('Contrato'), sg.Input(key=DEFAULT_KEY_INPUT_SEARCH_SELECT), sg.Button('Selecionar', key=DEFAULT_KEY_BTN_SELECT)],
                        [self._table_search()]
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
            
            self.table_elements[id] = elem
            
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
        
    def exec_file_word(self,file_path):
        if platform == "linux" or platform == "linux2":
            #os.system('libreoffice --writer '+ "'"+arq+"'")
            pid = subprocess.Popen(["libreoffice", file_path]).pid
            print(pid)
            
        elif platform == "win32":
            path = 'C:/Program Files (x86)/Microsoft Office/'
            path_office_to_exec_file_word = None
            '''
                search among the office versions for the folder containing the word execution file
            '''
            for root, dirs, files in os.walk(path, topdown=True):
                #print(root)
                if root[len(path):].find('Office') != -1:
                    path_office_to_exec_file_word = root
                    break
            pid = subprocess.Popen([path_office_to_exec_file_word+ "/WINWORD.EXE", file_path]).pid
            print(pid)
    
    def exec_classes(self):
        window_input_layout = sg.Window('Modelos de Contratos', self.layout(),icon=r'image/iconLogo.ico', keep_on_top=True, modal=True)
        closed = False
        path_file = None
        
        while(True):
            event, value = window_input_layout.read(timeout=100)  
            
            if event == sg.WINDOW_CLOSED:
                break
            
            if event == DEFAULT_KEY_TABLE_INPORT_CONTRACT:
                if self.__return_only_the_path != True:
                    if len(window_input_layout.Element(DEFAULT_KEY_TABLE_INPORT_CONTRACT).TKTreeview.get_children()) > 0 and len(window_input_layout.Element(DEFAULT_KEY_TABLE_INPORT_CONTRACT).TKTreeview.selection()) > 0:
                            self._disable_btns(window_input_layout,False, False)
                    else:
                        self._disable_btns(window_input_layout,True, True)
                        
            if self.__return_only_the_path == True:        
                window_input_layout[DEFAULT_KEY_TABLE_INPORT_CONTRACT].bind('<Double-Button-1>', '_dublo')
                if event == DEFAULT_KEY_TABLE_INPORT_CONTRACT + '_dublo':
                    if len(window_input_layout.Element(DEFAULT_KEY_TABLE_INPORT_CONTRACT).TKTreeview.selection()) > 0:
                        name, _ =self._selected_element_table(window_input_layout)
                        path_file = self.path_docs + '/' + name[0]
                        
                        closed = True
                        break
                    
            if event == DEFAULT_KEY_BTN_IMPORT:
                if value[DEFAULT_KEY_INP_PATH] != '':
                    self.import_file(window_input_layout, event,  DEFAULT_KEY_TABLE_INPORT_CONTRACT, value[DEFAULT_KEY_INP_PATH])
                    window_input_layout.Element(DEFAULT_KEY_INP_PATH).update('')
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
                
                self.exec_file_word(arq)
                
            if event == DEFAULT_KEY_BTN_DELET:
                element_selection, id_selection_table = self._selected_element_table(window_input_layout)
                self._delete_regist(window_input_layout, DEFAULT_KEY_TABLE_INPORT_CONTRACT, element_selection, id_selection_table)
                
        window_input_layout.close()
        if closed == True:
            return path_file
        return -1