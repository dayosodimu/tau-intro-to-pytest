def test_one_plus_one():
    assert 1 + 1 ==2

# ------------------
# Atest function to show assertion introspection
#-------------------

def test_one_plus_two():
    a = 1 
    b = 2
    c = 3
    assert a + b == c

# ------------------
# A test function that verifies an exception 
#-------------------

def test_divide_by_zore():
    num = 1 / 0
    