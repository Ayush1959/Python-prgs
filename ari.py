def ari (filename):
    f=open(filename)
    nwords = 0
    nchars = 0
    reading_level={ 1: 'Kintergarden',
                    2: 'First grade',
                    3: 'second grade',
                    4: 'third grade',
                    5: 'fourth grade',
                    6: 'fifth grade',
                    7: 'sith grade',
                    8: 'seventh grade',
                    9: 'eigth grade',
                    10: 'nineth grade',
                    11: 'tenth grade',
                    12: 'eleventh grade',
                    13: 'tewelveth grade',
                    14: 'college'}
    content=f.readlines()
    f.close()
    l=len(content)
    for i in content:
        words = i.split(" ")     
        nwords = nwords + len(words)
        nchars = nchars + len(i)
    a= nchars / nwords
    b= nwords / l
    ari= 4.71 * (nchars/nwords) + 0.5 * (nwords/l) - 21.43
    import math
    e=math.ceil(ari)
    if e > 14:
        print("Automatic readability index gives a score above 14,so the book is readable by college students")
    else:
        t=reading_level[e]
        print("Automatic readability index gives a score of {},so the book is readable by {} students".format(e, t ))
