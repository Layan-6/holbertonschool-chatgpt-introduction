class Checkbook:
    def __init__(self):
        """
        Initialize a Checkbook with zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.
        
        Parameters:
        amount (float): The amount to deposit
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook.
        
        Parameters:
        amount (float): The amount to withdraw
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to run the checkbook application.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            print("Goodbye!")
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    print("Error: Deposit amount must be positive.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Error: Please enter a valid numeric amount.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    print("Error: Withdrawal amount must be positive.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Error: Please enter a valid numeric amount.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
