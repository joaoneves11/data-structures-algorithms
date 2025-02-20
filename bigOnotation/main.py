#fala sbre escabalidade e não necessariamente sobre perfomance
#medir a complexidade temporal e espacial de u algoritmo
#temporal: quanto tempo o algoritmo demora para executar
#espacial: quanto de memória o algoritmo precisa para executar

#O(1) - tempo: constante - independente da quantidade de dados 
#O(n) - tempo: linear - proporcional a quantidade de dados - memoria também é linear
#O(n^2) - tempo: quadrático - proporcional ao quadrado da quantidade de dados 
#O(log n) - tempo: logarítmico - proporcional ao logaritmo da quantidade de dados 
    #quando dobrar o input, não necessaraimente dobra o tempo de execução
    #log2(10) -> 3.32
    #log2(20) -> 4.32
    #log2(40) -> 5.32

#O(n log n) - tempo: linearitmico - proporcional a quantidade de dados multiplicado pelo logaritmo da quantidade de dados 
    #sorting (quicksort, mergesort)
    #divide and conquer

#O(2^n) - tempo: exponencial - proporcional a 2 elevado a quantidade de dados 
    # for i in arr
        # for j in arr
    #para cada item do array ele checka todos os outros itens do array
