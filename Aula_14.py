 # <<<<<<<<<<<<<<<<<< Match Case >>>>>>>>>>>>>>>

# Semelhante as condicionais o Match Case, faz o computador fazer escolhas.
# Conhecido também como Strutural Pattern Matching


# <<<<<<<<<<<<<<<<<<<<<< EXERCÍCIOS >>>>>>>>>>>>>>>>>>>>>>>>> 

# 1: Verificando se o número é par ou ímpar

num1 = int(input("Digite um número: "))

match num1:
    case num1 if num1 % 2 == 0:
        print("O número é Par.")
    case _:
        print("O número é Ímpar.")


# 2: Verificando se um número é positivo, negativo ou zero

num = int(input("Digite um número: "))

match num:
    case 0:
        print("O número é zero.")
    case num if num > 0:
        print("O número é Positivo.")
    case _:
        print("O número é Negativo.")

# 3: Verificando se uma string é vazia ou não

texto = input("Digite uma Palavra: ")

match texto:
    case "":
        print("String vazio")
    case _:
        print("String preenchido.")

# 4: Verificando se um número é maior, menor ou igual a 10

num2 = int(input("Digite um número: "))

match num2:
    case 10:
        print("O número é Dez.")
    case num2 if num2 > 10:
        print("O número é maior que Dez.")
    case _:
        print("O número é menor que Dez.")

# 5: Classificando uma idade em faixas etárias - criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65).

idade = int(input("Digite sua Idade: "))

match idade:
    case idade if idade <= 12:
        print("Você é Criança")
    case idade if idade <= 17:
        print("Você é Adolescente")
    case idade if idade <= 35:
        print("Você é Jovem")
    case idade if idade <= 64:
        print("Você é Adulto")    
    case _:
        print("Você é Idoso")    