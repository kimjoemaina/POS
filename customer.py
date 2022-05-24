from fileinput import filename
import random
import json


filename = "customer.json"
# class Customer:
#     def __init__(self, customer_id, name, age, phoneNo):
#         self.customer_id = customer_id
#         self.name = name
#         self.age = age
#         self.phone = phoneNo
def customer_menu():
    while True:
        print("Select a Customer Operation.")
        print(" (1) Add customer ")
        print(" (2) Delete customer ")
        print(" (3) Update customer ")
        print(" (4) View customer")
        print(" (5) View customer database ")
        # print(" (6) Go back ")
        selection = int(input("Enter your choice : \n"))

        if selection == 1:
            add_customer()
            break
        elif selection == 2:
            delete_customer()
            break
        elif selection == 3:
            update_customer()
            break
        elif selection == 4:
            view_customer()
            break
        elif selection == 5:
            view_customer_db()
            break
        else:
            print("Invalid selection! Please try again.")

def add_customer():
    with open(filename) as customer_db:
        customer_data = json.load(customer_db)
        id_generator = str(random.randint(1000, 9999))
        customer_id = id_generator
        name = input("Customer name:\n").capitalize()
        age = input("Age:\n")
        phone_no = input("Enter customer phone:\n")
        email = input("Customer Email:\n")
        new_customer = {"customer_id": customer_id, "name": name, "age": age, "phone_no": phone_no, "email": email}
        customer_data.append(new_customer)

    with open(filename, "w") as f:
        json.dump(customer_data, f, indent=4)
    print(f"Customer {customer_id} added successfully!")

def delete_customer():
    view_customer_db()
    c_data = []
    with open(filename, "r") as customer_db:
        customer_data = json.load(customer_db)
        c_index = len(customer_data) - 1
        id = int(input(f"Enter customer entry to delete: (0 - {c_index})\n"))
        warning = input("Are you sure? *** THIS ACTION IS IRREVERSIBLE! *** (Y/N)\n").upper()
        i = 0
        
        for c in customer_data:
            if warning == "Y":
                if i == id:
                    pass
                    i += 1
                else:
                    c_data.append(c)
                    i += 1
            elif warning == "N":
                c_data.append(c)
                i += 1
        
        if warning == "Y":
            print(f"Customer {id} deleted successfully!")
        elif warning == "N":
            print(f"No changes made!")

    with open(filename, "w") as f:
        json.dump(c_data, f, indent=4)

def update_customer():
    view_customer_db()
    with open(filename, "r") as customer_db:
        customer_data = json.load(customer_db)
        id_generator = str(random.randint(1000, 9999))
        c_entry = len(customer_data) - 1
        id = int(input(f"Which entry would you like to modify? 0 - {c_entry}\n"))
        i = 0
        for c in customer_data:
            if i == id:
                customer_id = c["customer_id"]
                name = c["name"]
                age = c["age"]
                phone_no = c["phone_no"]
                email = c["email"]
                
                print(f"Customer ID: {customer_id}")
                print(f"Name: {name}")
                print(f"Age: {age}")
                print(f"Phone No.: {phone_no}")
                print(f"Email: {email}\n")
            i += 1
        print("Which attribute would you like to modify?")
        print(" (1) Customer ID ")
        print(" (2) Name ")
        print(" (3) Age")
        print(" (4) Phone No.")
        print(" (5) Email ")
        attribute = int(input(""))

        n = 0
        for p in customer_data:
            if n == id:
                if attribute == 1:
                    p["customer_id"] = id_generator
                    break
                elif attribute == 2:
                    p["name"] = input("Enter new name:\n")
                    break
                elif attribute == 3:
                    p["age"] == input("Enter new age:\n")
                elif attribute == 4:
                    p["phone_no"] == input("Enter new Phone No.:\n")
                elif attribute == 5:
                    p["email"] == input("Enter new Email: \n")
            n += 1

    with open(filename, "w") as f:
        json.dump(customer_data, f, indent=4)
    print("Customer details updated successfully!")

def view_customer():
    view_customer_db()
    with open(filename) as customer_db:
        customer_data = json.load(customer_db)
        id = int(input("Entry to view:\n"))
        i = 0
        for c in customer_data:
            if i == id:
                customer_id = c["customer_id"]
                name = c["name"]
                age = c["age"]
                phone_no = c["phone_no"]
                email = c["email"]
                
                print(f"Customer ID: {customer_id}")
                print(f"Name: {name}")
                print(f"Age: {age}")
                print(f"Phone No.: {phone_no}")
                print(f"Email: {email}\n")
            i += 1


def view_customer_db():
    with open(filename, "r") as customer_db:
        customer_data = json.load(customer_db)
        i = 0
        for item in customer_data:
            customer_id = item["customer_id"]
            name = item["name"]
            age = item["age"]
            phone_no = item["phone_no"]
            email = item["email"]
            
            print(f"Entry: {i}")
            print(f"Customer ID: {customer_id}")
            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"Phone No.: {phone_no}")
            print(f"Email: {email}")
            print("\n")
            i += 1
  
if __name__ == "__main__":
    customer_menu()