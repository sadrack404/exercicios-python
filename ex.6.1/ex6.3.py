# Josefson deseja fazer compras na China. Ela quer comprar um celular de USD 299,99, uma chaleira de
# USD 23,87, um gnomo de jardim de USD 66,66 e 6 adesivos de unicórnio de USD 1,42 cada um. O frete
# de tudo isso para a cidade de Rolândia, no Paraná, ficou em USD 12,34.

celular = 299.99
chaleira = 23.87
gnomo = 66.66
adesivos = 6 * 1.42

totalDolar = celular + chaleira + gnomo + adesivos
iof = 0.0638
totalReal = (totalDolar / 5.40)

print("A) ", totalDolar)
print("B) ", totalReal - (totalReal * iof))
print("C) ", totalReal * iof)

