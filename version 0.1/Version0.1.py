from rich.console import Console
from rich.table import Table
import numpy as np

def _print_start_caption(console):
    console.print("Welcome to Group Accounting version 0.1", style="green")
    console.print("Developed by Chen Si, March 2023\n\n", style="green")

# Main Function
if __name__ == '__main__':
    console = Console()
    _print_start_caption(console)

    console.print("------Group Initialization------\n", style="bold orange3")

    console.print("Please enter the number of people in the group below:", style="bold deep_sky_blue1")
    console.print("---Begin Input---", style="plum3")
    num = input()
    console.print("---End Input---\n", style="plum3")
    assert num.isnumeric()
    N = int(num)
    
    Names = []
    i = 0
    while i < N:
        console.print(f"Please enter name of member {i+1}:", style="bold deep_sky_blue1")
        console.print("---Begin Input---", style="plum3")
        name = input()
        console.print("---End Input---", style="plum3")

        if len(name) > 64:
            console.print("Invalid Input --> Name Too Long!\n", style="red3")
        elif name in Names:
            console.print("Invalid Input --> Name Already Entered!\n", style="red3")
        elif not name.isalpha():
            console.print("Invalid Input --> Invalid Name!\n", style="red3")
        else:
            console.print()
            Names.append(name)
            i += 1
    

    console.print("\n\n------Bills Initialization------\n", style="bold orange3")

    bills=[]

    while True:
        console.print("----------New Bill----------", style="bold yellow")
        console.print("Please enter name of member paying this bill:", style="bold deep_sky_blue1")
        console.print("(Hit \\Enter\\ to end)", style="deep_sky_blue1")
        console.print("---Begin Input---", style="plum3")
        name = input()
        console.print("---End Input---", style="plum3")

        if name == "":
            break
        elif not name in Names:
            console.print("Invalid Input --> Name Not In NameList!\n", style="red3")
            continue

        console.print("Please enter issue of the bill:", style="bold deep_sky_blue1")
        console.print("---Begin Input---", style="plum3")
        issue = input()
        console.print("---End Input---", style="plum3")

        console.print("Please enter members to share the bill:", style="bold deep_sky_blue1")
        console.print("(Hit Enter to end)", style="deep_sky_blue1")
        console.print("---Begin Input---", style="plum3")
        members=[]
        while True:
            nm = input()
            if nm == "":
                break
            elif not nm in Names:
                console.print("Invalid Input --> Name Not In NameList!\n", style="red3")
                continue
            else:
                members.append(nm)
        console.print("---End Input---", style="plum3")

        console.print("Please enter value of the bill ($):", style="bold deep_sky_blue1")
        console.print("---Begin Input---", style="plum3")
        value = float(input())
        console.print("---End Input---\n", style="plum3")

        # console.log((name, issue, members, value))
        bills.append((name, issue, members, value))

    # console.log(bills)


    console.print("\n------Calculating Bills------\n", style="bold orange3")

    M = np.zeros((N,N))    
    if not len(bills)==0:
        for (name, issue, members, value) in bills:
            console.log(name, issue, members, value)
            console.print(f"{name} pays ${value:.2f} for {issue}.")
            console.print(f"This bill is shares for {','.join(members)}.")

            avg_value = value/len(members)
            table = Table(title=f"Bill Issue {issue}")
            table.add_column("Sender", justify="center")
            table.add_column("Receiver", justify="center")
            table.add_column("Amount", justify="center")


            for member in members:
                M[Names.index(member), Names.index(name)] += avg_value
                table.add_row(member, name, f"$ {avg_value:.2f}")
            
            console.print(table)

    console.print("\n------Results------\n", style="bold orange3")

    table = Table(title=f"Final Result (Simplified)")
    table.add_column("Sender", justify="center", style="bold")
    table.add_column("Receiver", justify="center", style="bold")
    table.add_column("Amount", justify="center", style="bold")

    for i in range(N):
        for j in range(i+1,N):
            if M[i,j]>=M[j,i]:
                table.add_row(Names[i], Names[j],  f"$ {M[i,j] - M[j,i]:.2f}")
            else:
                table.add_row(Names[j], Names[i],  f"$ {M[j,i] - M[i,j]:.2f}")

    console.print(table)


    input()


