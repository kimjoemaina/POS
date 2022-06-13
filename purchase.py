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
        self.product_skus = product_skus
        self.product_name = product_name
        self.price = int(price)
        self.quantities = int(quantities)
        self.date = date
    
    def checkout(self):
        return self.price * self.quantities
    
   
def purchase_operations():
    while True:
        print('''
        ------------ Purchase Menu ------------

            [1] Sell
            [2] View customer transactions
            [3] Main Menu

            ------------ End ------------
        ''')
        
        try:
            selection = int(input("\n\tSelect option:\n\t"))
            if selection == 1:
                check = input("\n\tNew or existing customer?\n\t[N] New\n\t[E] Existing\n\t").upper()
                if check == "N":
                    new_customer = add_customer()
                    purchase_operations()
                    break
                elif check == "E":
                    sell()
                    purchase_operations()
                    break
                else:
                    print("\n\tInvalid input!\n\tTry again.\n\t")
            elif selection == 2:
                search_transactions()
                purchase_operations()
                break
            elif selection == 3:
                from main import menu
                menu()
                break
            else:
                print("\n\tInvalid selection! Try again.\n\t")
        except ValueError:
            print("\n\tInvalid value. Try again.\n\t")
            
        
def sell():
    product_skus = []
    product_names = []
    prices_list = []
    quantity_list = []
    totals_list = []
    new_order = True

    with open(products) as product_db:
        product_data = json.load(product_db)


    with open(customers) as customer_db:
        customer_data = json.load(customer_db)
        customer = view_customer()
            

    with open(purchase_file) as purchase_db:
        purchase_data = json.load(purchase_db)

    
    while new_order:
        if customer == None:
                break
        print("\n\tWhat would you like to sell?\t")    
        product_id = int(input("\tEnter product SKU:\n\t"))


        for i in product_data:  
            if i["sku"] == product_id:
                print(f'\n\tSKU: {i["sku"]}\n\tProduct Category: {i["product_category"]}\n\tProduct Name: {i["product_name"]}\n\tPrice: {i["product_price"]}\n\t')
                transaction_id = random.randint(1000000, 9999999)
                customer_id = customer["customer_id"]
                customer_name = f'{customer["first_name"]} {customer["last_name"]}'
                price = i["product_price"]
                prod_sku = i["sku"]
                prod_name = (i["product_name"])
                while True:
                    try:
                        quantity = int(input('\n\tQuantity (QTY):\n\t'))
                        if quantity > i["stock_capacity"]:
                            print(f'\n\tQuantity entered exceeds stock available.\n\tAvailable Quantity: {i["stock_capacity"]}.\n\t')
                        elif quantity < i["stock_capacity"]:
                            break

                    except ValueError:
                        print("\n\tInvalid value entered. Please enter a valid quantity.\n\t")
                
                today = datetime.now()
                date = today.strftime("%d/%m/%Y")
                purchases = Purchase(transaction_id, customer_id, customer_name, prod_sku, prod_name, price, quantity, date)
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
                

                while True:
                    confirmation = input("\n\tWould you like anything else? (Y/N)\n\t").upper()                    
                    if confirmation == "Y":
                        new_order
                        break
                    elif confirmation == "N":
                        new_order = False
                        receipt = (f'''
                                    --------- Receipt ---------

                            Transaction ID      :      {transaction_id}
                            Customer ID         :      {customer_id}
                            Customer Name       :      {customer_name}
                            Products SKU        :      {purchase["product_sku"]}
                            Product Names       :      {purchase["product_name"]}
                            Prices              :      {purchase["price"]}
                            Quantities          :      {purchase["quantities"]}
                            Date                :      {purchase["date"]}
                            Totals              :      {purchase["totals"]}
                            Grand Total         :      {purchase["grand_total"]}

                                --------- Welcome again ---------
                        ''')

                        print(f"\n\tTotal: {sum(totals_list)}\n\t")
                        while True:
                            cash_given = int(input("\n\tAmount Tendered (Ksh):\n\t"))
                            if cash_given < sum(totals_list):
                                print(f'\n\tAmount entered is less than the total amount. Please enter an amount equal to or greater than the total.\n\t')
                            else:
                                change = cash_given - sum(totals_list)
                                print(f"\n\tChange: Ksh. {change}\n\t")
                                print(receipt)
                                purchase_data.append(purchase)
                                break
                        break      
                    elif confirmation != "Y" and confirmation != "N":
                        print("\n\tInvalid input. Try again.\n\t")
                break                
        else:
            print("\n\tProduct not in database.\n\n\tPlease add the desired product\n\tfrom the product operations menu.\n\t")
                
    with open (products, "w") as p:
        json.dump(product_data, p, indent=4)
    with open(purchase_file, "w") as f:
        json.dump(purchase_data, f, indent=4)

def search_transactions():
    with open(purchase_file) as purchase_db:
        purchase_data = json.load(purchase_db)
        search = input("\n\tSearch using:\n\t[T] Transaction ID\n\t[A] View all transactions\n\t[U] Up\n\t").upper()
        if search == "T":
            while True:
                try:
                    transaction_id = int(input("\n\tEnter transaction ID:\n\t"))
                    break
                except ValueError:
                    print("\n\tInvalid transaction ID. Try again.\n\t")
            for i in purchase_data:
                if i["transaction_id"] == transaction_id:
                    print(f'''
                        ---------- Transaction Details ----------

                        Transaction ID      :       {i["transaction_id"]}
                        Customer ID         :       {i["customer_id"]}
                        Customer Name       :       {i["customer_name"]}
                        Products SKU        :       {i["product_sku"]}
                        Product Names       :       {i["product_name"]}
                        Prices              :       {i["price"]}
                        Quantities          :       {i["quantities"]}
                        Date                :       {i["date"]}
                        Totals              :       {i["totals"]}
                        Grand Total         :       {i["grand_total"]}

                                ---------- End ---------                        
                        ''')
        elif search == "A":
            for i in purchase_data:
                print(f'''
                        Transaction ID      :       {i["transaction_id"]}
                        Customer ID         :       {i["customer_id"]}
                        Customer Name       :       {i["customer_name"]}
                        Products SKU        :       {i["product_sku"]}
                        Product Names       :       {i["product_name"]}
                        Prices              :       {i["price"]}
                        Quantities          :       {i["quantities"]}
                        Date                :       {i["date"]}
                        Totals              :       {i["totals"]}
                        Grand Total         :       {i["grand_total"]}
                ''')
        elif search == "U":
            purchase_operations()
        else:
            print("\n\tInvalid input! Exiting...\n\t")

if __name__ == "__main__":
    purchase_operations()