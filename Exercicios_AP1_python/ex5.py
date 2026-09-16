nota = float(input("Digite a nota: "))
frequencia = float(input("Digite a frequência (%): "))

# operadores lógicos que verificam se o aluno foi aprovado ou reprovado, de acordo com a nota e a frequência digitadas pelo usuário.
if frequencia >= 75:
    if nota >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado por nota.")
else:
    print("Aluno reprovado por falta.")


# Classificação da nota com operadores logicos, cada classificação é exibida de acordo com a nota digitada pelo usuário.
if nota >= 9:
    print("Classificação: Excelente")
elif nota >= 7:
    print("Classificação: Bom")
elif nota >= 5:
    print("Classificação: Regular")
else:
    print("Classificação: Ruim")


# Menu simples

print("\nMENU")
print("1 - Listar alunos")
print("2 - Cadastrar aluno")
print("3 - Calcular média")
print("4 - Sair")

opcao = input("Escolha uma opção: ")

# um match case simples que exibe uma mensagem de acordo com a opção escolhida pelo usuário, caso a opção não seja válida, será exibida uma mensagem de erro.
match opcao:
    case "1":
        print("Listando alunos...")
    case "2":
        print("Cadastrando aluno...")
    case "3":
        print("Calculando média...")
    case "4":
        print("Saindo do sistema...")
    case _:
        print("Opção inválida.")