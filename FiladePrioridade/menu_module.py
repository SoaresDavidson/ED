class Menu():
    def color(self,txt,cor):
        print(f'\033[{cor}m{txt}\033[m')

    def menu(self,fila):
        self.color('='*30,'034')
        self.color(f'{"ATENDIMENTO":-^30}','037;1')
        self.color('='*30,'034')
        self.color(f'''1) Inserir pessoa na fila.
2) Atender pessoa da fila.
3) Listar pessoas da fila.
4) Situação atual da fila.
5) sair''','034;1')
        opc = str(input('escola uma opção: ')).strip()
        if opc == '1':
            nome = str(input('digite o nome da pessoa: ')).strip()
            while True:
                idade = str(input('digite a idade da pessoa: ')).strip() 
                if idade.isnumeric():
                    break
                self.color('insira uma idade válida','031;1')
            fila.push(nome,idade)
            self.color(f'{nome} foi adicionado na fila','032')
            input('pressione qualquer tecla para continuar...')

        elif opc == '2':
            if not fila.empty():
                pessoa = fila.pop_front()
                self.color(f'{pessoa}, acabou de ser atendido','032')
            else:
                self.color('fila vazia','031;1')    
            input('pressione qualquer tecla para continuar...')
        elif opc == '3':
            if not fila.empty():
                print('Estão na fila: ',end='')
                print(fila)
            else:
                self.color('fila vazia','031;1')    
            input('pressione qualquer tecla para continuar...')
        elif opc == '4':
            atendimentos = fila.atendidasComum+fila.atendidasPrioridade
            prioridade = fila.filaPrioridade-fila.atendidasPrioridade
            comum = fila.filaComum-fila.atendidasComum
            self.color(f'quantidade de pessoas atendidas: {atendimentos}','032;1')
            self.color(f'tamanho da fila de prioridade: {prioridade}','032;1')
            self.color(f'tamanho da fila de comum: {comum}','032;1')
            input('pressione qualquer tecla para continuar...')
        elif opc == '5':
            if fila.empty():

                return True
            else:
                self.color('Ainda existe pessoas que não foram atendidas','031;1') 
                input('pressione qualquer tecla para continuar...')

        else:
            self.color('Opção incorreta!','031;1')
            input('pressione qualquer tecla para continuar...')