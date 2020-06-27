# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e em milímetros.
m = float(input('Digite seu valor em metros: '))
km = m / 10**3
hm = m / 10**2
dam = m / 10
dm = m * 10
cm = m * 10**2
mm = m * 10**3
print('{} metros é o mesmo que: \n{} quilômetros, \n{} hectomêtros, \n{} decâmetros, \n{} decímetros, \n{} centímetros e \n{} milímetros'.format(m, km, hm, dam, dm, cm, mm))
