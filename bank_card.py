import uuid
from datetime import datetime
login_data = {}


class CardNumberException(Exception):
    pass
class CvvException(Exception):
    pass
class BankCard():
    def __init__(self,name,surname,cardnumber,cvv,pin,balance = 50000):
        self.name = name
        self.surname = surname
        if len(cardnumber) != 16:
            raise CardNumberException("CardNumber length must be 16")
        self._cardnumber = cardnumber
        if len(cvv)  != 3:
            raise CvvException("cvv length must be 3")
        self._cvv = cvv
        self._pin = pin
        self.balance = balance 
        self.unique_id = ''
        self.transactions = []
        self.count = 0

    def make_action(self):
        while self.count < 3:
            password = input("Enter your pin: ")
            if str(password) == self._pin:
                self.unique_id = uuid.uuid4()
                login_data[self.unique_id] = True
                self.count = 0
                break
            else:
                print("Incorrect PIN.")
                self.count += 1
        if self.count >= 3:
            print('The card was blocked.')
            exit()
            
    def withdraw(self,amount):
        if self.unique_id != '' and login_data[self.unique_id] is True:
            if self.balance < amount:
                return "There are not enough funds in your account."
            else:
                self.balance -= amount
                self.transactions.append({
                'type': 'withdraw',
                'amount': amount,
                'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        else:
            return "ooops..."

  
    def deposit(self,amount):
        if self.unique_id != '' and login_data[self.unique_id] is True:
            self.balance += amount
            self.transactions.append({
            'type': 'deposit',
            'amount': amount,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        else:
            return "ooops..."
    def get_balance(self):
        return f'Balance : {self.balance}'
    def get_transaction(self):
        result = ""
        for txn in self.transactions:
            result += f"{txn['date']} - {txn['type'].capitalize()}: {txn['amount']}֏\n"
        return result
    def logout(self):
        if self.unique_id in login_data:
            login_data[self.unique_id] = False
        self.unique_id = ""
        print("Logged out successfully.")
        

if __name__ == "__main__":
    cardnumber = "1553217320474153"
    cvv = "148" 
    pin = "1234"

    obj = BankCard("Narine","Vardanyan",cardnumber,cvv,pin)
    obj.make_action()
    obj.withdraw(1000)
    obj.deposit(110000)
    print(obj.get_balance())
    print(obj.get_transaction())
    obj.logout()





