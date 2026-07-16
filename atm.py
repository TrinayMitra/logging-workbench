import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log")

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(funcName)s | %(message)s"
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions=[]
    
    def deposit(self,amount):
        if amount > 0:
            self.balance = amount
            self.transactions.append(f"Deposited: {amount}")
            logger.info(f"Deposited: {amount} And New Balance is : {self.balance}")
        else:
            logger.warning("Deposit amount must be positive.")
    def withdraw(self,amount):
        if amount >0:
            if amount <=self.balance:
                self.balance -=amount
                self.transactions.append(f"Withdrew: {amount}")
                logger.info(f"whithdrew: {amount} And New Balance is : {self.balance}")
            else:
                logger.warning("Insufficient funds for withdrawal.")
        else:
            logger.warning("Withdrawal amount must be positive.")
    
    def get_balance(self):
        logger.info(f"Current balance is: {self.balance}")
        return self.balance
    
    def Statement(self):
        logger.info("Transaction Statement:")
        with open("statement.txt", "w") as file:
            for transaction in self.transactions:
                file.write(transaction + "\n")
    
def main():
    atm = ATM()
    while True:
        print("\nWelcome to the ATM!")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Print Statement")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(amount)
            except ValueError:
                logger.exception("Invalid input. Please enter a valid number.")
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            except ValueError:
                logger.exception("Invalid input. Please enter a valid number.")
        elif choice == '3':
            balance = atm.get_balance()
            logger.info(f"Current balance is: {balance}")
            print(f"Current balance: {balance}")
        elif choice == '4':
            logger.info("Printing transaction statement.")
            atm.Statement()
        elif choice == '5':
            logger.info("Exiting the ATM.")
            break
        else:
            logger.warning("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()