class Cat():
    @classmethod
    def generic_greeting(cls):
        print("Hello! I'm a cat")

kitty = Cat()
type(kitty).generic_greeting()