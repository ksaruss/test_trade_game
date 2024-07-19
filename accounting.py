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

    def add_capital_stock(self, name_value: 'BaseValue', quantity: int, cost: float):
        if name_value.get_type() == 'money':
            self.accounting_book['cash'] += quantity
        elif name_value.get_type() == 'product':
            self.accounting_book['inventory'] += quantity * cost
        self.accounting_book['capital_stock'] += quantity * cost

    def get_accounting_book(self):
        return self.accounting_book

    
