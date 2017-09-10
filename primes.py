def primes (n):
    r=range(2,n+1,1)
    for i in r:
        if i == 2:
            print (2)
        
        elif i == 3:
            print (3)
        
        elif i == 5:
            print (5)
        
        elif i == 7:
            print (7)
        
        if i % 2 == 0:
            pass
        elif i % 3 ==0:
            pass
        elif i % 5 ==0:
            pass
        elif i % 7 ==0:
            pass
              
        else:
           print (i)
