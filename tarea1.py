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

def comTab():
    if listaEnRango(secuencia, 1, 7) == 1:
        completarTableroEnOrden(tablero, secuencia)
        mostrarTablero(tablero)
    else:
        print ("Error, Numeros fuera de rango")
