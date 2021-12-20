from mega import  Mega
from datetime import datetime
import os

import shutil
import zipfile

def creat_dir(m):
    root_folde, file = compact()
    
    if m.find(root_folde) == None:
        m.create_folder(root_folde)
        
    if m.find(file) == None:   
        m.upload(file, m.find(root_folde)[0])

def compact():
    date = '_'+datetime.today().strftime('%Y_%m_%d %He%M hs')
    root_folde = 'backup_database'
    arqzip = 'backup_database/database'+date
    shutil.make_archive(arqzip, 'zip', './', 'database')
    
    return root_folde, arqzip + '.zip'

def desconpacta(arq, pasta):
    
    with zipfile.ZipFile('backup_database/pull/'+arq,"r") as Zip_ref:
        Zip_ref.extractall(pasta)   
 
def download(m, path, remote_filename, local_filename=None):
        mega_file = m.find_path_descriptor(path, remote_filename)
        print('\n',mega_file)
        if local_filename:
            local_dir = os.path.dirname(local_filename)
            local_file_basename = os.path.basename(local_filename)
            return m.download(mega_file, local_filename)
        else:
            m.download(mega_file)
            

#print(os.path.dirname('teste'))
#print(os.path.basename('teste'))

def test():
    """
    Enter your account details to begin
    comment/uncomment lines to test various parts of the API
    see readme.md for more information
    """

    #user details
    email = 'andre-luizpiresguimaraes@outlook.com'
    password = 'andertron123'

    mega = Mega()
    #mega = Mega({'verbose': True})  # verbose option for print output

    # login
    m = mega.login(email, password)

    # get user details
    details = m.get_user()
    print(details)

    # get account files
    files = m.get_files()

    # get account disk quota in MB
    print(m.get_quota())
    # get account storage space
    print(m.get_storage_space())

    # example iterate over files
    #cont = 0
    #for file in files:
    #    files[file]
    #    cont+= 1
        #print(cont)

    # upload file
    #if m.find('geovale/teste') == None:
    #    m.create_folder('geovale/teste')
    #m.upload('database', m.find('geovale/teste')[0])
    #creat_dir(m)
    m.download_url('https://mega.nz/file/eQlGQKCZ#aa1DAqhLC7_Di3ITRkLUTe1YsOspTnROtKcd5AcEiVU', 'backup_database/pull')
    #ownload(m, 'database_2021_12_19 21e23 hs/files_pdf', 'tags_para_cadastro.pdf', 'teste')
    
    
#test()
#compact()
desconpacta('database_2021_12_20 08e28 hs.zip','backup_database/pull')