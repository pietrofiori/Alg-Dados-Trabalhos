from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self,id,nome,telefone):
        self.id = id
        self.nome = nome
        self._telefone = telefone

    # def getInformacoes(self):
    #     return f"Modelo: {self.modelo} \n Cor: {self.cor} \n Preco: {self.preco}"
    
    @abstractmethod
    def marcarPresenca(self):
        pass

    def matricular(self):
        pass

class AlunoGraduacao(Pessoa):
     def __init__(self, id, nome, telefone, matricula,presencas):
        super().__init__(id, nome, telefone)
        self.__matricula = matricula
        self.__presencas = presencas

     def matricular(self):
            pass
    
     def marcarPresenca(self):
           self.__presencas += 1
           print("Presença Marcada")
        
     def getMatricula(self):
            return self.__matricula
    
     def setMatricula(self,matricula):
            return self.__matricula == matricula


aluno1 = AlunoGraduacao(2,"Pietro","23879438927","771800405",5)
print(aluno1.getMatricula())
aluno1.marcarPresenca()
