from base_value import BaseValue


class Milk(BaseValue):
    def __init__(self):
        super().__init__()
        self._name = 'milk'
        self._type = 'product'


