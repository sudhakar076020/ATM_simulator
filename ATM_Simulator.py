# ATM Simulator

class BankAccount:
    def __init__(self):
        self.__user_current_pin = 7602      # Private PIN
        self.__current_balance = 1000      # Private Balance

    # Private method to check PIN
    def __check_pin(self, pin):
        return pin == self.__user_current_pin

    # Public method to show balance
    def show_balance(self):
        print(f"Your current balance is: {self.__current_balance}")

    # Public method to deposit
    def deposit(self):
        try:
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                self.__current_balance += amount
                print(f"Deposit amount is: {amount}")
                print(f"Your current balance is: {self.__current_balance}")
            else:
                print("Enter a positive amount.")
        except ValueError:
            print("Please enter a valid number.")

    # Public method to withdraw
    def withdraw(self):
        try:
            amount = float(input("Enter withdraw amount: "))
            if amount > self.__current_balance:
                print("Insufficient balance!")
            elif amount <= 0:
                print("Enter a positive amount.")
            else:
                self.__current_balance -= amount
                print(f"Withdraw amount is: {amount}")
                print(f"Your current balance is: {self.__current_balance}")
        except ValueError:
            print("Please enter a valid number.")

    # Public ATM menu system
    def start_atm(self):
        pin_attempt = 3

        while pin_attempt > 0:
            try:
                user_input_pin = int(input("Enter your 4-digit pin: "))
                if self.__check_pin(user_input_pin):
                    print("Access granted!")
                    while True:
                        print("\nMenu:\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
                        try:
                            choice = int(input("Enter option: "))
                            if choice == 1:
                                self.show_balance()
                            elif choice == 2:
                                self.deposit()
                            elif choice == 3:
                                self.withdraw()
                            elif choice == 4:
                                print("Thank you! Exiting...\nATM session ended. Have a nice day!")
                                break
                            else:
                                print("Invalid option")
                        except ValueError:
                            print("Please enter an option from 1 to 4")
                    break
                else:
                    pin_attempt -= 1
                    print(f"Wrong pin! Attempts left: {pin_attempt}")
            except ValueError:
                print("Please enter numbers only")


# Run the ATM
atm = BankAccount()
atm.start_atm()
