# Constants
TUT_CHAR = "？"
END_CHAR = "退出"
NEWSYS = "新帐本"
ADD_PERSON = "添加人物"
DEL_PERSON = "删除人物"
ADD_BILL = "添加账单"
DEL_BILL = "删除帐单"
CALC = "计帐"
CALC_CLEAN = "计帐 简算"
SHOW_BILLS = "查看账目"
SHOW_PEOPLE = "查看人物"

# Class Bill
class Bill:
    payer = []
    issue = ""
    amount = 0.0
    spender = []

    def __init__(self, p:list, i:str, a:float, sp:list):
        self.amount=a
        self.issue=i
        self.payer=p
        self.spender=sp
    
    def __eq__(self, other): 
        if not isinstance(other, Bill):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.get_payer==other.get_payer and self.get_amount==other.get_amount and self.get_issue==other.get_issue and self.get_spender==other.get_spender
    
    def get_payer(self):
        return self.payer
    def get_issue(self):
        return self.issue
    def get_amount(self):
        return self.amount
    def get_spender(self):
        return self.spender
    
    def print_bill(self, console):
        console.print(f"Bill Details:")
        console.print(f"Payer: {','.join(self.payer)};")
        console.print(f"Issue: {self.issue};")
        console.print(f"Amount: $ {self.amount};")
        console.print(f"Spender: {','.join(self.spender)};")

    
    def is_valid(self):
        if len(self.payer)==0:
            return False
        elif len(self.spender)==0:
            return False
        elif self.amount<=0.0:
            return False
        
        return True
    

# Class Accounting System
class AS:
    bills = []
    people = []

    def add_person(self, p_name:str):
        if (len(p_name) > 0 and (not p_name in self.people)):
            self.people.append(p_name)
            return 0
        else:
            return 1
    
    def delete_person(self, p_name:str):
        if (p_name in self.people):
            self.people.remove(p_name)
            return 0
        else:
            return 1
        
    def get_people(self):
        return self.people
    
    def has_person(self, name):
        return name in self.people
    
    def add_bill(self, bill:Bill):
        if (Bill.is_valid(bill)):
            self.bills.append(bill)
            return 0
        else:
            return 1
    
    def delete_bill(self, bill:Bill):
        if (bill in self.bills):
            self.bills.remove(bill)
            return 0
        else:
            return 1
        
    def get_bills(self):
        return self.bills
    

