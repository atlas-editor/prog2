class Laptop:

    def __init__(self, name, processor):
        self.name = name
        self.processor = processor
        self.is_powered_on = False

    def start(self):
        print('Laptop is starting..')
        self.is_powered_on = True

    def restart(self):
        if self.is_powered_on:
            print('Laptop is restarting..')
        else:
            self.start()

    def shutdown(self):
        print('Laptop is shutting down..')
        self.is_powered_on = False

    def details(self):
        if self.is_powered_on:
            print(f'The laptop\'s name is: {self.name}')
            print(f'It has {self.processor} processor.')
        else:
            print('The laptop must be turned on to access details.')


lenovo = Laptop('Lenovo IdeaPad 5', 'Intel Core i7')

lenovo.start()

lenovo.details()

lenovo.shutdown()

lenovo.details()
