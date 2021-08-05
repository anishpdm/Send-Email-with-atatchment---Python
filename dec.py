def myWrapper(func):
    def myInnerFunc():
        print("Inside wrapper.")
        func()
    return myInnerFunc
 
@myWrapper
def myFunc(x,y):
  print(str(x+y))
 
myFunc(10,2)