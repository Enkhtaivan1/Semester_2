X = 5
def foo():
    Y = 10
    print(X+Y)

def bar():
    x = 7
    foo()

bar()
print(X)