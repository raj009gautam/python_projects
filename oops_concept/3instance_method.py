# instance Method 
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} and {self.last_name}"

    def is_above_18(self):
        return self.age>18
  

p1 = Person('Harshit','gautam',14)
p2 = Person('mohit','Gupta',23)
# print(p1.full_name())
# print(p2.full_name())
print(p1.is_above_18())
 


l = [1,2,3.4]

# l.clear()
list.clear(l)
print(l)