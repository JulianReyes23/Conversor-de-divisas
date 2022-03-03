def conversion():
    print('Bienvenido al sistema de conversion de Dolar a Peso Colombiano')
    vd=float(input('Ingrese el valor en dolares que desea convertir'))
    vp=vd*4000
    print(f'{vd} eqivalen a ${vp}Pesos')
    op=int(input('''Que desea realizar?
    1. Realizar una nueva conversion
    2. Terminar'''))
    if op==1:
        return conversion
    elif op==2:
        exit