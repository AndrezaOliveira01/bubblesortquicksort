# Importacoes
import random
import time
import matplotlib.pyplot as plt

# Funcao de lista de numeros aleatorios
def lista_aleatoria(tamanho):
    return [random.randrange(1, 100, 1) for i in range(tamanho)]

# Funcao ordenacao Bubble Sort
def bubble_sort(lista):
    itens = len(lista) - 1
    ordenacao = False
    while not ordenacao:
        ordenacao = True
        for i in range(itens):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                ordenacao = False
    return lista

# Funcao de tempo de Execucao do Bubble Sort
def tempo_bubble_sort(tamanho):
    lista = lista_aleatoria(tamanho)
    t0 = time.perf_counter()
    bubble_sort(lista)
    t1 = time.perf_counter()
    return t1 - t0

# Gerar dados para o gráfico
tamanhos = list(range(10, 9990, 20))
tempos = [tempo_bubble_sort(tamanho) for tamanho in tamanhos]

# Plotar o gráfico
plt.plot(tamanhos, tempos, marker='o', linestyle='-')
plt.title('Bubble Sort Performance')
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Tempo (s)')
plt.grid(True)
plt.show()