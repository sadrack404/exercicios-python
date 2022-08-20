# 2. Qual o tamanho dessa frase? E qual o tamanho de cada palavra?

frase = "Python é muito legal."

palavra1 = frase[0:5]
print("A primeira aplavra tem", len(palavra1))
palavra2 = frase[7]
print("A segunda aplavra tem", len(palavra2))
palavra3 = frase[9:14]
print("A terceira aplavra tem", len(palavra3))
palavra4 = frase[15:21]
print("A quarta aplavra tem", len(palavra4))

print("A frase tem caracteres", len(palavra1) + len(palavra2) + len(palavra3) + len(palavra4) + 3)