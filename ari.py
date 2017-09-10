def ari (x):
    f=open(x)
    no_words = 0
    charecters = 0
    table={ 1: 'Kintergarden', 2: 'First grade', 3: 'second grade', 4: 'third grade', 5: 'fourth grade', 6: 'fifth grade', 7: 'sith grade', 8: 'seventh grade', 9: 'eigth grade', 10: 'nineth grade', 11: 'tenth grade', 12: 'eleventh grade', 13: 'tewelveth grade', 14: 'college'}
    content=f.readlines()
    l=len(content)
    for i in content:
        words = i.split()     
        no_words = no_words + len(words)
        charecters = charecters + len(i)
    a= charecters / no_words
    b= no_words / l
    c= 4.71 * a + 0.5* b -21.43
    d= round (c)
    if c > d:
        e=d + 1
    else:
        e=d
    if e > 14:
        print("Automatic readability index gives a score above 14,so the book is readable by college students")
    else:
        t=table[e]
        print("Automatic readability index gives a score of {},so the book is readable by {} students".format(e, t ))
