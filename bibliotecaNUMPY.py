import numpy as np
a = np.array([0,1,2,3,4,5,6,7,8,9])
print(a)

b = np.array([[0,1,2,3], [4,5,6,7]])


print(b)
print(b.ndim)
print(b.shape) 
print(len(b))

c = np.arange(0, 1001, 10) #like a range() 3 parâmetros (0 = inicio, 1001 = até onde vai, 10 = passo)
print(c)

d = np.linspace(1, 10, 20) # 1 = inicio, 10 = até onde vai 20 = quantidade de elementos ENTRE 1 e 10
print(d)
# da para incluir endpoint=False para ir de 1 a 9, não incluindo o ultimo valor (10)

#Criando matrizes

e = np.ones((5,8)) #5 = linhas , 8 = colunas 
print(e)

f = np.random.rand(10, 10) #matriz 10x10
print(f)

g = np.eye(3) #cria matriz com elementos 1 na diagonal
print(g)

