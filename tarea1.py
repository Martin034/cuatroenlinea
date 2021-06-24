tablero = [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]
secuencia = [1, 2, 3, 5, 1]

def soltarFichaEnColumna(ficha, columna, tablero):
    for fila in range (6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            return

def completarTableroEnOrden(tab, sec):
    for I in range (0, len(sec), +1):
        soltarFichaEnColumna((I%2)+1, sec[I], tab)
    tab = resett(tab)
    sec = resets(sec)

def reTab():
    tab = [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]
    return tab

def listaEnRango(sec, min, max):
    con = 0
    for I in range (0, len(sec), +1):
        if sec[I] in range (min, max+1):
            con = con + 1
    if con == len(sec):
        return 1
    else:
        return 0

def mostrarTablero(tab):
    for I in range (0, len(tab), +1):
        print(tab[I])

def resett(tab):
    tab = reTab()
    return tab

def resets(sec):
    sec = []
    return sec

def comTab():
    if listaEnRango(secuencia, 1, 7) == 1:
        completarTableroEnOrden(tablero, secuencia)
        listToStr = ' '.join([str(elem) for elem in tablero])
        print("", listToStr.replace("]", "|\n").replace("[", "|").replace(",", "").replace("0", " "), "|_____________|")
        resett(tablero)
        resets(secuencia)
    else:
        print ("Error, Numeros fuera de rango")

def mostrarColumna(num, tab):
    columna = []
    for fila in tab:
        celda = fila[num-1]
        columna.append(celda)
    return columna

def mostrarFila(num, tab):
    for I in range (0, len(tab)):
        if I+1 == num:
            return tab[I]

def todasFilas(tab):
    for I in range (0, len(tab)):
        columna = []
        for J in range (0, len(tab)):
            celda = tab[I][J]
            columna.append(celda)
        print(columna)

def todasColumnas(tab):
    for I in range (0, len(tab)):
        Fila = []
        for J in range (0, len(tab)):
            celda = tab[J][I]
            Fila.append(celda)
        print(Fila)