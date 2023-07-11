minha_lista = ["abacaxi", "melancia", "abacate"]

print(minha_lista)
minha_lista_2 = [1,2,3,4,5]

print(minha_lista_2)

minha_lista.append("limao") #append adiciona novo iten na lista
print(minha_lista)

if 3 in minha_lista_2: # if 3 in ... mostra se o 3 está na lista 2
    print("3 esta na lista")

    del minha_lista[2: ] #del para apagar iten da lista
    print(minha_lista)

    # Metodo .sort() ele ordena a lista automaticamente
    # se adicionar .sort(reverse=true) ele ordena decrescente