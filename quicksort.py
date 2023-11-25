import random
import time
import matplotlib.pyplot as plt

# Função de lista de números aleatórios
def lista_aleatoria(tamanho):
    return [random.randrange(1, 100, 1) for _ in range(tamanho)]

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

# Função de tempo de Execução do Quick Sort
def tempo_quick_sort(tamanho):
    lista = lista_aleatoria(tamanho)
    t0 = time.perf_counter()
    quick_sort(lista)
    t1 = time.perf_counter()
    return t1 - t0

# Gerar dados para o gráfico
tamanhos = list(range(10, 9990, 20))
tempos = [tempo_quick_sort(tamanho) for tamanho in tamanhos]

# Plotar o gráfico
plt.plot(tamanhos, tempos, marker='o', linestyle='-')
plt.title('Quick Sort Performance')
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Tempo (s)')
plt.grid(True)
plt.show()