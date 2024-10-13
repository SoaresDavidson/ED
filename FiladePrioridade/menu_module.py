import itertools,os
class Menu:
    def __init__(self, mode_array = False):
        self.mode_array = mode_array

    def color(self, txt, cor):
        """Aplica cores ao texto para a interface do menu."""
        print(f'\033[{cor}m{txt}\033[m')

    def exibir_menu(self):
        """Exibe o menu principal."""
        self.color('=' * 30, '034')
        self.color(f'{"ATENDIMENTO":-^30}', '037;1')
        self.color('=' * 30, '034')
        self.color(f'''1) Inserir pessoa na fila.
2) Atender pessoa da fila.
3) Listar pessoas da fila.
4) Situação atual da fila.
5) Sair''', '034;1')

    def escolher_opcao(self):
        return input('Escolha uma opção: ').strip()

    def inserir_pessoa(self, fila):
        nome = input('Digite o nome da pessoa: ').strip()
        while True:
            idade = input('Digite a idade da pessoa: ').strip()
            if idade.isnumeric():
                idade = int(idade)
                break
            self.color('Insira uma idade válida', '031;1')
        fila.push(nome, idade)
        self.color(f'{nome} foi adicionado à fila', '032')
        input('Pressione qualquer tecla para continuar...')

    def atender_pessoa(self, fila):
        if not fila.empty():
            pessoa = fila.pop_front()
            self.color(f'{pessoa} acabou de ser atendido', '032')
        else:
            self.color('Fila vazia', '031;1')
        input('Pressione qualquer tecla para continuar...')

    def listar_pessoas(self, fila):
        if not fila.empty():
            print('Estão na fila: ', end='')
            print(fila)
        else:
            self.color('Fila vazia', '031;1')
        input('Pressione qualquer tecla para continuar...')

    def situacao_fila(self, fila):
        """Mostra a situação atual da fila."""
        if self.mode_array:
            pass
        else:
            atendimentos = fila.atendidasComum + fila.atendidasPrioridade
            prioridade = fila.size_prioridade
            comum = fila.size_comum
            self.color(f'Quantidade de pessoas atendidas: {atendimentos}', '032;1')
            self.color(f'Tamanho da fila de prioridade: {prioridade}', '032;1')
            self.color(f'Tamanho da fila comum: {comum}', '032;1')
            input('Pressione qualquer tecla para continuar...')

    def sair(self,fila):
        return fila.empty()
  
    def executar(self, fila):
        self.exibir_menu()
        opc = self.escolher_opcao()

        if opc == '1':
            self.inserir_pessoa(fila)
        elif opc == '2':
            self.atender_pessoa(fila)
        elif opc == '3':
            self.listar_pessoas(fila)
        elif opc == '4':
            self.situacao_fila(fila)
        elif opc == '5':
            if self.sair(fila):
                return True
            else:
                self.color('Ainda há pessoas que não foram atendidas', '031;1')
                input('Pressione qualquer tecla para continuar...')    
                
        else:
            self.color('Opção incorreta!', '031;1')
            input('Pressione qualquer tecla para continuar...')


class Menu_Array(Menu):
    def inserir_pessoa(self, fila):
        from filaArray import Pessoa
        self.color('=' * 30, '034')
        self.color(f'{"INSERIR PESSOA":-^30}', '037;1')
        self.color('=' * 30, '034')
        
        nome = input("Digite o nome da pessoa: ").strip()
        while True:
            idade = input("Digite a idade: ").strip()
            if idade.isnumeric():
                idade = int(idade)
                break
            self.color('Insira uma idade válida!', '031;1')
        
       
        if idade >= 100:
            fila[0].add(nome,idade)  
        elif idade >= 90:
            fila[1].add(nome,idade)  
        elif idade >= 80:
            fila[2].add(nome,idade)  
        elif idade >= 70:
            fila[3].add(nome,idade) 
        elif idade >= 60:
            fila[4].add(nome,idade)  
        else:
            fila[5].add(nome,idade)  

        self.color(f'{nome} foi adicionado à fila!', '032')
        input('Pressione qualquer tecla para continuar...')

    def atender_pessoa(self, fila,ciclo):
        self.color('=' * 30, '034')
        self.color(f'{"ATENDER PESSOA":-^30}', '037;1')
        self.color('=' * 30, '034')

        turno = next(ciclo) 
        if turno == 'C':
            if not fila[5].attend():  
                self.color("Fila comum vazia!", '031;1')
        else:
            for i in range(5):  
                if not fila[i].isEmpty():
                    fila[i].attend()
                    break
            else:
                if not fila[5].attend():
                    self.color("Todas as filas estão vazias!", '031;1')

        input('Pressione qualquer tecla para continuar...')


    def listar_pessoas(self, fila):
        self.color('=' * 30, '034')
        self.color(f'{"LISTAR PESSOAS":-^30}', '037;1')
        self.color('=' * 30, '034')

        for i in range(5):
            if not fila[i].isEmpty():
                self.color(f"Fila de prioridade {i+1}: ", '032;1')
                print(fila[i])
        
        self.color("Fila comum: ", '032;1')
        print(fila[5])

        input('Pressione qualquer tecla para continuar...')

    def situacao_fila(self, fila):
        self.color('=' * 30, '034')
        self.color(f'{"SITUAÇÃO DA FILA":-^30}', '037;1')
        self.color('=' * 30, '034')

        
        atendimentos_comum = fila[5].getAttended()
        atendimentos_prioridade = sum(fila[i].getAttended() for i in range(5))

        self.color(f'Atendimentos comuns realizados: {atendimentos_comum}', '032;1')
        self.color(f'Atendimentos prioritários realizados: {atendimentos_prioridade}', '032;1')

        fila_restante_comum = fila[5].filled()
        fila_restante_prioridade = sum(fila[i].filled() for i in range(5))

        self.color(f'Pessoas restantes na fila comum: {fila_restante_comum}', '034;1')
        self.color(f'Pessoas restantes nas filas prioritárias: {fila_restante_prioridade}', '034;1')

        input('Pressione qualquer tecla para continuar...')

    def sair(self, fila):
       
        for i in range(5):
            if not fila[i].isEmpty():
                self.color("Impossível finalizar, ainda há pessoas em filas prioritárias", '031;1')
                return False
        
        if not fila[5].isEmpty():
            self.color("Impossível finalizar, ainda há pessoas na fila comum", '031;1')
            return False

        
        self.color("Atendimento finalizado com sucesso", '032;1')
        atendimentos_comum = fila[5].getAttended()
        atendimentos_prioridade = sum(fila[i].getAttended() for i in range(5))
        
        self.color(f'Atendimentos comuns: {atendimentos_comum}', '034;1')
        self.color(f'Atendimentos prioritários: {atendimentos_prioridade}', '034;1')
        return True

    def executar(self, fila,ciclo):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.exibir_menu()
            opc = self.escolher_opcao()

            if opc == '1':
                self.inserir_pessoa(fila)
            elif opc == '2':
                self.atender_pessoa(fila,ciclo)
            elif opc == '3':
                self.listar_pessoas(fila)
            elif opc == '4':
                self.situacao_fila(fila)
            elif opc == '5':
                if self.sair(fila):
                    break
                else:
                    self.color('Ainda há pessoas que não foram atendidas', '031;1')
                    input('Pressione qualquer tecla para continuar...')    
                    
            else:
                self.color('Opção incorreta!', '031;1')
                input('Pressione qualquer tecla para continuar...')    