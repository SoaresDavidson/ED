def realiza_operacao(arquivo:str, algoritimo) -> float:
    arr = []
    with open(arquivo, "r", encoding= "utf-8") as arq:
        arr = arq.readlines()
        tempo = algoritimo(arr)
        return tempo
    
def checa_se_ta_ordenando(arquivo:str, algoritmo):
    arr = []
    with open(arquivo, "r", encoding= "utf-8") as arq:
        arr = arq.readlines()
        tempo = algoritmo(arr)
        print(f"{algoritmo.__name__} levou {tempo} segundos")

    with open("checa.txt", "w", encoding="utf-8") as arq:
        arq.writelines(arr)

def calcula_media(arquivo:str,algoritimo, quant:int = 5):
    sum = 0
    for i in range(quant):
        sum += realiza_operacao(arquivo, algoritimo)
    return sum/quant


if __name__ == "__main__":
    print("cu")
    pass