from search import *

def test_readfile() :
    assert readfile("text_example_1.txt") == ['While the Congress of the Republic endlessly debates', 'this alarming chain of events, the Supreme Chancellor has', 'secretly dispatched two Jedi Knights.']
    assert readfile("text_example_2.txt") == []
    assert readfile("essai.txt") == None
    
def test_get_words() :
    assert get_words("Salut c'est Gérard\n") == ['salut', "cest", 'gérard']
    assert get_words("\n") == []
    assert get_words("") == []
    
def test_create_index() :
    assert create_index("text_example_1.txt") == {'while': {0: 1}, 'the': {0: 2, 1: 1}, 'congress': {0: 1}, 'of': {0: 1, 1: 1}, 'republic': {0: 1}, 'endlessly': {0: 1}, 'debates': {0: 1},
                                                  'this': {1: 1}, 'alarming': {1: 1}, 'chain': {1: 1}, 'events': {1: 1}, 'supreme': {1: 1}, 'chancellor': {1: 1}, 'has': {1: 1},
                                                  'secretly': {2: 1}, 'dispatched': {2: 1}, 'two': {2: 1}, 'jedi': {2: 1}, 'knights': {2: 1}}
    assert create_index("text_example_2.txt") == {}

def test_get_lines() :
    assert get_lines(["the"], create_index("text_example_1.txt")) == [0,1]
    assert get_lines(["the","republic"], create_index("text_example_1.txt")) == [0]
    assert get_lines(["the","LINFO1101"], create_index("text_example_1.txt")) == []
    assert get_lines(["LEPL1401","LINFO1101"], create_index("text_example_1.txt")) == []
    assert get_lines([], create_index("text_example_1.txt")) == []
    assert get_lines(["the"], create_index("text_example_2.txt")) == []
    assert get_lines(["the","republic"], create_index("text_example_2.txt")) == []
    assert get_lines(["the","LINFO1101"], create_index("text_example_2.txt")) == []
    assert get_lines(["LEPL1401","LINFO1101"], create_index("text_example_2.txt")) == []
    assert get_lines([], create_index("text_example_2.txt")) == []
    
def run_tests() :
    test_readfile() 
    test_get_words()
    test_create_index()
    test_get_lines()
    
run_tests()