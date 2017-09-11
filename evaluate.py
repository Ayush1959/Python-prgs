def evaluate (n):
    l=[]
    for i in n:
        if i.isdigit() == True:
            l.append(i)
        else:
            t=int(l.pop())
            s=int(l.pop())
            if i == '+':
                z=t+s
                l.append(z)
            elif i == '-':
                z=t-s
                l.append(z)
            elif i == '*':
                z=t*s
                l.append(z)
            elif i == '/':
                z=t/s
                l.append(z)
            elif i == '%':
                z=t%s
                l.append(z)
            else:
                z="error"
    return l

