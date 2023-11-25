import random
import time
import matplotlib.pyplot as plt

# Função de lista de números aleatórios
def lista_aleatoria(tamanho):
    return [random.randrange(1, 100, 1) for _ in range(tamanho)]

# Função ordenação Bubble Sort
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

# Função ordenação Quick Sort
def quick_sort(lista):
    if len(lista) > 1:
        pivo = int(len(lista) / 2)
        valor = lista[pivo]
        esq = [i for i in lista if i < valor]
        meio = [i for i in lista if i == valor]
        dir = [i for i in lista if i > valor]
        res = quick_sort(esq) + meio + quick_sort(dir)
        return res
    else:
        return lista

# Função de tempo de Execução do Bubble Sort
def tempo_bubble_sort(tamanho):
    lista = lista_aleatoria(tamanho)
    t0 = time.perf_counter()
    bubble_sort(lista)
    t1 = time.perf_counter()
    return t1 - t0

# Função de tempo de Execução do Quick Sort
def tempo_quick_sort(tamanho):
    lista = lista_aleatoria(tamanho)
    t0 = time.perf_counter()
    quick_sort(lista)
    t1 = time.perf_counter()
    return t1 - t0

# Gerar dados para o gráfico
tamanhos = list(range(10, 9990, 20))
tempos_bubble_sort = [tempo_bubble_sort(tamanho) for tamanho in tamanhos]
tempos_quick_sort = [tempo_quick_sort(tamanho) for tamanho in tamanhos]

# Plotar o gráfico comparativo
plt.plot(tamanhos, tempos_bubble_sort, marker='o', linestyle='-', label='Bubble Sort')
plt.plot(tamanhos, tempos_quick_sort, marker='o', linestyle='-', label='Quick Sort')
plt.title('Comparação de Performance entre Bubble Sort e Quick Sort')
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Tempo (s)')
plt.legend()
plt.grid(True)
plt.show()
