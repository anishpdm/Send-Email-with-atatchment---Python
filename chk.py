import timeit
def hello():
    print("hello")
def f1():
    for n in range(100):
        pass
v='''print('hello)'''
x='''x=(10+15)*10'''
# print("The time taken is ",timeit.timeit(stmt=x))
print(timeit.timeit(f1, number=100000))
print (timeit.timeit(hello,number=1))
print (timeit.timeit(v,number=1))

