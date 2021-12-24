#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:16:17 2021

@author: andre
"""


#sg.ChangeLookAndFeel('DarkTeal10')

#-------------------------------BOOLEAN KEYS------------------------------
KEY_YES = 'Sim' 
KEY_NOT = 'Não'

#-------------------------------KEYS FOR THE spouse_frame------------------ 

DEFAULT_KEY_NAME_SPOUSE = '«NOME_DO_CONJUGE»'
DEFAULT_KEY_SEX_SPOUSE = '«SEXO_DO_CONJUGE»'
DEFAULT_KEY_BIRTHDATE_SPOUSE = '«DATA_DE_NASCIMENTO_DO_CONJUGE»'
DEFAULT_KEY_AGE_SPOUSE = '«IDADE_DO_CONJUGE»'
DEFAULT_KEY_NATURALNESS_SPOUSE = '«NATURALIDADE_DO_CONJUGE»'
DEFAULT_KEY_TEL_SPOUSE = '«TELEFONE_DO_CONJUGE»'
DEFAULT_KEY_CEL_SPOUSE = '«CELULAR_DO_CONJUGE»'
DEFAULT_KEY_RG_SPOUSE = '«RG_DO_CONJUGE»'
DEFAULT_KEY_ISSUING_BODY_SPOUSE = '«ORGAO_EMISSOR_DO_CONJUGE»'
DEFAULT_KEY_CPF_SPOUSE = '«CPF_DO_CONJUGE»'
DEFAULT_KEY_CNH_SPOUSE = '«CNH_DO_CONJUGE»'
DEFAULT_KEY_VOTER_TITLE_SPOUSE = '«TITULO_ELEITORAL_DO_CONJUGE»'
DEFAULT_KEY_SCHOOLING_SPOUSE = '«ESCOLARIDADE_DO_CONJUGE»'

#----------------------------- key batch to be regularized-------------------

DEFAULT_KEY_BATCH_REGU_BATCH = '«LOTE_REGULARIZAR»'
DEFAULT_KEY_BATCH_REGU_BLOCK = '«QUADRA_REGULARIZAR»'
DEFAULT_KEY_BATCH_REGU_BATCH_REGULARIZAR_DISTRICT = '«BAIRRO_REGULARIZAR»'
DEFAULT_KEY_BATCH_REGU_AREA = '«AREA_M_QUADRADO_REGULARIZAR»'
DEFAULT_KEY_BATCH_REGU_STREET_LOTE = '«RUA_DO_LOTE_REGULARIZAR»'

#------------------------------key combo type of framework----------------------
DEFAULT_KEY_TYPE_FRAMEWORK = '«TIPO_DE_ENQUADRAMENTO_REURB»'

#------------------------------KEYS TO personal_data_tab-------------------

DEFAULT_KEY_NOME_PERSONAL_DATA = '«NOME_PESSOAL»'
DEFAULT_KEY_SEX_PERSONAL_DATA = '«SEXO»'
DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA = '«DATA_DE_NASCIMENTO»'
DEFAULT_KEY_AGE_PERSONAL_DATA = '«IDADE'
DEFAULT_KEY_NATURALNESS_PERSONAL_DATA = '«NATURALIDADE»'
DEFAULT_KEY_UF_PERSONAL_DATA = '«UF'
DEFAULT_KEY_TEL_PERSONAL_DATA = '«TELEFONE»'
DEFAULT_KEY_CEL_PERSONAL_DATA = '«CELULAR»'
DEFAULT_KEY_EMAIL_PERSONAL_DATA = '«EMAIL»'
DEFAULT_KEY_CITY = '«CIDADE»'
DEFAULT_KEY_STATE = '«ESTADO»'
DEFAULT_KEY_CEP = '«CEP»'
DEFAULT_KEY_ADDRESS_PERSONAL_DATA = '«ENDERECO»'
DEFAULT_KEY_DISTRICT_PERSONAL_DATA = '«BAIRRO»'
DEFAULT_KEY_HOUSE_NUMBER_PERSONAL_DATA = '«NUMERO_DA_CASA»'
DEFAULT_KEY_RG_PERSONAL_DATA = '«RG»'
DEFAULT_KEY_ISSUING_BODY_PERSONAL_DATA = '«ORGAO_EMISSOR»'
DEFAULT_KEY_CPF_PERSONAL_DATA = '«CPF»'
DEFAULT_KEY_CNH_PERSONAL_DATA = '«CNH»'
DEFAULT_KEY_VOTER_TITLE_PERSONAL_DATA = '«TITULO_ELEITORAL»'
DEFAULT_KEY_CONSIDER_PERSONAL_DATA = '«CONSIDERA_SE»'
DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA = '«ESTADO_CIVIL»'
DEFAULT_KEY_SCHOOLING_PERSONAL_DATA = '«ESCOLARIDADE»'
DEFAULT_KEY_UNION_REGIME = '«REGIME_DE_UNIAO»'

#----------------------------keys to TabGroup------------------------

DEFAULT_KEY_PERSONAL_DATA_TABGROUP = '-TABDADOSPESSOAL-'
DEFAULT_KEY_OTHER_INFOR_TABGROUP = '-TABOUTRASINFOR-'
DEFAULT_KEY_RESIDENTS_REGIST_TABGROUP = '-TABCADASMORA-'
DEFAULT_KEY_TABGROUP = '-TABGROUDADOPESSOAL-'

#-------------------------KEY to tab other_information----------------------
DEFAULT_KEY_COMB_WORKS = '«TRABALHA»'
DEFAULT_KEY_INP_WHERE = '«ONDE»'
DEFAULT_KEY_TXT_PROFESSION = '«PROFISSAO»'
DEFAULT_KEY_COMB_RETIREE = '«E_APOSENTADO»'
DEFAULT_KEY_BENEF_CAMB_SOCI_PROG = '«BENEFICIARIO_DE_ALGUM_PROGRAMA_SOCIAL»'
DEFAULT_KEY_INCOME_COMB_INCOME = '«RENDA»'
DEFAULT_KEY_COMB_HAVE_CHILDREM = '«TEM_FILHOS»'
DEFAULT_KEY_HOW_MANY_CHILDREM = '«QUANTOS_FILHOS»'
DEFAULT_KEY_LIVES_DISABLED_OR_ELDERLY = '«MORA_DEFICIENTE_OU_IDOSO»'
DEFAULT_KEY_DISABLED_ELDERLY_HOW_MANY = '«QUANTOS_DEFIENTES_OU_IDOSOS»'
DEFAULT_KEY_COMB_OWN_RURAL_PROPERTY = '«POSSUI_OUTRO_IMOVEL_RURAL»'

DEFAULT_KEY__COMB_OWNS_CAR = '«POSSUI_AUTOMOVEL»'
DEFAULT_KEY_OWNS_CAR_HOW_MANY = '«QUANTOS_AUTOMOVEIS»'
DEFAULT_KEY__COMB_HAS_MOTORCICLE = '«POSSUI_MOTOCICLETAS»'
DEFAULT_KEY_HAS_MOTORCICLE_HOW_MANY = '«QUANTAS_MOTOCICLETAS»'
DEFAULT_KEY_COMB__HAVE_FRIDGE = '«TEM_GELADEIRA»'
DEFAULT_KEY_HAVE_FRIDGE_HOW_MANY = '«QUANTAS_GELADEIRAS»'
DEFAULT_KEY_COMB__HAVE_TELEVI = '«POSSUI_TELEVISAO»'
DEFAULT_KEY_HAVE_TELEVI_HOW_MANY = '«QUANTAS_TELEVISOES»'
DEFAULT_KEY_COMB__HAVE_COMPUTER = '«POSSUI_COMPUTADOR»'
DEFAULT_KEY_HAVE_COMPUTER_HOW_MANY = '«QUANTOS_COMPUTADORES»'
DEFAULT_KEY_COMB__HAVE_INTERNET = '«POSSUI_INTERNET»'
DEFAULT_KEY_COMB__HAVE_ACESS_ELECTRI = '«POSSUI_ENERGIA_ELETRICA»'
DEFAULT_KEY_COMB__HAVE_DRAINAG_WATER = '«POSSUI_AGUA_ENCANADA»'

#--------------------------KEY FRAME PROPERTY CONDITIONS-----------------
DEFAULT_KEY_COMB_ONLY_OWNER = '«TEM_OUTRO_DONO»'
DEFAULT_KEY_TXT_ANOTHER_OWNER = '«NOME_DO_OUTRO_DONO»'
DEFAULT_KEY_TXT_STILL_TIME = '«QUANTO_TEMPO_POSSUI_O_IMOVEL»'
DEFAULT_KEY_COMB_HAVE_ANOTHER_URBAN_PROPERTY = '«POSSUI_OUTRO_IMOVEL_URBANO»'    
DEFAULT_KEY_ANOTHER_PROPERTY_HOW_MANY = '«QUANTOS_IMOVEL_URBANO_POSSUI»'
DEFAULT_KEY_TXT_ANOTHER_PROPERTY_WHERE = '«ONDE_POSSUI_O_IMOVEL_URBANO»'
DEFAULT_KEY_COMB_REAL_ESTATE_CONSTRUC = '«TEM_EDIFICACAO_NO_IMOVEL»'
DEFAULT_KEY_PROPERTY_USED_FOR = '«UTILIZA_O_IMOVEL_PARA»'

DEFAULT_KEY_TXT_FRONT = '«FRENTE»'
DEFAULT_KEY_TXT_RIGHT = '«DIREITA»'
DEFAULT_KEY_TXT_LEFT = '«ESQUERDA»'
DEFAULT_KEY_TXT_FUNDS = '«FUNDOS»'

DEFAULT_KEY_COMB_TYPE = '«TIPO_DO_IMOVEL»'
DEFAULT_KEY_COMB_IS_WALLED = '«E_MORADA»'
DEFAULT_KEY_COMB_BATCH_POSITION = '«POSICAO_DO_LOTE»'
DEFAULT_KEY_COMB_STATE_BUILDINGS = '«ESTADO_DAS_EDIFICACOES»'
DEFAULT_KEY_COMB_BUILDING_TYPE = '«TIPO_DE_CONSTRUCAO»'
DEFAULT_KEY_COMB_IS_BEDRIDDEN = '«TEM_ACABAMENTO»'
DEFAULT_KEY_NUMB_FLOORS = '«NUMERO_DE_PAVIMENTOS»'
DEFAULT_KEY_ROOMS = '«COMODOS»'
DEFAULT_KEY_BATHROOMS = '«BANHEIROS»'

DEFAULT_KEY_PROJECT_SERVICES = '«PROJETOS_SERVICOS»'

#-------------------------key registration residents--------------------
DEFAULT_KEY_TABLE_RESIDENTS = '«RESIDENTS»'

DEFAULT_KEY_INPUT_ID_REGIST_RESID = '«ID_CADASTRO_MORADORES»'
DEFAULT_KEY_TXT_NOME_REGIST_RESID = '«NOME_CADASTRO_MORADORES»'
DEFAULT_KEY_SPIN_KINSHIP_REGIST_RESID = '«PARENTESCO_CADASTRO_MORADORES»'
DEFAULT_KEY_SPIN_AGE = '«IDADE_CADASTRO_MORADORES»'
DEFAULT_KEY_COMB_SEX_REGIST_RESID = '«SEXO_CADASTRO_MORADORES»'
DEFAULT_KEY_COMB_MARITAL_STATUS_REGIST_RESID = '«ESTADO_CIVIL_CADASTRO_MORADORES»'
DEFAULT_KEY_TXT_OCCUPATION_REGIST_RESID = '«OCUPAÇÃO_CADASTRO_MORADORES»'
DEFAULT_KEY_TXT_INCOME_REGIST_RESID = '«RENDA_CADASTRO_MORADORES»'

DEFAULT_KEY_TXT_FAMILY_INCOME_REGIST_RESID = '«RENDA_FAMILIAR_TOTAL_CADASTRO_MORADORES»'


#-----------------------------BTNS--------------------------


#-------------------------BTNS TYPE OFF FRAMEWORKS REURBS-------------------
DEFAULT_KEY_EDIT_TYPE_FRAMEWORK = '«BTN_EDITAR_TIPO_ENQUADRAMENTO_REURB»'
DEFAULT_KEY_SAVE_TYPE_FRAMEWORK = '«BTN_SAVAR_TIPO_ENQUADRAMENTO_REURB»'

def keys_fields():
        keys = [               
                #-------------------------KEYS TO personal_data_tab------------------------------
                DEFAULT_KEY_NOME_PERSONAL_DATA,         DEFAULT_KEY_SEX_PERSONAL_DATA,
                DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA,    DEFAULT_KEY_AGE_PERSONAL_DATA,
                DEFAULT_KEY_NATURALNESS_PERSONAL_DATA,  DEFAULT_KEY_UF_PERSONAL_DATA,
                DEFAULT_KEY_TEL_PERSONAL_DATA,          DEFAULT_KEY_CEL_PERSONAL_DATA,
                DEFAULT_KEY_EMAIL_PERSONAL_DATA,        DEFAULT_KEY_CITY,
                DEFAULT_KEY_STATE,                      DEFAULT_KEY_CEP,
                DEFAULT_KEY_ADDRESS_PERSONAL_DATA,
                DEFAULT_KEY_DISTRICT_PERSONAL_DATA,     DEFAULT_KEY_HOUSE_NUMBER_PERSONAL_DATA,
                DEFAULT_KEY_RG_PERSONAL_DATA,           DEFAULT_KEY_ISSUING_BODY_PERSONAL_DATA,
                DEFAULT_KEY_CPF_PERSONAL_DATA,          DEFAULT_KEY_CNH_PERSONAL_DATA,
                DEFAULT_KEY_VOTER_TITLE_PERSONAL_DATA,  DEFAULT_KEY_CONSIDER_PERSONAL_DATA,
                DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA, DEFAULT_KEY_SCHOOLING_PERSONAL_DATA,
                DEFAULT_KEY_BATCH_REGU_BATCH,           DEFAULT_KEY_BATCH_REGU_BLOCK,
                DEFAULT_KEY_BATCH_REGU_BATCH_REGULARIZAR_DISTRICT, DEFAULT_KEY_BATCH_REGU_AREA,
                DEFAULT_KEY_BATCH_REGU_STREET_LOTE,
                
                #-------------------------KEY to tab other_information----------------------------
                DEFAULT_KEY_COMB_WORKS,                 DEFAULT_KEY_INP_WHERE,
                DEFAULT_KEY_TXT_PROFESSION,             DEFAULT_KEY_COMB_RETIREE,
                DEFAULT_KEY_BENEF_CAMB_SOCI_PROG,       DEFAULT_KEY_INCOME_COMB_INCOME,
                DEFAULT_KEY_COMB_HAVE_CHILDREM,         DEFAULT_KEY_HOW_MANY_CHILDREM,
                DEFAULT_KEY_LIVES_DISABLED_OR_ELDERLY,  DEFAULT_KEY_DISABLED_ELDERLY_HOW_MANY,
                DEFAULT_KEY_COMB_OWN_RURAL_PROPERTY, 
                
                DEFAULT_KEY__COMB_OWNS_CAR,         DEFAULT_KEY_OWNS_CAR_HOW_MANY,
                DEFAULT_KEY__COMB_HAS_MOTORCICLE,   DEFAULT_KEY_HAS_MOTORCICLE_HOW_MANY,
                DEFAULT_KEY_COMB__HAVE_FRIDGE,      DEFAULT_KEY_HAVE_FRIDGE_HOW_MANY,
                DEFAULT_KEY_COMB__HAVE_TELEVI,      DEFAULT_KEY_HAVE_TELEVI_HOW_MANY,
                DEFAULT_KEY_COMB__HAVE_COMPUTER,    DEFAULT_KEY_HAVE_COMPUTER_HOW_MANY,
                DEFAULT_KEY_COMB__HAVE_INTERNET,    DEFAULT_KEY_COMB__HAVE_ACESS_ELECTRI,
                DEFAULT_KEY_COMB__HAVE_DRAINAG_WATER, 
                
                #--------------------------KEY FRAME PROPERTY CONDITIONS---------------------------
                DEFAULT_KEY_COMB_ONLY_OWNER,             DEFAULT_KEY_TXT_ANOTHER_OWNER,
                DEFAULT_KEY_TXT_STILL_TIME,              DEFAULT_KEY_COMB_HAVE_ANOTHER_URBAN_PROPERTY,
                DEFAULT_KEY_ANOTHER_PROPERTY_HOW_MANY,   DEFAULT_KEY_TXT_ANOTHER_PROPERTY_WHERE,
                DEFAULT_KEY_COMB_REAL_ESTATE_CONSTRUC,   DEFAULT_KEY_PROPERTY_USED_FOR,
                
                DEFAULT_KEY_TXT_FRONT,   DEFAULT_KEY_TXT_RIGHT,
                DEFAULT_KEY_TXT_LEFT,    DEFAULT_KEY_TXT_FUNDS,
                
                DEFAULT_KEY_COMB_TYPE,               DEFAULT_KEY_COMB_IS_WALLED,
                DEFAULT_KEY_COMB_BATCH_POSITION,     DEFAULT_KEY_COMB_STATE_BUILDINGS,
                DEFAULT_KEY_COMB_BUILDING_TYPE,      DEFAULT_KEY_COMB_IS_BEDRIDDEN,
                DEFAULT_KEY_NUMB_FLOORS,             DEFAULT_KEY_ROOMS,
                DEFAULT_KEY_BATHROOMS,               DEFAULT_KEY_PROJECT_SERVICES,
                DEFAULT_KEY_TYPE_FRAMEWORK]
        return keys
    
def keys_fields_spouse():
        keys = [
            DEFAULT_KEY_NAME_SPOUSE,
            DEFAULT_KEY_SEX_SPOUSE,
            DEFAULT_KEY_BIRTHDATE_SPOUSE,
            DEFAULT_KEY_AGE_SPOUSE,
            DEFAULT_KEY_NATURALNESS_SPOUSE,
            DEFAULT_KEY_TEL_SPOUSE,
            DEFAULT_KEY_CEL_SPOUSE,
            DEFAULT_KEY_RG_SPOUSE,
            DEFAULT_KEY_ISSUING_BODY_SPOUSE,
            DEFAULT_KEY_CPF_SPOUSE,
            DEFAULT_KEY_CNH_SPOUSE,
            DEFAULT_KEY_VOTER_TITLE_SPOUSE,
            DEFAULT_KEY_SCHOOLING_SPOUSE,
            DEFAULT_KEY_UNION_REGIME
            ]
        return keys
    
def key_fields_residents():
    keys = [
        DEFAULT_KEY_INPUT_ID_REGIST_RESID,
        DEFAULT_KEY_TXT_NOME_REGIST_RESID,
        DEFAULT_KEY_SPIN_KINSHIP_REGIST_RESID,
        DEFAULT_KEY_SPIN_AGE,
        DEFAULT_KEY_COMB_SEX_REGIST_RESID,
        DEFAULT_KEY_COMB_MARITAL_STATUS_REGIST_RESID,
        DEFAULT_KEY_TXT_OCCUPATION_REGIST_RESID,
        DEFAULT_KEY_TXT_INCOME_REGIST_RESID]
    return keys
    