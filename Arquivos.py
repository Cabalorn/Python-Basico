# -*- coding: utf-8: -*-

#modo R - Somente leitura
#modo W - Escrita ( Caso o arquivo já exista, ele será apagado e um novo arquivo vazio sera criado)
#Modo a - Leitura e escrita
#Modo r+ Leitura e escrtia
#Modo w+ Escrita (tbm apaga o conteudo anterior do arquivo)
#a+ Leitura e escrita (abre o arquivo pra att)

W = open("arquivo2.txt", "w")

W.write("Esse é o meu arquivo")

W.close()