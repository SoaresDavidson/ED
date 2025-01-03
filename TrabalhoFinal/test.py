import menu,collections
import matplotlib.pyplot as plt
palavras = ["Lisbon", "NASA",
"Kyunghee", "Konkuk", "Sogang", "momentarily", "rubella", "vaccinations", "government",
"Authorities"]
tempos_lista_dict = [0.64,0.29,0.17,0.12,0.17,0.10,0.21,0.10,0.02,0.10]
menu.costruir_grafico(palavras, tempos_lista_dict,Xlabel='Tabelas',Ylabel='Tempos (ms)',title='Tempos de Busca hash table', save_path= "searchTimesListDict.png",directory= "TrabalhoFinal/tempos") 