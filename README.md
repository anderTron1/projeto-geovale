"""
Created on Fri Oct  8 11:38:16 2021

@author: andre Luiz Pires Guimarães
"""

# projeto-geovale

Para executar as funcionalidades instala os requisitos do arquivo requirements.txt.txt
O arquivo layouts.py é onde se encontra o mean de execução do sistema.
O banco de dados utilizado é o sqlite3 chamado database.sqlite3, juntamente com outras bases de dados que se encontram na pasta chamada database

### PROBLEMA DE NEGÓCIO
O sistema em questão tem por objetivos:
  * Realizar cadastros de clientes
  * Cadastra contratos com tags onde as mesmas seram substituidas por valores salvos dos registros clientes
  * Gerar relatorios excel dos registros cadastrados dos clientes
  * Gerar backup e salvar localmente e remotamente no site mega, e da mesma forma importar a base de dados salvo no mega para o sistema caso necessario
    * (O mega foi escolhido devido a disponibilidade gratuida de 50G para utiliza-lo)
    
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

![Alt text](sistema/pagina_principal.PNG?raw=true "Title")

### PAGINA DE CADASTRO
Nesta pagina seram feitos os cadastros de todos os clientes
e também onde são feitas as auterações necessarias no mesmo. Para consultar novos clientes, no canto inferior esquerto tem a opção [procurar]
![Alt text](sistema/cadastro.PNG?raw=true "Title")

#### PAGINA PARA CONSULTAR CLIENTES
![Alt text](sistema/clientes.PNG?raw=true "Title")

### PAGINA PARA EXPORTAR DADOS
Nesta pagina é possivel exportar os registros em excel de acordo com as configurações que for preenchidas. 
![Alt text](sistema/exportar_dados.PNG?raw=true "Title")

### PAGINA PARA CONFIGURAÇÃO
Nesta pagina fica as configurações que serão necessarias quando for cadastra algum cliente, dessa forma o tipo de cliente será cadastrado de agordo com as configurações desta pagina.
![Alt text](sistema/configurações_basicas.PNG?raw=true "Title")
![Alt text](sistema/configurações_basicas_projeto.PNG?raw=true "Title")




