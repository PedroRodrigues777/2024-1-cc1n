import math  # Importando o módulo math para usar a função sqrt (raiz quadrada)

print('Calcular hipotenusa')

# Solicitando os valores de B e C ao usuário e convertendo para float
B = float(input('Qual o valor de B: '))
C = float(input('Qual o valor de C: '))

# Calculando a hipotenusa usando a fórmula matemática
hipotenusa = math.sqrt((B ** 2) + (C ** 2))

# Exibindo o resultado formatado com uma casa decimal
print(f"O valor da hipotenusa é {hipotenusa:.1f}")