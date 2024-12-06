class parrot:
    species = "bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sing(self,song):
        return self.name + " sings " +song 
    def dance(self):
        return self.name + " is dancing"
    
obj1=parrot("blu",2.5)
print(obj1.sing("happy"))
print(obj1.dance())





