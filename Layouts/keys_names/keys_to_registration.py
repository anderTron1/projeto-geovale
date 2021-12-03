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

DEFAULT_KEY_NAME_SPOUSE = '-NOMECONJ-'
DEFAULT_KEY_SEX_SPOUSE = '-SEXCONJ-'
DEFAULT_KEY_BIRTHDATE_SPOUSE = '-DATANASCICONJ-'
DEFAULT_KEY_AGE_SPOUSE = '-IDADECONJ-'
DEFAULT_KEY_NATURALNESS_SPOUSE = '-NATURALICONJ-'
DEFAULT_KEY_TEL_SPOUSE = '-TELCONJUGE-'
DEFAULT_KEY_CEL_SPOUSE = '-CELCONJUGE-'
DEFAULT_KEY_RG_SPOUSE = '-RGCONJ-'
DEFAULT_KEY_ISSUING_BODY_SPOUSE = '-ORGEMICONJ-'
DEFAULT_KEY_CPF_SPOUSE = '-CPFCONJUGE-'
DEFAULT_KEY_CNH_SPOUSE = '-CNHCONJ-'
DEFAULT_KEY_VOTER_TITLE_SPOUSE = '-TITELEITORCONJU-'
DEFAULT_KEY_SCHOOLING_SPOUSE = '-COMBOESCOLACONJ-'

#----------------------------- key batch to be regularized-------------------

DEFAULT_KEY_BATCH_REGU_BATCH = '<<-LOTE_REGULARIZAR->>'
DEFAULT_KEY_BATCH_REGU_BLOCK = '<<-QUADRA_REGULARIZAR->>'
DEFAULT_KEY_BATCH_REGU_BATCH_REGULARIZAR_DISTRICT = '<<-BAIRRO_REGULARIZAR->>'
DEFAULT_KEY_BATCH_REGU_AREA = '<<-AREA_M_QUADRADO_REGULARIZAR->>'
DEFAULT_KEY_BATCH_REGU_STREET_LOTE = '<<-RUA_DO_LOTE_REGULARIZAR->>'

#------------------------------key combo type of framework----------------------
DEFAULT_KEY_TYPE_FRAMEWORK = '<<-TIPO_DE_ENQUADRAMENTO_REURB->>'

#------------------------------KEYS TO personal_data_tab-------------------

DEFAULT_KEY_NOME_PERSONAL_DATA = '-NOMEDADOSPESSOAL-'
DEFAULT_KEY_SEX_PERSONAL_DATA = '-SEXPERSONALDATA-'
DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA = '-DATNACIPESSOAL-'
DEFAULT_KEY_AGE_PERSONAL_DATA = '-IDADEDADOPESSOAL-'
DEFAULT_KEY_NATURALNESS_PERSONAL_DATA = '-NATURALDADOSPESSOAL-'
DEFAULT_KEY_UF_PERSONAL_DATA = '-UFDADOSPESSOAL-'
DEFAULT_KEY_TEL_PERSONAL_DATA = '-TELDADOSPESSOAL-'
DEFAULT_KEY_CEL_PERSONAL_DATA = '-CELDADOSPESSOAL-'
DEFAULT_KEY_EMAIL_PERSONAL_DATA = '-EMAILDADOSPESSOAL-'
DEFAULT_KEY_ADDRESS_PERSONAL_DATA = '-ENDDADOSPESSOAL-'
DEFAULT_KEY_DISTRICT_PERSONAL_DATA = '-BAIRDADOSPESSOAL-'
DEFAULT_KEY_HOUSE_NUMBER_PERSONAL_DATA = '-NCASADADOPESSOAL-'
DEFAULT_KEY_RG_PERSONAL_DATA = '-RGDADOPESSOAL-'
DEFAULT_KEY_ISSUING_BODY_PERSONAL_DATA = '-ORGAOEMIDADOSPESSOAL-'
DEFAULT_KEY_CPF_PERSONAL_DATA = '-CPFDADOSPESSOAL-'
DEFAULT_KEY_CNH_PERSONAL_DATA = '-CNHPERSONALDATA-'
DEFAULT_KEY_VOTER_TITLE_PERSONAL_DATA = '-TITELEITORPESSOAL-'
DEFAULT_KEY_CONSIDER_PERSONAL_DATA = '-CONSIDEDADOSPESSOAL-'
DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA = '-ESTACIVILDADPESSOAL-'
DEFAULT_KEY_SCHOOLING_PERSONAL_DATA = '-COMBOESCOLA-'

#----------------------------keys to TabGroup------------------------

DEFAULT_KEY_PERSONAL_DATA_TABGROUP = '-TABDADOSPESSOAL-'
DEFAULT_KEY_OTHER_INFOR_TABGROUP = '-TABOUTRASINFOR-'
DEFAULT_KEY_RESIDENTS_REGIST_TABGROUP = '-TABCADASMORA-'
DEFAULT_KEY_TABGROUP = '-TABGROUDADOPESSOAL-'

#-------------------------KEY to tab other_information----------------------
DEFAULT_KEY_COMB_WORKS = '-RADIOWORKS-'
DEFAULT_KEY_INP_WHERE = '-INPUTWHERE-'
DEFAULT_KEY_TXT_PROFESSION = '-PROFESSION-'
DEFAULT_KEY_COMB_RETIREE = '-RETIREEY-'
DEFAULT_KEY_BENEF_CAMB_SOCI_PROG = '-BENEFICIARYSOCIALPROGRAM-'
DEFAULT_KEY_INCOME_COMB_INCOME = '-INCOME-'
DEFAULT_KEY_COMB_HAVE_CHILDREM = '-HAVECHILDREN-'
DEFAULT_KEY_HOW_MANY_CHILDREM = '-HOWMANYCRILDREN-'
DEFAULT_KEY_LIVES_DISABLED_OR_ELDERLY = '-LIVESDISABLEDORELDERLY-'
DEFAULT_KEY_DISABLED_ELDERLY_HOW_MANY = '-DISABLEDELDERLYHOWMANY-'
DEFAULT_KEY_COMB_RURAL_URBAN_BENEFICIARY = '-RURALURBANPROPERTYBENEFICIARY-'

DEFAULT_KEY__COMB_OWNS_CAR = '-OWNSACAR-'
DEFAULT_KEY_OWNS_CAR_HOW_MANY = '-OWNSCARHOWMANY-'
DEFAULT_KEY__COMB_HAS_MOTORCICLE = '-HASMOTORCICLE-'
DEFAULT_KEY_HAS_MOTORCICLE_HOW_MANY = '-HASMOTORCICLEHOWMANY-'
DEFAULT_KEY_COMB__HAVE_FRIDGE = '-HAVEFRIDGE-'
DEFAULT_KEY_HAVE_FRIDGE_HOW_MANY = '-HAVEFRIDGEHOWMANY-'
DEFAULT_KEY_COMB__HAVE_TELEVI = '-HAVETELEVISION-'
DEFAULT_KEY_HAVE_TELEVI_HOW_MANY = '-HAVETELEVISIONHOWMANY-'
DEFAULT_KEY_COMB__HAVE_COMPUTER = '-HAVECOMPUTER-'
DEFAULT_KEY_HAVE_COMPUTER_HOW_MANY = '-HAVECOMPUTERHOWMANY-'
DEFAULT_KEY_COMB__HAVE_INTERNET = '-HAVEINTERNET-'
DEFAULT_KEY_COMB__HAVE_ACESS_ELECTRI = '-HASACCESSELECTRICITY-'
DEFAULT_KEY_COMB__HAVE_DRAINAG_WATER = '-ACESSODRAINAGEWATER-'

#--------------------------KEY FRAME PROPERTY CONDITIONS-----------------
DEFAULT_KEY_COMB_ONLY_OWNER = '-ONLYOWNER-'
DEFAULT_KEY_TXT_ANOTHER_OWNER = '-ANOTHEROWNER-'
DEFAULT_KEY_TXT_STILL_TIME = '-TIMEYOUOWNTHEPROPERTY-'
DEFAULT_KEY_COMB_ANOTHER_PROPERTY = '-HASANOTHERPROPERTY-'
DEFAULT_KEY_ANOTHER_PROPERTY_HOW_MANY = '-ANOTHERPROPERTYHOWMANY-'
DEFAULT_KEY_TXT_ANOTHER_PROPERTY_WHERE = '-ANOTHERPROPERTYWHERE-'
DEFAULT_KEY_COMB_REAL_ESTATE_CONSTRUC = '-REALESTATECONSTRUCTION-'
DEFAULT_KEY_PROPERTY_USED_FOR = '-PROPERTYUSEDFOR-'

DEFAULT_KEY_TXT_FRONT = '-INPUTFRONT-'
DEFAULT_KEY_TXT_RIGHT = '-INPUTRIGHT-'
DEFAULT_KEY_TXT_LEFT = '-INPUTLEFT-'
DEFAULT_KEY_TXT_FUNDS = '-INPUTFUNDS-'

DEFAULT_KEY_COMB_TYPE = '-TYPEOFPROPERTY-'
DEFAULT_KEY_COMB_IS_WALLED = '-ISWALLED-'
DEFAULT_KEY_COMB_BATCH_POSITION = '-BATCHPOSITION-'
DEFAULT_KEY_COMB_STATE_BUILDINGS = '-STATEOFBUILDINGS-'
DEFAULT_KEY_COMB_BUILDING_TYPE = '-BUILDINGTYPE-'
DEFAULT_KEY_COMB_IS_BEDRIDDEN = '-ISBEDRIDDEN-'
DEFAULT_KEY_NUMB_FLOORS = '-NUMBEROFFLOORS-'
DEFAULT_KEY_ROOMS = '-ROOMS-'
DEFAULT_KEY_BATHROOMS = '-BATHROOMS-'

#-------------------------key registration residents--------------------
DEFAULT_KEY_TABLE_RESIDENTS = '-RESIDENTS-'

DEFAULT_KEY_INPUT_ID_REGIST_RESID = '-ID_CADASTRO_MORADORES-'
DEFAULT_KEY_TXT_NOME_REGIST_RESID = '-NOME_CADASTRO_MORADORES-'
DEFAULT_KEY_SPIN_KINSHIP_REGIST_RESID = '-PARENTESCO_CADASTRO_MORADORES-'
DEFAULT_KEY_COMB_SEX_REGIST_RESID = '-SEXO_CADASTRO_MORADORES-'
DEFAULT_KEY_COMB_MARITAL_STATUS_REGIST_RESID = '-ESTADO_CIVIL_CADASTRO_MORADORES-'
DEFAULT_KEY_TXT_OCCUPATION_REGIST_RESID = '-OCUPAÇÃO_CADASTRO_MORADORES-'
DEFAULT_KEY_TXT_INCOME_REGIST_RESID = '-RENDA_CADASTRO_MORADORES-'

DEFAULT_KEY_TXT_FAMILY_INCOME_REGIST_RESID = '-RENDA_FAMILIAR_TOTAL_CADASTRO_MORADORES-'


#-----------------------------BTNS--------------------------


#-------------------------BTNS TYPE OFF FRAMEWORKS REURBS-------------------
DEFAULT_KEY_EDIT_TYPE_FRAMEWORK = '<<-BTN_EDITAR_TIPO_ENQUADRAMENTO_REURB->>'
DEFAULT_KEY_SAVE_TYPE_FRAMEWORK = '<<-BTN_SAVAR_TIPO_ENQUADRAMENTO_REURB->>'