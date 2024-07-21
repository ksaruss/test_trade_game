import copy

from base_value import BaseValue


class Accounting:
    def __init__(self):
        self.accounting_book = {'capital': 0,
                                'equipment': 0,
                                'cash': 0,
                                'accounts_receivable': 0,
                                'inventory': 0,
                                'foreign_currency': 0,

                                'capital_stock': 0,
                                'equity_capital': 0,
                                'accounts_payable': 0,

                                'financial_result': 0,
                                }

    def start_accounting(self):
        pass

    def get_accounting_book(self, list_values: dict[str, 'BaseValue']):
        book = copy.deepcopy(self.accounting_book)
        for name_value in list_values:
            f = [list_values[name_value].get_type(), list_values[name_value].get_cost()]
            if f[0] == 'money':
                book['cash'] += f[1]
            elif f[0] == 'product':
                book['inventory'] += f[1]
            elif f[0] == 'foreignCurrency':
                book['foreign_currency'] += f[1]
        return book

    def add_capital_stock(self, quantity: int, cost: float):
        self.accounting_book['capital_stock'] += quantity * cost

    def add_financial_result(self, quantity):
        self.accounting_book['financial_result'] += quantity

