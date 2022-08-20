# Crie três listas, uma lista de cada coisa a seguir:

frutas = ["laranja", "maçãs", "pêra"]
docinhosDeFesta = ["brigadeiro", "beijinho", "bala de coco"]
feijoada = ["eu até faria", "mas acabaie me recusando", "odieo feijão"]

listona = frutas + docinhosDeFesta + feijoada

print("A) ", listona)
print("B) ", listona[3])

listona.insert(7, "BRIGADEIROS")
listona = listona

print("C) ", listona)
listona.insert(11, "Refrigerante")
listona.insert(12, "Suco")
listona.insert(13, "cerveja")

print("D) ", listona )
