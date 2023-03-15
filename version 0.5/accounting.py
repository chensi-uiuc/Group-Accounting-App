from rich.console import Console
from rich.table import Table
from os import get_terminal_size
from numpy import zeros
# import numpy as np

import utils

def _print_welcome_caption(console):
    console.print("Welcome to Group Accounting version 0.5", style="green")
    console.print("Developed by Chen Si, March 2023", style="green")

def _print_start_instruction(console):
    console.print("To start, type instructions in the console.", style="white")
    console.print("For more help, try \"?\". \n", style="white")

def _print_end_caption(console):
    console.print("Thanks for using!", style="green")
    console.print("Wish you have a great day!", style="green")
    console.print("Good bye ~~~ \n\n", style="green")

def _print_h_line(console, style):
    terminal_size = get_terminal_size().columns - 1
    console.print("-"*terminal_size, style=style)

def _print_tutorial(console):
    # _print_h_line(console, "white")
    console.print("Tutorial", style="bold yellow")
    console.print(f"1. Enter \"{utils.END_CHAR}\" to end the program;", style="white")
    console.print(f"2. Enter \"{utils.NEWSYS}\" to start a new account;", style="white")
    console.print(f"3. Enter \"{utils.ADD_PERSON}\" to add a new person into the accounting system;", style="white")
    console.print(f"4. Enter \"{utils.DEL_PERSON}\" to delete a person from the accounting system;", style="white")
    console.print(f"5. Enter \"{utils.ADD_BILL}\" to add a new bill into the accounting system;", style="white")
    console.print(f"6. Enter \"{utils.DEL_BILL}\" to delete a bill from the accounting system;", style="white")
    console.print(f"6. Enter \"{utils.CALC}\" to start calculating and show the results;", style="white bold")
    console.print(f"6. Enter \"{utils.CALC_CLEAN}\" to start calculating (hiding internal process) and show the results;", style="white bold")
    # _print_h_line(console, "white")

def _print_new_system(console):
    # _print_h_line(console, "white")
    console.print("Initializing New Accounting System ... ", style="bold yellow")
    console.print("Initializzation Complete", style="bold yellow")
    # _print_h_line(console, "white")

def _print_add_person(console):
    # _print_h_line(console, "white")
    console.print("Add Person", style="bold yellow")
    console.print("Please enter a valid person name below. ", style="yellow")
    # _print_h_line(console, "white")

def _print_del_person(console):
    # _print_h_line(console, "white")
    console.print("Delete Person", style="bold yellow")
    console.print("Please enter a valid person name below. ", style="yellow")
    # _print_h_line(console, "white")

def _print_add_bill(console):
    # _print_h_line(console, "white")
    console.print("Add Bill", style="bold yellow")
    console.print("Please enter a valid bill info below. ", style="yellow")
    # _print_h_line(console, "white")

def _print_del_bill(console):
    # _print_h_line(console, "white")
    console.print("Delete Bill", style="bold yellow")
    console.print("Please select a bill below. ", style="yellow")
    # _print_h_line(console, "white")

def _check_name(name:str):
    if not name.isalpha():
        return False
    return True

def is_valid_float(string):
    try:
        float(string)
    except ValueError:
        return False
    else:
        return True

"""
code 0: Normal Condition
code 1: No Lower 
"""
def _get_input(code=0):
    txt = input(">: ")
    if (code == 1):
        return txt.strip()
    else:
        return txt.strip().lower()


# Main Function
if __name__ == '__main__':
    console = Console()
    _print_welcome_caption(console)
    _print_start_instruction(console)

    acct_system = None

    # Main Loop
    run_flag = True
    while (run_flag == True):
        _print_h_line(console, "bold yellow")
        input_txt = _get_input()

        if (input_txt == utils.TUT_CHAR):
            _print_tutorial(console)
        elif (input_txt == utils.END_CHAR):
            _print_end_caption(console)
            input("Enter anything to exit.")
            run_flag = False
            break
        elif (input_txt == utils.NEWSYS):
            acct_system = utils.AS()
            _print_new_system(console)
        elif (input_txt == utils.ADD_PERSON):
            if acct_system==None:
                console.print("ERROR: No Accounting systems found, please start a new accounting system!", style="bold red")
                continue

            _print_add_person(console)
            name = _get_input(code=1)
            if _check_name(name)==True:
                flag = acct_system.add_person(name)
                if flag!=0:
                    console.print("Error: Error in adding person.", style="bold red")
                    continue
                else:
                    console.print(f"Success in adding person {name}.", style="yellow")
                    # print(flag)
                    # print(acct_system.people)
            else:
                console.print("Error: Invalid Person Name.", style="bold red")
                continue
        elif (input_txt == utils.DEL_PERSON):
            if acct_system==None:
                console.print("ERROR: No Accounting systems found, please start a new accounting system!", style="bold red")
                continue

            _print_del_person(console)
            name = _get_input(code=1)
            if _check_name(name)==False:
                console.print("Error: Invalid Person Name.", style="bold red")
                continue
            if acct_system.delete_person(name)==0:
                console.print(f"Success in deleting person {name}.", style="yellow")
            else:
                console.print(f"Error: Error in deleting person {name}.", style="bold red")

        elif (input_txt == utils.ADD_BILL):
            if acct_system==None:
                console.print("ERROR: No Accounting systems found, please start a new accounting system!", style="bold red")
                continue

            _print_add_bill(console)

            _print_h_line(console, "white")
            console.print("Payer:", style="bold")
            payer=[]
            while True:
                name = _get_input(code=1)
                if len(name)==0:
                    break
                elif not acct_system.has_person(name):
                    console.print("Error: Person not in system.", style="bold red")
                    continue
                else:
                    payer.append(name)

            _print_h_line(console, "white")
            console.print("Issue:", style="bold")
            issue = _get_input()

            _print_h_line(console, "white")
            console.print("Amount:", style="bold")
            while True:
                string = _get_input()
                if is_valid_float(string):
                    amount=float(string)
                    break
                else:
                    console.print("Error: Not valid float amount.", style="bold red")

            _print_h_line(console, "white")
            console.print("Spender:", style="bold")
            spender=[]
            while True:
                name = _get_input(code=1)
                if len(name)==0:
                    break
                elif not acct_system.has_person(name):
                    console.print("Error: Person not in system.", style="bold red")
                    continue
                else:
                    spender.append(name)
            
            _print_h_line(console, "white")

            bill = utils.Bill(payer, issue, amount, spender)

            acct_system.add_bill(bill)

            console.print(f"Success in adding bill.", style="yellow")

            bill.print_bill(console)

        elif (input_txt == utils.DEL_BILL):
            if acct_system==None:
                console.print("ERROR: No Accounting systems found, please start a new accounting system!", style="bold red")
                continue

            _print_del_bill(console)

            bills = acct_system.get_bills()

            console.print("Current Bills", style="bold")
            _print_h_line(console, "white")
            for i in range(len(bills)):
                console.print(f"Bill {i+1}", style="bold")
                bills[i].print_bill(console)
                _print_h_line(console, "white")

            console.print("Select a bill to delete", style="bold")

            while True:
                index = _get_input()
                if index.isnumeric():
                    if int(index)-1<len(bills) and int(index)-1>0:
                        del acct_system.bills[int(index)-1]
                        console.print(f"Delete Bill {int(index)}.", style="yellow")
                        break
                    else:
                        console.print("Error: Not valid index.", style="bold red")
                        continue
                else:
                    console.print("Error: Not valid index.", style="bold red")
                    continue

        elif (input_txt == utils.CALC):
            if acct_system==None:
                console.print("ERROR: No Accounting systems found, please start a new accounting system!", style="bold red")
                continue

            if len(acct_system.get_bills())<=0 or len(acct_system.get_people())<=0:
                console.print("Error: Empty Bill-set or Empty People-set.", style="bold red")
                continue

            N = len(acct_system.get_people())

            console.print("Calculating Bills ... ", style="yellow")

            M=zeros((N,N))
            people = acct_system.get_people()
            for i in range(len(acct_system.get_bills())):
                _print_h_line(console, "white")
                payer = acct_system.get_bills()[i].get_payer()
                issue = acct_system.get_bills()[i].get_issue()
                amount = acct_system.get_bills()[i].get_amount()
                spender = acct_system.get_bills()[i].get_spender()

                console.print(f"{','.join(payer)} pays ${amount:.2f} for {issue}.")
                console.print(f"This bill is spent by {','.join(spender)}.")

                avg_value = (amount/len(payer))/len(spender)

                table = Table(title=f"Bill Issue {issue}")
                table.add_column("Sender", justify="center")
                table.add_column("Receiver", justify="center")
                table.add_column("Amount", justify="center")

                for p in payer:
                    for sp in spender:
                        M[people.index(sp), people.index(p)] += avg_value
                        table.add_row(sp, p, f"$ {avg_value:.2f}")
                
                console.print(table)

            _print_h_line(console, "bold yellow")
            console.print("Results", style="bold yellow")
            _print_h_line(console, "bold yellow")

            table = Table(title=f"Final Result (Simplified)")
            table.add_column("Sender", justify="center", style="bold")
            table.add_column("Receiver", justify="center", style="bold")
            table.add_column("Amount", justify="center", style="bold")

            for i in range(N):
                for j in range(i+1,N):
                    if M[i,j]>=M[j,i]:
                        table.add_row(people[i], people[j],  f"$ {M[i,j] - M[j,i]:.2f}")
                    else:
                        table.add_row(people[j], people[i],  f"$ {M[j,i] - M[i,j]:.2f}")

            console.print(table)
            _print_h_line(console, "bold yellow")

        elif (input_txt == utils.CALC_CLEAN):
            if acct_system==None:
                console.print("ERROR: No Accounting systems found, please start a new accounting system!", style="bold red")
                continue

            if len(acct_system.get_bills())<=0 or len(acct_system.get_people())<=0:
                console.print("Error: Empty Bill-set or Empty People-set.", style="bold red")
                continue

            N = len(acct_system.get_people())

            console.print("Calculating Bills ... ", style="yellow")

            M=zeros((N,N))
            people = acct_system.get_people()
            for i in range(len(acct_system.get_bills())):
                _print_h_line(console, "white")
                payer = acct_system.get_bills()[i].get_payer()
                issue = acct_system.get_bills()[i].get_issue()
                amount = acct_system.get_bills()[i].get_amount()
                spender = acct_system.get_bills()[i].get_spender()

                # console.print(f"{','.join(payer)} pays ${amount:.2f} for {issue}.")
                # console.print(f"This bill is spent by {','.join(spender)}.")

                avg_value = (amount/len(payer))/len(spender)

                # table = Table(title=f"Bill Issue {issue}")
                # table.add_column("Sender", justify="center")
                # table.add_column("Receiver", justify="center")
                # table.add_column("Amount", justify="center")

                for p in payer:
                    for sp in spender:
                        M[people.index(sp), people.index(p)] += avg_value
                        # table.add_row(sp, p, f"$ {avg_value:.2f}")
                
                # console.print(table)

            _print_h_line(console, "bold yellow")
            console.print("Results", style="bold yellow")
            _print_h_line(console, "bold yellow")

            table = Table(title=f"Final Result (Simplified)")
            table.add_column("Sender", justify="center", style="bold")
            table.add_column("Receiver", justify="center", style="bold")
            table.add_column("Amount", justify="center", style="bold")

            for i in range(N):
                for j in range(i+1,N):
                    if M[i,j]>=M[j,i]:
                        table.add_row(people[i], people[j],  f"$ {M[i,j] - M[j,i]:.2f}")
                    else:
                        table.add_row(people[j], people[i],  f"$ {M[j,i] - M[i,j]:.2f}")

            console.print(table)
            _print_h_line(console, "bold yellow")
        else:
            console.print("Invalid Command. Please check the tutorial \"?\"")









        

