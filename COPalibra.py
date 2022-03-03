def conversion():
    print('Bienvenido al sistema de conversion de Peso Colombiano a Libras Esterlinas')
    vp=float(input('Ingrese el valor en pesos que desea convertir'))
    vl=vp*0.00019 
    print(f'{vp} eqivalen a ${vl}Libras Esterlinas')
    op=int(input('''Que desea realizar?
    1. Realizar una nueva conversion
    2. Terminar'''))
    if op==1:
        return conversion
    elif op==2:
        exit