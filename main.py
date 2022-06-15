from customer import customer_menu
from product import product_menu
from purchase import purchase_operations

def menu():
    while True:
        print('''
        --------------- Welcome to the POS -------------
                ---------- Select a Menu ----------

                    1 : Customer Operations
                    2 : Product Operations
                    3 : Purchase Operations
                    4 : Exit

                    ---------- End ----------
        ''')

        try:
            selection = int(input('\n\tEnter your choice:\n\t'))
            if selection == 1:
                customer_menu()
                break
            elif selection == 2:
                product_menu()
                break
            elif selection == 3:
                purchase_operations()
                break
            elif selection == 4:
                break
            else:
                print("\n\t\tInvalid selection. Try again.\n")
        except ValueError:
            print("\n\t\tInvalid input! Please enter a valid value.\n")
        
     

if __name__ == "__main__":
    menu()