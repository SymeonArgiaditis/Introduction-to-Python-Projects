class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
        if self.get_balance() < amount:
            return False
        else:
            self.ledger.append({'amount': -amount, 'description': description})
            return True
    
    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        title = self.name.center(30,'*') + '\n'
        total = f"Total: {self.get_balance()}"
        
        entries = ''
        for item in self.ledger:
            description = item['description'][:23].ljust(23)
            amount = f"{item['amount']:.2f}".rjust(7)
            entries += f"{description}{amount}\n"

        return title + entries + total

#Function to create Spending Percentage Graph, based on spending
def create_spend_chart(categories):
    spends = []
    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spends.append(spent)
    total_spent = sum(spends)
    
    percents = [int((spend / total_spent) * 100) // 10 * 10 for spend in spends]
    
    chart = "Percentage spent by category\n"
    
    for i in range(100, -1, -10):
        line = str(i).rjust(3) + "|"
        for percent in percents:
            line += " o" if percent >= i else "  "
            line += " " 
        chart += line + "\n"
    
    chart += "    " + "-"*(len(categories)*3 + 1) + "\n"
    
    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        line = "     "
        for category in categories:
            if i < len(category.name):
                line += category.name[i] + "  "
            else:
                line += "   "
        if i != max_len - 1:
            line += "\n"
        chart += line

    return chart

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

print(create_spend_chart([food, clothing]))