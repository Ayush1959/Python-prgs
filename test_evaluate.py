import evaluate

def test_add():
    c=evaluate.evaluate("545++")
    e=[14]
    assert c == e

def test_sub():
    csub = evaluate.evaluate("455-+")
    esub = [4]
    assert csub == esub

def test_mul():
    cmul = evaluate.evaluate("5455-+*")
    emul = [20]
    assert cmul == emul

def test_div():
    cdiv = evaluate.evaluate("45455-+*/")
    ediv = [0.2]
    assert cdiv == ediv
