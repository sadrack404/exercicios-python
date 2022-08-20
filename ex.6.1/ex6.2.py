# Qual dessas médias dá a maior nota pra Rondineli?
# E qual das médias dá a pior nota?
import math

p1 = 8.66
p2 = 5.35
p3 = 5
p4 = 1

MA = (p1 + p2 + p3 + p4) / 4
MG = math.sqrt(p1 * p2 * p3 * p4)
MH = 4 / ((1 / p1) + (1 / p2) + (1 / p3) + (1 / p4))

if MA > MG and MA > MH:
    print("MA,  É o maior")
elif MG > MH:
    print("MG,  É o maior")
else:
    print("MH,  É o maior")

if MA < MG and MA < MH:
    print("MA,  É o menor")
elif MG < MH:
    print("MG,  É o menor")
else:
    print("MH,  É o menor")
