def conversion():
    print('Bienvenido al sistema de conversion de Euro a Peso Colombianor')
    ve=float(input('Ingrese el valor en Euros que desea convertir'))
    vp=ve*4362
    print(f'{ve} eqivalen a ${vp}Pesos')
    op=int(input('''Que desea realizar?
    1. Realizar una nueva conversion
    2. Terminar'''))
    if op==1:
        return conversion
    elif op==2:
        exit