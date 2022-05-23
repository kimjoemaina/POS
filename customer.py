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
        print(" (6) Go back ")
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
        elif selection == 5:
            view_customer_db()
            break

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
        # print(f"Customer {customer_id} added successfully!")

    with open(filename, "w") as f:
        json.dump(customer_data, f, indent=4)
    print(f"Customer {customer_id} added successfully!")

        
    
def delete_customer():
    view_customer_db()
    c_data = []
    with open(filename, "r") as customer_db:
        customer_data = json.load(customer_db)
        c_index = len(customer_data) - 1
        id = int(input(f"Enter customer index to delete: (0 - {c_index})\n")) #3
        i = 0
        for c in customer_data:
            if i == id:
                pass
                i += 1
            else:
                c_data.append(c)
                i += 1

    with open(filename, "w") as f:
        json.dump(c_data, f, indent=4)
    print(f"Customer {id} deleted successfully!")

def update_customer():
    print("Later")
    
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
            
            print(f"Index: {i}")
            print(f"Customer ID: {customer_id}")
            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"Phone No.: {phone_no}")
            print(f"Email: {email}")
            print("\n")
            i += 1
  
if __name__ == "__main__":
    customer_menu()