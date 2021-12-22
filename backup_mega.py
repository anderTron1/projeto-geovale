from mega import  Mega
from datetime import datetime
import os

import shutil
import zipfile
from pathlib import Path

import PySimpleGUI as sg
import time

class Backup_mega:
    def __init__(self):
        self.__folder_database = 'database'
        self.__folder_save_database = 'backup_database'
        self.__folder_database_pull = 'backup_database/pull'
        
        self.mega = Mega() 
        self.m = None
        #mega = Mega({'verbose': True})  # verbose option for print output
        
    def compact(self):
        date = '_'+datetime.today().strftime('%Y_%m_%d %He%M hs')
        root_folde = self.__folder_save_database
        arqzip = root_folde + '/'+self.__folder_database+date
        
        shutil.make_archive(arqzip, 'zip', './', self.__folder_database)
        
        return root_folde, arqzip + '.zip', self.__folder_database+date+'.zip'
    
    def __desconpacta(self, window, progress_bar):
        arq = None
        for _,_, file in os.walk(self.__folder_save_database):
            arq = file[0]
        
        print(arq)
        window.Element(DEFAULT_KEY_TXT_PROCESS_DOWNLOAD).update('Descompactando arquivo \n['+arq+']...')
        progress_bar.UpdateBar(2,5)
        time.sleep(.6)
        
        with zipfile.ZipFile(self.__folder_database_pull+'/'+arq,"r") as Zip_ref:
            Zip_ref.extractall(self.__folder_database_pull)
    
        
        root_src_dir = self.__folder_database_pull + '/' + self.__folder_database + '/'
        root_dst_dir = self.__folder_database +'/'
    
        window.Element(DEFAULT_KEY_TXT_PROCESS_DOWNLOAD).update('Extraindo registros do backup\n ['+arq+']...')
        progress_bar.UpdateBar(3,5)
        time.sleep(.6)
        for src_dir, dirs, files in os.walk(root_src_dir):
            dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file):
                    # in case of the src and dst are the same file
                    if os.path.samefile(src_file, dst_file):
                        continue
                    os.remove(dst_file)
                shutil.move(src_file, dst_dir)
        
        window.Element(DEFAULT_KEY_TXT_PROCESS_DOWNLOAD).update('Substituindo registros pelo backup...')
        progress_bar.UpdateBar(4,5)
        time.sleep(.6)
        try:
            shutil.rmtree('backup_database/pull/database')
            os.remove('backup_database/pull/'+arq)
            
            window.Element(DEFAULT_KEY_TXT_PROCESS_DOWNLOAD).update('Processo realizado com sucesso...')
            progress_bar.UpdateBar(5,5)
            time.sleep(.6)
            
            return True
        except OSError as e:
            window.Element(DEFAULT_KEY_TXT_PROCESS_DOWNLOAD).update('ERRO! Não foi possivel realizar o processo de substituição...')
            return False
            
            
        
    def login_mega(self,window, email, password):
        window.Element(DEFAULT_KEY_LOGADO).update("Aguarde, realizando conexão com o site do mega...", text_color='white')
        #user details
        email = email
        password = password
        # login
        try:
            self.m = self.mega.login(email, password)
        except: 
            self.m = None
            
        if self.m != None:
            return self.m.get_user()['name']
        return None
        
    def upload(self, window, progress_bar):
        window.Element(DEFAULT_KEY_PROCESS_UPLOAD).update('Compactando databases...')
        progress_bar.UpdateBar(1,4)
        time.sleep(.6)
        
        root_folde, path, file = self.compact()
        
        try:
            if self.m.find(root_folde) == None:
                window.Element(DEFAULT_KEY_PROCESS_UPLOAD).update("Criando pasta ["+root_folde+"] no Mega\n para o arquivo ["+file+"] gerado...")
                progress_bar.UpdateBar(2,4)
                time.sleep(.6)
                self.m.create_folder(root_folde)
                
            
            if self.m.find(path) == None:  
                window.Element(DEFAULT_KEY_PROCESS_UPLOAD).update("Fazendo upload do arquivo\n ["+file+"] para o mega...")
                progress_bar.UpdateBar(3,4)
                time.sleep(.6)
                self.m.upload(path, self.m.find(root_folde)[0])
                
                window.Element(DEFAULT_KEY_PROCESS_UPLOAD).update("Processo finalizado!")
                progress_bar.UpdateBar(4,4)
                time.sleep(.6)
        except ConnectionError:
            window.Element(DEFAULT_KEY_PROCESS_UPLOAD).update("Erro de conexão com o mega ocorreu!")
            
    def download(self,window, progress_bar, link):
        window.Element(DEFAULT_KEY_TXT_PROCESS_DOWNLOAD).update('Iniciando download...')
        progress_bar.UpdateBar(1,5)
        time.sleep(.6)
        
        try:
            self.m.download_url(link, self.__folder_database_pull)
        except ConnectionError:
            window.Element(DEFAULT_KEY_TXT_PROCESS_DOWNLOAD).update('Erro de conexão com o mega ocorreu!')
        except:
            window.Element(DEFAULT_KEY_TXT_PROCESS_DOWNLOAD).update('Um erro ocorreu e não foi possivel continuar...ERRO: ')
            
        return self.__desconpacta(window, progress_bar)
        

DEFAULT_KEY_EMAIL = '<<EMAIL_MEGA>>'
DEFAULT_KEY_PASSWORD = '<<SENHA_MEGA>>'
DEFAULT_KEY_BTN_UPLOAD = '<<SALVAR_E_FAZER_UPLOAD>>'
DEFAULT_KEY_PROGRESS = '<<BARRA_DE_PROGRESSO>>'
DEFAULT_KEY_TEXT_CONDITION_PROCESS = '<<PROCESSO_REALIZADO>>'
DEFAULT_KEY_LOGAR = '<<LOGAR_NO_MEGA>>'
DEFAULT_KEY_LOGADO = '<<ESTA_LOGADO_NA_CONTA>>'
DEFAULT_KEY_PROCESS_UPLOAD = '<<PROCESSO_DE_UPLOAD>>'

DEFAULT_KEY_PROGRESS_DOWNLOAD = '<<PROGROSSO_DE_DOWNLOAD>>'
DEFAULT_KEY_LINK_DOWNLOAD = '<<LINK_DO_DOWNLOAD>>'
DEFAULT_KEY_BTN_DOWNLOAD = '<<BTN_DOWNLOAD>>'
DEFAULT_KEY_TXT_PROCESS_DOWNLOAD = '<<TXT_PROCESSO_DE_DOWNLOAD>>'

class Backup_database:
    def __init__(self):
        self.backup_mega = Backup_mega()
        
        
    def layout(self):
        
        login = [
                [sg.T('Email'), sg.Input('andre-luizpiresguimaraes@outlook.com',size=45, key=DEFAULT_KEY_EMAIL)],
                [sg.T('Senha'), sg.Input('andertron123', size=20, password_char='*', key=DEFAULT_KEY_PASSWORD)],
                [sg.Button('loga', key=DEFAULT_KEY_LOGAR), sg.T('', key=DEFAULT_KEY_LOGADO)]
                ]
        
        backup = [
                [sg.Button('Upload backup', key=DEFAULT_KEY_BTN_UPLOAD)],
                [sg.ProgressBar(1, orientation='h',size=(25,15),key=DEFAULT_KEY_PROGRESS)],
                [sg.T('', key=DEFAULT_KEY_PROCESS_UPLOAD)]
                ]
        download = [
                    [sg.T('Link mega do arquivo zip para o download')],
                    [sg.Input(size=60, key=DEFAULT_KEY_LINK_DOWNLOAD)],
                    [sg.Button('Baixar e atualizar', key=DEFAULT_KEY_BTN_DOWNLOAD)],
                    [sg.ProgressBar(1, orientation='h', size=(25,15),key=DEFAULT_KEY_PROGRESS_DOWNLOAD)],
                    [sg.T('', key=DEFAULT_KEY_TXT_PROCESS_DOWNLOAD)]
                   ]
        tag_backup = [
                    [sg.Tab('Config para backup', [[sg.Frame('Realizar backup e fazer upload para o mega', backup)]])],
                    [sg.Tab('Config para download', [[sg.Frame('Realizar download dos dados e importar o novo db para o sistema', download)]])]
                    ]
        
        layout = [
                    [login],
                    [sg.TabGroup(tag_backup)]
                 ]
        
        return layout
    
    def exec_class(self):
        window = sg.Window('Gerenciamento de backup da base de dados', self.layout(), icon=r'image/iconLogo.ico', modal=True)
        
        while(True):
            event, value = window.read(timeout=100)
            
            if event == sg.WINDOW_CLOSED:
                break
            
            if event == DEFAULT_KEY_LOGAR:
                result = self.backup_mega.login_mega(window,value[DEFAULT_KEY_EMAIL], value[DEFAULT_KEY_PASSWORD])
                if result != None:
                    window.Element(DEFAULT_KEY_LOGADO).update("Usuario: "+ result+' logado no mega', text_color='white')
                else:
                    window.Element(DEFAULT_KEY_LOGADO).update('Um erro ocorreu ao tentar loga na conta', text_color='red')
            if event == DEFAULT_KEY_BTN_UPLOAD:
                progress_bar = window.Element(DEFAULT_KEY_PROGRESS)
                self.backup_mega.upload(window, progress_bar)
                
            if event == DEFAULT_KEY_BTN_DOWNLOAD:
                progress_bar = window.Element(DEFAULT_KEY_PROGRESS_DOWNLOAD)
                result = self.backup_mega.download(window, progress_bar, value[DEFAULT_KEY_LINK_DOWNLOAD])
                
                if result != False:
                    window.Element(DEFAULT_KEY_LINK_DOWNLOAD).update('')
                
        window.close()
        
if __name__ == '__main__':
    
    app = Backup_database()
    app.exec_class()