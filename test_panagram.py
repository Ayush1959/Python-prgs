import panagram

def test_panagram():
    c=panagram.panagram("the quick brown fox jumps over the lazy dog")
    expected_output= True
    assert c == expected_output

def test_nxtpanagram():
    c=panagram.panagram("jived fox nymph grabs quick waltz")
    ex = True
    assert c == ex

def test_er():
    c=panagram.panagram("the quick")
    e=False
    assert c == e
