#use mutable sequence to maintain a local inside the function

def make_withdraw(balance):
    b = [balance]
    def withdraw(amount):
        if amount > balance:
            print("No sufficient fund")
        else:
            b[0] -= amount
            return b[0]
    return withdraw