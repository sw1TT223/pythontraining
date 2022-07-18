# calculadora de imc
# imc = peso / (altura x altura)
# < 19: delgadez
# entre 20 y 25: normal
# entre 26 y 30: sobrepeso
# más de 30: obesidad

peso = int(input("ingrese su peso en kilos "))

altura = float(input("ingrese su valor(con punto) "))

imc = peso / (altura ** 2)

if imc < 19:
    print(
        "Estado de delgadez"
    )
if imc >= 20 and imc <= 25:
    print(
        "Estado normal"
    )
if imc >= 26 and imc <= 30:
    print(
        "Estado de sobrepeso"
    )
if imc > 30:
    print(
        "Estado de obesidad"
    )