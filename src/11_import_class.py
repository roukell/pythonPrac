import modules.shape as shape
import modules.car as car

s1 = shape.Square()
s2 = shape.Square(2, 1, 2)
print(s2)

s2.move(0, 3)
print(s2)

c1 = shape.Circle()
c2 = shape.Circle(5, 15, 20)
print(c2)

car1 = car.Car("Lexus", "RX350", "white")
car2 = car.Car("Lexus", "LM600", "black")
print(car1)
print(car2)
