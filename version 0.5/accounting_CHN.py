from rich.console import Console
from rich.table import Table
# from os import get_terminal_size
import numpy as np

import utils_CHN as utils

def _print_welcome_caption(console):
    console.print("欢迎使用小组活动算账软件 0.5", style="green")
    console.print("本软件由 司宸 开发于2023年3月，内测中", style="green")

def _print_start_instruction(console):
    console.print("使用本软件，请在命令行中输入正确的指令", style="white")
    console.print("查看使用说明，请输入 \"？\"\n", style="white")

def _print_end_caption(console):
    console.print("感谢使用！", style="green")
    console.print("软件开发者祝您生活愉快，学习顺利！", style="green")
    console.print("再见~~~ \n\n", style="green")

def _print_h_line(console, style):
    # terminal_size = get_terminal_size().columns - 1
    terminal_size=30
    console.print("-"*terminal_size, style=style)

def _print_tutorial(console):
    # _print_h_line(console, "white")
    console.print("使用说明", style="bold yellow")
    console.print(f"1. 输入 \"{utils.END_CHAR}\" 退出使用；", style="white")
    console.print(f"2. 输入 \"{utils.NEWSYS}\" 新建一个账本；", style="white")
    console.print(f"3. 输入 \"{utils.ADD_PERSON}\" 添加一个新人物；", style="white")
    console.print(f"4. 输入 \"{utils.DEL_PERSON}\" 删除已经存在的人物；", style="white")
    console.print(f"5. 输入 \"{utils.ADD_BILL}\" 添加一张新帐单；", style="white")
    console.print(f"6. 输入 \"{utils.DEL_BILL}\" 删除已经存在的帐单；", style="white")
    console.print(f"6. 输入 \"{utils.CALC}\" 开始计算账目（默认开启细节展示）；", style="white bold")
    console.print(f"6. 输入 \"{utils.CALC_CLEAN}\" 开始计算账目（隐藏细节展示）；", style="white bold")
    # _print_h_line(console, "white")

def _print_new_system(console):
    # _print_h_line(console, "white")
    console.print("新帐本创建中 ... ", style="bold yellow")
    console.print("创建完毕", style="bold yellow")
    # _print_h_line(console, "white")

def _print_add_person(console):
    # _print_h_line(console, "white")
    console.print("添加新人物", style="bold yellow")
    console.print("请输入有效的人物名称", style="yellow")
    # _print_h_line(console, "white")

def _print_del_person(console):
    # _print_h_line(console, "white")
    console.print("删除已经存在的人物", style="bold yellow")
    console.print("请输入有效的人物名称", style="yellow")
    # _print_h_line(console, "white")

def _print_add_bill(console):
    # _print_h_line(console, "white")
    console.print("添加新帐单", style="bold yellow")
    console.print("请输入有效的账单细节", style="yellow")
    # _print_h_line(console, "white")

def _print_del_bill(console):
    # _print_h_line(console, "white")
    console.print("删除已经存在的帐单", style="bold yellow")
    console.print("请挑选已有的账单", style="yellow")
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
            input("输入任意继续...")
            run_flag = False
            break
        elif (input_txt == utils.NEWSYS):
            acct_system = utils.AS()
            _print_new_system(console)
        elif (input_txt == utils.ADD_PERSON):
            if acct_system==None:
                console.print("ERROR: 当前无账本，请新建账本后继续！", style="bold red")
                continue

            _print_add_person(console)
            name = _get_input(code=1)
            if _check_name(name)==True:
                flag = acct_system.add_person(name)
                if flag!=0:
                    console.print("ERROR: 添加新人物错误", style="bold red")
                    continue
                else:
                    console.print(f"成功添加新人物 {name}.", style="yellow")
                    # print(flag)
                    # print(acct_system.people)
            else:
                console.print("ERROR: 无效的人物名称", style="bold red")
                continue
        elif (input_txt == utils.DEL_PERSON):
            if acct_system==None:
                console.print("ERROR: 当前无账本，请新建账本后继续！", style="bold red")
                continue

            _print_del_person(console)
            name = _get_input(code=1)
            if _check_name(name)==False:
                console.print("ERROR: 无效的人物名称", style="bold red")
                continue
            if acct_system.delete_person(name)==0:
                console.print(f"成功删除人物 {name}.", style="yellow")
            else:
                console.print(f"ERROR: 删除人物错误 {name}.", style="bold red")

        elif (input_txt == utils.ADD_BILL):
            if acct_system==None:
                console.print("ERROR: 当前无账本，请新建账本后继续！", style="bold red")
                continue

            _print_add_bill(console)

            _print_h_line(console, "white")
            console.print("付款者：", style="bold")
            payer=[]
            while True:
                name = _get_input(code=1)
                if len(name)==0:
                    break
                elif not acct_system.has_person(name):
                    console.print("ERROR: 人物不存在", style="bold red")
                    continue
                else:
                    payer.append(name)

            _print_h_line(console, "white")
            console.print("事由：", style="bold")
            issue = _get_input()

            _print_h_line(console, "white")
            console.print("金额：", style="bold")
            while True:
                string = _get_input()
                if is_valid_float(string):
                    amount=float(string)
                    break
                else:
                    console.print("ERROR: 无效金额", style="bold red")

            _print_h_line(console, "white")
            console.print("享受服务者：", style="bold")
            spender=[]
            while True:
                name = _get_input(code=1)
                if len(name)==0:
                    break
                elif not acct_system.has_person(name):
                    console.print("ERROR: 人物不存在", style="bold red")
                    continue
                else:
                    spender.append(name)
            
            _print_h_line(console, "white")

            bill = utils.Bill(payer, issue, amount, spender)

            acct_system.add_bill(bill)

            console.print(f"添加账单成功", style="yellow")

            bill.print_bill(console)

        elif (input_txt == utils.DEL_BILL):
            if acct_system==None:
                console.print("ERROR: 当前无账本，请新建账本后继续！", style="bold red")
                continue

            _print_del_bill(console)

            bills = acct_system.get_bills()

            console.print("当前帐单", style="bold")
            _print_h_line(console, "white")
            for i in range(len(bills)):
                console.print(f"帐单 {i+1}", style="bold")
                bills[i].print_bill(console)
                _print_h_line(console, "white")

            console.print("选择一个账单以删除", style="bold")

            while True:
                index = _get_input()
                if index.isnumeric():
                    if int(index)-1<len(bills) and int(index)-1>0:
                        del acct_system.bills[int(index)-1]
                        console.print(f"成功删除帐单 {int(index)}.", style="yellow")
                        break
                    else:
                        console.print("ERROR: 无效编号", style="bold red")
                        continue
                else:
                    console.print("ERROR: 无效编号", style="bold red")
                    continue

        elif (input_txt == utils.CALC):
            if acct_system==None:
                console.print("ERROR: 当前无账本，请新建账本后继续！", style="bold red")
                continue

            if len(acct_system.get_bills())<=0 or len(acct_system.get_people())<=0:
                console.print("ERROR: 当前无人物 或 当前无帐单", style="bold red")
                continue

            N = len(acct_system.get_people())

            console.print("正在算账请稍后 ... ", style="yellow")

            M=np.zeros((N,N))
            people = acct_system.get_people()
            for i in range(len(acct_system.get_bills())):
                _print_h_line(console, "white")
                payer = acct_system.get_bills()[i].get_payer()
                issue = acct_system.get_bills()[i].get_issue()
                amount = acct_system.get_bills()[i].get_amount()
                spender = acct_system.get_bills()[i].get_spender()

                console.print(f"{','.join(payer)} 为了 {issue} 帮 {','.join(spender)} 支付了 ${amount:.2f}")

                avg_value = (amount/len(payer))/len(spender)

                table = Table(title=f"帐单： {issue}")
                table.add_column("支付者", justify="center")
                table.add_column("收款者", justify="center")
                table.add_column("金额", justify="center")

                for p in payer:
                    for sp in spender:
                        M[people.index(sp), people.index(p)] += avg_value
                        table.add_row(sp, p, f"$ {avg_value:.2f}")
                
                console.print(table)

            _print_h_line(console, "bold yellow")
            console.print("计账结果", style="bold yellow")
            _print_h_line(console, "bold yellow")

            table = Table(title=f"计帐结果（总计）")
            table.add_column("支付者", justify="center", style="bold")
            table.add_column("收款者", justify="center", style="bold")
            table.add_column("金额", justify="center", style="bold")

            for i in range(N):
                for j in range(i+1,N):
                    if M[i,j]>=M[j,i]:
                        table.add_row(people[i], people[j],  f"$ {M[i,j] - M[j,i]:.2f}")
                    else:
                        table.add_row(people[j], people[i],  f"$ {M[j,i] - M[i,j]:.2f}")

            console.print(table)
            # _print_h_line(console, "bold yellow")

        elif (input_txt == utils.CALC_CLEAN):
            if acct_system==None:
                console.print("ERROR: 当前无账本，请新建账本后继续！", style="bold red")
                continue

            if len(acct_system.get_bills())<=0 or len(acct_system.get_people())<=0:
                console.print("ERROR: 当前无人物 或 当前无帐单", style="bold red")
                continue

            N = len(acct_system.get_people())

            console.print("正在算账请稍后 ... ", style="yellow")

            M=np.zeros((N,N))
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
            console.print("计账结果", style="bold yellow")
            _print_h_line(console, "bold yellow")

            table = Table(title=f"计帐结果（总计）")
            table.add_column("支付者", justify="center", style="bold")
            table.add_column("收款者", justify="center", style="bold")
            table.add_column("金额", justify="center", style="bold")

            for i in range(N):
                for j in range(i+1,N):
                    if M[i,j]>=M[j,i]:
                        table.add_row(people[i], people[j],  f"$ {M[i,j] - M[j,i]:.2f}")
                    else:
                        table.add_row(people[j], people[i],  f"$ {M[j,i] - M[i,j]:.2f}")

            console.print(table)
            # _print_h_line(console, "bold yellow")
        else:
            console.print("无效指令！如不清楚指令请参考使用说明： \"？\"",style="bold red")









        

