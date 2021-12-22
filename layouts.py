#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 00:20:07 2021
# token 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
@author: André Luiz Pires Guimarães
"""

from Layouts.import_contract import Import_contract
from Layouts.registration import Registration
from Layouts.generate_construct import Generate_contract
from Layouts.settings import Settings
from Layouts.generate_pdf import Generate_pdf
from Layouts.export_data import Export_data

from backup_mega import Backup_database
from databaseConection import Database

import screeninfo
import PySimpleGUI as sg
import sys
import ctypes


class main_layout: 
    def __init__(self):
        try:
            self._conn = Database()
        except AttributeError:
            sys.exit()
        self._class_registration = Registration(self._conn)
        self._class_inport_contract = Import_contract()
        self._class_generate_constract = Generate_contract(self._conn)
        self.__class_Settings = Settings(self._conn)
        self.__class_generate_pdf = Generate_pdf()
        self.__class_export_data = Export_data(self._conn)
        self.__class_backup = Backup_database()
        
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
                [   ['&Menu', ['&Cadastros', '&Exportar dados', 'Co&nfigurações', '&Backup', 'E&xit']],
                    ['C&ontratos', ['&Gerar Tegs para contratos', '&Lista de Contratos', 'G&erar contrato']],
                    ['Sobre', ['Dados desenvolvedor']]
                ])]]#, background_color='#176d81')]]
        layout = [menu,
                  [sg.Image(image,  background_color='white', size=(self._current_screen.width, self._current_screen.height))]
                  ]
        return layout
    
    def exec_classes(self):
        window = sg.Window('Janela Principal', self.layout(),icon=r'image/iconLogo.ico',
                           default_button_element_size=(25,1), background_color='white', 
                           resizable=True, size=(self._current_screen.width, self._current_screen.height))
        
        while(True):
            event, valuer = window.read(timeout=100)
            
            if event == 'Cadastros':
                self._class_registration.exec_classes()
            if event == 'Exportar dados':
                self.__class_export_data.exec_class()
            if event == 'Configurações':
                self.__class_Settings.exec_class()
            if event == 'Backup':
                 self.__class_backup.exec_class()
            if event == 'Lista de Contratos':
                self._class_inport_contract.exec_classes()
            if event == 'Gerar Tegs para contratos':
                self.__class_generate_pdf.exec_class()
            if event == 'Gerar contrato':
                self._class_generate_constract.exec_class()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Exit':
                close = sg.popup_ok_cancel('Deseja fechar o sistema?')
                if close == 'OK':
                    break
        window.close()
        
if __name__ == '__main__':
    
    app = main_layout()
    app.exec_classes()