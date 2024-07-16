from base_value import BaseValue


class Money(BaseValue):
    def __init__(self):
        super().__init__()
        self._name = 'money'
        self._type = 'money'

    def add_value(self, quantity, cost=1):
        r = quantity * cost
        self._quantity += r
        self._cost += r
        return {'type': 'add', 'name': self.get_name(), 'quantity': quantity}

    def delete_value(self, quantity, cost=0):
        if self._quantity < quantity * cost:
            raise Exception(f'not resources {self.get_name()}')
        elif self._quantity == quantity:
            cost_all = self._cost
            self._quantity = 0
            self._cost = 0
        else:
            cost_all = round(quantity * cost, 2)
            self._quantity = round(self._quantity - cost_all, 2)
            self._cost = round(self._cost - cost_all, 2)
        return {'type': 'delete', 'name': self.get_name(), 'cost_one': 1, 'cost_all': cost_all}