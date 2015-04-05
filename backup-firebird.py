#!/usr/bin/python
#-=- encoding: latin-1 -=-
import os
import shutil
import commands
import datetime
import smtplib
from email.MIMEText import MIMEText

BD='/opt/HBSISTEMAS/'
PATH = '/BKP-FIREBIRD'
DOIS_PONTOS = "-"
BARRA = '/'
NOW  = datetime.datetime.now()
HOJE = NOW.strftime('%d-%m')
HORARIO_ATUAL = str(NOW.hour) + DOIS_PONTOS + str(NOW.minute)
DIAS_ATRAS = 1

# criando o diretório
now = datetime.datetime.now()

#verificando se existe o diretório raiz
if not os.path.exists(PATH):
    os.mkdir(PATH)

#verificando se existe o diretório do dia
if not os.path.exists(PATH + BARRA + HOJE):
    os.mkdir(PATH + BARRA + HOJE)

#criando o diretório de hora
DIR_HORAIO = (PATH + BARRA + HOJE + BARRA + HORARIO_ATUAL)
os.mkdir(DIR_HORAIO)

#gerando os bkps
for i in os.listdir(BD):
    os.system('/usr/bin/gbak -B -G -V %s%s %s/%s.bkp' %(BD,i,DIR_HORAIO,i))

#removendo bkps antigos, conforme a variavel DIAS_ATRAS
AGORA = datetime.date.today()
DATAANTIGA = (AGORA - datetime.timedelta(DIAS_ATRAS)).strftime('%d-%m')
if os.path.exists(PATH + BARRA + DATAANTIGA):
    shutil.rmtree(PATH + BARRA + DATAANTIGA)
