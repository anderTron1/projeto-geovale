#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 17:17:50 2021

@author: andre
"""
import re

class ElementsAdditional:

    def Table(sg, headings, key, num_rows=20, dados=[], col_width=10):
        headings = headings
        dados = dados
                
        table = [sg.Table(values=dados, headings=headings,max_col_width=25,
                          auto_size_columns=False, display_row_numbers=False, row_height=10,
                          enable_events=True, bind_return_key=True, def_col_width=col_width,
                          justification='right', num_rows=num_rows, alternating_row_color='DimGray', key=key,
                          background_color='Gray',)]
        return table

    def event_keyboard_enter(window, event, keyObj):
        window[keyObj].bind('<Return>', '_Enter')
        window[keyObj].bind('<Tab>', '_Tab')
        window[keyObj].bind('<FocusOut>', '_Leave')
        
        if event == keyObj+ "_Enter":
            return True
        elif event == keyObj + "_Tab":
            return True
        elif event == keyObj + "_Leave":
            return True
        return False
    
    def money_validation(sg, num):
        num = re.sub('[^0-9]', '', num)
        print(num)
        default = '([0-9]*)'
        result = re.search(default, num)
        return 'R$: {},00'.format(result.group(1))
    
    def valid_birth(sg, num):
        num = re.sub('[^0-9]', '', num)
        if len(num) == 8:
            default = "([0-9]{2})([0-9]{2})([0-9]{4})"
            result = re.search(default, num)
            return '{}/{}/{}'.format(result.group(1), result.group(2), result.group(3))
        elif len(num) > 0 and len(num) < 8:
            return -1
    def valid_cell_number(sg, num):
        num = re.sub('[^0-9]', '', num)
        if len(num) == 11:
            default = "([0-9]{2})([0-9]{5})([0-9]{4})"
            result = re.search(default, num)
            return '({}){}-{}'.format(result.group(1), result.group(2), result.group(3))
        elif len(num) == 13:
            default = "([0-9]{2,3})?([0-9]{2})([0-9]{5})([0-9]{4})"
            result = re.search(default, num)
            return '+{}({}){}-{}'.format(result.group(1), result.group(2), result.group(3), result.group(4))
        elif len(num) == 14:
            default = "([0-9]{2,3})?([0-9]{2})([0-9]{5})([0-9]{4})"
            result = re.search(default, num)
            return '+{}({}){}-{}'.format(result.group(1), result.group(2), result.group(3), result.group(4))
        elif len(num) > 0 and len(num) < 11:
            #val = sg.popup('Número com menos digitos que o necéssario!')
            return -1
    
    def valid_cpf(sg, num):
        num = re.sub('[^0-9]','', num)
        
        if len(num) == 11:
            default = '^([0-9]{3})([0-9]{3})([0-9]{3})([0-9]{2})*$'
            result = re.search(default, num)
            return '{}.{}.{}-{}'.format(result.group(1), result.group(2), result.group(3),result.group(4))
        
        elif len(num) > 0 and len(num) < 11:
            #val = sg.popup('Número com menos digitos que o necéssario!')
            return -1
        
    def valid_titulo_eleitor(sg, num):
        num = re.sub('[^0-9]', '', num)
        if len(num) == 12:
            default = '([0-9]{4})([0-9]{4})([0-9]{4})'
            result = re.search(default, num)
            return '{} {} {}'.format(result.group(1),result.group(2), result.group(3))
        
        elif len(num) > 0 and len(num) < 12:
            #val = sg.popup('Número com menos digitos que o necéssario!')
            return -1
    def valid_email(sg, email):
        default = '(^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,3}$)'
        if len(email) > 0:
            if re.match(default, email):
                return '{}'.format(email)
            else:
                return -1
    
    def valid_rg(sg, num):
        num = re.sub('[^0-9]','', num)
        return num
    def valid_just_number(sg, num):
        stringNumber = re.sub('[^[a-zA-Z]]', '', num)
        print(re.match('[^0-9]', num))
        if len(stringNumber) > 0 and stringNumber != 'S/N' and re.match('[^0-9]', num) != None:
            sg.popup('Caso não tenha um numero, informe apenas\n S/N')
        else:
            return stringNumber
        
        num = re.sub('[^0-9]','', num)
        return num
        
def ListPerson():
    headings = ['Nome:', 'CPF']
    NUM_ROWS = 5
    
    dados = [i for i in range(NUM_ROWS)]
    