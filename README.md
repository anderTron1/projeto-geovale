"""
Created on Fri Oct  8 11:38:16 2021

@author: andre Luiz Pires Guimarães
@cell: (66)984185015
@email: andreluizpires1507@gmail.com
"""

# projeto-geovale

Para executar as funcionalidades instala os requisitos do arquivo requirements.txt
O arquivo layouts.py é onde se encontra o mean de execução do sistema.
O banco de dados utilizado é o sqlite3 chamado database.sqlite3, juntamente com outras bases de dados que se encontram na pasta chamada database

### PROBLEMA DE NEGÓCIO
O sistema em questão tem por objetivos:
  * Realizar cadastros de clientes
  * Cadastra contratos com tags onde as mesmas seram substituidas por valores salvos dos registros clientes
  * Gerar relatorios excel dos registros cadastrados dos clientes
  * Gerar backup e salvar localmente e remotamente no site mega, e da mesma forma importar a base de dados salvo no mega para o sistema caso necessario
    * (O mega foi escolhido devido a disponibilidade gratuita de 50G para utiliza-lo)
    
### PAGINA PRINCIPAL
Nesta pagina possui as principais funcionalidades 
#### Menu:
 * Cadastro
 * Exportar Dados
 * Configurações
 * Sair
#### Contratos:
 * Gerar tags para contratos
 * Lista de contratos
 * Gerar contratos
#### Sobre
 * Dados do desenvolvedor

![Alt text](image_system/pagina_principal.PNG?raw=true "pagina_principal")

### PAGINA DE CADASTRO
Nesta pagina seram feitos os cadastros de todos os clientes
e também onde são feitas as auterações necessarias no mesmo. Para consultar novos clientes, no canto inferior esquerto tem a opção [procurar]
![Alt text](image_system/cadastro.PNG?raw=true "cadastro")

#### PAGINA PARA CONSULTAR CLIENTES
![Alt text](image_system/clientes.PNG?raw=true "clientes")

### PAGINA PARA EXPORTAR DADOS
Nesta pagina é possivel exportar os registros em excel de acordo com as configurações que for preenchidas. 
![Alt text](image_system/exportar_dados.PNG?raw=true "exportar_dados")

### PAGINA PARA CONFIGURAÇÃO
Nesta pagina fica as configurações que serão necessarias quando for cadastra algum cliente, dessa forma o tipo de cliente será cadastrado de agordo com as configurações desta pagina.

![Alt text](image_system/configurações_basicas.PNG?raw=true "configurações_basicas")

![Alt text](image_system/configurações_basicas_projeto.PNG?raw=true "configurações_basicas_projeto")

### PAGINA PARA BACKUP
Nesta pagina é feita o backup do banco de dados, incluendo os contrados que estiverem salvos. São feitos dois backup, um localmente e outro no site do mega.
Para realizar o backup, deve-se primeiro fazer o login no site do mega, dessa forma as outras funcionalidades seram liberadas. Na parte [conf para download] é onde é feita o download do backup com o link do arquivo do mega, dessa forma o processo é automativo onde ele faz o download e substitui o database do sistema.

![Alt text](image_system/realizar_backup.PNG?raw=true "realizar_backup")

![Alt text](image_system/realizar_download_backup.png?raw=true "realizar_download_backup")

### PAGINA GERAR TAGS PARA CONTRATOS
Nesta pagina são geradas as tags para colocar no arquivo word, onde as mesmas seram substituidas pelos campos dos registros salvos no banco de dados,
onde o [arquivo pdf gerado] são as informações em pdf de cada tag, e na opção [exportar arq. excel] são as tags em excel para usar na mala direta no word para informar os campos onde seram reconhecidas pelo sistema.

![Alt text](image_system/gerar_tags.PNG?raw=true "gerar_tags")

Lista de contratos

### PAGINA LISTA DE CONTRATOS
Nesta pagina ficam o banco de dados dos contratos em word, nela é possivel importar novos contratos, abrir contratos salvos e exlui-los.

![Alt text](image_system/importar_contratos.PNG?raw=true "importar_contratos")

### PAGAINA GERAR CONTRATOS 
Nesta pagina é onde seram exportados os contratos com as informações do cliente, esse arquivo será gerado e salvo em word.

![Alt text](image_system/gerar_contratos.PNG?raw=true "gerar_contratos")






