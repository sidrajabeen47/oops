from abc import ABC, abstractmethod

# Step 1 & 2: Base Class with Abstraction and Encapsulation
class Payment(ABC):
    def __init__(self, initial_balance):
        # Encapsulation: __balance is private
        self.__balance = initial_balance 

    def get_balance(self):
        return self.__balance

    def _update_balance(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    @abstractmethod
    def pay(self, amount):
        if amount <= 0:
            print("Validation Error: Payment amount must be positive.")
            return False
        print(f"\n[System] Validating request for {amount}...")
        return True

# Step 3, 4 & 5: Inheritance and Polymorphism
class CreditCardPayment(Payment):
    def pay(self, amount):
        # Call base class validation
        if not super().pay(amount):
            return False
        
        fee = amount * 0.02
        total_cost = amount + fee
        
        if self._update_balance(total_cost):
            print(f" Success! Paid {amount} via Credit Card (+{fee} fee).")
            print(f" Remaining Balance: {self.get_balance()}")
            return True
        else:
            print(f" Error: Insufficient funds for Credit Card (Total: {total_cost})")
            return False

class UPIPayment(Payment):
    def pay(self, amount):
        if not super().pay(amount):
            return False
        
        if self._update_balance(amount):
            print(f" Success! Paid {amount} via UPI.")
            print(f" Remaining Balance: {self.get_balance()}")
            return True
        else:
            print(f" Error: Insufficient balance for UPI.")
            return False

class PayPalPayment(Payment):
    def pay(self, amount):
        if not super().pay(amount):
            return False
        
        service_charge = 5
        total_cost = amount + service_charge
        
        if self._update_balance(total_cost):
            print(f" Success! Paid {amount} via PayPal (+{service_charge} fee).")
            print(f" Remaining Balance: {self.get_balance()}")
            return True
        else:
            print(f" Error: Insufficient funds for PayPal.")
            return False

# Step 7: Demonstration
cc_payment = CreditCardPayment(1000)
upi_payment = UPIPayment(1000)
paypal_payment = PayPalPayment(1000)

payment_list = [cc_payment, upi_payment, paypal_payment]

print("--- STARTING MULTI-METHOD PAYMENT BATCH ---")
amount_to_pay = 200

for method in payment_list:
    method.pay(amount_to_pay)
