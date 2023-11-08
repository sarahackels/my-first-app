

from app.my_mod import enlarge

def test_example():
    assert 2+2 == 4

def test_enlarge():
    ##if we pass in the number 10 we expect to get 1000 back
    assert enlarge(10) == 1000