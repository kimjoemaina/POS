# class MyNumber:
#     def __init__(self, number):
#         self.number = number
    
#     def returnNumber(self):
#         return self.number
    
# var = MyNumber(7)

# print(var.returnNumber())
import json
from operator import indexOf
import random
from textwrap import indent

filename = "customer.json"

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
        

def view_customer_database():
    with open(filename, "r") as customer_db:
        customer_data = json.load(customer_db)
        i = 0
        for item in customer_data:
            customer_id = item["customer_id"]
            name = item["name"]
            age = item["age"]
            phone_no = item["phone_no"]
            email = item["email"]
            
            print(f'Entry: {i}')
            print(f"Customer ID: {customer_id}")
            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"Phone No.: {phone_no}")
            print(f"Email: {email}")
            print("\n")
            i += 1
            
def delete_customer():
    view_customer_database()
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
                print(f"Email: {email}")
            i += 1

        
        attribute = input("Which attribute would you like to modify?")
        print("")



if __name__ == "__main__":
    update_customer()