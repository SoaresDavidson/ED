import HashTable,time
tabela = HashTable.tabelaHash(227)

with open("TabelaDeSimbolos/leipzig100k.txt", "r", encoding="utf-8") as liepzig:
    arr = liepzig.readlines()
    t1 = time.time()
    for line in arr:
        for word in line.split():
            tabela.put(word, 0)
    t2 = time.time() - t1
    print(t2)

print(tabela.search("You").value)
#for i in tabela.table:
 #   if i == None:continue
  #  print(i.key)