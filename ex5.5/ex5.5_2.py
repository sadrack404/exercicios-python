# Se você correr 65 quilômetros em 3 horas, 23 minutos e 17 segundos, qual é a sua velocidade média em m/s?

km = 65
horas = 3
minutos = 23
segundos = 17

DeltaT = (horas * 3600) + (minutos * 60) + segundos
DeltaD = km * 1000
print("Velocidade %.2f" % (DeltaD / DeltaT), "m/s")
