class Atm(object):
    def __init__(self,users,atmCardNumber,pinNumber):
        self.users=users
        self.atmCardNumber=atmCardNumber
        self.pinNumber=pinNumber
    
    def CashWithdrawl(self):
        print("Withdrawl")
    
    def BalanceEnquiry(self):
        print("Balance Enquiry")

tanmay=Atm("Tanmay","4563 6742 4572 2957","5632")
mahart=Atm("Mahart","2784 3854 1435 8935","3782")
print(tanmay.pinNumber)
tanmay.CashWithdrawl()