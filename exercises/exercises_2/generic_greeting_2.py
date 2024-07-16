class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @classmethod
    def generic_greeting(cls):
        print("Hello! I'm a cat")

    def personal_greeting(self):
        print(f"Hello! My name is {self.name}")



kitty = Cat('Sophie')

# Comments show expected output
Cat.generic_greeting()        # Hello! I'm a cat!
kitty.personal_greeting()     # Hello! My name is Sophie!

