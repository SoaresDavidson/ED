import random
from time import sleep
import os
class Cartas:
    def __init__(self, val, nap):
        self.naipe = nap
        self.valor = val

    def __repr__(self):
        if self.valor in ['A', 'K', 'J', 'Q']:
            if self.valor == 'A':
                return f'Ás de {self.naipe}'  
            if self.valor == 'J':
                return f'Valete de {self.naipe}'  
            if self.valor == 'Q':
                return f'Rainha de {self.naipe}' 
            if self.valor == 'K':
                return f'Rei de {self.naipe}'       
        return f'{self.valor} de {self.naipe}'    

class Baralho:
    np = ['Ouros', 'Espadas', 'Copas', 'Paus']
    v = ['A', 'J', 'K', 'Q', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    valores = {'A': 1, 'J': 11, 'K': 13, 'Q': 12}

    def __init__(self):
        self.cartas = [Cartas(valor, naipe) for naipe in Baralho.np for valor in Baralho.v]
        self.embaralhar()

    def embaralhar(self):
        random.shuffle(self.cartas)  

    def retirar(self):
        if len(self.cartas) > 0:
            return self.cartas.pop()
        else:
            return None    

    def contador(self, jogador):
        val = 0
        for cartas in jogador:
            if cartas.valor in self.valores:
                val += self.valores[cartas.valor]
            else:
                val += int(cartas.valor)    
        return val 

def cor(texto, cor_code):
    return f'\033[{cor_code}m{texto}\033[0m'

def imprimir_placar(jogador_1, jogador_2):
    print(cor("\n----- Placar Atual -----", "36;1"))
    print(cor(f'Jogador 1: {pontuacao_j1} pontos - Cartas: {jogador_1}', "32"))
    print(cor(f'Jogador 2: {pontuacao_j2} pontos - Cartas: {jogador_2}', "32"))
    print(cor("-------------------------", "36"))

if __name__ == '__main__':
    game = True
     
    while game:

        baralho = Baralho()
        jogador_1 = []
        jogador_2 = []
        vez_jogador1=vez_jogador2=True
        pontuacao_j1=pontuacao_j2=0
        print(cor('---------- Bem-vindo ao Jogo 21! ----------', '34;1'))
        
        while True:
      
            if vez_jogador1:
                print(cor('-=-=-= Vez do Jogador 1 -=-=-', '36;1'))
                if baralho.cartas:
                    while True:
                        ans = str(input('Deseja pegar uma carta na pilha? (sim/não) ')).strip().upper()
                        if ans in 'SIMNÃONNSSNAO':
                            break 
                        else:
                            print(cor('Resposta Inválida', '31'))
                    if ans in 'SIMSS':
                        carta_jogador1 = baralho.retirar()
                        jogador_1.append(carta_jogador1)
                        pontuacao_j1 = baralho.contador(jogador_1)
                        print(cor(f'Você retirou a carta {carta_jogador1}.', '32'))
                        sleep(0.5)
                        imprimir_placar(jogador_1, jogador_2)
                        if pontuacao_j1 >= 21:
                            break
                    elif ans in 'NÃONAONN':
                        print(cor('Você optou por não retirar mais cartas.', '35'))
                        vez_jogador1=False
                    if vez_jogador2:     
                        sleep(1.5)
                        print(cor('Próximo jogador...', '34'))
                        sleep(0.5)
                else:
                    print(cor('Acabaram as cartas na pilha do baralho!', '31'))
                    break      


            if vez_jogador2:
                print(cor('-=-=-= Vez do Jogador 2 -=-=-', '36;1'))
                if baralho.cartas: 
                    while True:
                        ans2 = str(input('Deseja pegar uma carta na pilha? (sim/não) ')).strip().upper()
                        if ans2 in 'SIMNÃOSSNNNAO':
                            break
                        else:
                            print(cor('Resposta Inválida', '31'))
                    if ans2 in 'SIMSS':
                        carta_jogador2 = baralho.retirar()
                        jogador_2.append(carta_jogador2) 
                        pontuacao_j2 = baralho.contador(jogador_2)
                        print(cor(f'Você retirou a carta {carta_jogador2}.', '32'))
                        sleep(0.5)
                        imprimir_placar(jogador_1, jogador_2)
                        if pontuacao_j2 >= 21:
                            break
                    elif ans2 in 'NAONÃONN':
                        print(cor('Você optou por não retirar mais cartas.', '35'))
                        vez_jogador2=False
                else:
                    print(cor('Acabaram as cartas na pilha do baralho!', '31'))
                    break 
                if vez_jogador1:
                    sleep(1.5)
                    print(cor('Próximo jogador...', '34'))
                    sleep(0.5)    
            if vez_jogador1==vez_jogador2==False:
                break         

 
        print(cor('--- Fim do Jogo! ---', '35;1'))
        if pontuacao_j1 > pontuacao_j2:
            if pontuacao_j1 > 21:
                print(cor('O Jogador 2 venceu!!!', '31') + cor(f' O Jogador 1 ultrapassou 21 pontos com {pontuacao_j1} pontos!', '37'))
            elif pontuacao_j1 == 21:
                print(cor('Incrível!', '32') + ' O Jogador 1 venceu ao atingir exatamente 21 pontos!!!')
            else:
                print(cor('Parabéns Jogador 1!', '32') + f' Você venceu com {pontuacao_j1} pontos! Cartas: {jogador_1}. Jogador 2 ficou com {pontuacao_j2} pontos.')
        elif pontuacao_j1 == pontuacao_j2:
            print(cor('EMPATE!', '33') + f' Ambos os jogadores conseguiram {pontuacao_j1} pontos!')
        else:
            if pontuacao_j2 > 21:
                print(cor('O Jogador 1 venceu!!!', '31') + cor(f' O Jogador 2 ultrapassou 21 pontos com {pontuacao_j2} pontos!', '37'))
            elif pontuacao_j2 == 21:
                print(cor('Fantástico!', '32') + ' O Jogador 2 venceu ao atingir exatamente 21 pontos!!!')
            else:
                print(cor('Parabéns Jogador 2!', '32') + f' Você venceu com {pontuacao_j2} pontos! Cartas: {jogador_2}. Jogador 1 ficou com {pontuacao_j1} pontos.')
        while True:        
            reiniciar = str(input('Deseja jogar novamente? [S/N]')).strip().upper()
            if reiniciar in 'SN':
                break
            else:
                print('Digite uma opção válida')
        if reiniciar=='N':
            game = False
        os.system('cls')
        