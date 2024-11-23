import matplotlib.pyplot as plt
import numpy as np
import menu,HashTable

def question1():
    M = 26
    tabela = HashTable.tabelaHash(M,hashing=False)

    with open("TabelaDeSimbolos\\alunosED_2024.txt", "r", encoding="utf-8") as txt:
        for linha in txt:
            tabela.put(linha)
        #print(tabela)

    lista_hashes = [chr(ord("A")+i) for i in range(M)]
    lista_colisoes = tabela.countByCapacity()
    for i in range(len(lista_colisoes)): 
        lista_colisoes[i] -= 1 if lista_colisoes[i] > 0 else 0
        
    print(lista_colisoes)
    x = np.array(lista_hashes)
    y = np.array(lista_colisoes)
    menu.costruir_grafico(x, y, "Hashes", "Colisões", f"Histograma com M = {M} e primeira letra como chave",save_path="questão-1")
    #plt.bar(x, y)
    #plt.xlabel("Hash")
    #plt.ylabel("Colisões")
    #plt.show()

def question2():
    M = 26
    tabela = HashTable.tabelaHash(M)
    

    with open("TabelaDeSimbolos\\alunosED_2024.txt", "r", encoding="utf-8") as txt:
        for linha in txt:
            tabela.put(linha)
        #print(tabela)
    
    lista_hashes = [chr(ord("A")+i) for i in range(M)]
    lista_colisoes = tabela.countByCapacity()
    for i in range(len(lista_colisoes)): 
        lista_colisoes[i] -= 1 if lista_colisoes[i] > 0 else 0

    x = np.array(lista_hashes)
    y = np.array(lista_colisoes)
    menu.costruir_grafico(x, y, "Hashes", "Colisões", f"Histograma com M = {M} e com Hash Padrão",save_path="questão-2")
    #plt.bar(x, y)
    #plt.xlabel("Hash")
    #plt.ylabel("Colisões")
    #plt.show()

def question3():
    for M in [19,31,47]:
        tabela = HashTable.tabelaHash(M)

        with open("TabelaDeSimbolos\\alunosED_2024.txt", "r", encoding="utf-8") as txt:
            for linha in txt:
                tabela.put(linha)
            #print(tabela)

        lista_hashes = [i for i in range(M)]
        lista_colisoes = tabela.countByCapacity()
        for i in range(len(lista_colisoes)): 
            lista_colisoes[i] -= 1 if lista_colisoes[i] > 0 else 0

        x = np.array(lista_hashes)
        y = np.array(lista_colisoes)
        menu.costruir_grafico(x, y, "Hashes", "Colisões", f"Histograma com M = {M} e com Hash Padrão",save_path=f"questão-3-{M}")
        #plt.bar(x, y)
        #plt.xlabel("Hash")
        #plt.ylabel("Colisões")
        #plt.show()

def question4():

    for M in [16,32,64]:
        tabela = HashTable.tabelaHash(M)

        with open("TabelaDeSimbolos\\alunosED_2024.txt", "r", encoding="utf-8") as txt:
            for linha in txt:
                tabela.put(linha)
            #print(tabela)

        lista_hashes = [i for i in range(M)]
        lista_colisoes = tabela.countByCapacity()
        for i in range(len(lista_colisoes)): 
            lista_colisoes[i] -= 1 if lista_colisoes[i] > 0 else 0

        x = np.array(lista_hashes)
        y = np.array(lista_colisoes)
        menu.costruir_grafico(x, y, "Hashes", "Colisões", f"Histograma com M = {M} e com Hash Padrão",save_path=f"questão-4-{M}")
        #plt.bar(x, y)
        #plt.xlabel("Hash")
        #plt.ylabel("Colisões")
        #plt.show()

question1()
question2()
question3()
question4()