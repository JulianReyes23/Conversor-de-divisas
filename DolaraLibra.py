def conversion():
    print('Bienvenido al sistema de conversion de Dolar a Libra Esterlina')
    vd=float(input('Ingrese el valor en dolares que desea convertir'))
    vl=vd*0.75
    print(f'{vd} eqivalen a ${vl}Libras Esterlinas')
    op=int(input('''Que desea realizar?
    1. Realizar una nueva conversion
    2. Terminar'''))
    if op==1:
        return conversion
    elif op==2:
        exit