import logging
from logician.stdlog.configurator import StdLoggerConfigurator
from logician.configurators.env import EnvListLC

base_logger = logging.getLogger(__name__)

logger = EnvListLC(
    ["ATM"],
    StdLoggerConfigurator(level=logging.DEBUG)
).configure(base_logger)

class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions=[]
    
    def deposit(self,amount):
        logger.trace(f"making a deposit: {amount}")
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
            logger.debug(f"Deposited: {amount} ")
            logger.success(f"Successfully deposited New balance: {self.balance}")
        else:
            logger.error("Deposit amount must be positive.")
    def withdraw(self,amount):
        logger.trace(f"making a withdrawl: {amount}")
        if amount >0:
            if amount <=self.balance:
                self.balance -=amount
                self.transactions.append(f"Withdrew: {amount}")
                logger.debug(f"whithdrew: {amount} ")
                logger.success(f"Successfully withdrew New balance: {self.balance}")
            else:
                logger.error("Insufficient funds for withdrawal.")
        else:
            logger.error("Invalid amount")
    
    def get_balance(self):
        logger.trace(f"checking balance: {self.balance}")
        logger.notice(" checking Current balance")
        logger.success(f"Current balance is: {self.balance}")
        return self.balance
    
    def Statement(self):
        logger.trace("Generating transaction statement.")
        logger.notice("Generating Transaction Statement:")
        with open("statement.txt", "w") as file:
            for transaction in self.transactions:
                file.write(transaction + "\n")
        logger.success("Transaction statement generated successfully.")
    
def main():
    logger.trace("Starting the ATM application.")
    atm = ATM()
    while True:
        print("\nWelcome to the ATM!")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Print Statement")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        logger.debug(f"User selected option: {choice}")
        
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
    logger.trace("ATM application has been terminated.")

if __name__ == "__main__":
    main()