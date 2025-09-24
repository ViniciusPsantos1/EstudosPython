# class - Classes são moldes para criar novos objetos
# As classes geram novos obejetos (instâncias) que
# podem ter seus proprios atributos e metodos
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar varias ações.
# Por convenção, usamos PascalCase para nomes de classes.
#string = "Vinicius" #str
#print(string.upper()) #upper - Deixar todas as letras maiusculas

#Aula 1
class Pessoa:
    def __init__(self, nome, sobrenome ):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Vinicius', 'Pereira')
p2 = Pessoa('Henrique', 'Juliano')
print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)

#Aula 2

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
            print(f"{self.nome} esta acelerando")

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

prisma = Carro(nome='Prisma')
print(prisma.nome)
prisma.acelerar()

#Aula 3



