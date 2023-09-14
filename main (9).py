class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print('Deposited rs.{}.New Balance:rs.{}'.format(amount,
                                                       self.__account_balance))
    else:
      print('Invalid deposit Amount.please deposit a   positive Amount')

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdrew rs.{}.New Balance:rs.{}".format(amount,
                                                      self.__account_balance))
    else:
      print("Invalid Withdrawal amount or insufficient balance")

  def display_balance(self):
    print("Account balance for{}(Account#{}):rs.{}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))


#create an instance of the bamk account class
account= BankAccount(account_number="12345678",
                      account_holder_name="Ajee",
                      initial_balance=5000.00)
#test deposit and withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()
