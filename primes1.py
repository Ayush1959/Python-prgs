def primes1 (n):
    r=range(2,n+1,1)
    set1=set()
    cancelled=set()
    for i in r:
        set1.add(i)
        for j in r:
            s=i*j
            if s not in cancelled:
                cancelled.add(s)
    d= set1 - cancelled
    return d
