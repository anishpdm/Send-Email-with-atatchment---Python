list=[0,1,2,3,4,5,6,100,99,101,933,124,86,1313]

def f1():
    filter(5,list)

def f2():
    n=0
    while n <= len(list):
        if(list[n] == 5):
            pass
            break
        else:
            pass
        n=n+1

if __name__ == "__main__":
    import timeit    
    print (timeit.timeit(f1, number=1000000))
    print (timeit.timeit(f2, number=1000000))