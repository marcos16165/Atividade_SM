"""
	* Projeto: Reconhecedor de símbolos 
	* Autor: Marcos Monteiro 
	* Dados: 06/10/2020
	* Versao: 1.0
	* Data da ultima modificao: 06/10/2020
	* Descricao: Programa que lê o conteúdo de um arquivo e apresente na tela a
          tabela de símbolos presentes no arquivo.
"""

#------------------------------------
#Abrir arquivo direto do terminal

import sys

if len(sys.argv)==3:
    if sys.argv[1]=="-f":
        arquivo=sys.argv[2]
    else:
        sys.exit(1)
else:
    sys.exit(1)

Abrir=open(arquivo)
#------------------------------------

aux=[]
texto=[]

caracter=''
frequencia=0

for i in Abrir:
    aux.append(i)

for i in range(1):
    for j in range(len(aux[i])):
        texto.append(aux[i][j])

aux.clear()

total = 0

#------------------------------------------------------------------------
#Printando saída semelhante ao exemplo
print(" Símbolo | Freq. Abs. | Freq. Rel | Cod. ASCII ")
#------------------------------------------------------------------------

for i in range(len(texto)):
    if texto[i] == None:
        continue
    else:
        caracter=texto[i]
        for j in range(len(texto)):
            if caracter==texto[j]:
                frequencia =  frequencia + 1
                #Conversão de caracter para binário
                B = ' '.join(format(ord(x),'b') for x in texto[j])
                while len(B)<8:
                    B ='0' + B
                total = total + 1
                texto[j] = None
    med = total // len(texto)

#------------------------------------------------------------------------
#Printando saída semelhante ao exemplo
    if caracter==' ':
        print("spc         ",frequencia,"       ","   {}/{}      ".format(frequencia,len(texto)),B)
    else:
        print(caracter,"          ",frequencia,"       ","   {}/{}      ".format(frequencia,len(texto)),B)
    frequencia=0
print("--------------------------------------------------------------------------\n")
print("Total       {}             {}".format(total,med))
#------------------------------------------------------------------------






