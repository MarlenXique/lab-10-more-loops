def move(f,t): #from,to.A value passed to a function (or method) when calling the function.
    print("move from {} to {}".format(f,t)) #.format is amethod because of the dot. ots a strong, class of data.
move("A","C")
def moveVia(f,v,t): #from,via,to.
    move(f,v) #function call to move(): move from step1 to step 2 (out of 3)
        #at first the destinations is v
    move(v,t) # move from step 2 to step 3 (out of 3)
        #now, the origin is v, and the desitination is t
def hanoi(n,f,h,t):
    #n: number of discs
    #f: front postion
    #h: helper position
    #t: target pposition
    if n==0:
        pass #this is the BASE CASE. termination condition
    else:
        hanoi(n-1,f,t,h) #functon call within the function definition (the recursion)!
        move(f,t)
        hanoi(n-1,h,f,t)
hanoi(4,"A","B","C")

# based on a tutorial by Professor Thorsten Altenkirch
