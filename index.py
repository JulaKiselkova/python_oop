class Matter():
    id = 333
    low = 'people'

    def setID(self, newID):  # метод экземпляра
        self.id = newID

    def setLow(self, newLow):  # метод экземпляра
        self.low = newLow

    @staticmethod
    def getInfo():  # статик метод подразумевает отсутвие self?
        print(f"My number is {Matter.id}. The main low {Matter.low}.")


milky_way = Matter()
milky_way.setID(555)
print(milky_way.id)
milky_way.getInfo()

# 2


class Car:
    brand = 'Kia'
    isWork = True

    def __init__(self, model, year, speed):  # атрибуты экземпляра
        self.model = model
        self.year = year
        self.__speed = speed

    def getSpeed(self):
        return self.__speed

    def setSpeed(self, newSpeed):
        self.__speed = newSpeed

    def isGood(self):
        if(self.year >= 2015 and self.__speed >= 140):
            # return True
            self.isWork = True
            return True
        else:
            self.isWork = False
            return False

    @staticmethod
    # статик метод подразумевает отсутвие self? The model {Car.model} {Car.year}. Max speed is {Car.__speed}.
    def getInfo():
        print(
            f"The brand is {Car.brand}. The car is {Car.isWork}")  # мы не можем в статик методе взаимодействовать с атрибутами экземпляра?

    @staticmethod
    def getArrOfInfo():
        return {'brand': Car.brand, 'isWorking': Car.isWork}

    @classmethod
    # def classmethod(cls, newBrand, newModel, newYear):
    def example1(cls):
        return cls('s', 2010, 150)


newCar = Car('Rio', 2015, 170)
newCar2 = Car.example1()
print(newCar2.model)

newCar2.setSpeed(700)
print(newCar2.getSpeed())
# если атрибут класса меняется у экземпляра, то он меняется и у каждого представителя класса?
print(newCar2.isGood())
print(newCar.isWork)
newCar2.getInfo()
