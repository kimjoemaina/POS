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
            Customer ID         : {self.customer_id}
            First Name          : {self.first_name}
            Last Name           : {self.last_name}
            Age                 : {self.age}
            Phone No.           : {self.phone}
            Email               : {self.email}
            City                : {self.city}
            Registration Date   : {self.reg_date}
        """)
        return customer_info

        
# View customer menu
def customer_menu():
    while True:
        print('''
        ------------ Customer Menu ------------

        Select a Customer Operation.

        [1] Add customer
        [2] Delete customer
        [3] Update customer
        [4] View customer
        [5] View customer database
        [6] No. of customers in DB
        [7] Main Menu

            ------------ End ------------
        ''')
    
        try:
            selection = int(input("\n\tEnter your choice:\n\t"))
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
                customer_menu()
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
                query_no_of_customers()
                customer_menu()
                break   
            elif selection == 7:
                from main import menu
                menu()
                break
            else:
                print("\n\tInvalid selection! Please try again.\t\t")
        except:
            print("\n\tInvalid input! Please enter a valid value.\t\t")
            
        
# 1. Add customer to JSON file
def add_customer():
    with open(filename) as customer_db:
        customer_data = json.load(customer_db)
        customer_id = random.randint(1000, 9999)
        first_name = input("\n\tFirst Name:\n\t").capitalize()
        last_name = input("\n\tLast Name:\n\t").capitalize()
        age = input("\n\tAge:\n\t")
        phone_no = input("\n\tPhone No.:\n\t")
        email = input("\n\tEmail:\n\t")
        city = input("\n\tCity of Residence:\n\t").capitalize()
        registration_date = datetime.now()
        date = registration_date.strftime("%d/%m/%Y")

        
        new_customer = Customer(customer_id, first_name, last_name, age, phone_no, email, city, date)
        c_details = new_customer.__dict__
        customer_data.append(c_details)  
        
    with open(filename, "w") as f:
        json.dump(customer_data, f, indent=4)
    print(f"\n\tCustomer {customer_id} added successfully!\n\t")


# 2. Delete customer from JSON File
def delete_customer():
    with open(filename) as customer_db:
        customer_data = json.load(customer_db)
        while True:
            try:
                c_ref = int(input("\n\tEnter Customer ID (Numbers only):\n\t"))
                j = 0
                # iterate over customer_data list
                for i in customer_data:
                    if i["customer_id"] == c_ref:
                        for key, value in i.items():
                            print("\t{} : {}\t".format(key, value))
                        warning = input("\n\tAre you sure?***THIS ACTION IS IRREVERSIBLE*** (Y/N)\n\t").upper()
                        if warning == "Y":
                            customer_data.pop(j)
                            print(f"\n\tCustomer {c_ref} deleted successfully!\n\t")
                            break
                        elif warning == "N":
                            print("\n\tNo changes made!\n\t")
                            break
                        else:
                            print("\n\tInvalid input! Exiting...\n\t")
                            break
                    j += 1
                else:
                    print("\n\tCustomer not found!\n\t")
                break
            except ValueError:
                print("\n\tInvalid input. Please enter a valid value.\n\t")
            
    with open(filename, "w") as f:
        json.dump(customer_data, f, indent=4)
               

# 3. Update customer details
def update_customer():
    with open(filename) as customer_db:
        customer_data = json.load(customer_db)
        while True:   
            try: 
                update_c = int(input("\n\tWhich customer would you like to update?\n\tEnter Customer ID:\n\t"))
                break
            except ValueError:
                print("\n\tInvalid input.\n")

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
                while True:
                    try:
                        update_a = int(input("\n\tWhich attribute you like to update?\n\t"))
                        break
                    except ValueError:
                        print("\n\tInvalid value. Try again.\n\t")
                # Customer ID update
                if update_a == 1:
                    new_id = random.randint(1000,9999)
                    confirm = input('\n\tAre you sure of this action? (Y/N)\n\t*** THIS ACTION IS IRREVERSIBLE! ***\n\t').upper()
                    if confirm == "Y":
                        i["customer_id"] = new_id
                        print(f"\n\tCustomer updated successfully! New ID: {new_id}.\n\t")
                        break
                    elif confirm == "N":
                        print("\n\tNo changes made!\n\t")
                        break
                    else:
                        print("\n\tInvalid input!\n\t")
                        break
                # Customer First Name update
                elif update_a == 2:
                    new_first_name = input("\n\tEnter new first name:\"").capitalize()

                    confirm = input("\n\tAre you sure of this action? (Y/N)\"*** THIS ACTION IS IRREVERSIBLE! ***\n\t").upper()

                    if confirm == "Y":
                        i["first_name"] = new_first_name
                        print(f"\n\tCustomer updated successfully! New first name: {new_first_name}.\n\t")
                        break
                    elif confirm == "N":
                        print("\n\tNo changes made!\n\t")
                        break
                    else:
                        print("\n\tInvalid input!\n\t")
                        break

                # Customer last name update
                elif update_a == 3:
                    new_last_name = input("\n\tEnter new last name:\"").capitalize()
                    confirm = input("\n\tAre you sure of this action? (Y/N)\n\t*** THIS ACTION IS IRREVERSIBLE! ***\n\t").upper()
                    if confirm == "Y":
                        i["last_name"] = new_last_name
                        print(f"\n\tCustomer updated successfully! New last name: {new_last_name}.\n\t")
                        break
                    elif confirm == "N":
                        print("\n\tNo changes made!\n\t")
                        break
                    else:
                        print("\n\tInvalid input!\n\t")
                        break

                # Customer age update
                elif update_a == 4:
                    new_age = input("\n\tEnter new age:\n\t")
                    confirm = input("Are you sure of this action? (Y/N)\n\t*** THIS ACTION IS IRREVERSIBLE! ***\n\t").upper()
                    if confirm == "Y":
                        i["age"] = new_age
                        print(f"\n\tCustomer updated successfully! New age: {new_age}.\n\t")
                        break
                    elif confirm == "N":
                        print("\n\tNo changes made!\n\t")
                        break 
                    else:
                        print("\n\tInvalid input\n\t")
                        break

                # Customer Phone No. update
                elif update_a == 5:
                    new_phone_no = input('\n\tEnter new phone number:\n\t')
                    confirm = input("\n\tAre you sure of this action? (Y/N)\n\t*** THIS ACTION IS IRREVERSIBLE! ***\n\t").upper()
                    if confirm == "Y":
                        i["phone"] == new_phone_no
                        print(f'\n\tCustomer updated successfully! New Phone No.: {new_phone_no}.\n\t')
                        break
                    elif confirm == "N":
                        print("\n\tNo changes made!\n\t")
                        break
                    else:
                        print("\n\tInvalid input!\n\t")
                        break

                # Customer email update
                elif update_a == 6:
                    new_email = input("\n\tEnter new email:\n\t")
                    confirm = input("\n\tAre you sure of this action? (Y/N)\n\t*** THIS ACTION IS IRREVERSIBLE! ***\n\t").upper()
                    if confirm == "Y":
                        i["email"] = new_email
                        print(f"Customer updated successfully! New email: {new_email}.\n\t")
                        break
                    elif confirm == "N":
                        print("\n\tNo changes made!\n\t")
                        break
                    else:
                        print("\n\tInvalid input!\n\t")
                        break

                # Customer city update
                elif update_a == 7:
                    new_city = input("\n\tEnter new city:\n\t")
                    confirm = input("\n\tAre you sure of this action? (Y/N)\n\t*** THIS ACTION IS IRREVERSIBLE! ***\n\t").upper()
                    if confirm == "Y":
                        i["city"] = new_city
                        print(f"\n\tCustomer updated successfully! New city: {new_city}.\n\t")
                        break
                    elif confirm == "N":
                        print("\n\tNo changes made!\n\t")
                        break
                    else:
                        print("\n\tInvalid input!\n\t")
                        break
                else:
                    print("\n\tInvalid entry. Try again!\n\t")
                    break
        else:
            print("\n\tCustomer not found!\n\t")
                    
    with open(filename, "w") as f:
        json.dump(customer_data, f, indent=4)
    customer_menu()

# 4. View customer details using Customer ID
def view_customer():
    with open(filename) as customer_db:
        customer_data = json.load(customer_db)

    while True:
        try:
            c_ref = int(input("\n\tEnter Customer ID:\n\t"))
            break
        except ValueError:
            print("\n\tInvalid input! Try again.\n\t")

    for i in customer_data:
        # instance of customer class
        c = Customer(i["customer_id"], i["first_name"], i["last_name"], i["age"], i["phone"], i["email"], i["city"], i["reg_date"])
        d = c.__dict__
        if d["customer_id"] == c_ref:
            print(c)
            return d
    else:
        print("\n\tCustomer not found!\n\t")
            
# 5. View customer Database
def view_customer_db():
    with open(filename, "r") as customer_db:
        customer_data = json.load(customer_db)

        while True:
            try:
                view_query = int(input("\n\t[1] View All\n\t[2] Sort by Customer ID\n\t[3] Sort by Name\n\t"))
                break
            except ValueError:
                print("\n\tInvalid input. Try again!\n\t")

        if customer_data == []:
            print("\n\tNo customers found in database.\n\t")
        for i in customer_data:
            c = Customer(i["customer_id"], i["first_name"], i["last_name"], i["age"], i["phone"], i["email"], i["city"], i["reg_date"])
            if view_query == 1:
                print(c)
            elif view_query == 2:
                order_id = input("\n\tSort:\n\t[A] Ascending\n\t[D] Descending\n\t(Enter A/D)\n\t").upper()
                if order_id == "A":
                    sorted_by_id = sorted(customer_data, key = lambda i: i["customer_id"])
                    for s in sorted_by_id:
                        print(f'''
                        Customer ID         : {s["customer_id"]}
                        Name                : {s["first_name"]} {s["last_name"]}
                        Age                 : {s["age"]}
                        Phone               : {s["phone"]}
                        Email               : {s["email"]}
                        City                : {s["city"]}
                        Registration Date   : {s["reg_date"]}
                        ''')
                    break                        
                elif order_id == "D":
                    sorted_by_id = sorted(customer_data, key = lambda d: d["customer_id"], reverse=True)
                    for s in sorted_by_id:
                        print(f'''
                        Customer ID         : {s["customer_id"]}
                        Name                : {s["first_name"]} {s["last_name"]}
                        Age                 : {s["age"]}
                        Phone               : {s["phone"]}
                        Email               : {s["email"]}
                        City                : {s["city"]}
                        Registration Date   : {s["reg_date"]}
                        ''')
                    break
                else:
                    print("\n\tInvalid input. Try again.\n\t")
            elif view_query == 3:
                order_name  = input("Sort:\n[A] Ascending\n[D] Descending\n(Enter A/D)\n").upper()
                if order_name == "A":
                    sorted_by_name = sorted(customer_data, key = lambda n: n["first_name"])
                    for s in sorted_by_name:
                        print(f'''
                        Customer ID         : {s["customer_id"]}
                        Name                : {s["first_name"]} {s["last_name"]}
                        Age                 : {s["age"]}
                        Phone               : {s["phone"]}
                        Email               : {s["email"]}
                        City                : {s["city"]}
                        Registration Date   : {s["reg_date"]}
                        ''')
                    break
                elif order_name == "D":
                    sorted_by_name = sorted(customer_data, key = lambda n: n["first_name"], reverse=True)
                    for s in sorted_by_name:
                        print(f'''
                        Customer ID         : {s["customer_id"]}
                        Name                : {s["first_name"]} {s["last_name"]}
                        Age                 : {s["age"]}
                        Phone               : {s["phone"]}
                        Email               : {s["email"]}
                        City                : {s["city"]}
                        Registration Date   : {s["reg_date"]}
                        ''')
                    break
                else:
                    print("\n\tInvalid input! Try again.\n\t")
                    break
            else:
                print("\n\tWrong selection! Exiting...\n\t")
                break
# Query no of customers in db                    
def query_no_of_customers():
    with open (filename) as customer_db:
        customer_data = json.load(customer_db)
        j = 0

        for i in customer_data:
            j += 1
        print(f"\n\tThere are {j} customers in the database!\n\t")
