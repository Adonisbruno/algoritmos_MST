Modelo de entrada PRIM e DIJKSTRA
	python main.py entrada.txt "PRIM | DIJK" > saida.txt
onde:
	PRIM - PRIM
	DIJK - DIJKSTRA

Exemplo: Exemplo: python mainPRIM-DIJKSTRA.py instancias_Dijkstra_e_PRIM/dij10.txt DIJK > saidaPD.txt"


Arquivo de entrada deve ser no formato:
10
270 3179 2991 2840 3031 3421 3738 4947 6226 
2903 2715 2564 2755 3144 4153 5362 6641
504 655 908 1299 2237 3446 3682
151 423 723 2040 3249 3485
272 571 1888 3098 3334 
241 1560 2770 3006 
1617 2827 3063 
1274 1510 
236 

Onde 10 é a ordem da matriz (10x10)
E os demais elementos é a matriz superior da Matriz de Adjacências.
O exemplo de arquivo acima, resulta na matriz de adjacência abaixo:

[[   0  270 3179 2991 2840 3031 3421 3738 4947 6226]
 [ 270    0 2903 2715 2564 2755 3144 4153 5362 6641]
 [3179 2903    0  504  655  908 1299 2237 3446 3682]
 [2991 2715  504    0  151  423  723 2040 3249 3485]
 [2840 2564  655  151    0  272  571 1888 3098 3334]
 [3031 2755  908  423  272    0  241 1560 2770 3006]
 [3421 3144 1299  723  571  241    0 1617 2827 3063]
 [3738 4153 2237 2040 1888 1560 1617    0 1274 1510]
 [4947 5362 3446 3249 3098 2770 2827 1274    0  236]
 [6226 6641 3682 3485 3334 3006 3063 1510  236    0]]