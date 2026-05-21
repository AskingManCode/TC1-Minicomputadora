import random

class Numeros:
    def __init__(self):
        self.preguntas = None
        self.preguntas = {1: '¿Cuál es mayor?', 2: '¿Cuál es menor?'}

    def generarNumero(self):
        return random.randint(1, 100)

    def JugarAdivinaNumero(self):
        respuesta = ''
        try:
            print('\n=====> Adivina el Número <=====\n')
            print('Observa la secuencia y adivina el número oculto.\n')
            print('Secuencia 1:')
            print('2  4  ?  8')
            respuesta = input('¿Cuál número falta?: ')
            if (respuesta == '6'):
                print('\n¡Felicidades, ganaste!\n')
            else:
                print('\nIncorrecto, inténtalo nuevamente.')
                print('La respuesta correcta era 6.\n')
            print('Secuencia 2:')
            print('5  ?  15  20')
            respuesta = input('¿Cuál número falta?: ')
            if (respuesta == '10'):
                print('\n¡Felicidades, ganaste!\n')
            else:
                print('\nIncorrecto, inténtalo nuevamente.')
                print('La respuesta correcta era 10.\n')
            print('Secuencia 3:')
            print('?  3  4  5')
            respuesta = input('¿Cuál número falta?: ')
            if (respuesta == '2'):
                print('\n¡Felicidades, ganaste!\n')
            else:
                print('\nIncorrecto, inténtalo nuevamente.')
                print('La respuesta correcta era 2.\n')
            print('GRACIAS POR JUGAR')
        except Exception as Err:
            print(Err)

    def OrdenaLosNumeros(self):
        numeros = []
        i = 0
        while (i < 4):
            numeros.append(self.generarNumero())
            i += 1
        numsOrdenados = []
        numerosRespaldo = []
        numerosRespaldo = numeros.copy()
        numsOrdenados.append(max(max(numerosRespaldo[0], numerosRespaldo[1]), max(numerosRespaldo[2], numerosRespaldo[3])))
        (numerosRespaldo.pop(numsOrdenados[0], None) if isinstance(numerosRespaldo, dict) else (numerosRespaldo.remove(numsOrdenados[0]) if numsOrdenados[0] in numerosRespaldo else None))
        numsOrdenados.append(max(max(numerosRespaldo[0], numerosRespaldo[1]), numerosRespaldo[2]))
        (numerosRespaldo.pop(numsOrdenados[1], None) if isinstance(numerosRespaldo, dict) else (numerosRespaldo.remove(numsOrdenados[1]) if numsOrdenados[1] in numerosRespaldo else None))
        numsOrdenados.append(max(numerosRespaldo[0], numerosRespaldo[1]))
        (numerosRespaldo.pop(numsOrdenados[2], None) if isinstance(numerosRespaldo, dict) else (numerosRespaldo.remove(numsOrdenados[2]) if numsOrdenados[2] in numerosRespaldo else None))
        numsOrdenados.append(numerosRespaldo[0])
        print('\n=====> Ordena Los Números <=====\nEn esta actividad se te mostrarán 4 números y tendrás que ordenarlos de mayor a menor.\n¿Listo?\n')
        continuar = True
        while True:
            try:
                print((((((((('Ordena de mayor a menor estos números\n' + str(numeros[0])) + ' ') + str(numeros[1])) + ' ') + str(numeros[2])) + ' ') + str(numeros[3])) + '\n'))
                mayor = int(input('¿Cuál es el número mayor? '))
                if (not str(mayor).isnumeric()):
                    print('Lo sentimos, pero solo se permite que escribas números.')
                else:
                    if (mayor == numsOrdenados[0]):
                        for num in numeros:
                            if (num == numsOrdenados[0]):
                                (numeros.pop(num, None) if isinstance(numeros, dict) else (numeros.remove(num) if num in numeros else None))
                        print('¡Vas por buen camino!\n')
                        while True:
                            try:
                                print((((((((('\nOrdena de mayor a menor estos números\n' + str(numsOrdenados[0])) + ' ') + str(numeros[0])) + ' ') + str(numeros[1])) + ' ') + str(numeros[2])) + '\n'))
                                mayor = int(input((('¿Cuál es el siguiente mayor, el que le sigue a ' + str(numsOrdenados[0])) + '?')))
                                if (not str(mayor).isnumeric()):
                                    print('Lo sentimos, pero solo se permite que escribas números.')
                                else:
                                    if (mayor == numsOrdenados[1]):
                                        for num in numeros:
                                            if (num == numsOrdenados[1]):
                                                (numeros.pop(num, None) if isinstance(numeros, dict) else (numeros.remove(num) if num in numeros else None))
                                        print('¡Lo estás haciendo muy bien!\n')
                                        while True:
                                            try:
                                                print((((((((('\nOrdena de mayor a menor estos números\n' + str(numsOrdenados[0])) + ' ') + str(numsOrdenados[1])) + ' ') + str(numeros[0])) + ' ') + str(numeros[1])) + '\n'))
                                                mayor = int(input((('¿Cuál es el siguiente mayor, el que le sigue a ' + str(numsOrdenados[1])) + '?')))
                                                if (not str(mayor).isnumeric()):
                                                    print('Lo sentimos, pero solo se permite que escribas números.')
                                                else:
                                                    if (mayor == numsOrdenados[2]):
                                                        print((((((((('\nEnhorabuena. ¡Lo has logrado!\n La secuencia ordenada quedaría así: ' + str(numsOrdenados[0])) + ' ') + str(numsOrdenados[1])) + ' ') + str(numsOrdenados[2])) + ' ') + str(numsOrdenados[3])) + '\n'))
                                                        continuar = False
                                                    else:
                                                        print('Inténtalo nuevamente.')
                                            except Exception as error:
                                                print('Lo sentimos, pero solo se permite que escribas números.\n')
                                            if not ((continuar == True)):
                                                break
                                    else:
                                        print('Inténtalo nuevamente.')
                            except Exception as error:
                                print('Lo sentimos, pero solo se permite que escribas números.')
                            if not ((continuar == True)):
                                break
                    else:
                        print('Inténtalo nuevamente.')
            except Exception as error:
                print('Lo sentimos, pero solo se permite que escribas números.')
            if not ((continuar == True)):
                break
        print('GRACIAS POR JUGAR')

    def MayorYMenor(self):
        numeros = []
        i = 0
        while (i < 3):
            numeros.append(self.generarNumero())
            i += 1
        menor = min(min(numeros[0], numeros[1]), numeros[2])
        mayor = max(max(numeros[0], numeros[1]), numeros[2])
        print('\n=====> Mayor Y Menor <=====\nEn esta actividad se te mostrarán 3 números y tendrás que responder cuál es número mayor o cuál el menor, según la pregunta que te aparezca.\n¿Listo?')
        continuar = True
        pregunta = random.randint(1, 2)
        while True:
            try:
                print(((((('\nDe los siguientes tres números: ' + str(numeros[0])) + ' ') + str(numeros[1])) + ' ') + str(numeros[2])))
                respuesta = int(input(str(self.preguntas[pregunta])))
                if (not str(respuesta).isnumeric()):
                    print('Lo sentimos, pero solo se permite que escribas números.')
                else:
                    if (pregunta == 1):
                        if (mayor == respuesta):
                            print('¡Bien hecho! Has ganado.')
                            continuar = False
                        else:
                            print('Respuesta incorrecta. Inténtalo nuevamente.')
                    else:
                        if (menor == respuesta):
                            print('\n¡Bien hecho! Has ganado.')
                            continuar = False
                        else:
                            print('\nRespuesta incorrecta. Inténtalo nuevamente.')
            except Exception as error:
                print('Lo sentimos, pero solo se permite que escribas números.')
            if not ((continuar == True)):
                break
        print('GRACIAS POR JUGAR')