import random

class Letras:
    def __init__(self):
        self.dictABC = {}
        self.dictABC = {'A': 'Animal', 'B': 'Bosque', 'C': 'Casa', 'D': 'Dado', 'E': 'Escoba', 'F': 'Faro', 'G': 'Gato', 'H': 'Hielo', 'I': 'Isla', 'J': 'Juguete', 'K': 'Koala', 'L': 'Luna', 'M': 'Mamut', 'N': 'Nube', 'O': 'Oso', 'P': 'Parque', 'Q': 'Queso', 'R': 'Rio', 'S': 'Sol', 'T': 'Tren', 'U': 'Uva', 'V': 'Viento', 'W': 'Waffle', 'X': 'Xilófono', 'Y': 'Yoyo', 'Z': 'Zanahoria'}

    def getLetras(self):
        acumuladorTexto = ''
        for i in self.dictABC:
            acumuladorTexto += (i + '  ')
        print(acumuladorTexto)

    def getPalabra(self, llave):
        return self.dictABC[llave]

    def JugarBosqueLetras(self):
        opcion = ''
        letraSeleccionada = ''
        try:
            while True:
                print('\n=====> Bosque de Letras <=====\n')
                opcion = input('¿Desea Continuar? \n[1] Si \n[2] No \n')
                if (opcion == '1'):
                    while True:
                        print('\nSeleccione una letra del abecedario.')
                        self.getLetras()
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
        try:
            while True:
                print('\n=====> Completa la Palabra <=====\n')
                opcion = input('¿Desea Continuar? \n[1] Si \n[2] No \n')
                if (opcion == '1'):
                    numeroRandom = random.randint(0, 26)
                    print(numeroRandom)
                    return
                elif (opcion == '2'):
                    print('\nVolviendo al menú principal...\n')
                else:
                    print('\nError: No ha seleccionado ninguna de las opciones disponibles, intente de nuevo.\n')
                if not (True):
                    break
        except Exception as Err:
            print(('\n' + Err))
letras = Letras()
letras.JugarCompletaPalabra()