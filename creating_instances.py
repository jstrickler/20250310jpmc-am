from datetime import date

cities = list()   # list cities = new list();

x = 5   #  int x = new int(5);

cities.append('Durham')

today = date.today()
print(f"{today.year = }")

class Dog:
    def bark(self):
        print("woof! woof!")

d1 = Dog()   #  Dog d1 = new Dog();
d2 = Dog()
d1.bark()
d2.bark()