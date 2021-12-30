import os
def tratamento_nome_pasta(caminho):
    #esse try e exept é para caso nao exista nenhum arquivo na pasta e de um erro retorne 1 para iniciar a contagem
    try:
        dirlist = [ item for item in os.listdir(caminho) if os.path.isdir(os.path.join(caminho, item)) ]


        #TRATAMENTO DO NOME DO ARQUIVO
        #Para pegar o ultimo item da lista que no caso será o maior pelo autoorganização do windows e convertendo para string tbm
        nome_ultimo = str(dirlist[-1])
        #print(nome_ultimo)
        #-1 para pegar a ultima letra que no caso é o numero em string > alocando em uma variavel e convertendo para int

        numero_string = nome_ultimo.split('-')[1]
        #print(numero_string)
        
        #adicionando +1 no numero convertido para int
        numero_convertido = int(numero_string) + 1
        #retornando o valor pronto
        return(numero_convertido)
    except:
        return 1
    
