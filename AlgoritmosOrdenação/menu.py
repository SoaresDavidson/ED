import time
def realiza_operacao(arquivo:str, algoritmo) -> time:
    arr = []
    with open(arquivo, "r", encoding= "utf-8") as arq:
        arr = arq.readlines()
        tempo:time = algoritmo(arr)
        return tempo
    
def checa_se_ta_ordenando(arquivo:str, algoritmo):
    arr = []
    with open(arquivo, "r", encoding= "utf-8") as arq:
        arr = arq.readlines()
        tempo = algoritmo(arr)
        print(f"{algoritmo.__name__} levou {tempo} segundos")

    with open("checa.txt", "w", encoding= "utf-8") as arq:
        for line in arq.lines:
            arq.write(f"{line}\n")


if __name__ == "__main__":
    print("cu")
    pass