import matplotlib.pyplot as plt
import numpy as np
import menu,HashTable

def question1():
    i = 26
    tabela = HashTable.tabelaHash(i,hashing=False)

    with open("TabelaDeSimbolos\\alunosED_2024.txt", "r", encoding="utf-8") as txt:
        for linha in txt:
            tabela.put(linha)
        #print(tabela)

    lista_hashes = [i for i in range(i)]
    lista_colisoes = tabela.countByCapacity()

    x = np.array(lista_hashes)
    y = np.array(lista_colisoes)
    menu.costruir_grafico(x, y, "Hashes", "Colisões", f"Histograma com M = {i} e primeira letra como chave",save_path="questão-1")
    #plt.bar(x, y)
    #plt.xlabel("Hash")
    #plt.ylabel("Colisões")
    #plt.show()

def question2():
    i = 26
    tabela = HashTable.tabelaHash(i)

    with open("TabelaDeSimbolos\\alunosED_2024.txt", "r", encoding="utf-8") as txt:
        for linha in txt:
            tabela.put(linha)
        #print(tabela)

    lista_hashes = [i for i in range(i)]
    lista_colisoes = tabela.countByCapacity()

    x = np.array(lista_hashes)
    y = np.array(lista_colisoes)
    menu.costruir_grafico(x, y, "Hashes", "Colisões", f"Histograma com M = {i} e com Hash Padrão",save_path="questão-2")
    #plt.bar(x, y)
    #plt.xlabel("Hash")
    #plt.ylabel("Colisões")
    #plt.show()

def question3():
    for i in [19,31,47]:
        tabela = HashTable.tabelaHash(i)

        with open("TabelaDeSimbolos\\alunosED_2024.txt", "r", encoding="utf-8") as txt:
            for linha in txt:
                tabela.put(linha)
            #print(tabela)

        lista_hashes = [i for i in range(i)]
        lista_colisoes = tabela.countByCapacity()

        x = np.array(lista_hashes)
        y = np.array(lista_colisoes)
        menu.costruir_grafico(x, y, "Hashes", "Colisões", f"Histograma com M = {i} e com Hash Padrão",save_path=f"questão-3-{i}")
        #plt.bar(x, y)
        #plt.xlabel("Hash")
        #plt.ylabel("Colisões")
        #plt.show()

def question4():

    for i in [16,32,64]:
        tabela = HashTable.tabelaHash(i)

        with open("TabelaDeSimbolos\\alunosED_2024.txt", "r", encoding="utf-8") as txt:
            for linha in txt:
                tabela.put(linha)
            #print(tabela)

        lista_hashes = [i for i in range(i)]
        lista_colisoes = tabela.countByCapacity()

        x = np.array(lista_hashes)
        y = np.array(lista_colisoes)
        menu.costruir_grafico(x, y, "Hashes", "Colisões", f"Histograma com M = {i} e com Hash Padrão",save_path=f"questão-4-{i}")
        #plt.bar(x, y)
        #plt.xlabel("Hash")
        #plt.ylabel("Colisões")
        #plt.show()

question1()
question2()
question3()
question4()