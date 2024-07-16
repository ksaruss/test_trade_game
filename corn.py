from base_value import BaseValue


class Corn(BaseValue):
    def __init__(self):
        super().__init__()
        self._name = 'corn'
        self._type = 'product'
