from mega import  Mega
from datetime import datetime
import os


def creat_dir(m):
    date = '_'+datetime.today().strftime('%Y_%m_%d %He%M hs')
    root_folde = 'database'+date
    
    if m.find(root_folde) == None:
        for pasta, subpasta, files in os.walk('database'):
        #for arq in arquivos:
            for path in subpasta:
                print(root_folde+'/'+path)
                m.create_folder(root_folde+'/'+path)
            print('Pasta Criada')
            
            for file in files:
                past_dir = pasta+'/'+file
                pasta_mega = pasta.replace('/', date+'/')
                print(file, pasta_mega)
                m.upload(past_dir, m.find(pasta_mega)[0])

def pull_dir():
    super
   
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

    #mega = Mega()
    mega = Mega({'verbose': True})  # verbose option for print output

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
    
    download(m, 'database_2021_12_19 21e23 hs/files_pdf', 'tags_para_cadastro.pdf', 'teste')

test()