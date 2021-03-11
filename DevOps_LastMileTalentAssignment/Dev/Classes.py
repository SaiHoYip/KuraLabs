class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")
#defines blueprints for creating objects


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()
point2 = Point()
#point2 = different object from point 1
point2.x = 30
print(point2.x)