from customer import customer_menu
from product import product_menu
from purchase import purchase_operations

def menu():
    while True:
        print("***** Welcome to the POS *****")
        print("***** Please choose a menu ******")
        print(" 1 : Customer Operations")
        print(" 2 : Product Operations")
        print(" 3 : Purchase Operations")

        selection = int(input(" Enter your choice: \n"))

        if selection == 1:
            customer_menu()
            break
        elif selection == 2:
            product_menu()
            break
        elif selection == 3:
            purchase_operations()
            break
        else:
            print(" Wrong selection, enter again. ")


if __name__ == "__main__":
    menu()