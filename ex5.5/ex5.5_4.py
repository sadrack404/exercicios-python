#  Rondinelly quer ligar três capacitores, de valores:
c1 = 10
c2 = 22
c3 = 6.8
uf = 10**(-6)

cp = c1 + c2 + c3
cs = 1/c1 + 1/c2 + 1/c3
cs2 = 1/(1/c1 + 1/c2 + 1/c3)


print("O valor resultate de CP é ", cs2, "μF")
print("O valor resultate de CS é ", cs, "μF")
print("O valor resultate de CS2 é ", cs2, "μF")