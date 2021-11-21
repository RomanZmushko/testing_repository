def fibo (x):
    a,b,c = 1, 1, 0
    for elem in range (x):
        print (a)
        c = a + b
        a = b
        b = c


fibo(5)
