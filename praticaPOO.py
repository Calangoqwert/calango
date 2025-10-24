class Pessoa:
    def __init__(self,nome) -> None:
        self.nome = nome

    def apresentar(self) -> str:
        return f"Olá, eu sou {self.nome}"

class Aluno(Pessoa):
    def __init__(self,nome=None ,matricula=None):

        if nome==None:
            nome=input("digite o nome do aluno: ")
        if matricula==None:
            matricula=input("digite a marticula do aluno: ")

        super().__init__(nome)
        self.matricula=matricula

    def apresentar(self) ->str:
        base = super().apresentar()
        return f"{base} e sou aluno,minha matricula é {self.matricula}"

class Professor(Pessoa):
    def __init__(self,nome=None, disciplina=None, matricula=None):
        
        if nome==None:
            nome=input("digite o nome do professor: ")
        if matricula==None:
            matricula=input("digite a matricula do professor: ")
        if disciplina==None:
            disciplina=input("digite o nome da disciplina do professor: ")
            
        super().__init__(nome)
        self.disciplina = disciplina
        self.matricula=matricula
    def apresentar(self) -> str:
        base= super().apresentar()
        return f"{base}, minha matricula é {self.matricula}, sou Professor de {self.disciplina}"
        
pessoa = Pessoa('Carlos')
aluno=Aluno()
professor=Professor()

print(pessoa.apresentar())
print(aluno.apresentar())
print(professor.apresentar())