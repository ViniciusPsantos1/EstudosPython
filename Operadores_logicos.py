#Operador_logico(AND) - se uma condição for falsa, toda linha sera considerada falsa também
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


#Operador_logico(Or) - se uma condição for verdadeira, toda linha sera considerada verdadeira também
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

#Operador_logico(not) - Utilizado para inverter expressõe
#not true = False
#not false = True

#Operador_logico(in e not in)
#Strings são interaveis
nome = 'Vinicius'
print(nome[2]) # [] - Utilizado para selecionar indice
# Lista
frutas = ["maçã", "banana", "laranja"]
print("maçã" in frutas)   # True
print("uva" in frutas)    # False

# String
texto = "Python é divertido"
print("Python" in texto)  # True
print("Java" in texto)    # False
