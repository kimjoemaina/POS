from customer import view_customer, add_customer
from datetime import datetime
import json
import random

purchase_file = "purchases.json"
products = "products.json"
customers = "customer.json"

class Purchase:
    def __init__(self, transaction_id, customer_id, customer_name, product_skus, product_name, price, quantities, date):
        ''' Calculate total amout '''
        self.transaction_id = transaction_id
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.product_sku = product_skus
        self.product_name = product_name
        self.price = int(price)
        self.quantities = int(quantities)
        self.date = date
    
    def checkout(self):
        return self.price * self.quantities
   
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
            elif check == "E":
                sell()
                purchase_operations()
                break
            else:
                print("\nInvalid input! Try again.\n")
        elif selection == 2:
            search_transactions()
        elif selection == 3:
            from main import menu
            menu()
            break
        else:
            print("\nInvalid selection! Try again.\n")

def sell():
    product_skus = []
    product_names = []
    prices_list = []
    quantity_list = []
    totals_list = []
    transaction_id = str(random.randint(100000, 9999999))
    new_order = True

    
    with open(customers) as customer_db:
        customer_data = json.load(customer_db)
        customer = view_customer()

        if customer == None:
            purchase_operations()

    with open(products) as product_db:
        product_data = json.load(product_db)
        print("What would you like to sell?\n")
        

    with open(purchase_file) as purchase_db:
        purchase_data = json.load(purchase_db)

    while new_order:
        product_id = input("Enter product SKU:\n")
        for i in product_data:
            if i["sku"] == product_id:
                print(f'\nSKU: {i["sku"]}')
                print(f'Product Category: {i["product_category"]}')
                print(f'Product Name: {i["product_name"]}')
                print(f'Price: {i["product_price"]}\n')

                c_id = customer["customer_id"]
                c_name = f'{customer["first_name"]} {customer["last_name"]}'
                price = i["product_price"]
                prod_sku = i["sku"]
                prod_name = (i["product_name"])
                while True:
                    quantity = int(input("Quantity (QTY):\n"))
                    if quantity > i["stock_capacity"]:
                        print(f'\nQuantity entered exceeds stock available. Available Quantity: {i["stock_capacity"]}.\n')
                    elif quantity < i["stock_capacity"]:
                        break
                
                today = datetime.now()
                date = today.strftime("%d/%m/%Y")
                purchases = Purchase(transaction_id, c_id, c_name, prod_sku, prod_name, price, quantity, date)
                totals = purchases.checkout()
                purchase = purchases.__dict__
                product_skus.append(i["sku"])
                product_names.append(i["product_name"])
                prices_list.append(i["product_price"])
                quantity_list.append(quantity)
                totals_list.append(totals)
                purchase.update({"product_sku": product_skus})
                purchase.update({"product_name": product_names})
                purchase.update({"price": prices_list})
                purchase.update({"quantities": quantity_list})
                purchase.update({"totals": totals_list})
                purchase.update({"grand_total": sum(totals_list)})

                new_stock_cnt = i["stock_capacity"] - quantity
                

                i.update({"stock_capacity": new_stock_cnt})
            

                confirmation = input("Would you like anything else? (Y/N)\n").upper()

                if confirmation == "Y":
                    new_order
                elif confirmation == "N":
                    print(f'\nTotal: {sum(totals_list)}\n')
                    cash_given = int(input("Amount Tendered (Ksh):"))
                    change = cash_given - sum(totals_list)
                    print(f'Change: Ksh. {change}\n')
                    new_order = False
    purchase_data.append(purchase)   
                
                
    with open (products, "w") as p:
        json.dump(product_data, p, indent=4)
    with open(purchase_file, "w") as f:
        json.dump(purchase_data, f, indent=4)

def search_transactions():
    with open(purchase_file) as purchase_db:
        purchase_data = json.load(purchase_db)
        transaction_id = input("Enter transaction ID:\n")

        for i in purchase_data:
            if i["transaction_id"] == transaction_id:
                print(f'''
                Transaction ID: {i["transaction_id"]}
                Customer ID: {i["customer_id"]}
                Customer Name: {i["customer_name"]}
                Products SKU: {i["product_sku"]}
                Product Names: {i["product_name"]}
                Prices: {i["price"]}
                Quantities: {i["quantities"]}
                Date: {i["date"]}
                Totals: {i["totals"]}
                Grand Total: {i["grand_total"]}
                ''')

if __name__ == "__main__":
    purchase_operations()