print("Bem-vindo ao sistema de entrada do evento!")

# input para o usuario digitar sua idade
idade = int(input("Digite sua idade: "))

# operador "while que verifica se a idade é menor que 0, caso seja, o usuário será solicitado a digitar novamente"
while idade < 0:
    print("Idade inválida!")
    idade = int(input("Digite sua idade novamente: "))

ingresso = input("Possui ingresso? (sim/nao): ").lower()

#operador lógico "if" que verifica se a idade é menor que 16, caso seja, o usuário não terá acesso ao evento. Caso contrário, será verificado se o usuário possui ingresso, caso possua, a entrada será liberada, caso contrário, será solicitado que o usuário compre um ingresso.
if idade < 18:
    print("Acesso não permitido.")
elif ingresso == "sim":
    print("Entrada liberada!")
else:
    print("Compre um ingresso.")