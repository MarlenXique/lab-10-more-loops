def move(f,t):
    print("move from {} to {}".format(f,t))
move("A","C")
def moveVia(f,v,t):
    move(f,t)
    move(v,t)
moveVia("A","B","C")
def foo(x):
    foo(x)
def hanoi(n,f,h,t):
    if n==0:
        pass
    else:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)
hanoi(4,"A","B","C")
