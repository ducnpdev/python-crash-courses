class Dog():
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        print("init")
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command.""" 
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)

my_dog.sit()

# your_dog = Dog('lucy', 3)

