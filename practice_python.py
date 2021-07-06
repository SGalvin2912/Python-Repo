class User:
    def __init__(self, name, email_address):# now our method has 2 parameters!
        self.name = name			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python
def make_deposit(self, amount):
    self.account_balance += amount
guido.make_deposit(100)