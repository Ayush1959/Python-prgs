def fizzbizz(n):
    r=range (1,n+1,1)
    for i in r:
        if i % 15 == 0:
             print("fizzbizz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("bizz")
        
        else:
            print("{}".format (i))
            
        
