ano = int(input('Digite o ano do carro: '))
preco = float(input('Digite o preco do carro: '))

valor_total = 0

if ano < 1990:
    valor_total = preco + preco*(1/100)
    print(f'Foi aplicada uma taxa de 1% sobre o valor do carro, ficando com preço de R$ {valor_total:.2f}')
else:
    valor_total = preco + preco*(1.5/100)
    print(f'Foi aplicada uma taxa de 1.5% sobre o valor do carro, ficando com preço de R$ {valor_total:.2f}')