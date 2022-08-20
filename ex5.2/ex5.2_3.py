# Davinir não gosta de ir às aulas. Mas ele é obrigado a comparecer a pelo menos 75% delas. Ele quer saber
# quantas aulas pode faltar, sabendo que tem duas aulas por semana, durante quatro meses. Ajude o Davinir!

aulaPorSemana = 2
aulasPorMes = 8
mesesDeAula = 4

aulas = ((aulaPorSemana * aulasPorMes) * mesesDeAula)

aulasQuePodeFaltar = ((aulas * 75) / 100)

print('Davinir pode faltar {} aulas'.format(aulas - aulasQuePodeFaltar))
