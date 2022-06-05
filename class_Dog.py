class Dog:

    # method for initializing the object with internal data
    def __init__(self, petname, temp):
        self.name = petname
        self.temperature = temp

    # get status
    def status(self):
        print('Dog`s name: ', self.name)
        print('Dog`s temperature: ', self.temperature) 
        pass

    # set the temperature
    def setTemperature(self, temp):
        self.temperature = temp
        pass

    # dogs can bark
    def bark(self):
        print("Bark!")  
        pass
    pass

# create a new dog object based on the class Dog
lassie = Dog('Lassie', 37)
lassie.status()

lassie.setTemperature(40)
lassie.status()
