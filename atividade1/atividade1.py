class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def detalhes_do_curso(self):
        return f"Nome do Curso: {self.nome}\nDuração: {self.duracao} anos"


class Presencial(Curso):
    def __init__(self, nome, duracao, numero_de_vagas):
        super().__init__(nome, duracao)
        self.numero_de_vagas = numero_de_vagas

    def detalhes_do_curso(self):
        return f"{super().detalhes_do_curso()}\nNúmero de Vagas: {self.numero_de_vagas}"


class Online(Curso):
    def __init__(self, nome, duracao, plataforma_online):
        super().__init__(nome, duracao)
        self.plataforma_online = plataforma_online

    def detalhes_do_curso(self):
        return f"{super().detalhes_do_curso()}\nPlataforma Online: {self.plataforma_online}"


curso_presencial = Presencial("Curso Presencial de Python", 2, 30)
curso_online = Online("Curso Online de Data Science", 1, "Coursera")


print("Detalhes do Curso Presencial:")
print(curso_presencial.detalhes_do_curso())

print("\nDetalhes do Curso Online:")
print(curso_online.detalhes_do_curso())