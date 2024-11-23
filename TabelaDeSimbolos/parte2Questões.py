import HashTable,menu
def question1():
    tabela = HashTable.tabelaHash(26,hashing=False)
    menu.read_from_file("ED/TabelaDeSimbolos/alunosED_2024.txt", tabela)
    print(tabela.countByCapacity())
    x = [chr(ord("A")+_) for _ in range(26)]
    menu.construir_grafico(x,tabela.countByCapacity(),"Colisões","Ordem","Questão 1",directory="ED")

question1()