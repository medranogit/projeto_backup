from datetime import datetime
import shutil


dia_user = input("Coloque o dia da semana do backup: ").lower()
hora_user = input("Coloque a hora da semana nesse formato [12:00]: ")

traducao = {"domingo":"Sunday","segunda":"Monday","terça":"Tuesday","quarta":"Wednesday","quinta":"Thursday","sexta":"Friday","sabado":"Saturday"}

diabackup = datetime.now().strftime("%A")
horabackup = datetime.now().strftime("%H:%M")

if traducao[dia_user] == diabackup and hora_user == horabackup:
    try:
        shutil.copytree(r'C:\Users\vinim\Documents\backup', r'C:\Users\vinim\Documents\pasta_backup')       
        print("\nBackup realizado com sucesso\n")
    except FileExistsError as e:
        shutil.rmtree(r'C:\Users\vinim\Documents\pasta_backup')
        shutil.copytree(r'C:\Users\vinim\Documents\backup', r'C:\Users\vinim\Documents\pasta_backup')  
        print("\nBackup realizado com sucesso\n")
else:
    print("Não realizar backup")