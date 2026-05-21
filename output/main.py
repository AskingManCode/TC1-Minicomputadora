import random

class Letras:
    def __init__(self):
        self.dictABC = {}
        self.dictABC = {'A': 'Animal', 'B': 'Bosque', 'C': 'Casa', 'D': 'Dado', 'E': 'Escoba', 'F': 'Faro', 'G': 'Gato', 'H': 'Hielo', 'I': 'Isla', 'J': 'Juguete', 'K': 'Koala', 'L': 'Luna', 'M': 'Mamut', 'N': 'Nube', 'O': 'Oso', 'P': 'Parque', 'Q': 'Queso', 'R': 'Rio', 'S': 'Sol', 'T': 'Tren', 'U': 'Uva', 'V': 'Viento', 'W': 'Waffle', 'X': 'Xilófono', 'Y': 'Yoyo', 'Z': 'Zanahoria'}

    def getListaLetras(self):
        listaLetras = []
        for letra in self.dictABC.keys():
            listaLetras.append(letra)
        return listaLetras

    def getListaPalabras(self):
        listaPalabras = []
        for palabra in self.dictABC.values():
            listaPalabras.append(palabra)
        return listaPalabras

    def getPalabra(self, llave):
        return self.dictABC[llave]

    def getPalabraRandom(self):
        listaPalabras = []
        numeroRandom = 0
        palabraRandom = ''
        listaPalabras = self.getListaPalabras()
        numeroRandom = random.randint(0, (len(listaPalabras) - 1))
        palabraRandom = listaPalabras[numeroRandom]
        return palabraRandom

    def quitarLetraRandom(self, palabra):
        posicionLetra = 0
        listaLetraPalabra = []
        palabraIncompleta = ''
        letraQuitada = ''
        posicionLetra = random.randint(0, (len(palabra) - 1))
        letraQuitada = palabra[posicionLetra:(posicionLetra + 1)]
        i = 0
        while (i < len(palabra)):
            if (i == posicionLetra):
                palabraIncompleta += '_'
            else:
                palabraIncompleta += palabra[i:(i + 1)]
            i += 1
        listaLetraPalabra.append(palabraIncompleta)
        listaLetraPalabra.append(letraQuitada.lower())
        return listaLetraPalabra

    def JugarBosqueLetras(self):
        opcion = ''
        letraSeleccionada = ''
        listaLetras = []
        acumuladorLetras = ''
        try:
            while True:
                print('\n=====> Bosque de Letras <=====\n')
                print('Este juego consiste en seleccionar una letra del abecedario y seguidamente \nse te mostrará una palabra que empiece con la letra seleccionada.')
                opcion = input('\n¿Desea Continuar? \n[1] Si \n[2] No \n')
                if (opcion == '1'):
                    while True:
                        print('\nSeleccione una letra del abecedario.')
                        listaLetras = self.getListaLetras()
                        for letra in listaLetras:
                            acumuladorLetras += (letra + '  ')
                        print(acumuladorLetras)
                        letraSeleccionada = str(input()).capitalize()
                        if (not letraSeleccionada.isalpha()):
                            print('\nError: No ha ingresado una letra del abecedario.')
                        if not ((not letraSeleccionada.isalpha())):
                            break
                    print(('\nHa seleccionado la letra: ' + letraSeleccionada))
                    print((((letraSeleccionada + ' - ') + self.getPalabra(letraSeleccionada)) + '\n'))
                    print('¡Bien hecho!\n')
                    return
                elif (opcion == '2'):
                    print('\nVolviendo al menú principal...\n')
                else:
                    print('\nError: No ha seleccionado ninguna de las opciones disponibles, intente de nuevo.\n')
                if not ((opcion != '2')):
                    break
        except Exception as Err:
            print(('\n' + Err))

    def JugarCompletaPalabra(self):
        opcion = ''
        palabraRandom = ''
        contadorPalabrasCompletadas = 0
        try:
            while True:
                print('\n=====> Completa la Palabra <=====\n')
                print('Este juego consiste en que se te muetre una palabra aleatoria, \nseguidamente se te mostrará la misma palabra pero sin una letra. \nDebes recordar la letra que falta e ingresarla.')
                opcion = input('\n¿Desea Continuar? \n[1] Si \n[2] No \n')
                if (opcion == '1'):
                    while True:
                        letraFaltante = ''
                        listaLetraPalabra = []
                        palabraRandom = self.getPalabraRandom()
                        print(('\nIntento #: ' + str((contadorPalabrasCompletadas + 1))))
                        print((('\nMemoriza la siguiente palabra: >>> ' + str(palabraRandom)) + ' <<<'))
                        listaLetraPalabra = self.quitarLetraRandom(palabraRandom)
                        print((('\nAhora observe: >>> ' + str(listaLetraPalabra[0])) + ' <<<'))
                        letraFaltante = input('¿Cuál es la letra que falta?').lower()
                        if (letraFaltante == listaLetraPalabra[1]):
                            print(('\n¡Bien hecho!, la letra faltante es la letra: ' + str(listaLetraPalabra[1])))
                            print(('Y la palabra completa es: ' + str(palabraRandom)))
                            contadorPalabrasCompletadas += 1
                        else:
                            print('\nError: No has ingresado la letra correcta, intenta de nuevo.')
                        if not ((contadorPalabrasCompletadas != 3)):
                            break
                    print('\n¡Bien hecho, has ganado!\n')
                    return
                elif (opcion == '2'):
                    print('\nVolviendo al menú principal...\n')
                else:
                    print('\nError: No ha seleccionado ninguna de las opciones disponibles, intente de nuevo.\n')
                if not ((opcion != '2')):
                    break
        except Exception as Err:
            print(('\n' + Err))

    def JugarLetraIntrusa(self):
        print('\n===== LETRA INTRUSA =====')
        print('Se muestran 4 letras. Una no está en orden alfabético.')
        print('Identifica cuál es la letra intrusa.\n')
        rondas = [['A', 'B', 'D', 'C'], ['E', 'G', 'F', 'H'], ['M', 'N', 'P', 'O']]
        intrusas = [2, 1, 2]
        puntaje = 0
        ronda = 0
        while (ronda < 3):
            print((('\n--- Ronda ' + str((ronda + 1))) + ' ---'))
            letras = rondas[ronda]
            i = 0
            while (i < len(letras)):
                print(((str((i + 1)) + '. ') + str(letras[i])))
                i += 1
            opcion = 0
            valido = False
            while (not valido):
                try:
                    opcion = int(input('¿Cuál es el número de la letra intrusa (1-4)? '))
                    if ((opcion >= 1) and (opcion <= 4)):
                        valido = True
                    else:
                        print('Número inválido. Elige 1, 2, 3 o 4.')
                except Exception as error:
                    print('Error: Debes ingresar un número.')
            if ((opcion - 1) == intrusas[ronda]):
                print((("¡Correcto! La intrusa era '" + str(letras[intrusas[ronda]])) + "'."))
                puntaje = (puntaje + 1)
            else:
                print('Incorrecto. Inténtalo nuevamente.')
            ronda += 1
        print('\n=== FIN DEL JUEGO ===')
        print((('Acertaste ' + str(puntaje)) + ' de 3 rondas.'))
        if (puntaje == 3):
            print('¡Felicidades, ganaste!')
        else:
            print('Sigue practicando.')
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

    def juegosNumeros(self):
        opcion = 0
        while (opcion != 4):
            print('====================')
            print('===                          ===')
            print('=             NUMEROS            =')
            print('===                          ===')
            print('====================')
            print('\n1. Ordena los números\n2. Mayor y menor\n3. Adivina el número\n')
            try:
                opcion = int(input('Elige una opción (1-4): '))
                __lucia_switch_0 = opcion
                if __lucia_switch_0 == 1:
                    self.OrdenaLosNumeros()
                elif __lucia_switch_0 == 2:
                    self.MayorYMenor()
                elif __lucia_switch_0 == 3:
                    self.JugarAdivinaNumero()
                elif __lucia_switch_0 == 4:
                    print('Regresando al menú principal...')
                else:
                    print('Debes ingresar una de las opciones establecidas.')
            except Exception as error:
                print('Solo se admiten números para elegir alguna opción.')
class Logica:
    def __init__(self):
        pass

    def JugarCualSobra(self):
        opcion = ''
        try:
            print('\n=====> ¿Cuál sobra? <=====\n')
            print('Seleccione la opción que no pertenece al grupo:\n')
            print('[1] Perro')
            print('[2] Gato')
            print('[3] Carro')
            print('[4] Conejo')
            opcion = input('\nDigite una opción: ')
            if (opcion == '3'):
                print('\n¡Felicidades, ganaste!\n')
                print("Correcto, 'Carro' sobra porque no es un animal.\n")
            else:
                print('\nIncorrecto, inténtalo nuevamente.\n')
        except Exception as Err:
            print(Err)
def queGrande():
    print('\n===== ¡QUÉ GRANDE! YO SOY ESTE =====')
    print('En cada ronda verás 3 animales. Elige el más grande.\n')
    conjuntos = [['Perro', 'Gato', 'Elefante'], ['Ratón', 'Caballo', 'Conejo'], ['Hormiga', 'Ballena', 'Mosca']]
    correctosIndex = [2, 1, 1]
    puntaje = 0
    ronda = 0
    while (ronda < 3):
        print((('\n--- Ronda ' + str((ronda + 1))) + ' ---'))
        animales = conjuntos[ronda]
        correctoIdx = correctosIndex[ronda]
        i = 0
        while (i < len(animales)):
            print(((str((i + 1)) + '. ') + str(animales[i])))
            i += 1
        opcion = 0
        valido = False
        while (not valido):
            try:
                opcion = int(input('¿Cuál es el animal más grande (1-3)? '))
                if ((opcion >= 1) and (opcion <= 3)):
                    valido = True
                else:
                    print('Número inválido. Elige 1, 2 o 3.')
            except Exception as error:
                print('Error: Debes ingresar un número.')
        if ((opcion - 1) == correctoIdx):
            print((("¡Correcto! El más grande es '" + str(animales[correctoIdx])) + "'."))
            puntaje = (puntaje + 1)
        else:
            print((("Incorrecto. El más grande era '" + str(animales[correctoIdx])) + "'."))
        ronda += 1
    print('\n=== FIN DEL JUEGO ===')
    print((('Acertaste ' + str(puntaje)) + ' de 3 rondas.'))
    if (puntaje == 3):
        print('¡Felicidades, ganaste!')
    else:
        print('¡Sigue practicando!')
letras = Letras()
numeros = Numeros()
logica = Logica()
def mostrarBienvenida():
    print('╔══════════════════════════════════════════╗')
    print('║    ¡Bienvenido a MINICOMPUTADORAS! 🌟    ║')
    print('║   El mundo de letras, números y lógica   ║')
    print('╚══════════════════════════════════════════╝')
    print('')
    print('¡Hola! Este es tu espacio para aprender jugando.')
    print('Elige una categoría y ¡a divertirse!')
    print('')
def mostrarMenuPrincipal():
    print('══════════════════════════════════════════')
    print('            📚 MENÚ PRINCIPAL             ')
    print('══════════════════════════════════════════')
    print('  1. 🔤 Letras')
    print('  2. 🔢 Números')
    print('  3. 🧠 Lógica')
    print('  4. 🎮 Juegos')
    print('  5. 🚪 Salir')
    print('══════════════════════════════════════════')
def mostrarMenuLetras():
    print('  1. 🌳 Bosque de Letras')
    print('  2. ✏️  Completa la Palabra')
    print('  3. 🔍 Letra Intrusa')
    print('  4. 🔙 Volver')
def mostrarMenuNumeros():
    print('  1. 🔃 Ordena los Números')
    print('  2. ⚖️  Mayor y Menor')
    print('  3. 🎯 Adivina el Número')
    print('  4. 🔙 Volver')
def mostrarMenuLogica():
    print('  1. ❓ ¿Cuál Sobra?')
    print('  2. 🔙 Volver')
def mostrarMenuJuegos():
    print('  1. 🏆 ¡Qué Grande!')
    print('  2. 🔙 Volver')
def leerOpcion(minimo, maximo):
    opcion = (-1)
    valido = False
    while (not valido):
        entrada = input((((('👉 Elige una opción (' + str(minimo)) + '-') + str(maximo)) + '): '))
        opcion = int(entrada)
        if ((opcion >= minimo) and (opcion <= maximo)):
            valido = True
        else:
            print((((('⚠️  Opción no válida. Por favor elige entre ' + str(minimo)) + ' y ') + str(maximo)) + '.'))
    return opcion
def menuLetras():
    salir = False
    while (not salir):
        mostrarMenuLetras()
        opcion = leerOpcion(1, 4)
        __lucia_switch_1 = opcion
        if __lucia_switch_1 == 1:
            letras.JugarBosqueLetras()
        elif __lucia_switch_1 == 2:
            letras.JugarCompletaPalabra()
        elif __lucia_switch_1 == 3:
            letras.JugarLetraIntrusa()
        elif __lucia_switch_1 == 4:
            salir = True
def menuNumeros():
    salir = False
    while (not salir):
        mostrarMenuNumeros()
        opcion = leerOpcion(1, 4)
        __lucia_switch_2 = opcion
        if __lucia_switch_2 == 1:
            numeros.OrdenaLosNumeros()
        elif __lucia_switch_2 == 2:
            numeros.MayorYMenor()
        elif __lucia_switch_2 == 3:
            numeros.JugarAdivinaNumero()
        elif __lucia_switch_2 == 4:
            salir = True
def menuLogica():
    salir = False
    while (not salir):
        mostrarMenuLogica()
        opcion = leerOpcion(1, 2)
        __lucia_switch_3 = opcion
        if __lucia_switch_3 == 1:
            logica.JugarCualSobra()
        elif __lucia_switch_3 == 2:
            salir = True
def menuJuegos():
    salir = False
    while (not salir):
        mostrarMenuJuegos()
        opcion = leerOpcion(1, 2)
        __lucia_switch_4 = opcion
        if __lucia_switch_4 == 1:
            queGrande()
        elif __lucia_switch_4 == 2:
            salir = True
def mostrarDespedida():
    print('')
    print('╔════════════════════════════════════════════╗')
    print('║           ¡Hasta la próxima! 👋            ║')
    print('║  Gracias por jugar con MINICOMPUTADORAS 🌟 ║')
    print('╚════════════════════════════════════════════╝')
mostrarBienvenida()
ejecutando = True
while ejecutando:
    mostrarMenuPrincipal()
    opcion = leerOpcion(1, 5)
    __lucia_switch_5 = opcion
    if __lucia_switch_5 == 1:
        menuLetras()
    elif __lucia_switch_5 == 2:
        menuNumeros()
    elif __lucia_switch_5 == 3:
        menuLogica()
    elif __lucia_switch_5 == 4:
        menuJuegos()
    elif __lucia_switch_5 == 5:
        ejecutando = False
mostrarDespedida()