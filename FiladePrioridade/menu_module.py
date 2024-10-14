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

        if self.mode_array and fila.isFulls():
            self.color('fila está cheia','031;1')
            input('Pressione qualquer tecla para continuar...')
            return
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
            atendimentos = fila.get_atendidos()
            prioridade = fila.get_size_prioridade()
            comum = fila.get_size_comum()
        else:
            atendimentos = fila.atendidasComum + fila.atendidasPrioridade
            prioridade = fila.size_prioridade()
            comum = fila.size_comum()
        self.color(f'Quantidade de pessoas atendidas: {atendimentos}', '032;1')
        self.color(f'Tamanho da fila de prioridade: {prioridade}', '032;1')
        self.color(f'Tamanho da fila comum: {comum}', '032;1')
        input('Pressione qualquer tecla para continuar...')

    def encerramento(self,fila,mode_array=False):
        if mode_array:
            try:
                self.color('Atendimento encerrado','032;1')
                self.color('Estátisticas: ','032;1')
                self.color(f'Atendimentos: {fila.get_atendidos()}','034;1')
                self.color(f'Percentual fila prioritária: {(fila.get_atendidos_prioridade()/(fila.get_atendidos()))*100:.2f}%','034;1')
                self.color(f'Percentual fila comum: {(fila.get_atendidos_comum()/(fila.get_atendidos()))*100:.2f}%','034;1')
            except:
                self.color('Não apareceu nenhuma pessoa hoje','031;1')   

            return 

        try:    
            self.color('Atendimento encerrado','032;1')
            self.color('Estátisticas: ','032;1')
            self.color(f'Atendimentos: {fila.atendidasComum+fila.atendidasPrioridade}','034;1')
            self.color(f'Percentual fila prioritária: {(fila.filaPrioridade/(fila.filaComum+fila.filaPrioridade))*100:.2f}%','034;1')
            self.color(f'Percentual fila comum: {(fila.filaComum/(fila.filaComum+fila.filaPrioridade))*100:.2f}%','034;1')
        except:
            self.color('Não apareceu nenhuma pessoa hoje','031;1')

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
                self.encerramento(fila,self.mode_array)
                return True
            else:
                self.color('Ainda há pessoas que não foram atendidas', '031;1')
                input('Pressione qualquer tecla para continuar...')    
                
        else:
            self.color('Opção incorreta!', '031;1')
            input('Pressione qualquer tecla para continuar...')
