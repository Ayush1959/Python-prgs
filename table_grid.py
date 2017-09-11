def tables_grid (n):
    k=range(0,n+1,1)
    r=range(1,n+1,1)
    t_s=[]
    for l in k:
        print ("{:3}".format(l),end="   ")
    print ("")
    for j in r:
        print ("{:3}".format(j),end="   ")
        for i in r:
            t=(i * j)
            print ("{:3}".format(t),end="   ")
        print("")
       
