import pandas as pd
from datetime import date,timedelta
import numpy as np


class bank_account(object):
    """
    Deposit in any denomination.
    Balance in ZAR
    Withdraw in any denomination in your choice.
    """
    c = {}
    base_currency = "ZAR"
    currency_ = c
    try:
        date_ = date.today()
        dfs= (pd.read_html("https://www.xe.com/currencytables/?from={}&date={}".format(base_currency,date_))[0]
             .rename(columns={"Currency code  ▲▼":"Currency code","Currency name  ▲▼":"Currency name"}))
        #currency = {self.base_currency:list(required["Units per {}".format(base_currency)])[0]}
        currency1 = dict(zip(dfs["Currency code"], dfs["Units per {}".format(base_currency)]))
        currency = currency1
    except KeyError as s:
        print("Date out of range. Displaying the results for current day.")
        date_ = date.today()-timedelta(1)
        dfs = (pd.read_html("https://www.xe.com/currencytables/?from={}&date={}".format(base_currency, date_))[0]
               .rename(columns={"Currency code  ▲▼": "Currency code", "Currency name  ▲▼": "Currency name"}))
        # currency = {self.base_currency:list(required["Units per {}".format(base_currency)])[0]}
        currency1 = dict(zip(dfs["Currency code"], dfs["Units per {}".format(base_currency)]))
        currency = currency1
    

    def __init__(self):
        self.balance = 0
        self.to = 0
        self.fromm = 0
        self.currency_from = ""
        self.currency_to = ""
    def open_account(self):
        def account_number_gen():
            accs = []
            try:
                with open("ac.txt") as accounts:
                    for line in accounts:
                        value = line.split()
                        accs.append(int(value[0]))
            except FileNotFoundError as s:
                f = open("ac.txt","w+")
                f.close()
            if not accs:
                ac = 140000000
            else:
                ac = np.max(accs) + 1
            return (ac)

        first = input("Enter your first name: ")
        last = input("Enter your last name: ")
        ac = account_number_gen()
        print("Your account number is", ac)
        print(60 * "-")
        print("MAKE YOUR FIRST DEPOSIT")
        print(60 * "-")
        c = self.currency_selection()
        self.balance = 0
        d = eval(input("Enter your first deposit: "))
        initial_deposit = self.convert_to(d, self.currency[c])
        print("The balance is:", self.balance + initial_deposit)
        self.balance = self.balance + initial_deposit
        with open("ac.txt", "a+") as fp:
            fp.write("{}{}{}{}{}{}{}\n".format(ac, " ", last, " ", first, " ", np.round(self.balance, 2)))
        print("Your details have been saved as follows: \n\n")
        print(60 * "#")
        print("\t\t", ac, last, first, np.round(self.balance,2))
        print(60 * "#")

    def account_number_check(self, ac_):
        account_numbers = []
        with open("ac.txt") as accounts:
            for line in accounts:
                value = line.split()
                account_numbers.append(value[0])
        if str(ac_) in account_numbers:
            return ("exists")
        else:
            return ("does_not_exist")

    def display_ac(self):
        ac_check = int(input("Enter the Account number: "))
        if self.account_number_check(ac_check) == "exists":
            q = open("ac.txt", "r+")
            while True:
                for i in q:
                    values = i.split()
                    if values[0] == str(ac_check):
                        print(50 * "#")
                        print(i)
                        print(50 * "#")
                        values[0]
                    else:
                        pass
                break
            q.close()
        elif self.account_number_check(ac_check) == "does_not_exist":
            print("Account does not exist.")
            print("press 1 to try again")
            print("Press 0 to go to the main menu")
            a = int(input())
            if a == 1:
                self.display_ac()
            else:
                # Todo: enter service selection here
                pass

    def display_all(self):
        file = 'ac.txt'
        n = 1
        with open(file) as fp:
            line = fp.readline()
            while line:
                print("{} : {}".format(n, line.strip()))
                line = fp.readline()
                n = n + 1
    def currency_codes(self):
        print(sorted(self.dfs["Currency code"]))
    def currency_selection(self):
        print("SELECT THE CURRENCY BELOW: ")
        print("1: UGX")
        print("2: TZ")
        print("3: ZAR")
        print("4: KES")
        print("5: Other(Specify the currency code)")
        print("6: Not sure of the country code? enter 6 to see all the codes.")
        deno = int(input("Select the currency: "))
        if deno == 1:
            c = "UGX"
            return c
        elif deno == 2:
            c = "TZS"
            return c
        elif deno == 3:
            c = "ZAR"
            return c
        elif deno == 4:
            c = "KES"
            return c
        elif deno == 5:
            c = input("Enter the currency code: ")
            return c
        elif deno == 6:
            print(self.currency_codes())
            print(20*"#")
            c = input("Enter the code below:")
            print(20*"#")
            return c
        else:
            print("The selected currency is not available. Please try again.")
            return self.currency_selection()

    def bal(self):
        q = open("ac.txt", "r")
        ac_check = int(input("Enter the Account number: "))
        print("\n")
        while True:
            for i in q:
                values = i.split()
                if values[0] == str(ac_check):
                    self.balance = float(values[-1])

                    print("Your balance is: R", round(self.balance, 2))
                    print(15 * "#", "MORE ACCOUNT DETAILS", 15 * "#")
                    print(i)
                    print(50 * "#")
                    values[0]
                    return (self.balance)
                else:
                    pass
            break
        q.close()

    def deposit(self):
        ac_check = int(input("Enter the account number: "))
        if self.account_number_check(ac_check) == "exists":
            # read all the lines
            with open("ac.txt", "r") as fp:
                lines = fp.readlines()
                # print(lines)
            # check the account in question, read the values and delete it
            with open("ac.txt", "w") as fp:
                for line in lines:
                    if str(ac_check) in line.strip("\n"):
                        line1 = line.split()
                        ac = line1[0]
                        last = line1[1]
                        first = line1[2]
                        bal = float(line1[-1])
                        c = self.currency_selection()
                        d = eval(input("Enter the amount to deposit: "))
                        dd = self.convert_to(d, self.currency[c])
                        self.balance = bal + dd
                    elif str(ac_check) not in line.strip("\n"):
                        fp.write(line)
            # append the new account details
            with open("ac.txt", "a") as fp:
                new_line = ac + " " + last + " " + first + " " + str(np.round(self.balance, 2)) + "\n"
                fp.write(new_line)

            print("Operation successful")
            print(" New account details:")
            print(50 * "#")
            print(new_line)
            print(50 * "#")
        elif self.account_number_check(ac_check) == "does_not_exist":
            print("Account does not exist. Try again")
            self.deposit()

    def withdraw(self):
        # read all the lines
        ac_check = int(input("Enter the account number: "))
        balance = self.bal()
        c = self.currency_selection()
        w = eval(input("Enter the amount to withdraw: "))
        ww = self.convert_to(w, self.currency[c])
        if self.account_number_check(ac_check) == "exists" and (balance - ww) >= 0:
            with open("ac.txt", "r") as fp:
                lines = fp.readlines()
                # print(lines)
            # check the account in question, read the values and delete it
            with open("ac.txt", "w") as fp:
                for line in lines:
                    if str(ac_check) in line.strip("\n"):
                        line1 = line.split()
                        ac = line1[0]
                        last = line1[1]
                        first = line1[2]
                        bal = float(line1[-1])

                        self.balance = bal - ww
                    elif str(ac_check) not in line.strip("\n"):
                        fp.write(line)
            # append the new account details

            with open("ac.txt", "a") as fp:
                new_line = ac + " " + last + " " + first + " " + str(np.round(self.balance, 2)) + "\n"
                fp.write(new_line)

            print("Operation successful")
            print(" New account details:")
            print(50 * "#")
            print(new_line)
            print(50 * "#")
        elif self.account_number_check(ac_check) == "does_not_exist":
            print("Account does not exist. Try again")
            self.withdraw()
        else:
            print("Operation unsucessful")
            print("Insufficient balance. Your balance is: ", balance, "ZAR and you are trying to withdraw", ww, "ZAR",
                  f"({w}{c})")
            self.withdraw()

    def convert_to(self, amount, rate):
        self.to = amount / rate
        return (self.to)
        print("Your balance is: R", round(self.balance, 2))

    def convert_from(self, amount, rate):
        self.fromm = amount * rate
        return (self.fromm)
    @staticmethod
    def currency_conversion():
        print("1: Historical")
        print("2: Current exchange rates")
        t = eval(input("Choose: 1 for Historical or 2 for current. Default current."))
        if t ==1: 
            print("Enter the currency you wish to compare and date in the format(YYYY-MM-DD) below separated by #")
            print("Example: USD#CAD#2020-06-01")
            cc = list(map(str,input().strip().split("#")))
            #date_= datetime.strptime(cc[2],'%Y-%m-%d').date()
            dffs= (pd.read_html("https://www.xe.com/currencytables/?from={}&date={}".format(cc[0],cc[2]))[0]
         .rename(columns={"Currency code  ▲▼":"Currency code","Currency name  ▲▼":"Currency name"}))
            required = dffs[dffs["Currency code"]==cc[1]]
            print(50*"-")
            print("Date:",cc[2])
            print(required)
        else:
            print("Enter the currency you wish to compare and date in the format(YYYY-MM-DD) below separated by #")
            print("Example: USD#CAD")
            cc = list(map(str,input().strip().split("#")))
            date_ = date.today()
            dffs= (pd.read_html("https://www.xe.com/currencytables/?from={}&date={}".format(cc[0],date_))[0]
         .rename(columns={"Currency code  ▲▼":"Currency code","Currency name  ▲▼":"Currency name"}))
            required = dffs[dffs["Currency code"]==cc[1]]
            print(50*"-")
            print("Date:",date_)
            print(required)
        
    def clear_account(self):
        print("Are you sure you want to clear the account? If yes, input the account number.")
        ac_check = int(input("Enter the account number: "))
        c = self.currency_selection()
        if self.account_number_check(ac_check) == "exists":
            with open("ac.txt", "r") as fp:
                lines = fp.readlines()
                # print(lines)
            # check the account in question, read the values and delete it
            with open("ac.txt", "w") as fp:
                for line in lines:
                    if str(ac_check) in line.strip("\n"):
                        line1 = line.split()
                        ac = line1[0]
                        last = line1[1]
                        first = line1[2]
                        bal = float(line1[-1])
                        bal = self.convert_from(bal, self.currency[c])
                        self.balance = 0
                    elif str(ac_check) not in line.strip("\n"):
                        fp.write(line)
            # append the new account details
            print(f"Paying all the amount in the account. A total of {np.round(bal, 2)}{c}")
            with open("ac.txt", "a") as fp:
                new_line = ac + " " + last + " " + first + " " + str(np.round(self.balance, 2)) + "\n"
                fp.write(new_line)

            print("Operation successful.Account cleared.")
            print(" New account details:")
            print(50 * "#")
            print(new_line)
            print(50 * "#")
        elif self.account_number_check(ac_check) == "does_not_exist":
            print("Account does not exist. Try again")
            self.service_offered()

    def close_account(self):
        print("WARNING: Are you sure you want to close the account? If yes, input the account number.")
        ac_check = int(input("Enter the account number: "))
        c = self.currency_selection()
        if self.account_number_check(ac_check) == "exists":
            with open("ac.txt", "r") as fp:
                lines = fp.readlines()
                # print(lines)
            # check the account in question, read the values and delete it
            with open("ac.txt", "w") as fp:
                for line in lines:
                    if str(ac_check) in line.strip("\n"):
                        line1 = line.split()
                        ac = line1[0]
                        last = line1[1]
                        first = line1[2]
                        bal = float(line1[-1])
                        bal = self.convert_from(bal, self.currency[c])
                    elif str(ac_check) not in line.strip("\n"):
                        fp.write(line)
            # append the new account details
            print(f"Paying all the amount in the account. A total of {np.round(bal, 2)}{c}")
            print("Operation successful.Account closed.")
        elif self.account_number_check(ac_check) == "does_not_exist":
            print("Account does not exist. Try again")
            self.service_offered()

    def services_offered(self):
        print(30 * "*")
        print(6 * " ", "SERVICES OFFERED")
        print(30 * "*")
        print("0: Open account")
        print("1: Deposit")
        print("2: Withdraw")
        print("3: Check balance")
        print("4: Display all accounts")
        print("5: Search for an account")
        print("6: Clear an account (Withdraw all the amount and set account bal to 0)")
        print("7: Close an account (Withdraw all the amount and delete account)")
        print("8: Currency Conversion")
        print("9: Quit")

