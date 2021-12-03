# -*- coding: utf-8 -*-
from elementsAdditional import ElementsAdditional
from Layouts.keys_names.keys_to_settings import *

import numpy as np

import PySimpleGUI as sg

DEFAULT_KEY_BTN_EDIT_REURB = '<<-EDIT_REURB->>'
DEFAULT_KEY_BTN_SAVE_REURB = '<<-SAVE_REURB->>'

DEFAULT_KEY_BTN_NEW_PROJECT = '<<-NEW_PROJECT->>'
DEFAULT_KEY_BTN_EDIT_PROJECT = '<<-EDIT_PROJECT->>'
DEFAULT_KEY_BTN_SAVE_PROJECT = '<<-SAVE_PROJECT->>'
DEFAULT_KEY_BTN_DEL_PROJECT = '<<-DEL_PROJECT->>'
DEFAULT_KEY_BTN_CANCEL_PROJECT = '<<CANCEL_PROJECT>>'

def rangeArray(init, size):
    return [num for num in range(init, size)]

################################################################
#
# CLASS FRAMEWORK_REURB TO TAB_GROUP
#
################################################################
class Framework_reurb:
    def __init__(self):
        self.__conn_db_to_framework_reurb= None
        self.__id_db = None
    #==============================
    #           TO DATABASE
    #==============================
    
    def __get_keys_fields_db(self, name_table):
        name_table = name_table
        keys_fields = self.__keys_fileds_framework()        
        keys_fields_db = self.__conn_db_to_framework_reurb._take_fields_records(name_table, keys_fields)

        return keys_fields_db
    
    def get_db_valuer_field_Framework(self, window):
        name_table = self.__conn_db_to_framework_reurb.basic_settings
        keys_fields = self.__get_keys_fields_db(name_table)
        
        keys_fields[self.__conn_db_to_framework_reurb.id_basic_settings] = 'id'
        
        datas = np.array(self.__conn_db_to_framework_reurb.select_register(keys_fields.keys(), name_table))
        print(datas[0])
        
        for count, key in enumerate(keys_fields.values()):
            if datas[0][count] != None:
                if key == 'id':
                    print('ID: ',datas[0][count])
                    self.__id_db = datas[0][count]
                    break
                if window.Element(key).Type == 'input':
                    print('Tipo input: ', datas[0][count])
                    window.Element(key).Update(datas[0][count])
                   
                elif window.Element(key).Type == 'combo':
                    print('Tipo combo: ', datas[0][count])
                    window.Element(key).TKCombo.set(datas[0][count])
                
                elif window.Element(key).Type == 'spind':
                    print('Tipo SPIND: ', datas[0][count])
                    window.Element(key).TKStringVar.set(datas[0][count])
                
                elif window.Element(key).Type == 'radio':
                    print('Tipo RADIO: ', datas[0][count])
                    if datas[0][count] == 'REURB-S':
                        window.Element(DEFAULT_KEY_REURB_S).update(True)
                    else:
                        window.Element(DEFAULT_KEY_REURB_E).update(True)

    def get_value_fields(self, value):
        all_fields_are_filled = True
        values = []
        
        keys_fields = self.__keys_fileds_framework()
        for key in keys_fields:
            value_field = value[key]
            print(value_field)
            
            if  value_field == '' or value_field == ' ':
                all_fields_are_filled = False
            else:
                values.append(value_field)
                
        
        return all_fields_are_filled, values
                
                
    def save_editon(self, window, value):
        name_table = self.__conn_db_to_framework_reurb.basic_settings
        keys_fields = self.__get_keys_fields_db(name_table) 
        id_name_table = self.__conn_db_to_framework_reurb.id_basic_settings
        
        print('inserindo dados no id: ', self.__id_db)
        print(self.get_value_fields(value))
        #self.__conn_db_to_framework_reurb.update_register(keys_fields.keys(), name_table, id_name_table, self.__id_db)
        #self.get_db_valuer_field_Framework(window)
        
    def tab_framework_reurb(self):
        setting_base_to = [
                [sg.T('Renda familiar inferior a:'), sg.Input(size=10, disabled=True, key=DEFAULT_KEY_FAMILY_INCOME_LESS_THAN)],
                [sg.T('Possuir lote de até (m²):'), sg.Input(size=10, disabled=True, key=DEFAULT_KEY_OWN_BATCH_OF_UP_TO)],
                [sg.T('Possuir a quantia de imóveis urbano de:'), sg.Spin(rangeArray(1, 100), disabled=True, key=DEFAULT_KEY_AMOUNT_REAL_ESTATE_URVAN)],
                [sg.T('Deve possuir imóvel rural?'), sg.Combo([KEY_YES, KEY_NOT], disabled=True, key=DEFAULT_KEY_OWN_RURAL_PROPERTY)],
                [sg.Radio('REURB-S', group_id='RADIO', disabled=True, key=DEFAULT_KEY_REURB_S), sg.Radio('REURB-E',group_id='RADIO', disabled=True, key=DEFAULT_KEY_REURB_E)],
                [sg.Button('Editar', key=DEFAULT_KEY_BTN_EDIT_REURB), sg.Button('Salvar', key=DEFAULT_KEY_BTN_SAVE_REURB)]
            ]
        tag_base_to =[
                [sg.Frame('Definir requisitos para enquadrar como REURB-S ou REURB-E', setting_base_to)]
            ]
        return tag_base_to
    
    def __keys_fileds_framework(self):
        keys = [
                DEFAULT_KEY_FAMILY_INCOME_LESS_THAN,
                DEFAULT_KEY_OWN_BATCH_OF_UP_TO,
                DEFAULT_KEY_AMOUNT_REAL_ESTATE_URVAN,
                DEFAULT_KEY_OWN_RURAL_PROPERTY,
                DEFAULT_KEY_REURB_S,
                DEFAULT_KEY_REURB_E
            ]
        return keys
    
    def __event_disabled(self, window, keys, disable):        
        for key in keys:
            window.Element(key).update(disabled=disable)       
    
    def disabled_fields_framework_reurb(self,window, disable):
        keys = self.__keys_fileds_framework()
        self.__event_disabled(window, keys, disable)
        
    def event_btns_framework_reurb(self,window, event, value):
        if event == DEFAULT_KEY_BTN_EDIT_REURB:
            self.disabled_fields_framework_reurb(window,False)
            
        if event == DEFAULT_KEY_BTN_SAVE_REURB:
            self.disabled_fields_framework_reurb(window, True)
            self.save_editon(window, value)
    
    def exec_tab_framework_reurb(self, window, event, value):
        self.event_btns_framework_reurb(window,event, value)

################################################################
#
# CLASS PROJECT TO TAB_GROUP
#
################################################################
class Project:
    def __init__(self):
        self.__elements = None
        self.__conn_db_to_project = None
    def __table(self):
        headings = ['ID', 'Projeto']
        table = self.__elements.Table(sg, headings, DEFAULT_KEY_TABLE_SETTINGS, col_width=25, num_rows=5)
        return table
        
    def tab_project(self):
        setting_projects = [
                [sg.T('Nome do projeto'), sg.Input(size=20, disabled=True, key=DEFAULT_KEY_NAME_PROJECT)],
                [sg.Column([self.__table()])],
                [sg.Button('Novo',key= DEFAULT_KEY_BTN_NEW_PROJECT),sg.Button('Editar', key=DEFAULT_KEY_BTN_EDIT_PROJECT), 
                 sg.Button('Salvar', key=DEFAULT_KEY_BTN_SAVE_PROJECT), sg.Button('Deletar', key=DEFAULT_KEY_BTN_DEL_PROJECT), 
                 sg.Button('Cancelar', key=DEFAULT_KEY_BTN_CANCEL_PROJECT)]
            ]        
        tab_projects = [
                [sg.Frame('Definir campos de projetos para os cadastros de clientes', setting_projects)]
            ]
        return tab_projects
    
    def __keys_fileds_framework(self):
        keys = [
                DEFAULT_KEY_NAME_PROJECT
            ]
        return keys
    
    def __event_disabled(self, window, keys, disable, clear_field=False):        
        for key in keys:
            if clear_field:
                window.Element(key).update(disabled=disable)
            else:
                window.Element(key).update(disabled=disable, value='')
        
    def disabled_fields_project(self,window, disable, clear_field=False):
        keys = self.__keys_fileds_framework()
        self.__event_disabled(window, keys, disable)
        
    def __disabled_btns_project(self, window, btn_new, btn_edit, btn_save, btn_del, btn_cancel):
        window.Element(DEFAULT_KEY_BTN_NEW_PROJECT).update(disabled=btn_new)
        window.Element(DEFAULT_KEY_BTN_EDIT_PROJECT).update(disabled=btn_edit)
        window.Element(DEFAULT_KEY_BTN_SAVE_PROJECT).update(disabled=btn_save)
        window.Element(DEFAULT_KEY_BTN_DEL_PROJECT).update(disabled=btn_del)
        window.Element(DEFAULT_KEY_BTN_CANCEL_PROJECT).update(disabled=btn_cancel)
        
    def event_btns_project(self,window, event):
        if event == DEFAULT_KEY_BTN_NEW_PROJECT:
            self.disabled_fields_project(window,False, clear_field=True)
            self.__disabled_btns_project(window, btn_new=True, btn_edit=True, btn_save=False, btn_del=True, btn_cancel=False)
                
        if event == DEFAULT_KEY_BTN_EDIT_PROJECT:
            self.disabled_fields_project(window,False)
            self.__disabled_btns_project(window, btn_new=True, btn_edit=False, btn_save=False, btn_del=True, btn_cancel=False)
        
        if event == DEFAULT_KEY_BTN_SAVE_PROJECT:
            self.disabled_fields_project(window,True, clear_field=True)
            self.__disabled_btns_project(window, btn_new=True, btn_edit=True, btn_save=True, btn_del=True, btn_cancel=True)
        
        if event == DEFAULT_KEY_BTN_DEL_PROJECT:
            self.disabled_fields_project(window,True, clear_field=True)
            self.__disabled_btns_project(window, btn_new=True, btn_edit=True, btn_save=True, btn_del=True, btn_cancel=True)
        
        if event == DEFAULT_KEY_BTN_CANCEL_PROJECT:
            self.disabled_fields_project(window,True, clear_field=True)
            self.__disabled_btns_project(window, btn_new=True, btn_edit=True, btn_save=True, btn_del=True, btn_cancel=True)
    
        
    def exec_tab_project(self, window, event, value):
        self.event_btns_project(window,event)
        
class Settings(Framework_reurb, Project):
    def __init__(self, database):
        self.__conn = database
        self._Framework_reurb__conn_db_to_framework_reurb = database
        self._Project__conn_db_to_project = database
        
        self._Project__elements = ElementsAdditional()
                
    def layout(self):
        layout = [
                    [sg.TabGroup([
                        [sg.Tab('Tipo de enquadramento', self.tab_framework_reurb())],
                        [sg.Tab('Projetos', self.tab_project())]])
                    ],
                ]
        return layout
    
    
    def exec_class(self):
        window_settings = sg.Window('Configurações basicas', self.layout(), icon=r'image/iconLogo.ico')
        loard_db_to_fields = True
        
        while(True):
            event, value = window_settings.read(timeout=100)
            
            self.exec_tab_framework_reurb(window_settings, event, value)
            self.exec_tab_project(window_settings, event, value)
            
            if loard_db_to_fields:
                print('Carregando')
                self.get_db_valuer_field_Framework(window_settings)
                loard_db_to_fields = False
            
            if event == sg.WINDOW_CLOSED:
                break
            
        window_settings.close()
        