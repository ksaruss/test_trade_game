from accounting import Accounting
from base_value import BaseValue
from money import Money
from corn import Corn
from milk import Milk


class Values:
    def __init__(self):
        self._res: [str, BaseValue] = {'money': Money(),
                                       'corn': Corn(),
                                       'milk': Milk()
                                       }
        self.accounting: 'Accounting' = Accounting()

    def get_list_resources(self):
        list_res = {}
        for name_res in self._res:
            list_res[name_res] = self._res[name_res].get_info()
        return list_res

    def get_assets(self):
        assets = 0
        for name_res in self._res:
            assets += self._res[name_res].get_cost()
        return round(assets, 2)

    def create(self, name_value: str, quantity: int, cost: float = 1.0):
        add_value: BaseValue = self._res[name_value]
        add_value.add_value(quantity, cost)
        self.accounting.add_capital_stock(add_value, quantity, cost)

    def trade(self, type_: str, value_one: str, quantity: int, price: float, value_two: str):
        one: BaseValue = self._res[value_one]
        two: BaseValue = self._res[value_two]

        if two.check_sufficiency(quantity, price):
            if one.get_type() == 'product' and two.get_type() == 'money' and type_ == 'buy':
                b = two.delete_value(quantity, price)
                one.add_value(quantity, b['cost_all'])
            elif one.get_type() == 'product' and two.get_type() == 'money' and type_ == 'sell':
                b = one.delete_value(quantity)
                two.add_value(quantity, price)
                # print(f'financial result {round(quantity * price - b["cost_all"], 2)}')
                self._financial_result += round(quantity * price - b["cost_all"], 2)
            elif one.get_type() != 'money' and two.get_type() != 'money' and type_ == 'buy':
                b = two.delete_value(quantity * price)
                one.add_value(quantity, b['cost_all'])
            else:
                raise Exception(f'not screenplay {one.get_type()}, {two.get_type()}, {type_}')
        else:
            raise Exception(f'not res {two.get_name()}')
