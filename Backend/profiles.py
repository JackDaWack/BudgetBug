class BudgetProfile:
    def __init__(self, user_id):
        self.user_id = user_id
        self.incomes = {}
        self.expenses = {}
    def add_income(self, amount, source):
        if source in self.incomes:
            self.incomes[source] += amount
        else:
            self.incomes[source] = amount
    def add_expense(self, amount, category):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
