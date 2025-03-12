from condicion import NumeroCondicion
from potencia import MetodoPotencia
from potencia_inverso import MetodoPotenciaInverso

class AnalisisPuente:
    def __init__(self):
        """
        Inicializa la clase con una matriz de rigidez generada aleatoriamente.
        """
        self.numero_condicion = NumeroCondicion(20)  # Tamaño de la matriz de rigidez
        self.matriz_rigidez = self.numero_condicion.generar_matriz_aleatoria()  # Generar matriz de rigidez
        self.potencia = MetodoPotencia(self.matriz_rigidez)  # Método de Potencia
        self.potencia_inverso = MetodoPotenciaInverso(self.matriz_rigidez)  # Método de Potencia Inverso

    def analizar_puente(self):
        """
        Realiza el análisis completo del puente, incluyendo el cálculo del número de condición,
        el autovalor dominante, el autovalor más pequeño y la visualización de la convergencia.
        """
        # 1. Cálculo del número de condición
        condicion = self.numero_condicion.obtener_condicion()
        print(f"Número de condición de la matriz de rigidez: {condicion}")
        if condicion > 1e6:
            print("Advertencia: El número de condición es alto. El diseño del puente puede ser inestable.")

        # 2. Método de Potencia para el autovalor dominante
        autovalor_dominante, autovector_dominante = self.potencia.calcular()
        print(f"Autovalor dominante (máxima rigidez): {autovalor_dominante}")
        print(f"Autovector asociado (dirección de máxima rigidez): {autovector_dominante}")
        self.potencia.graficar_convergencia()

        # 3. Método de Potencia Inverso para el autovalor más pequeño
        autovalor_pequeno, autovector_pequeno = self.potencia_inverso.calcular_autovalor()
        print(f"Autovalor más pequeño (mínima rigidez): {autovalor_pequeno}")
        print(f"Autovector asociado (dirección de mínima rigidez): {autovector_pequeno}")
        self.potencia_inverso.graficar_convergencia()

# Ejecutar el análisis del puente
AnalisisPuente().analizar_puente()