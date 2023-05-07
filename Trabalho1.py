
from abc import ABC, abstractmethod

class Computador(ABC):
    def __init__(self,modelo,cor,preco):
        self.modelo = modelo 
        self.cor = cor
        self.preco = preco 

    def getInformacoes(self):
        return f"Modelo: {self.modelo} \n Cor: {self.cor} \n Preco: {self.preco}"
    
    @abstractmethod
    def cadastrar(self):
        pass

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return f"{super().getInformacoes()}, Potência da Fonte: {self._potenciaDaFonte}"

    def cadastrar(self):
        print("Desktop Cadastrado")

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        return f"{super().getInformacoes()}, Tempo da Bateria: {self.__tempoDeBateria}"

    def cadastrar(self):
        print("Notebook Cadastrado")


desktop  = Desktop ("Pichau Home Gamer", "preto", 3500.50, "650W")

notebook = Notebook ("Vostro", "cinza", 1230.80, "3h")

desktop.cadastrar()
print(" ")
print(desktop.getInformacoes())
print(" ")
notebook.cadastrar()
print(" ")
print(notebook.getInformacoes())
print(" ")