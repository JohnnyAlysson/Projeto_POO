import uuid
class Pessoa:
    def __init__(self,nome:str,idade: int):
        self.matricula = uuid.uuid4()
        self.nome= nome
        self.idade= idade

    def __repr__(self):
        return f" Matricula: {self.matricula} \n nome: {self.nome}"
    
if __name__ == "__main__":
    print(Pessoa("Jonas",28))