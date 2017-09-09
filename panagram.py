def panagram (s):
    y="qwertyuiopasdfghjklzxcvbnm "
    for i in y:
        if i not in s:
            return False
    return True           
    
