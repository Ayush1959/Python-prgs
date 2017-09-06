def smallest_in (l):
    tmp = l[0]
    for i in l[1:]:
        if i < tmp:
            tmp = i
    return tmp
