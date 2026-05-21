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
                opcion = input('¿Desea Continuar? \n[1] Si \n[2] No \n')
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
                opcion = input('¿Desea Continuar? \n[1] Si \n[2] No \n')
                if (opcion == '1'):
                    while True:
                        letraFaltante = ''
                        listaLetraPalabra = []
                        palabraRandom = self.getPalabraRandom()
                        print(('\nIntento #: ' + str(contadorPalabrasCompletadas)))
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
                    print('\n¡Bien hecho, has ganado!')
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