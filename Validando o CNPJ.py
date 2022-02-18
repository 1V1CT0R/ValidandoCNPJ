cnpj=input('digite o CNPJ')
novo_cnpj=cnpj[:-2]

contador=5
soma=0
for num in novo_cnpj:
    soma=soma+(int(num)*contador)
    contador=contador-1
    if contador<2:
        contador=9
d1=11-(soma%11)
if d1>9:
    d1=0
novo_cnpj+=str(d1)

contador=6
soma=0
for num1 in novo_cnpj:
    soma=soma+(int(num1)*contador)
    contador=contador-1
    if contador<2:
        contador=9
d2=11-(soma%11)
if d2>9:
    d2=0
novo_cnpj+=str(d2)


print(f'O cnpj válido é {novo_cnpj}')



