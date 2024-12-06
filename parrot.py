class parrot:
    species = "bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age
obj1=parrot("blu",2.5)
obj2=parrot("woo",4.5)
print("blu is a",obj1.species)
print("woo is a",obj2.species)
print(obj1.name,"is",obj1.age,"years old")
print(obj2.name,"is",obj2.age,"years old")



