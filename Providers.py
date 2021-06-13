import pandas as pd 

class providers():

    def iniciar(self):
        print('\n>>>>>>Bem vindo<<<<<<\n')

        print('Olá, nos da empresa providers, estamos fazendo uma pesquisa\npara saber como esta nosso serviço de  internet na sua casa\nIremos fazer uma pesquisa para melhorar nosso sistema e nossos serviços.\n') 

        while True:
            try:

                self.nome = str(input('Nome: '.strip()))
                self.a = self.nome

                self.segundo = str(input(f'Qual bairro voçe mora {self.a}?\n'.strip()))
                self.b = self.segundo 
                print('=================================\n')
                self.terceiro = int(input(f'muito bem de uma escala de 0 a 10 {self.a}\nquanto o senhor(a) e satisfeito com nosso serviço de internet No bairro {self.b} ? \n '))
                self.c = self.terceiro 
                          
                if self.c <= 5:
                    print(f'Obrigado {self.a} pelo seu fedback,\n ')
                    print(f'Vamos começa a melhorar nossos serviços no bairro {self.b}\npara melhor atender voçe cliente')
                    print('================================') 
                    self.pergunta = int(input('Qual problema o senhor tem ?\n1= lentidao\n2= sem internet durante certa hora do dia \n responda 1 ou 2\n '))
                    self.c = self.pergunta
                                         
                    if self.c == 1:
                        print(f'vamos começa uma varredura na rede do bairro {self.b}\npara averiguar posiveis problemas na rede optica, a Providers a gradece sua preferencia OBRIGADO !!')
                        print('>>>>>>><<<<<<<<')
                        self.pedir = input('Pedir copia?')
                        if self.pedir == 'sim'.strip():
                            print(f'nome do cliente >({self.a})<')
                            print(f'nome do bairro do cliente > ({self.b}) <')
                            print(f'nota do cliente foi >({self.terceiro})<') 
                            
                            if self.terceiro <= 5:
                                print(f'cliente insatisfeito no bairro {self.b} ') 

                            else:
                                print(f'o cliente esta satisfeito a nota foi >> {self.terceiro} << ') 
                            break

                            '''self.recebido = ['nome', self.a, 'bairro', self.b, 'Nota', self.terceiro,]
                            with open('recebido.txt','w')as arquivo:
                                for self.lista in self.recebido:
                                    arquivo.write(self.lista + '\n')'''
                                    
                        elif self.pedir == 'não'.strip():
                            print('Providers ')
                            break

                    elif self.c == 2:
                        print(f'Vamos enviar um tecnico ate sua residencia senhor(a) {self.a}\npara a veriguar posiveis problemas em seu kit de instalação a Providers a gradece sua preferencia OBRIGADO!!\n')
                        print('>>>>>>><<<<<<<<')
                        self.pedir = input('Pedir copia?')
                        if self.pedir == 'sim'.strip():
                            print(f'nome do cliente >({self.a})<')
                            print(f'nome do bairro do cliente > ({self.b}) <')
                            print(f'nota do cliente foi >({self.terceiro})<') 

                            if self.terceiro <= 5:
                                print(f'cliente insatisfeito no bairro {self.b} ') 

                            else:
                                print(f'o cliente esta satisfeito a nota foi >> {self.terceiro} << ') 
                            break

                            '''self.recebido = ['nome', self.a, 'bairro', self.b, 'Nota', self.terceiro,]
                            with open('recebido.txt','w')as arquivo:
                                for self.lista in self.recebido:
                                    arquivo.write(self.lista + '\n')
                                    break'''

                        elif self.pedir == 'náo'.strip():
                            print('Providers ')
                            break

                    else:
                        print('Digete uma das opção citada a cima obrigado ')

                elif self.c > 5 and self.c < 11:
                    print(f'obrigado {self.a} pela sua nota >> {self.c} \nnos taremos sempre melhorando nosso serviços no bairro {self.b}\n') 
                    break

                else:        
                    print(f'Digete um numero de (0 a 10) por favor {self.a}\n') 
            
            except:
                print('====== Erro! ======\ntente novamente.')
        

comecar= providers()
comecar.iniciar()