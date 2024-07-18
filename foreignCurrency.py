from base_value import BaseValue


class ForeignCurrency(BaseValue):
    def __init__(self):
        super().__init__()
        self._name = 'currency'
        self._type = 'foreignCurrency'

