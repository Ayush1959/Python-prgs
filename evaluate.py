def evaluate (post_fix_string):
    l=[]
    for i in post_fix_string:
        try:
            if i.isdigit():
                l.append(i)
            else:
                t=int(l.pop())
                s=int(l.pop())
                import operator
                ops = { '+' : operator.add,
                    '-' : operator.sub,
                    '*' : operator.mul,
                    '/' : operator.truediv,
                    '%' : operator.mod,
                    '^' : operator.xor
                   }
                z=ops[i](t,s)
                l.append(z)
        except IndexError:
                    print ("Expression Error")
    
    
    return l

