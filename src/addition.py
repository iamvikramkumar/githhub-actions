# app.py
# This is a test commit
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0


# use add function and print result
print(add(1, 2))

# use mul function and print result
print(mul(1, 2))