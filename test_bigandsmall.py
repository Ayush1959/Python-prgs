import bigandsmall

def test_big():
    c=bigandsmall.big([1,5,8,6,4])
    ex = 8
    assert c == ex

def test_small():
    c=bigandsmall.small([5,4,2,9,1,6])
    e = 1
    assert c == e
