import numpy as np
import matplotlib.pyplot as plt

class NumeroCondicion:
    def __init__(self, n):
        self.n = n
        self.tamano_matriz = []
        self.condicion_matriz = []
    
    def generar_matriz_aleatoria(self):
        tamano = self.n
        matriz = np.random.randint(-20, 20, size=(tamano, tamano))
        print("Matriz generada:\n", matriz)
        return matriz
    
    def obtener_condicion(self):
        tamano = self.n
        matriz = self.generar_matriz_aleatoria()
        det = np.linalg.det(matriz)
        if det != 0.0:
            nc = np.linalg.cond(matriz)
            self.tamano_matriz.append(tamano)
            self.condicion_matriz.append(nc)
            print(f"Número de condición: {nc}")
            return nc
        else:
            print(f"La matriz {matriz.shape[0]}x{matriz.shape[1]} es singular")
            return None
        
    def graficar(self):
        """
        Grafica el número de condición en función del tamaño de la matriz.
        """
        if len(self.tamano_matriz) > 0:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            x = self.tamano_matriz
            y = self.condicion_matriz
            z = np.zeros_like(x)

            ax.scatter(x, y, z, c='b', marker='o', s=100)

            ax.set_xlabel('Tamaño de la matriz')
            ax.set_ylabel('Número de condición')
            ax.set_zlabel('Z')
            plt.title('Tamaño vs Condición')

            ax.view_init(elev=20, azim=30)
            plt.show()
        else:
            print("No hay datos para graficar: todas las matrices son singulares.")
    

def main():
    nxn = 4
    cond = NumeroCondicion(nxn)
    resultado = cond.obtener_condicion()
    print(resultado)

    cond.graficar()
