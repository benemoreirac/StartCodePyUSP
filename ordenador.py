import random
class Ordenador:

    def cria_lista(self):
        lista = list(range(1,100))
        random.shuffle(lista)
        return lista
     
    def selecao_direta(self, lista):
        
        fim = len(lista)

        for i in range(fim - 1):
            #Inicialmente, o menor elemento ja visto e o i-esimo
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j]<lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            #coloca o menor elemento encontrado no inicio da sub-lista
            #para isso, troca de lugar os elementos nas posicoes i e posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
