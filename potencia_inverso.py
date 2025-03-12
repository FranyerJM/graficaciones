import numpy as np
import matplotlib.pyplot as plt
import condicion

class MetodoPotenciaInverso:
    def __init__(self, matriz, max_iter=300, tolerancia=1e-8):
        """
        Inicializa la clase con la matriz, el número máximo de iteraciones y la tolerancia.
        """
        self.matriz = matriz
        self.max_iter = max_iter
        self.tolerancia = tolerancia
        self.n = matriz.shape[0]
        self.vector_actual = np.random.randint(-5, 6, size=self.n)
        print("Vector inicial utilizado:\n", self.vector_actual)
        self.vector_actual = self.vector_actual / np.linalg.norm(self.vector_actual, ord=np.inf)
        self.autovalores_hist = []

    def calcular_autovalor(self):
        """
        Implementa el método de potencia inverso para calcular el autovalor más pequeño y su autovector asociado.
        """
        for i in range(self.max_iter):
            try:
                nuevo_vector = np.linalg.solve(self.matriz, self.vector_actual)
            except np.linalg.LinAlgError:
                print("Error: La matriz es singular o no se puede resolver el sistema lineal.")
                return None, None

            # Calcular el autovalor aproximado
            u = np.dot(self.vector_actual, nuevo_vector)
            u_normalizado = u / (self.vector_actual @ self.vector_actual)

            if abs(u_normalizado) < 1e-10:
                print("Error: División por cero en el cálculo del autovalor.")
                return None, None

            autovalor_aprox = 1 / u_normalizado
            self.autovalores_hist.append(autovalor_aprox)

            # Normalizar el nuevo vector
            norma_nuevo = np.linalg.norm(nuevo_vector, ord=np.inf)
            if norma_nuevo == 0:
                print("Error: Vector nulo después de la normalización.")
                return None, None

            self.vector_actual = nuevo_vector / norma_nuevo

            # Verificar convergencia
            if len(self.autovalores_hist) > 1:
                diferencia = abs(self.autovalores_hist[-1] - self.autovalores_hist[-2])
                if diferencia < self.tolerancia:
                    print(f"Convergencia alcanzada en {i + 1} iteraciones")
                    break

        return autovalor_aprox, self.vector_actual

    def graficar_convergencia(self):
        """
        Grafica la convergencia del autovalor más pequeño.
        """
        plt.figure(figsize=(12, 5))
        plt.plot(self.autovalores_hist, 'o--', markersize=4, label="Autovalor estimado")
        plt.xlabel('N Iteración')
        plt.ylabel("Valor del Autovalor")
        plt.title("Convergencia del Menor Autovalor")
        plt.grid()
        plt.legend()
        plt.show()
        
def main():
    matriz =  condicion.NumeroCondicion(4).generar_matriz_aleatoria()
    metodo = MetodoPotenciaInverso(matriz)

    autovalor, autovector = metodo.calcular_autovalor()

    print(f"Autovalor aproximado: {autovalor}")
    print(f"Autovector asociado:\n{autovector}")

    metodo.graficar_convergencia()
