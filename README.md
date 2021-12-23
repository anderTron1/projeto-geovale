"""
Created on Fri Oct  8 11:38:16 2021

@author: andre Luiz Pires Guimarães
"""

# projeto-geovale

Para executar as funcionalidades instala os requisitos do arquivo requirements.txt.txt
O arquivo layouts.py é onde se encontra o mean de execução do sistema.
O banco de dados utilizado é o sqlite3 chamado database.sqlite3, juntamente com outras bases de dados que se encontram na pasta chamada database

PROBLEMA DE NEGÓCIO
O sistema em questão tem por objetivos:
  * Realizar cadastros de clientes
  * Cadastra contratos com tags onde as mesmas seram substituidas por valores salvos dos registros clientes
  * Gerar relatorios excel dos registros cadastrados dos clientes
  * Gerar backup e salvar localmente e remotamente no site mega, e da mesma forma importar a base de dados salvo no mega para o sistema caso necessario
    * (O mega foi escolhido devido a disponibilidade gratuida de 50G para utiliza-lo)
    
