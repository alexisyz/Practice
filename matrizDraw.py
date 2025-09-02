def one(i): #Diagonal principal.
    m[i][i] = 1
    return

def two(i, n):  #Inversa.
    m[i][(n-i)-1] = 1
    return

def three(i, n): #Bordes laterales.
    m[i][0] = 1
    m[i][(n-1)] = 1

def four(i,n): #Bordes superiores.
    m[0][i] = 1
    m[(n-1)][i] = 1

def suma(n):
    mid = int(n/2) #Obtiene la Fila/Columna del central.
    for i in range(n): #Rellena las mitades.
        m[i][mid] = 1
        m[mid][i] = 1


n = int(input())
m = [[0 for _ in range(n)]for _ in range(n)]
u = int(input()) #Opcion.

if u == 1:
    for i in range(n):
        one(i)
elif u == 2:
    for i in range(n):
        two(i,n)
elif u == 3:
    for i in range(n):
        three(i,n)
elif u == 4:
    for i in range(n):
        four(i,n)
elif u == 5:
    for i in range(n):
        four(i,n)
        three(i,n)
elif u == 6:
    suma(n)
elif u == 7:
    for i in range(n):
        one(i)
        two(i,n)
        three(i,n)
        four(i,n)
    suma(n)

for i in range(n): #Iterar matriz para mostrarla.
    s = "" #String que muestra la matriz.
    for j in range(n):
        s = s + str(m[i][j]) #Guardamos numero.
    print(s)
