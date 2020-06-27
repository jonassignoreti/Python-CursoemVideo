v1 = str(input('Digite o primeiro nome: ')).strip()
v2 = str(input('Digite o segundo nome: ')).strip()
v3 = str(input('Digite o terceiro nome: ')).strip()
v4 = str(input('Digite o quarto nome: ')).strip()
p1, p2, p3, p4 = 0

if (v1 > v2) and (v1 > v3) and (v1 > v4):
    v1 = p4
if (v1 < v2) and (v1 < v3) and (v1 < v4):
    v1 = p1
