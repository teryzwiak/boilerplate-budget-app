class Category:

    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.history = [None] #amount, descriptifaon

    def __str__(self):
        print(f'*********{self.name}********')
        for x in self.history:
            print(x)
        return "Total: " + str(self.balance)

    def deposit(self, amount, description):
        self.balance = self.balance + amount
        self.history.append(amount)
        self.history.append(description)
        #print(balance)

    def withdraw(self, amount, description=None):
        self.balance = self.balance - amount
        self.history.append(-amount)
        self.history.append(description)

    def get_balance(self):
        balance = self.balance
        return str(balance)
    
    def transfer(self, amount, category):
        category.deposit(amount, "transfer")




def create_spend_chart(categories):
    print(categories)