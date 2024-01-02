import random


class casillas:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.adyacente = 0
        self.is_mina = False

class tablero:
    def __init__(self, columnas, filas, nMinas):
        self.columnas = columnas
        self.filas = filas
        self.minas = nMinas
        self.casillas = [[casillas(fila, columna) for columna in range(columnas)] for fila in range(filas)]
        self.posicion_minas = set()
        self.minas_aleatorias()


    def contar_minas_adyacentes(self, fila, columna):
        minas_adyacentes = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nueva_fila, nueva_columna = fila + dx, columna + dy
                if (0 <= nueva_fila < self.filas) and (0 <= nueva_columna < self.columnas) and self.casillas[nueva_fila][nueva_columna].is_mina:
                    minas_adyacentes += 1
        return minas_adyacentes


    def minas_aleatorias(self):
        while len(self.posicion_minas) < self.minas:
            numFila_Random = random.randint(0, self.filas -1)
            numColumna_Random = random.randint(0, self.columnas -1)
            self.posicion_minas.add((numFila_Random, numColumna_Random))
            self.casillas[numFila_Random][numColumna_Random].is_mina = True

            for numFila_Random in range(self.filas):
                for numColumna_Random in range(self.columnas):
                    if not self.casillas[numFila_Random][numColumna_Random].is_mina:
                        self.casillas[numFila_Random][numColumna_Random].adyacente = self.contar_minas_adyacentes(numFila_Random, numColumna_Random)