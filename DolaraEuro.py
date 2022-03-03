def conversion():
    print('Bienvenido al sistema de conversion de Dolar a Euro')
    vd=float(input('Ingrese el valor en dolares que desea convertir'))
    ve=vd*0.90
    print(f'{vd} eqivalen a ${ve}Euros')
    op=int(input('''Que desea realizar?
    1. Realizar una nueva conversion
    2. Terminar'''))
    if op==1:
        return conversion
    elif op==2:
        exit