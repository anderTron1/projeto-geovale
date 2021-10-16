#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 14:15:13 2021

@author: andre
"""
import sqlite3
import os.path as path
import collections

patch_file = 'database/sqlite_database/Database.sqlite3'

class Database:
    def __init__(self, path_file = patch_file):
        self._conection = None
        self._cur = None
        self._conected = False
        
        self.register_people = 'register_people'
        self.id_register_people = 'id_register_people'
        
        self.id_register_spouse = 'id_register_spouse'
        self.register_spouse = 'register_spouse'
        
        self.name_id_to_table_register = 'id_to_register_people'
        
        self.register_residents = 'register_residents'
        self.id_register_residents = 'id_register_residents'
                
        if path.exists(patch_file):
            self._conection = sqlite3.Connection(path_file)    
            self._cur = self._conection.cursor()
            self._conected = True
    
    def connection_right_here(self):
        return self._conected
    
    def close_connection(self):
        self._cur.close()
        

    #function to get the fields from the names of each column in the database
    def _take_fields_records(self, name_table, register_layout):
        list_fields = dict()
        
        cont = 0
        self._cur.execute(f'PRAGMA table_info({name_table})')
        
        for row in self._cur:
            if 'id_' not in row[1]:
                if register_layout[cont] != None:
                    list_fields[row[1]] = register_layout[cont]
                cont += 1
        return list_fields

    def _get_id_table_register_people(self):
        super
        
    def insert_register(self, register, name_table, name_id_table, insert_id = None):
        dic_datas = self._take_fields_records(name_table, register)
        sql = None
        sql_last_id = None
        
        if insert_id == None:
            sql = "INSERT INTO {0} ({1}) VALUES ({2});".format(name_table, ', '.join([str(_) for _ in dic_datas.keys()]), ', '.join(['"' +str(_)+'"' for _ in dic_datas.values()]))
            
            self._cur.execute(sql)
            #self._conection.commit()
            
            sql_last_id = f'SELECT {name_id_table} FROM {name_table} ORDER BY {name_id_table} DESC LIMIT 1;'
            self._cur.execute(sql_last_id)
            
            id = [row[0] for row in  self._cur]
            
            self._conection.commit()
            return id[0]
        else:
            sql = "INSERT INTO {0} ({1}, {3}) VALUES ({2},{4});".format(name_table, ', '.join([str(_) for _ in dic_datas.keys()]), ', '.join(['"' +str(_)+'"' for _ in dic_datas.values()]),
                                                                       self.name_id_to_table_register, insert_id)
            self._cur.execute(sql)
            self._conection.commit()

       
    def commit(self):
        self._conection.commit()
        
    def select_register(self, names_columns, name_table, name_id_table = None, id_table=None):
        sql = None
        datas_db = []
        
        if id_table == None:
            sql = 'SELECT {0} FROM {1};'.format(', '.join([str(_) for _ in names_columns]), name_table)
        else:
            sql = 'SELECT {0} FROM {1} WHERE {2} = {3};'.format(', '.join([str(_) for _ in names_columns]), name_table, name_id_table, id_table)

        self._cur.execute(sql)
        for row in self._cur:
            datas_db.append(row)
                
        return datas_db
    
    def update_register(self, registers, name_table, name_id_table, id_register):        
        dic_datas = self._take_fields_records(name_table, registers)
        sql = None
        
        valuers = ''
        size_columns = len(dic_datas)
        cont = 0
        for key, valuer in dic_datas.items():
            cont += 1
            if cont != size_columns:
                valuers += '{0} = {1}, '.format(key, '"'+str(valuer)+'"')
            else:
                valuers += '{0} = {1}'.format(key, '"'+str(valuer)+'"')
        
        sql = f'UPDATE {name_table} SET {valuers} WHERE {name_id_table} = {id_register};'
        
        self._cur.execute(sql)
        self._conection.commit()
        
    def delete_register(self, name_table, name_id_table, id_register):
        sql = f'DELETE FROM {name_table} WHERE {name_id_table} = {id_register}'
        self._cur.execute(sql)
        self._conection.commit()

    def query_record(self, name_table, name_id_table, id_register):
        sql = f'SELECT COUNT(*) FROM {name_table} WHERE {name_id_table} = {id_register};'
        
        register_exist = None
        
        self._cur.execute(sql)
        for row in self._cur:
            register_exist = row[0]
                
        if register_exist == 0:
            return False
        return True

        
#data = Database()
#data.insert_register()
'''
valor = 'teste'
tes = 'ola'
print('{0} = {1}, '.format(valor, '"'+tes+'"'))


val = {'id_register_people':'Andre luiz', 'name':'Pires', 'sex':1}
print('{}'.format(', '.join(['"' +str(_)+'"' for _ in val.values()])))


valores = ['id_register_people', 'name', 'sex', 'novo']
val = {'id_register_people':'Andre', 'name':'Pires', 'sex':1}

val['novo'] = 56

print(val.values())

User= collections.namedtuple('User', valores)



print(','.join([str(_) for _ in val]))

m = User(**val)
m.count(val)

print(User._fields)

for i in m:
    print(i)'''