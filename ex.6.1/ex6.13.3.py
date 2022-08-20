# Agora que conhecemos atribuição múltipla
# e o método str.split() refaça os dois
# exercícios anteriores usando essas técnicas
frase = "Python é muito legal."

print("A frase tem ", len(frase), " letras")

print("A primeira aplavra tem", len(str.split(frase)[0]))
print("A primeira segunda tem", len(str.split(frase)[1]))
print("A primeira terceira tem", len(str.split(frase)[2]))
print("A primeira quarta tem", len(str.split(frase)[3]))
