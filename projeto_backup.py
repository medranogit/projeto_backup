#! /usr/bin/python
from datetime import datetime, timedelta, date
import shutil
import os, os.path, subprocess

dia_user = input("Coloque o dia da semana do backup: ").lower()
hora_user = input("Coloque a hora da semana nesse formato [12:00]: ")

traducao = {"sabado":"Saturday"}

diabackup = datetime.now().strftime("%A")

horabackup = datetime.now().strftime("%H:%M")

if traducao[dia_user] == diabackup and hora_user == horabackup:

    pastabackup = r'C:\Users\vinim\Documents\backup'
    localbackup = r'C:\Users\vinim\Documents\pasta_do_backup'



    print("Backup Completo")

    print("Backup realizado com sucesso")
else:
    print("Não realizar backup")








