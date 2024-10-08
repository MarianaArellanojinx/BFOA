import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d
# Definir la clase ChartData
class ChartData:
    def __init__(self, interaction: int, fitness: float, nfe: int):
        self.interaction = interaction
        self.fitness = fitness
        self.nfe = nfe

    def __repr__(self):
        return f"ChartData(Interaccion={self.interaction}, fitness={self.fitness}, NFE={self.nfe})"


# Definir la clase Chart para manejar los objetos y gráficos
class Chart:
    def __init__(self):
        self.lista_objetos = []

    def agregar_objeto(self, interaccion: int, fitness: float, nfe: int):
        nuevo_objeto = {'interaccion': interaccion, 'fitness': fitness, 'nfe': nfe}
        self.lista_objetos.append(nuevo_objeto)

    # Gráfico 1: Fitness vs Iteración con línea suavizada
    def graficar_fitness_vs_interaccion_suavizado(self):
        interacciones = [obj['interaccion'] for obj in self.lista_objetos]
        fitness = [obj['fitness'] for obj in self.lista_objetos]
        fitness_suavizado = gaussian_filter1d(fitness, sigma=2)
        return interacciones, fitness, fitness_suavizado

    # Gráfico 2: NFE vs Iteración con escala logarítmica
    def graficar_nfe_vs_interaccion_log(self):
        interacciones = [obj['interaccion'] for obj in self.lista_objetos]
        nfe = [obj['nfe'] for obj in self.lista_objetos]
        return interacciones, nfe

    # Gráfico 3: Fitness y NFE vs Iteración en ejes diferentes
    def graficar_fitness_y_nfe_vs_interaccion_dual(self):
        interacciones = [obj['interaccion'] for obj in self.lista_objetos]
        fitness = [obj['fitness'] for obj in self.lista_objetos]
        nfe = [obj['nfe'] for obj in self.lista_objetos]
        return interacciones, fitness, nfe

    # Gráfico 4: Tasa de cambio de Fitness
    def graficar_tasa_cambio_fitness(self):
        interacciones = [obj['interaccion'] for obj in self.lista_objetos]
        fitness = [obj['fitness'] for obj in self.lista_objetos]
        tasa_cambio = np.diff(fitness) / np.diff(interacciones)
        interacciones_medias = (np.array(interacciones[:-1]) + np.array(interacciones[1:])) / 2
        return interacciones_medias, tasa_cambio

    # Método para graficar todas las gráficas en subgráficas
    def graficar_todas(self):
        # Crear figura y ejes para las subgráficas
        fig, axs = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle('Resultados del Algoritmo BFOA')

        # Gráfico 1: Fitness vs Iteración suavizado
        interacciones, fitness, fitness_suavizado = self.graficar_fitness_vs_interaccion_suavizado()
        axs[0, 0].plot(interacciones, fitness, 'o-', color='b', label='Fitness Original')
        axs[0, 0].plot(interacciones, fitness_suavizado, '-', color='r', label='Fitness Suavizado')
        axs[0, 0].set_title('Fitness vs Iteración (Suavizado)')
        axs[0, 0].set_xlabel('Iteración')
        axs[0, 0].set_ylabel('Fitness')
        axs[0, 0].legend()

        # Gráfico 2: NFE vs Iteración logarítmico
        interacciones, nfe = self.graficar_nfe_vs_interaccion_log()
        axs[0, 1].plot(interacciones, nfe, 's-', color='r', label='NFE')
        axs[0, 1].set_title('NFE vs Iteración')
        axs[0, 1].set_xlabel('Iteración')
        axs[0, 1].set_ylabel('NFE')
        axs[0, 1].set_yscale('log')
        axs[0, 1].legend()

        # Gráfico 3: Fitness y NFE vs Iteración en ejes diferentes
        interacciones, fitness, nfe = self.graficar_fitness_y_nfe_vs_interaccion_dual()
        ax1 = axs[1, 0]
        ax1.plot(interacciones, fitness, 'o-', color='b', label='Fitness')
        ax1.set_title('Fitness y NFE vs Iteración')
        ax1.set_xlabel('Iteración')
        ax1.set_ylabel('Fitness')
        ax1.tick_params(axis='y', labelcolor='b')

        ax2 = ax1.twinx()
        ax2.plot(interacciones, nfe, 's-', color='r', label='NFE')
        ax2.set_ylabel('NFE', color='r')
        ax2.tick_params(axis='y', labelcolor='r')
        ax1.legend()

        # Gráfico 4: Tasa de Cambio de Fitness
        interacciones_medias, tasa_cambio = self.graficar_tasa_cambio_fitness()
        axs[1, 1].plot(interacciones_medias, tasa_cambio, 'o-', color='g', label='Tasa de Cambio de Fitness')
        axs[1, 1].set_title('Tasa de Cambio de Fitness entre Iteraciones')
        axs[1, 1].set_xlabel('Iteración')
        axs[1, 1].set_ylabel('Tasa de Cambio de Fitness')
        axs[1, 1].legend()

        # Ajustar el layout
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()