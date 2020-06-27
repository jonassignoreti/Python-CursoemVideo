inss = 0
base_calculo = 0
irrf = 0
salario_bruto = float(input('Salário Bruto: R$'))
n_dependentes = int(input('Nº de Dependentes: '))
deducao_por_dependentes = 189.59 * n_dependentes

if 6101.06 <= salario_bruto:
    inss = 713.08
    base_calculo = salario_bruto - inss - deducao_por_dependentes
if 3134.41 <= salario_bruto <= 6101.05:
    inss = salario_bruto * 14/100
    base_calculo = salario_bruto - inss - deducao_por_dependentes
if 2089.61 <= salario_bruto <= 3134.40:
    inss = salario_bruto * 12 / 100
    base_calculo = salario_bruto - inss - deducao_por_dependentes
if 1045.01 <= salario_bruto <= 2089.60:
    inss = salario_bruto * 9 / 100
    base_calculo = salario_bruto - inss - deducao_por_dependentes
if salario_bruto <= 1045.00:
    inss = salario_bruto * 7.5 / 100
    base_calculo = salario_bruto - inss - deducao_por_dependentes

if 4664.69 <= base_calculo:
    irrf = (base_calculo * 27.5/100) - 869.36
if 3751.06 <= base_calculo <= 4664.68:
    irrf = (base_calculo * 22.5/100) - 636.13
if 2826.66 <= base_calculo <= 3751.05:
    irrf = (base_calculo * 15/100) - 354.80
if 1903.99 <= base_calculo <= 2826.65:
    irrf = (base_calculo * 7.5/100) - 142.80
if base_calculo <= 1903.98:
    irrf = 0
salario_liquido = salario_bruto - inss - irrf

print('Salário Líquido: R${:.2f}'.format(salario_liquido))
print('INSS: R${:.2f}'.format(inss))
print('IRRF: R${:.2f}'.format(irrf))
