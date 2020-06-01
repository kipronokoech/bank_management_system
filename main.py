#Calling the bank_account class on bank.py
from bank import bank_account

bank_account = bank_account()

print(70 * "#")
print("\n")
print(20 * " ", "AIMS Bank and Exchange Centre", 10 * " ")
print(30 * " ", "WELCOME!!!", 15 * " ")
print(8 * " ", "brought to you by KIPRONO ELIJAH KOECH(kiprono@aims.ac.za)")
print(10 * " ", "and SAUMU ABDALLAH ATHMAN KOECH(saumu@aims.ac.za)")
print("\n")
print(70 * "#")
bank_account.services_offered()
while True:
    option = int(input("Select the service: "))
    print(20 * "_")
    if option == 0:
        bank_account.open_account()
        print(50 * "#")
        bank_account.services_offered()
    elif option == 1:
        bank_account.deposit()
        print(50 * "#")
        bank_account.services_offered()
    elif option == 2:
        bank_account.withdraw()
        print(50 * "#")
        bank_account.services_offered()
    elif option == 3:
        bank_account.bal()
        print(50 * "#")
        bank_account.services_offered()
    elif option == 4:
        bank_account.display_all()
        print(50 * "#")
        bank_account.services_offered()
    elif option == 5:
        bank_account.display_ac()
        print(50 * "#")
        bank_account.services_offered()
    elif option == 6:
        bank_account.clear_account()
        print(50 * "#")
        bank_account.services_offered()
    elif option == 7:
        bank_account.close_account()
        print(50 * "#")
        bank_account.services_offered()
    elif option == 8:
        print(50 * "*")
        print(5 * "*", "Thank you for banking with us.", 12 * "*")
        print(50 * "*")
        break
    else:
        # Give an invalid selection alert and allow the user to input the selection again.
        print("Invalid selection")
        print(50 * "#")


