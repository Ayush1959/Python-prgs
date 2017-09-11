def freq1 (n):
    letter={}
    for i in n:
            letter[i]=0
    for i in n:
        letter[i] = letter[i] +1
    return letter
