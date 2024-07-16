# greet() -> prints name and color
# Cat class has a default color constant
# Cat initializer uses the color constant to set the color of the instance

class Cat():
    DEFAULT_COLOR = 'purple'

    def __init__(self, name):
        self._name = name
        self._color = Cat.DEFAULT_COLOR

    def greet(self):
        print(f"Hello! My name is {self._name} and I'm a {self._color} cat")

kitty = Cat('Sophie')
kitty.greet()