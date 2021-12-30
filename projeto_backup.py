from time import sleep
from tratamento import tratamento_nome_pasta
from diretorios import pasta_para_backup, local_do_backup
import shutil
import datetime

dia_user = input("Coloque o dia da semana do backup: ").lower()
hora_user = input("Coloque a hora da semana nesse formato [12:00]: ")

traducao = {"domingo":"Sunday","segunda":"Monday","terça":"Tuesday","quarta":"Wednesday","quinta":"Thursday","sexta":"Friday","sabado":"Saturday"}

while True:
    diabackup = datetime.now().strftime("%A")
    horabackup = datetime.now().strftime("%H:%M")

    if traducao[dia_user] == diabackup and hora_user == horabackup:
        proximo_numero = str(tratamento_nome_pasta(local_do_backup))
        try:
            #Ato de copiar e colar em um novo local
            shutil.copytree(pasta_para_backup, local_do_backup+'/backup-' + proximo_numero)       
            print("\nBackup realizado com sucesso\n")
            sleep(86398)
        #Caso existe ja uma pasta
        except FileExistsError as e:
            print("Erro, ero, errrouu")
            sleep(86398)
