# -*- coding: utf-8: -*-

#a = "Lucas"
#b = "Mariano"

#concatenar = a + " " + b + "\n" # para dar espaço entre as strings
#print(concatenar)


#tamanho = len(concatenar) # para calcular os caracteres das strings
#print(tamanho)

#print(a[0])
#print(a[1])
#print(a[2])
#print(a[3])
#print(a[4]) #para selecionar o caracteres na string A

#print(concatenar[6:13])
# o /n da uma quebra de linha

#print(concatenar)
#print(concatenar.lower())
#print(concatenar.upper())

#a função strip remove o espaço entre as linhas

#print(concatenar.strip())

minha_string = "O rato roeu a roupa do rei de Roma"

#minha_lista = minha_string.split(" ")
#print(minha_lista)

#busca = minha_string.find("rei") #Find busca em qual ordem a letra ou palavra está
#print(busca)

busca = minha_string.find("rei") #find dentro da string busca: busca todas as palavras a partir do rei

print(minha_string[busca:]) 

minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)
