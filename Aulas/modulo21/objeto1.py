# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

#classes

class Tv():
    
    #metodo da classe
    def __init__(self, tamanho):
        self.cor = 'preta'
        self.ligada = True
        self.tamaho = tamanho
        self.canal = 'netflix'
        self.volume = 10
    
    def mudar_canal(self,novo_canal):#parametro
        self.canal = novo_canal
                
        

#aqui é a herança
tv_sala = Tv(55) # -> aqui é uma instância  
tv_quarto = Tv(70)   

tv_sala.mudar_canal('globo')   

print(tv_sala.canal)
print(tv_quarto.canal)