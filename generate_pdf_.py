#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:07:25 2021

@author: andre
"""
from keys_to_registration import *

from reportlab.pdfgen import canvas

def GeneratePDF(lista):
    try:
        nome_pdf = 'arquivo'
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        for nome,idade in lista.items():
            x -= 20
            pdf.drawString(40,x, '{} : {}'.format(nome,idade))
            
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(170,750, 'Lista das tags para colocar nos contratos')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245,724, 'Cadastro Socioeconômico')
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))

lista = {
            
        '1-': 'Dados do Cônjuge',
        'Nome': DEFAULT_KEY_NAME_SPOUSE,
        'Sexo': DEFAULT_KEY_SEX_SPOUSE,
        'Data de Nascimento': DEFAULT_KEY_BIRTHDATE_SPOUSE,
        'Idade': DEFAULT_KEY_AGE_SPOUSE,
        'Naturalidade': DEFAULT_KEY_NATURALNESS_SPOUSE,
        'Telefone':DEFAULT_KEY_TEL_SPOUSE,
        'Celular': DEFAULT_KEY_CEL_SPOUSE,
        'RG':DEFAULT_KEY_RG_SPOUSE,
        'Orgão Emissor':DEFAULT_KEY_ISSUING_BODY_SPOUSE,
        'CPF':DEFAULT_KEY_CPF_SPOUSE,
        'CNH':DEFAULT_KEY_CNH_SPOUSE,
        'Titulo de eleitor':DEFAULT_KEY_VOTER_TITLE_SPOUSE,
        'Escolaridade':DEFAULT_KEY_SCHOOLING_SPOUSE
        }
        
"""
        #------------------------------KEYS TO personal_data_tab-------------------
        
        DEFAULT_KEY_NOME_PERSONAL_DATA,
        DEFAULT_KEY_SEX_PERSONAL_DATA,
        DEFAULT_KEY_BIRTHDATE_PERSONAL_DATA,
        DEFAULT_KEY_AGE_PERSONAL_DATA,
        DEFAULT_KEY_NATURALNESS_PERSONAL_DATA,
        DEFAULT_KEY_UF_PERSONAL_DATA,
        DEFAULT_KEY_TEL_PERSONAL_DATA,
        DEFAULT_KEY_CEL_PERSONAL_DATA,
        DEFAULT_KEY_EMAIL_PERSONAL_DATA,
        DEFAULT_KEY_ADDRESS_PERSONAL_DATA,
        DEFAULT_KEY_DISTRICT_PERSONAL_DATA,
        DEFAULT_KEY_HOUSE_NUMBER_PERSONAL_DATA,
        DEFAULT_KEY_RG_PERSONAL_DATA,
        DEFAULT_KEY_ISSUING_BODY_PERSONAL_DATA,
        DEFAULT_KEY_CPF_PERSONAL_DATA,
        DEFAULT_KEY_CNH_PERSONAL_DATA,
        DEFAULT_KEY_VOTER_TITLE_PERSONAL_DATA,
        DEFAULT_KEY_CONSIDER_PERSONAL_DATA,
        DEFAULT_KEY_MARITAL_STATUS_PERSONAL_DATA,
        DEFAULT_KEY_SCHOOLING_PERSONAL_DATA,
        
        #----------------------------keys to TabGroup------------------------
        
        DEFAULT_KEY_PERSONAL_DATA_TABGROUP,
        DEFAULT_KEY_OTHER_INFOR_TABGROUP,
        DEFAULT_KEY_RESIDENTS_REGIST_TABGROUP,
        DEFAULT_KEY_TABGROUP,
        
        #-------------------------KEY to tab other_information----------------------
        DEFAULT_KEY_COMB_WORKS,
        DEFAULT_KEY_INP_WHERE,
        DEFAULT_KEY_TXT_PROFESSION,
        DEFAULT_KEY_COMB_RETIREE,
        DEFAULT_KEY_BENEF_CAMB_SOCI_PROG,
        DEFAULT_KEY_INCOME_COMB_INCOME,
        DEFAULT_KEY_COMB_HAVE_CHILDREM,
        DEFAULT_KEY_HOW_MANY_CHILDREM,
        DEFAULT_KEY_LIVES_DISABLED_OR_ELDERLY,
        DEFAULT_KEY_DISABLED_ELDERLY_HOW_MANY,
        DEFAULT_KEY_COMB_RURAL_URBAN_BENEFICIARY,
        
        DEFAULT_KEY__COMB_OWNS_CAR,
        DEFAULT_KEY_OWNS_CAR_HOW_MANY,
        DEFAULT_KEY__COMB_HAS_MOTORCICLE,
        DEFAULT_KEY_HAS_MOTORCICLE_HOW_MANY,
        DEFAULT_KEY_COMB__HAVE_FRIDGE,
        DEFAULT_KEY_HAVE_FRIDGE_HOW_MANY,
        DEFAULT_KEY_COMB__HAVE_TELEVI,
        DEFAULT_KEY_HAVE_TELEVI_HOW_MANY,
        DEFAULT_KEY_COMB__HAVE_COMPUTER,
        DEFAULT_KEY_HAVE_COMPUTER_HOW_MANY,
        DEFAULT_KEY_COMB__HAVE_INTERNET,
        DEFAULT_KEY_COMB__HAVE_ACESS_ELECTRI,
        DEFAULT_KEY_COMB__HAVE_DRAINAG_WATER,
        
        #--------------------------KEY FRAME PROPERTY CONDITIONS-----------------
        DEFAULT_KEY_COMB_ONLY_OWNER ,
        DEFAULT_KEY_TXT_ANOTHER_OWNER,
        DEFAULT_KEY_TXT_STILL_TIME,
        DEFAULT_KEY_COMB_ANOTHER_PROPERTY,
        DEFAULT_KEY_ANOTHER_PROPERTY_HOW_MANY,
        DEFAULT_KEY_TXT_ANOTHER_PROPERTY_WHERE,
        DEFAULT_KEY_COMB_REAL_ESTATE_CONSTRUC,
        DEFAULT_KEY_PROPERTY_USED_FOR,
        
        DEFAULT_KEY_TXT_FRONT,
        DEFAULT_KEY_TXT_RIGHT,
        DEFAULT_KEY_TXT_LEFT,
        DEFAULT_KEY_TXT_FUNDS,
        
        DEFAULT_KEY_COMB_TYPE,
        DEFAULT_KEY_COMB_IS_WALLED,
        DEFAULT_KEY_COMB_BATCH_POSITION,
        DEFAULT_KEY_COMB_STATE_BUILDINGS,
        DEFAULT_KEY_COMB_BUILDING_TYPE,
        DEFAULT_KEY_COMB_IS_BEDRIDDEN,
        DEFAULT_KEY_NUMB_FLOORS,
        DEFAULT_KEY_ROOMS,
        DEFAULT_KEY_BATHROOMS,
        
        #-------------------------key registration residents--------------------
        DEFAULT_KEY_TABLE_RESIDENTS,
        
        DEFAULT_KEY_INPUT_ID_REGIST_RESID,
        DEFAULT_KEY_TXT_NOME_REGIST_RESID,
        DEFAULT_KEY_SPIN_KINSHIP_REGIST_RESID,
        DEFAULT_KEY_COMB_SEX_REGIST_RESID,
        DEFAULT_KEY_COMB_MARITAL_STATUS_REGIST_RESID,
        DEFAULT_KEY_TXT_OCCUPATION_REGIST_RESID,
        DEFAULT_KEY_TXT_INCOME_REGIST_RESID,
        
        DEFAULT_KEY_TXT_FAMILY_INCOME_REGIST_RESID

    }"""

GeneratePDF(lista)