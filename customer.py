import random
import json

filename = "customer.json"

class Customer:
    def __init__(self, customer_id, first_name, last_name, age, phone, email, city):
        """ Enter Customer Details """
        # assert customer_id == int, "Customer ID should be int!"

        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = phone
        self.email = email
        self.city = city

    def person(self):
        c_details = {"Customer ID": self.customer_id, "First Name": self.first_name, "Last Name": self.last_name, "Age": self.age, "Phone No.": self.phone, "Email": self.email, "City": self.city}
        return c_details

    def __str__(self):
        customer_info = (f"""
        Customer ID: {self.customer_id}
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Age: {self.age}
        Phone No.: {self.phone}
        Email: {self.email}
        City: {self.city}
        """)
        return customer_info
        
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
        # elif selection == 3:
        #     update_customer()
        #     break
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
        customer_id = str(random.randint(1000, 9999))
        first_name = input("First Name:\n").capitalize()
        last_name = input("Last Name:\n").capitalize()
        age = input("Age:\n")
        phone_no = input("Phone No.:\n")
        email = input("Email:\n")
        city = input("City of Residence:\n")
        
        new_customer = Customer(customer_id, first_name, last_name, age, phone_no, email, city)
        customer_data.append(new_customer.person())
        

    with open(filename, "w") as f:
        json.dump(customer_data, f, indent=4)
    print(f"Customer {customer_id} added successfully!")

def delete_customer():
    with open(filename) as customer_db:
        customer_data = json.load(customer_db)
        c_ref = input("Enter Customer ID:\n")
        warning = input("Are you sure? ***THIS ACTION IS IRREVERSIBLE*** (Y/N)\n").upper()
        j = 0

        # iterate over customer_data list
        for i in customer_data:
            if i["Customer ID"] == c_ref:
                customer_data.pop(j)
            j += 1
        
        
        # if warning == "Y":
        #     print(f"Customer {c_ref} deleted successfully!")
        # elif warning == "N":
        #     print("No changes made!")
        # else:
        #     print("Invalid Entry. Try again.")


        with open(filename, "w") as f:
            json.dump(customer_data, f, indent=4)
        

# View customer details using Customer ID
def view_customer():
    with open(filename) as customer_db:
        customer_data = json.load(customer_db)
        c_ref = input("Enter Customer ID:\n")
        j = 0

        for i in customer_data:
            c = Customer(i["Customer ID"], i["First Name"], i["Last Name"], i["Age"], i["Phone No."], i["Email"], i["City"])
            d = c.person()
            if d["Customer ID"] == c_ref:
                print(c)
            j += 1

# View customer Database
def view_customer_db():
    with open(filename, "r") as customer_db:
        customer_data = json.load(customer_db)

        for c in customer_data:
            c = Customer(c["Customer ID"], c["First Name"], c["Last Name"], c["Age"], c["Phone No."], c["Email"], c["City"])
            print(c)
  
if __name__ == "__main__":
    delete_customer()