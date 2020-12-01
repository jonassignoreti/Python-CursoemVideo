
fileName = r'REL.doc'
'''if not os.path.isfile(fileName):
    arquivo = open('REL.doc', 'x+') #Cria o arquivo'''

arquivo = open('REL.doc', 'r+') #Lê o arquivo

print(arquivo.read())
arquivo.close()
