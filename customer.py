from datetime import datetime
import random
import json

filename = "customer.json"

class Customer:
    def __init__(self, customer_id, first_name, last_name, age, phone, email, city, reg_date):
        """ Enter Customer Details """
        self.customer_id = int(customer_id)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = phone
        self.email = email
        self.city = city
        self.reg_date = reg_date

    def __str__(self):
        customer_info = (f"""
        Customer ID: {self.customer_id}
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Age: {self.age}
        Phone No.: {self.phone}
        Email: {self.email}
        City: {self.city}
        Registration Date: {self.reg_date}
        """)
        return customer_info

        
# View customer menu
def customer_menu():
    while True:
        print("Select a Customer Operation.")
        print(" [1] Add customer ")
        print(" [2] Delete customer ")
        print(" [3] Update customer ")
        print(" [4] View customer")
        print(" [5] View customer database ")
        print(" [6] Main Menu ")

        # print(" (6) Go back ")
        selection = int(input("Enter your choice : \n"))

        if selection == 1:
            add_customer()
            customer_menu()
            break
        elif selection == 2:
            delete_customer()
            customer_menu()
            break
        elif selection == 3:
            update_customer()
            break
        elif selection == 4:
            view_customer()
            customer_menu()
            break
        elif selection == 5:
            view_customer_db()
            customer_menu()
            break
        elif selection == 6:
            from main import menu
            menu()
            break
        else:
            print("\nInvalid selection! Please try again.\n")

# 1. Add customer to JSON file
def add_customer():
    with open(filename) as customer_db:
        customer_data = json.load(customer_db)
        customer_id = random.randint(1000, 9999)
        first_name = input("First Name:\n").capitalize()
        last_name = input("Last Name:\n").capitalize()
        age = input("Age:\n")
        phone_no = input("Phone No.:\n")
        email = input("Email:\n")
        city = input("City of Residence:\n").capitalize()
        registration_date = datetime.now()
        date = registration_date.strftime("%d/%m/%Y")

        
        new_customer = Customer(customer_id, first_name, last_name, age, phone_no, email, city, date)
        c_details = new_customer.__dict__
        customer_data.append(c_details)  
        
    with open(filename, "w") as f:
        json.dump(customer_data, f, indent=4)
    print(f"\nCustomer {customer_id} added successfully!\n")


# 2. Delete customer from JSON File
def delete_customer():
    with open(filename) as customer_db:
        customer_data = json.load(customer_db)
        c_ref = int(input("Enter Customer ID:\n"))
        
        j = 0

        # iterate over customer_data list
        for i in customer_data:
            if i["customer_id"] == c_ref:
                for key, value in i.items():
                    print("{} : {}".format(key, value))
                warning = input("\nAre you sure? ***THIS ACTION IS IRREVERSIBLE*** (Y/N)\n").upper()
                if warning == "Y":
                    customer_data.pop(j)
                    print(f"\nCustomer {c_ref} deleted successfully!\n")
                    break
                elif warning == "N":
                    print("\nNo changes made!\n")
                    break
                else:
                    print("\nInvalid input!\n")
                    break
            j += 1
        else:
            print("\nCustomer not found!\n")


    with open(filename, "w") as f:
        json.dump(customer_data, f, indent=4)
               

# 3. Update customer details
def update_customer():
    with open(filename) as customer_db:
        customer_data = json.load(customer_db)
        update_c = int(input("Which customer would you like to update?\nEnter Customer ID:\n"))

        for i in customer_data:            
            c = Customer(i["customer_id"], i["first_name"], i["last_name"], i["age"], i["phone"], i["email"], i["city"], i["reg_date"])
            d = c.__dict__
            if d["customer_id"] == update_c:
                print(c)

                print('''
                [1] Customer ID
                [2] First Name
                [3] Last Name
                [4] Age
                [5] Phone No.
                [6] Email
                [7] City
                ''')

                # update attribute
                update_a = int(input("Which attribute you like to update?\n"))
                # Customer ID update
                if update_a == 1:
                    new_id = random.randint(1000,9999)
                    confirm = input("\nAre you sure of this action? (Y/N)\n*** THIS ACTION IS IRREVERSIBLE! ***\n").upper()
                    if confirm == "Y":
                        i["customer_id"] = new_id
                        print(f'\nCustomer updated successfully! New ID: {new_id}.\n')
                        break
                    elif confirm == "N":
                        print("\nNo changes made!\n")
                        break
                    else:
                        print("\nInvalid input!\n")
                        break

                # Customer First Name update
                elif update_a == 2:
                    new_first_name = input("Enter new first name:\n").capitalize()
                    confirm = input("\nAre you sure of this action? (Y/N)\n*** THIS ACTION IS IRREVERSIBLE! ***\n").upper()
                    if confirm == "Y":
                        i["first_name"] = new_first_name
                        print(f'\nCustomer updated successfully! New first name: {new_first_name}.\n')
                        break
                    elif confirm == "N":
                        print("\nNo changes made!\n")
                        break
                    else:
                        print("\nInvalid input!\n")
                        break

                # Customer last name update
                elif update_a == 3:
                    new_last_name = input("Enter new last name:\n").capitalize()
                    confirm = input("\nAre you sure of this action? (Y/N)\n*** THIS ACTION IS IRREVERSIBLE! ***\n").upper()
                    if confirm == "Y":
                        i["last_name"] = new_last_name
                        print(f'\nCustomer updated successfully! New last name: {new_last_name}.\n')
                        break
                    elif confirm == "N":
                        print("\nNo changes made!\n")
                        break
                    else:
                        print("\nInvalid input!\n")
                        break

                # Customer age update
                elif update_a == 4:
                    new_age = input("Enter new age:\n")
                    confirm = input("\nAre you sure of this action? (Y/N)\n*** THIS ACTION IS IRREVERSIBLE! ***\n").upper()
                    if confirm == "Y":
                        i["age"] = new_age
                        print(f'\nCustomer updated successfully! New age: {new_age}.\n')
                        break
                    elif confirm == "N":
                        print("\nNo changes made!\n")
                        break 
                    else:
                        print("\nInvalid input!\n")
                        break

                # Customer Phone No. update
                elif update_a == 5:
                    new_phone_no = input("Enter new phone number:\n")
                    confirm = input("\nAre you sure of this action? (Y/N)\n*** THIS ACTION IS IRREVERSIBLE! ***\n").upper()
                    if confirm == "Y":
                        i["phone"] == new_phone_no
                        print(f'\nCustomer updated successfully! New Phone No.: {new_phone_no}.\n')
                        break
                    elif confirm == "N":
                        print("\nNo changes made!\n")
                        break
                    else:
                        print("\nInvalid input!\n")
                        break

                # Customer email update
                elif update_a == 6:
                    new_email = input("Enter new email:\n")
                    confirm = input("\nAre you sure of this action? (Y/N)\n*** THIS ACTION IS IRREVERSIBLE! ***\n").upper()
                    if confirm == "Y":
                        i["email"] = new_email
                        print(f'\nCustomer updated successfully! New email: {new_email}.\n')
                        break
                    elif confirm == "N":
                        print("\nNo changes made!\n")
                        break
                    else:
                        print("\nInvalid input!\n")
                        break

                # Customer city update
                elif update_a == 7:
                    new_city = input("Enter new city:\n")
                    confirm = input("\nAre you sure of this action? (Y/N)\n*** THIS ACTION IS IRREVERSIBLE! ***\n").upper()
                    if confirm == "Y":
                        i["city"] = new_city
                        print(f'\nCustomer updated successfully! New city: {new_city}.\n')
                        break
                    elif confirm == "N":
                        print("\nNo changes made!\n")
                        break
                    else:
                        print("\nInvalid input!\n")
                        break
                else:
                    print("\nInvalid entry. Try again!\n")
                    break
        else:
            print("\nCustomer not found!\n")
                    
    with open(filename, "w") as f:
        json.dump(customer_data, f, indent=4)
    customer_menu()

# 4. View customer details using Customer ID
def view_customer():
    with open(filename) as customer_db:
        customer_data = json.load(customer_db)
        c_ref = int(input("Enter Customer ID:\n"))
        for i in customer_data:
            # instance of customer class
            c = Customer(i["customer_id"], i["first_name"], i["last_name"], i["age"], i["phone"], i["email"], i["city"], i["reg_date"])
            d = c.__dict__
            if d["customer_id"] == c_ref:
                print(c)
                return d
        else:
            print("\nCustomer not found!\n")
            
# 5. View customer Database
def view_customer_db():
    with open(filename, "r") as customer_db:
        customer_data = json.load(customer_db)
        view_query = int(input("[1] View All\n[2] Sort by Customer ID\n[3] Sort by Name\n[4] Sort by Date\n"))
        j=0
        

        if view_query == 1:
            for i in customer_data:
                c = Customer(i["customer_id"], i["first_name"], i["last_name"], i["age"], i["phone"], i["email"], i["city"], i["reg_date"])
                print(c)

        elif view_query == 2:
            pass
  
if __name__ == "__main__":
    view_customer_db()