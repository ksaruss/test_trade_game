class BaseValue:
    def __init__(self):
        self._quantity = 0
        self._cost = 0
        self._name = 'base_value'
        self._type = 'base_value'

    def get_quantity(self):
        return self._quantity

    def get_cost(self):
        return self._cost

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_cost_one(self):
        if self._quantity == 0:
            return 0
        else:
            return round(self._cost / self._quantity, 2)

    def get_info(self):
        return {'quantity': self.get_quantity(),
                'cost': self.get_cost(),
                'cost_one': self.get_cost_one()}

    def check_sufficiency(self, quantity, price):
        if self._quantity >= quantity * price:
            return True
        return False

    def add_value(self, quantity, cost=1):
        self._quantity += quantity
        self._cost = round(self._cost + cost, 2)
        return {'type': 'add', 'name': self.get_name(), 'quantity': quantity}

    def delete_value(self, quantity, cost=0):
        cost_one = self.get_cost_one()
        if self._quantity < quantity:
            raise Exception(f'not resources {self.get_name()}')
        elif self._quantity == quantity:
            cost_all = self._cost
            self._quantity = 0
            self._cost = 0
        else:
            cost_all = round(self.get_cost_one() * quantity, 2)
            self._quantity -= quantity
            self._cost = round(self._cost - cost_all, 2)
        return {'type': 'delete', 'name': self.get_name(), 'cost_one': cost_one, 'cost_all': cost_all}

    @property
    def type(self):
        return self._type


