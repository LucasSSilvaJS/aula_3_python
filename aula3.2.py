gerente = 101
engenheiro = 102
tecnico = 103

cargo = int(input('Digite o código do seu cargo: '))
salario = float(input('Digite seu salario: '))

salario_com_aumento = 0
diferenca_entre_salarios = 0

if cargo == gerente:
    salario_com_aumento = salario + salario * (10/100)
elif cargo == engenheiro:
    salario_com_aumento = salario + salario * (20/100)
elif cargo == tecnico:
    salario_com_aumento = salario + salario * (30/100)
else:
    salario_com_aumento = salario + salario * (40/100)

diferenca_entre_salarios = salario_com_aumento - salario

print(f'Salario antigo: {salario:.2f}')
print(f'Salario com aumento: {salario_com_aumento:.2f}')
print(f'Diferença: {diferenca_entre_salarios:.2f}')