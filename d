[33mcommit 71585e040fa378a8f4d1baecfa9a4076f1199af3[m[33m ([m[1;36mHEAD -> [m[1;32mmain[m[33m)[m
Author: Andre Luiz <andre-luizpiresguimaraes@outlook.com>
Date:   Sun Oct 10 17:52:09 2021 -0400

    update projeto-geovale

[1mdiff --git a/__pycache__/databaseConection.cpython-38.pyc b/__pycache__/databaseConection.cpython-38.pyc[m
[1mindex edfea98..5630657 100644[m
Binary files a/__pycache__/databaseConection.cpython-38.pyc and b/__pycache__/databaseConection.cpython-38.pyc differ
[1mdiff --git a/database/Database.sqlite3 b/database/Database.sqlite3[m
[1mindex 0bd0a29..2a9279c 100644[m
Binary files a/database/Database.sqlite3 and b/database/Database.sqlite3 differ
[1mdiff --git a/databaseConection.py b/databaseConection.py[m
[1mindex 772bda9..1016130 100644[m
[1m--- a/databaseConection.py[m
[1m+++ b/databaseConection.py[m
[36m@@ -22,7 +22,8 @@[m [mclass Database:[m
         [m
         self.id_register_spouse = 'id_register_spouse'[m
         self.register_spouse = 'register_spouse'[m
[31m-        self.id_to_table_register_spouse = 'id_to_register_people'[m
[32m+[m[41m        [m
[32m+[m[32m        self.name_id_to_table_register = 'id_to_register_people'[m
         [m
         self.register_residents = 'register_residents'[m
         self.id_register_residents = 'id_register_residents'[m
[36m@@ -137,11 +138,12 @@[m [mclass Database:[m
         [m
 #data = Database()[m
 #data.insert_register()[m
[32m+[m[32m'''[m
 valor = 'teste'[m
 tes = 'ola'[m
 print('{0} = {1}, '.format(valor, '"'+tes+'"'))[m
 [m
[31m-'''[m
[32m+[m
 val = {'id_register_people':'Andre luiz', 'name':'Pires', 'sex':1}[m
 print('{}'.format(', '.join(['"' +str(_)+'"' for _ in val.values()])))[m
 [m
[1mdiff --git a/layouts.py b/layouts.py[m
[1mindex 0094fcc..0468ae5 100644[m
[1m--- a/layouts.py[m
[1m+++ b/layouts.py[m
[36m@@ -176,7 +176,6 @@[m [mclass button_search:[m
         [m
         dados = [i for i in range(NUM_ROWS)][m
         table = ElementsAdditional.Table(sg, headings, DEFAULT_KEY_TABLE_SEARCH_REGISTRATION, dados = self._databases_db(), col_width=15)[m
[31m-        [m
         return table[m
     [m
     def _layout(self):[m
[36m@@ -218,8 +217,6 @@[m [mclass register_personal_data:[m
     [m
     def __init__(self):[m
         self._marital_status = 'Casado'[m
[31m-        #self._style = sg.ttk.Style()[m
[31m-        #self._style.configure('TCombobox', fieldbackground='red')[m
         [m
     def load_window_layout(self):[m
         listEstadoCivil = [self._marital_status, 'Solteiro', 'Divorciado', 'Amasiado/Convivente', 'Viúvo'][m
[36m@@ -370,10 +367,10 @@[m [mclass register_personal_data:[m
         [m
         if velue[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == estadCivil and window.Element(DEFAULT_KEY_BTN_NEW).TKButton['state'] == 'disabled':# and velue[DEFAULT_KEY_NAME_SPOUSE] != '':# and window.Element(DEFAULT_KEY_BTN_SAVE).TKButton['state'] == 'normal':[m
             if window.Element(DEFAULT_KEY_NAME_SPOUSE).TKEntry['state'] == 'readonly':[m
[31m-                self.disable_objts(key_to_disable,window, False)[m
[31m-                [m
[32m+[m[32m                self.disable_objts(key_to_disable,window, False, False)[m
[32m+[m[41m                                [m
         elif  window.Element(DEFAULT_KEY_NAME_SPOUSE).TKEntry['state'] == 'normal':[m
[31m-                self.disable_objts(key_to_disable,window, True)[m
[32m+[m[32m            self.disable_objts(key_to_disable,window, True)[m
 [m
     def _change_fields_color(self, window, key, color):[m
         if window.Element(key).Type == 'input':[m
[36m@@ -558,8 +555,9 @@[m [mclass register_personal_data:[m
             DEFAULT_KEY_TXT_ANOTHER_PROPERTY_WHERE :DEFAULT_KEY_COMB_ANOTHER_PROPERTY[m
             }[m
         [m
[31m-        if window.Element(DEFAULT_KEY_DISABLED_ELDERLY_HOW_MANY).Widget['state'] == 'disable':[m
[31m-            for key_disabled, keys_itens in dict_key_Comb.items():[m
[32m+[m[32m        #print(window.Element(DEFAULT_KEY_INP_WHERE).Widget['state'])[m
[32m+[m[32m        #if window.Element(DEFAULT_KEY_INP_WHERE).Widget['state'] == 'readonly':[m
[32m+[m[32m        for key_disabled, keys_itens in dict_key_Comb.items():[m
                 if value[keys_itens] == KEY_YES:[m
                     window.Element(key_disabled).update(disabled=False)[m
                 elif value[keys_itens] == KEY_NOT or value[keys_itens] == '':[m
[36m@@ -582,7 +580,7 @@[m [mclass register_personal_data:[m
             [m
      [m
     def _select_rows_table_residents(self, window):[m
[31m-        if len(window.Element(DEFAULT_KEY_TABLE_RESIDENTS).SelectedRows) > 0:[m
[32m+[m[32m        if len(window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.selection()) > 0:[m
             rows = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).SelectedRows[0][m
             dados = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values[int(rows)][m
                 [m
[36m@@ -603,11 +601,7 @@[m [mclass register_personal_data:[m
         [m
         window.Element(DEFAULT_KEY_TABLE_RESIDENTS).update(values=data, num_rows=20,select_rows=[indice_table])[m
     [m
[31m-    def _save_record_regist_resid(self, window, value, keys, alternating_row_color='DimGray', background_color='Gray'):[m
[31m-        datas = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values[m
[31m-        count_rows = len(datas)[m
[31m-        list_record = [value[key] for key in keys][m
[31m-                [m
[32m+[m[32m    def __save_regist_table(self, window, count_rows, list_record, alternating_row_color, background_color):[m
         window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.tag_configure('oddrow', background=alternating_row_color)[m
         window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.tag_configure('evenrow', background=background_color)[m
         if count_rows % 2 == 0:[m
[36m@@ -617,6 +611,34 @@[m [mclass register_personal_data:[m
         window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values.append(list_record)[m
                 [m
         window.Element(DEFAULT_KEY_TABLE_RESIDENTS).update(select_rows=[int(id)-1])[m
[32m+[m[41m        [m
[32m+[m[32m    def delete_table(self, window, key, id = None):[m
[32m+[m[32m        if id == None:[m
[32m+[m[32m            rows = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.get_children()[m
[32m+[m[32m            if len(rows) > 0:[m
[32m+[m[32m                for row in rows:[m
[32m+[m[32m                    window.Element(key).TKTreeview.delete(row)[m
[32m+[m[32m        else:[m
[32m+[m[32m            if id > 0:[m
[32m+[m[32m                window.Element(key).TKTreeview.delete(id)[m
[32m+[m[41m        [m
[32m+[m[41m    [m
[32m+[m[32m    def save_record_regist_resid(self, window, value, keys, alternating_row_color='DimGray', background_color='Gray'):[m
[32m+[m[32m        datas = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values[m
[32m+[m[32m        count_rows = len(datas)[m
[32m+[m[32m        list_record = [value[key] for key in keys][m
[32m+[m[41m                [m
[32m+[m[32m        self.__save_regist_table(window, count_rows, list_record, alternating_row_color, background_color)[m
[32m+[m[41m    [m
[32m+[m[32m    def save_regist_table(self, window, datas, alternating_row_color='DimGray', background_color='Gray'):[m
[32m+[m[32m        #list_record = [key for key in datas][m
[32m+[m[32m        elem = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values[m
[32m+[m[32m        count_rows = len(elem)[m
[32m+[m[41m        [m
[32m+[m[32m        print(datas)[m
[32m+[m[32m        print(count_rows)[m
[32m+[m[41m        [m
[32m+[m[32m        self.__save_regist_table(window, count_rows, datas, alternating_row_color, background_color)[m
     [m
     def key_to_disable_regist(self):[m
         key_to_disable_regist = [DEFAULT_KEY_TXT_NOME_REGIST_RESID,[m
[36m@@ -631,7 +653,7 @@[m [mclass register_personal_data:[m
         dados = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values[m
                 [m
         if event == DEFAULT_KEY_TABLE_RESIDENTS:[m
[31m-            if len(dados) > 0:[m
[32m+[m[32m            if len(window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.selection()) > 0:[m
                 self._select_rows_table_residents(window)[m
                 self.disable_objts(self.key_to_disable_regist(), window,True,closeValue=False)[m
                 self.event_buttons_residents(window, False,True, True, False, False)[m
[36m@@ -652,7 +674,7 @@[m [mclass register_personal_data:[m
                 self._edit_table(window, valuer, dados, self.key_to_disable_regist(), window.Element(DEFAULT_KEY_TABLE_RESIDENTS).SelectedRows[0])[m
                 [m
             elif window.Element(DEFAULT_KEY_BTN_NEW_REGIST_RESID).Disabled == False:[m
[31m-                self._save_record_regist_resid(window, valuer,self.key_to_disable_regist()) [m
[32m+[m[32m                self.save_record_regist_resid(window, valuer,self.key_to_disable_regist())[m[41m [m
 [m
             #update valuer to family income[m
             total_income = [sum(int(i[5]) for i in dados)][0][m
[36m@@ -666,6 +688,8 @@[m [mclass register_personal_data:[m
             self.event_buttons_residents(window, True, False, False, False, True)[m
                 [m
         if event == DEFAULT_KEY_BTN_DEL_REGIST_RESID:[m
[32m+[m[32m            id = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.selection()[0][m
[32m+[m[32m            self.delete_table(window, DEFAULT_KEY_TABLE_RESIDENTS, id)[m
             self.disable_objts(self.key_to_disable_regist(),window,True,closeValue=False)[m
             [m
             [m
[36m@@ -730,13 +754,11 @@[m [mclass register_personal_data:[m
             result = ElementsAdditional.valid_titulo_eleitor(sg, velue[DEFAULT_KEY_VOTER_TITLE_SPOUSE])[m
             self._event_have_information(window, result, DEFAULT_KEY_VOTER_TITLE_SPOUSE, 'Número do Titulo de Eleitor incorreto!')[m
 [m
[31m-           [m
     def exec_layout(self, window, event, valuer):[m
        self.event_inputs(sg, window, event, valuer)[m
        self.event_other_infor(window, valuer)[m
        self.disable_input_conjuge(window, valuer, self._marital_status)[m
        self._event_table_regist_resid(window, event, valuer)[m
[31m-                [m
 [m
 [m
 class registration:[m
[36m@@ -758,19 +780,29 @@[m [mclass registration:[m
             [m
         return layout[m
     [m
[31m-    def _loard_records_into_fields(self,window, name_table, keys_fields, name_id_table, id_register):[m
[31m-        fileds_and_field_db = self._conn._take_fields_records(name_table, keys_fields)      [m
[31m-        datas = self._conn.select_register(fileds_and_field_db.keys(), name_table, name_id_table, id_register)[0][m
[32m+[m[32m    def _loard_records_into_fields(self,window, name_table, keys_fields, name_id_table, id_register, is_table = False, key_table = None, valuer=None):[m
[32m+[m[32m        fileds_and_field_db = self._conn._take_fields_records(name_table, keys_fields)[m
[32m+[m[32m        datas = None[m
[32m+[m[41m        [m
[32m+[m[32m        if is_table:[m
[32m+[m[32m            datas = self._conn.select_register(fileds_and_field_db.keys(), name_table, name_id_table, id_register)[m
[32m+[m[32m        else:[m
[32m+[m[32m            datas = self._conn.select_register(fileds_and_field_db.keys(), name_table, name_id_table, id_register)[0][m
         datas = np.array(datas)[m
[31m-[m
[31m-        for cont, key in enumerate(fileds_and_field_db.values()):[m
[31m-            if datas[cont] != None:[m
[31m-                if window.Element(key).Type == 'input':[m
[31m-                    window.Element(key).Update(datas[cont])[m
[31m-                elif window.Element(key).Type == 'combo':[m
[31m-                    window.Element(key).TKCombo.set(datas[cont])[m
[31m-                elif window.Element(key).Type == 'spind':[m
[31m-                    window.Element(key).TKStringVar.set(datas[cont])[m
[32m+[m[41m        [m
[32m+[m[32m        if key_table == None:[m
[32m+[m[32m            for cont, key in enumerate(fileds_and_field_db.values()):[m
[32m+[m[32m                if datas[cont] != None:[m
[32m+[m[32m                    if window.Element(key).Type == 'input':[m
[32m+[m[32m                        window.Element(key).Update(datas[cont])[m
[32m+[m[32m                    elif window.Element(key).Type == 'combo':[m
[32m+[m[32m                        window.Element(key).TKCombo.set(datas[cont])[m
[32m+[m[32m                    elif window.Element(key).Type == 'spind':[m
[32m+[m[32m                        window.Element(key).TKStringVar.set(datas[cont])[m
[32m+[m[32m        else:[m
[32m+[m[32m            for row in datas:[m
[32m+[m[32m                val = [i for i in row][m
[32m+[m[32m                self._class_register.save_regist_table(window, val)[m
         if len(datas) > 0:[m
             return True[m
         return False[m
[36m@@ -830,12 +862,13 @@[m [mclass registration:[m
             self._activate_registration_buttons(window, btnNew=True, btnCancel=False, btnSave=False, btnEdit=True, btnDel=True)[m
             self._activate_search_buttons(window, buttons=True)[m
             #event buttons registration residents[m
[31m-            self._class_register.event_buttons_residents(window, False, True, True, True, True)            [m
[32m+[m[32m            self._class_register.event_buttons_residents(window, False, True, True, True, True)[m
[32m+[m[41m            [m
[32m+[m[32m            self._class_register.delete_table(window, DEFAULT_KEY_TABLE_RESIDENTS)[m
             [m
         elif event == DEFAULT_KEY_BTN_CANCEL:[m
             self._btn_edit_clicked = False[m
[31m-            self._class_register.disable_objts(key_to_update,window, True,False)[m
[31m-            [m
[32m+[m[41m                        [m
             if value[DEFAULT_KEY_NOME_PERSONAL_DATA] != '':[m
                 self._activate_registration_buttons(window, btnNew=False, btnCancel=True, btnSave=True, btnEdit=False, btnDel=False)[m
             else:[m
[36m@@ -846,7 +879,7 @@[m [mclass registration:[m
             self._class_register.event_buttons_residents(window, True, True, True, True, False)[m
             [m
             #disable functions to register residents tab[m
[31m-            self._class_register.disable_objts(self._class_register.key_to_disable_regist(), window,True,closeValue=True)[m
[32m+[m[32m            self._class_register.disable_objts(self._class_register.key_to_disable_regist(), window,True,True)[m
             self._class_register.event_buttons_residents(window, True, True, True, True, True)[m
             [m
             for item in window.Element(DEFAULT_KEY_TABLE_RESIDENTS).TKTreeview.get_children():[m
[36m@@ -854,6 +887,9 @@[m [mclass registration:[m
                 [m
             for key in key_to_update:[m
                 self._class_register._change_fields_color(window, key, "white")[m
[32m+[m[41m                [m
[32m+[m[32m            self._class_register.disable_objts(key_to_update, window, True,False)[m
[32m+[m[32m            self._class_register.disable_objts(self._class_register.keys_fields_spouse(), window, True, False)[m
             [m
         elif event == DEFAULT_KEY_BTN_SAVE:[m
             resultFields = self._class_register.required_fields(window, event,value)[m
[36m@@ -866,24 +902,29 @@[m [mclass registration:[m
                 keys_numeric_fields = [DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA, DEFAULT_KEY_TEL_PERSONAL_DATA,DEFAULT_KEY_CEL_PERSONAL_DATA,[m
                                            DEFAULT_KEY_RG_PERSONAL_DATA, DEFAULT_KEY_CPF_PERSONAL_DATA][m
                 keys_numeric = [DEFAULT_KEY_BIRTHDATE_SPOUSE, DEFAULT_KEY_CEL_SPOUSE,DEFAULT_KEY_TEL_SPOUSE, DEFAULT_KEY_RG_SPOUSE,DEFAULT_KEY_CPF_SPOUSE][m
[32m+[m[32m                register_exist_db = False[m
                 [m
                 if self._btn_edit_clicked == False: #Save register[m
                     [m
[31m-                    self._id_register_db = self._conn.insert_register(self._class_register.get_key_values(value,self._class_register.keys_fields_tab(), keys_numeric_fields), self._conn.register_people, self._conn.id_register_people)[m
[31m-                [m
[31m-                    if value[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == self._class_register._marital_status:[m
[31m-                        self._conn.insert_register(self._class_register.get_key_values(value,self._class_register.keys_fields_spouse(), keys_numeric) , self._conn.register_spouse, self._conn.id_register_spouse, self._id_register_db)[m
[32m+[m[32m                    register_exist_db = self._conn.query_record(self._conn.register_people, 'cpf', re.sub('[^0-9]', '', value[DEFAULT_KEY_CPF_PERSONAL_DATA]))[m
[32m+[m[32m                    if register_exist_db != True:[m
[32m+[m[32m                        self._id_register_db = self._conn.insert_register(self._class_register.get_key_values(value,self._class_register.keys_fields_tab(), keys_numeric_fields), self._conn.register_people, self._conn.id_register_people)[m
                     [m
[31m-                    if len(value[DEFAULT_KEY_TABLE_RESIDENTS]) > 0:[m
[31m-                        datas = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values[m
[32m+[m[32m                        if value[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == self._class_register._marital_status:[m
[32m+[m[32m                            self._conn.insert_register(self._class_register.get_key_values(value,self._class_register.keys_fields_spouse(), keys_numeric) , self._conn.register_spouse, self._conn.id_register_spouse, self._id_register_db)[m
[32m+[m[41m                        [m
[32m+[m[32m                        if len(value[DEFAULT_KEY_TABLE_RESIDENTS]) > 0:[m
[32m+[m[32m                            datas = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values[m
[32m+[m[41m                            [m
[32m+[m[32m                            for register in datas:[m
[32m+[m[32m                                self._conn.insert_register(register, self._conn.register_residents, self._conn.id_register_residents, self._id_register_db)[m
[32m+[m[32m                    else:[m
[32m+[m[32m                        sg.popup('ERRO!\n  cadastro do titular do CPF: {0} já existente na base de dados.'.format(value[DEFAULT_KEY_CPF_PERSONAL_DATA]), keep_on_top=True)[m
                         [m
[31m-                        for register in datas:[m
[31m-                            self._conn.insert_register(register, self._conn.register_residents, self._conn.id_register_residents, self._id_register_db)[m
[31m-                    [m
                 else: #save edition register[m
                     self._conn.update_register(self._class_register.get_key_values(value,self._class_register.keys_fields_tab(), keys_numeric_fields), self._conn.register_people, self._conn.id_register_people, self._id_register_db)[m
                     [m
[31m-                    register_exist = self._conn.query_record(self._conn.register_spouse, self._conn.id_to_table_register_spouse, self._id_register_db)[m
[32m+[m[32m                    register_exist = self._conn.query_record(self._conn.register_spouse, self._conn.name_id_to_table_register, self._id_register_db)[m
                     [m
                     if value[DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA] == self._class_register._marital_status:[m
                         if register_exist:[m
[36m@@ -896,14 +937,14 @@[m [mclass registration:[m
                     #if len(value[DEFAULT_KEY_TABLE_RESIDENTS]) > 0:[m
                     #    datas = window.Element(DEFAULT_KEY_TABLE_RESIDENTS).Values[m
                         [m
[32m+[m[32m                if register_exist_db == True:[m
[32m+[m[32m                    self._class_register.disable_objts(key_to_update, window, True,False)[m
[32m+[m[32m                    self._class_register.disable_objts(self._class_register.keys_fields_spouse(), window, True, False)[m
                     [m
[31m-                self._class_register.disable_objts(key_to_update, window, True,False)[m
[31m-                self._class_register.disable_objts(self._class_register.keys_fields_spouse(), window, True, False)[m
[31m-                [m
[31m-                self._activate_registration_buttons(window, btnNew=False, btnCancel=True, btnSave=True, btnEdit=False, btnDel=False)[m
[31m-                self._activate_search_buttons(window, buttons=False)[m
[31m-                #event buttons registration residents[m
[31m-                self._class_register.event_buttons_residents(window, False, True, True, True, False)[m
[32m+[m[32m                    self._activate_registration_buttons(window, btnNew=False, btnCancel=True, btnSave=True, btnEdit=False, btnDel=False)[m
[32m+[m[32m                    self._activate_search_buttons(window, buttons=False)[m
[32m+[m[32m                    #event buttons registration residents[m
[32m+[m[32m                    self._class_register.event_buttons_residents(window, False, True, True, True, False)[m
             [m
         elif event == DEFAULT_KEY_BTN_EDIT:[m
             self._btn_edit_clicked = True[m
[36m@@ -914,30 +955,44 @@[m [mclass registration:[m
             self._class_register.event_buttons_residents(window, False, True, True, True, True)[m
         [m
         elif event == DEFAULT_KEY_BTN_DELETE:  [m
[32m+[m[41m            [m
[32m+[m[32m            self._class_register.delete_table(window, DEFAULT_KEY_TABLE_RESIDENTS)[m
[32m+[m[41m            [m
             self._class_register.disable_objts(key_to_update, window, True,True)[m
             self._activate_registration_buttons(window, btnNew=False, btnCancel=True, btnSave=True, btnEdit=False, btnDel=False)[m
             self._activate_search_buttons(window, buttons=False)[m
             self._class_register.event_buttons_residents(window, True, True, True, True, True)[m
         [m
         if event == DEFAULT_KEY_BTN_SEARCH:[m
[31m-            self._class_register.disable_objts(key_to_update, window, True,True)[m
[31m-            self._class_register.disable_objts(self._class_register.keys_fields_spouse(), window, True)[m
[31m-            [m
             search = button_search(sg, self._conn)[m
             self._window_button_search, self._id_register_db = search.window_button_search()[m
[31m-                        [m
[31m-            register_ok = self._loard_records_into_fields(window, self._conn.register_people, self._class_register.keys_fields_tab(), self._conn.id_register_people, self._id_register_db)[m
[31m-        [m
[31m-            register_spouse_exist = self._conn.query_record(self._conn.register_spouse, self._conn.id_to_table_register_spouse, self._id_register_db)[m
             [m
[31m-            if register_spouse_exist is True:[m
[31m-                self._loard_records_into_fields(window, self._conn.register_spouse, self._class_register.keys_fields_spouse(), self._conn.id_to_table_register_spouse, self._id_register_db)[m
[31m-        [m
[31m-            if register_ok:[m
[31m-                self._activate_registration_buttons(window, btnNew=False, btnCancel=True, btnSave=True, btnEdit=False, btnDel=False)[m
[32m+[m[32m            if self._window_button_search != None or self._id_register_db != None:[m
[32m+[m[32m                #event to residents[m
[32m+[m[32m                self._class_register.disable_objts(self._class_register.key_to_disable_regist(), window,True,closeValue=True)[m
[32m+[m[32m                self._class_register.event_buttons_residents(window, True, True, True, True, True)[m
[32m+[m[32m                self._class_register.delete_table(window, DEFAULT_KEY_TABLE_RESIDENTS)[m
[32m+[m[41m                [m
[32m+[m[32m                self._class_register.disable_objts(key_to_update, window, True,True)[m
[32m+[m[32m                self._class_register.disable_objts(self._class_register.