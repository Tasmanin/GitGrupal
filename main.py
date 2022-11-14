''' PEP1T_3_JMBC   1ºDAM  JUAN MANUEL BECERRA CUMBRERA '''

'''Commit Inicial'''
'''Commit Maqueda'''
'''Commit Naza'''
#Rama creada
'''Rama para mezclar on a anterior'''
'''PROGRAMA OPTIMIZACIÓN TELEGRAMA'''


import sys


argumento=sys.argv  #llego mañana alrededor del almuerzo. Yo Llevo los pasteles.

mensaje=(' '.join(argumento[1:])).upper() #LLEGO MAÑANA ALREDEDOR DEL ALMUERZO. YO LLEVO LOS PASTELES.




def mensaje_tl(mensaje):

    ''' Función a la que se le pasa el parámetro "mensaje", lo convierte en una lista para poder modificar la cadena.
    Donde haya punto se sustituye por STOP, si el punto es punto y final será un doble STOPSTOP '''

    lista=list(mensaje)
    if lista[-1]=='.':
        lista[-1]=' STOPSTOP'
    mensaje=''.join(lista)
    return mensaje.replace('.',' STOP')

def quitarStop(listaPalabras):

    ''' Función que recibe como parámetro "listaPalabras" y devuelve una lista de palabras sin STOP.
    Donde se ha usado una lista auxiliar "aux" como método de filtrado '''


    aux = ['STOP', 'STOPSTOP']   #lista auxiliar
    return [w for w in listaPalabras if w not in aux]

def morse(mensaje):

    '''Función que recibe como parámetro "mensaje" y devuelve una tranducción en str de este al código morse.
     El código morse se ha guardado en un diccionario "morse", el cual ha sido invocado en un método de iteración al
      recorrer el mensaje letra por letra buscando las coincidencias de las claves y sustituyéndolas por su valor'''

    morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
             'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-','R': '.-.'
             ,'S': '...','T': '-','U': '..-','V': '...-','W': '.--','X': '-..-','Y': '-.--','Z': '--..','.': '.-.-.-'
             ,'0': '-----', '1': '.----','2': '..---','3': '...--','4': '....-','5': '.....','6': '-....','7': '--...'
             ,'8': '---..', '9': '----.'}

    traduccion=""

    for w in mensaje:
        if w in morse:
            traduccion+=morse[w]
        elif w==" ":
            traduccion+='/'
        else:
           traduccion+='???'

    return traduccion



def mostrar_menu():

    '''  Función: muestra menú de opciones al usurario en consola, no espera ningún parámetro.
     El usuario elige una opción de las presentadas en pantalla a través del teclado. Si selecciona la casilla 4 él
       programa termina. '''

    menu = """
                               \033[1m Menú de Opciones \033[0m
                                ===============

                    1) Envío con precio normal
                    2) Envío con precio reducido
                    3) Envío barato en código Morse
                    4) Salir
               """


    while True:

        print(menu)
        opcion = input("Elige una opción: ".rjust(38))
        if opcion == "1":
             print((" Opción: 1 ").center(100,'='))
             accion1(mensaje)
             print(("").center(100,'='))
        elif opcion == "2":
            print((" Opción: 2 ").center(100,'='))
            accion2(mensaje)
            print(("").center(100, '='))
        elif opcion == "3":
            print((" Opción: 3 ").center(100,'='))
            accion3(mensaje)
            print(("").center(100, '='))
        elif opcion == "4":
            print((" Salir ").center(100,'*'))
            break
        else:
            print((" Error: Debes digitar un número del 1 al 4 ").center(100,'='))



def accion1(mensaje):

    ''' Opción 1: ENVÍO CON PRECIO NORMAL, función que recibe como parámetro "mensaje" y devuelve un mensaje en formato
        telégrafo invocando a las funciones "mensaje_tl" y "quitarStop", contando cuantas palabras hay en total.
        Se calcula el coste del mensaje según el total de letras por palabra.
        Las palabras de más de 5 letras 0.50/palabra y el resto a 0.25/palabra. Los resultados se imprimen en pantalla.
     '''

    print('\033[1mEnvío con precio normal:\033[0m ')
    print()

    listaPalabras = mensaje_tl(mensaje).split()

    listaPalabrasF = quitarStop(listaPalabras)

    caracter_5 = 0

    caracter = 0

    for w in listaPalabrasF:
        if len(w) > 5:
            caracter_5 += 1
        else:
            caracter += 1


    print("La cadena contiene "+str(len(listaPalabrasF))+", de las cuales "+str(caracter_5)+" tienen más de 5 letras.")
    #Sacamos el total de palabras con el tamaño de la lista con len

    print("Por tanto, al precio de 0.25/palabra tenemos "+str(caracter)+" y a 0.50/palabra hay "+str(caracter_5))

    print("Total: "+str((caracter_5*0.5)+(caracter*0.25))+" €")
    print()

    print("Mensaje enviado:\n" + mensaje_tl(mensaje))  # Imprime mensaje

def accion2(mensaje):

    ''' Opción 2: ENVÍO CON PRECIO REDUCIDO, función que recibe como parámetro "mensaje"
    y devuelve un mensaje en formato telégrafo version reducida. Donde las palabras >5 letras se han rebanado
    los caracteres de más y añadido un "@". Se calcula el coste del mensaje según el total de letras por palabra.
    Al precio reducido 0.25/palabra. Los resultados se imprimen en pantalla.
        '''

    print('\033[1mEnvío con precio reducido:\033[0m ')
    print()

    listaPalabras = mensaje_tl(mensaje).split()

    caracter_5 = 0

    caracter = 0

    palabras=" ".join(listaPalabras)

    for w in palabras.split():
        if w!='STOPSTOP' and w!='STOP':
            if len(w) > 5:
                caracter_5 += 1
                palabras = palabras.replace(w, w[:5] + "@")
            else:
                caracter += 1

    listaPalabrasF = quitarStop(listaPalabras)

    listaPalabrasC = palabras.split()

    listaPalabrasCF = quitarStop(listaPalabrasC)

    print("La cadena contiene " + str(len(listaPalabrasF)) + " palabras, de las cuales " + str(
        caracter_5) + " tienen más de 5 letras pero se han recortado.")
    # Sacamos el total de palabras con el tamaño de la lista con len

    print("Por tanto, el mensaje se envía al precio de 0.25/palabra.")

    print("Total: "+ str((len(listaPalabrasCF)) * 0.25) + " €")
    print()

    print("Mensaje enviado:\n" + palabras)  # Imprime mensaje

def accion3(mensaje):

    ''' Opción 3: ENVÍO BARATO EN CÓDIGO MORSE. Función que recibe como parámetro "mensaje" y devuelve la traducción en
    morse invocando la función "morse". También devuelve el precio de cada carácter una vez realizado el conteo.
     Imprime los resultados en pantalla '''

    print('\033[1mEnvío barato en código Morse:\033[0m ')
    print()

    morse(mensaje)

    traduccion=morse(mensaje)

    conteoP = 0

    conteoG = 0

    for c in traduccion:
        if c == ".":
            conteoP += 1
        elif c == "-":
            conteoG += 1
        else:
            conteoP = conteoP
            conteoG = conteoG



    print("La cadena convertida a código morse tiene "+str(conteoP)+" puntos (0.005€/punto) y "+str(conteoG)+" rayas"
    "(0.01€/raya)")

    print("Por tanto el mensaje se envía al precio de "+str((conteoP*0.005)+(conteoG*0.01))+" € "
    "("+str(conteoP*0.005)+"€ y "+str(conteoG*0.01)+"€)")
    print()

    print("Mensaje enviado:\n" + morse(mensaje))  # Imprime mensaje




if __name__ == '__main__':
    print()
    print("Cadena recibida: ",mensaje)
    mostrar_menu()