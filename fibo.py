def fibo (x):
    a = 1
    b = 1
    c = 0
    for elem in range (x):
        print (a)
        c = a + b
        a = b
        b = c


fibo(5)
