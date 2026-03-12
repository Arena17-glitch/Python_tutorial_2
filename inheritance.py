class Person:
    def __init__(self,id,name):
        print("Object created! ")
        self.id = id
        self.name = name

class Student(Person):
    def __init__(self, id, name, sem, mark1, mark2):
        Person.__init__(self, id, name)
        self.sem = sem
        self.mark1 = mark1
        self.mark2 = mark2

    def avrmarks(self):
        total = self.mark1 + self.mark2
        avg = total / 2
        print("Average Marks: ", avg)
        print()

    def getdata(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Sem: ", self.sem)
        print("Marks1: ", self.mark1)
        print("Marks2: ", self.mark2)

    def __del__(self):
        print("Object Destroyed!")

# --- test code -----------------------------------------------------
if __name__ == "__main__":
    x = Student(1, "Swayam", 2, 60, 60)
    x.getdata()
    x.avrmarks()
    y = Student(2, "Swayam", 1, 80, 90)
    y.getdata()
    y.avrmarks()