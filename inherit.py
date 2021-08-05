listtt=[]
class Student():

    def __init__(self, name,roll):
        self.name = name
        self.roll = roll
        
    def getName(self):
        return self.name
    def getRoll(self):
        return self.roll      

class Marks(Student):
    def __init__(self, maths,english):
        self.maths = maths
        self.english = english
    def getMaths(self):
        return self.maths
    def getEnglish(self):
        return self.english       
        
def add(n, r, m, e):
    dictionary = {"name": n, "roll": r, "maths": m, "english": e}
    listtt.append(dictionary)



x = Student("Geek2",123) # An Object of Employee
y = Marks(12, 22)
add(y.getName(), y.getRoll(), y.getMaths(), y.getEnglish())

print(listtt)



