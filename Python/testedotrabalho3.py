
  ##########################################################################
 ################# SISTEMA DE CAIXA ELETRONICO ###########################
#########################################################################
 
class Caixa:
    cofre=[10,10,10,10,10]
    saida=[0,0,0,0,0]
    valor=0
    saldo=1050
 
    def loop(self):# interface
        while(True):
            resp=int(raw_input("1-cliente 2-tecnico 3-sair: "))
            
            if(resp==1):
                if(self.login(str(raw_input("numero do cartao: ")), int(raw_input("senha: ")), resp) ):
                    
                    while(True):
                        op=int(raw_input("1-saque 2-saldo 3-voltar: "))
                        
                        if(op==1):
                            valorSaque=int(raw_input("digite valor que o senhor(a) desejar sacar: "))
                        
                            if(valorSaque> self.statusSaldo()):
                                print("saldo insuficiente\n")
                            else:   
                                self.saque(valorSaque)
                                self.saldo=self.saldo-valorSaque
                        
                        elif(op==2):
                            print (self.statusSaldo())
                        
                        elif(op==3):
                            break
 
                        elif(op not in [1,2]):
                            print("opcao invalida") 
 
            elif(resp==2):
                if(self.login(str(raw_input("numero do cartao: ")), int(raw_input("senha: ")), resp) ):
                    while(True):        
                        op=int(raw_input("1-status do cofre: 2-voltar: "))
                        if(op==1):
                            self.statusCofre()
                        elif(op==2):
                            break
 
                        elif(op not in [1,2]):
                            print("opcao invalida\n")   
                        
            elif(resp==3):
                sair=int(raw_input("deseja sair 1-sim 2-nao: "))
                if(sair==1):
                    break
                elif(sair not in [1,2]):
                    print("opcao invalida\n")   
            else:
                print("opcao invalida\n")
            
    def statusSaldo(self):#retorna o saldo  
        return self.saldo
        
    def statusCofre(self):#imprime a quantidade de notas
        print(str(self.cofre)+"\n")
 
 
    def login(self,cartao,senha,modo):#retorna falso se ocorrer algum erro
        cliente={}
        if(modo==1):
            cliente={"666":1979}#tabela de clientes
            
        elif(modo==2):
            cliente={"222":1234}#tabela de funcionarios
    
        if(cartao not in cliente):
            print("cartao invalido\n")
            return False
 
        elif(senha != cliente[cartao]):
            print("senha incorreta\n")
            return False
        else:
            print("bem-vindo!\n")
            return True
 
    def cofreTotal(self):#retorna a quantia total de dinheiro no cofre
        return (self.cofre[0]*100)+(self.cofre[1]*50)+(self.cofre[2]*20)+ \
        (self.cofre[3]*10)+(self.cofre[4]*5)
 
    def desconto(self,nota):#administra a saida das notas
        i=None
        if(nota==100):
            i=0
        elif(nota==50):
            i=1
        elif(nota==20):
            i=2
        elif(nota==10):
            i=3
        elif(nota==5):
            i=4
 
        while(self.valor>=nota and self.cofre[i]>0):
            self.cofre[i]=self.cofre[i]-1
            self.saida[i]=self.saida[i]+1
            self.valor=self.valor-nota
 
    def saque(self,valor):
        self.valor=valor
        if(self.valor% 5 >0):
            print("apenas valores terminados em 5 ou 0\n")
 
        elif( self.valor<50  or self.valor>5000 or self.valor>self.cofreTotal() ):
            print("valor indisponivel\n")
        
        else:
            while(self.valor>0):#imprime as notas
                if(self.valor>=100 and self.cofre[0]>0):
                    self.desconto(100)  
        
                elif(self.valor>=50 and self.cofre[1]>0):
                    self.desconto(50)
 
                elif(self.valor>=20 and self.cofre[2]>0):
                    self.desconto(20)
 
                elif(self.valor>=10 and self.cofre[3]>0):
                    self.desconto(10)
 
                elif(self.valor>=5 and self.cofre[4]>0):
                    self.desconto(5)
 
            print (self.saida)
            self.saida=[0,0,0,0,0]
 
 
caixa = Caixa()
caixa.loop()
