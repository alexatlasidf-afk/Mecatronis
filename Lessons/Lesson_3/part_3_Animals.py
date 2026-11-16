
class Animal:
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.pat_counter = 0


    def pat(self):
        self.pat_counter += 1

    def speak(self):
        print(" * ")


class Cat(Animal):

    def speak(self):
        print(f"{self.name} meows")

    def pat(self):
        super().pat() 
        if self.pat_counter % 3 == 0:
            print("prrrr")
        else:
            print("...")

class Dog(Animal):

    def __init__(self, name, color, chip_id):
        super().__init__(name,color)
        self.dog_id = chip_id

    def pat(self):
        super().pat()
        if self.pat_counter % 2 == 0:
            print(" Happy Dog ")  
        else:
            print(f'{self.name} begs for more ')      


    def speak(self):
        print("Hav Hav")


#מריץ את הקובץ כולל שורות בדיקה
#בקבצים אחרים שעשינו "אאימפורט" לחיות הבדיקה לא תעבוד


if __name__ == '__main__':
    cat1 = Cat("miki", "grey")
    dog1 = Dog("Chiki","white","555")

    cat1.pat()
    cat1.speak()

    dog1.pat()
    dog1.speak()
    


