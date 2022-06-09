from customer import customer_menu
from product import product_menu
from purchase import purchase_operations

def menu():
    while True:
        print("***** Welcome to the POS *****")
        print("***** Please select a menu ******")
        print(" 1 : Customer Operations")
        print(" 2 : Product Operations")
        print(" 3 : Purchase Operations")
        print(" 4 : Exit")


        selection = input("Enter your choice:\n")

        if selection.isdigit():
            if selection == "1":
                customer_menu()
                break
            elif selection == "2":
                product_menu()
                break
            elif selection == "3":
                purchase_operations()
                break
            elif selection == "4":
                exit()
            else:
                print("\nWrong selection, enter again.\n")
        else:
            print("\nInvalid input! Try again.\n")

if __name__ == "__main__":
    menu()