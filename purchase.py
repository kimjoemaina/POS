from audioop import add
from customer import view_customer, add_customer
from datetime import datetime
import json

purchases = "purchases.json"
products = "products.json"
customers = "customer.json"

class Purchase:
    def __init__(self, customer_id, customer_name, product_name, price, quantity, date):
        ''' Calculate total amout '''
        assert type(price) == int and type(quantity) == int, "ints not used"
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.date = date
    
    def checkout(self):
        return self.price * self.quantity
   
def purchase_operations():
    while True:
        print("  ***** Purchase Operations *****")
        print("  [1] Sell")
        print("  [2] View customer transactions.")
        print("  [3] Main Menu")

        selection = int(input("Select option:\n"))

        if selection == 1:
            check = input("New or existing customer?\n[N] New\n[E] Existing\n").upper()
            if check == "N":
                new_customer = add_customer()
                print(new_customer)
                break
            elif check == "E":
                sell_something()
                break
            else:
                print("Invalid input! Try again.")
        elif selection == 2:
            pass
        elif selection == 3:
            from main import menu
            menu()
            break
        else:
            print("Invalid selection! Try again.")

def sell_something():
    
    with open(customers) as customer_db:
        customer_data = json.load(customer_db)
        customer = view_customer()  
    with open(products) as product_db:
        product_data = json.load(product_db)
        sell = input("What would you like to sell?\nEnter product SKU:\n")

    with open(purchases) as purchase_db:
        purchase_data = json.load(purchase_db)
        
        for i in product_data:
            if i["sku"] == sell:
                print(f'\nSKU: {i["sku"]}')
                print(f'Product Category: {i["product_category"]}')
                print(f'Product Name: {i["product_name"]}')
                print(f'Price: {i["product_price"]}\n')

                c_id = customer["customer_id"]
                c_name = customer["first_name"]
                price = i["product_price"]
                prod_name = i["product_name"]
                quantity = int(input("QTY:\n"))
                today = datetime.now()
                date = today.strftime("%d/%m/%Y")
                purchase = Purchase(c_id, c_name, prod_name, price, quantity, date)
                first_purchase = purchase.__dict__
                first_checkout = purchase.checkout()
                first_purchase.update({"Total" : first_checkout})
                purchase_data.append(purchase.__dict__)
                
                while True:
                    confirmation = input("Would you like anything else? (Y/N)\n").upper()
                    
                    if confirmation == "Y":
                        other_item = input("Enter product SKU:\n")
                        for i in product_data:
                            if i["sku"] == other_item:
                                print(f'\nSKU: {i["sku"]}')
                                print(f'Product Category: {i["product_category"]}')
                                print(f'Product Name: {i["product_name"]}')
                                print(f'Price: {i["product_price"]}\n')

                                c_id = customer["customer_id"]
                                c_name = customer["first_name"]
                                price = i["product_price"]
                                prod_name = i["product_name"]

                                quantity = int(input("QTY:\n"))
                                today = datetime.now()
                                date = today.strftime("%d/%m/%Y")
                                purchase = Purchase(c_id, c_name, prod_name, price, quantity, date)                                
                                purchase_data.append(purchase.__dict__)
                    elif confirmation == "N":
                        break
                    else:
                        print("Invalid input. Try again.")
    
    with open(purchases, "w") as f:
        json.dump(purchase_data, f, indent=4)


if __name__ == "__main__":
    purchase_operations()