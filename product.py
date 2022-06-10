import json
import random

from customer import view_customer_db

filename = "products.json"

class Product:
    def __init__(self, sku, product_category, product_name, product_price, product_vendor, vendor_phone, stock_capacity):
        # assert type(sku) == int and type(product_price) == int and type(stock_capacity) == int, "ints not used"
        self.sku = sku
        self.product_category = product_category
        self.product_name = product_name
        self.product_price = int(product_price)
        self.product_vendor = product_vendor
        self.vendor_phone = vendor_phone
        self.stock_capacity = int(stock_capacity)
    
    def __str__(self):
        p_info = (f"""
        SKU             : {self.sku}
        Product Category: {self.product_category}
        Product Name    : {self.product_name}
        Price           : {self.product_price}
        Vendor          : {self.product_vendor}
        Vendor Phone No.: {self.vendor_phone}
        Stock Capacity  : {self.stock_capacity}
        """)

        return p_info

        

def product_menu():
    while True:
        print('''
        ------------ Product Menu ------------

        Select a Product Operation

        [1] Add New Item
        [2] Delete Item
        [3] Update Existing Item
        [4] View Existing Item
        [5] View Product Database
        [6] No. of products in DB
        [7] Back to main menu

            ------------ End ------------ 
        ''')

        try:
            selection = int(input('''
        Enter product operation:
        '''))

            if selection == 1:
                add_new_item()
                product_menu()
                break
            elif selection == 2:
                delete_item()
                product_menu()
                break
            elif selection == 3:
                update_product()
                product_menu()
                break
            elif selection == 4:
                view_item()
                product_menu()
                break
            elif selection == 5:
                view_product_db()
                product_menu()
                break
            elif selection == 6:
                query_no_items()
                product_menu
            elif selection == 7:
                from main import menu
                menu()
                break
            else:
                print('''
        Invalid selection! Please try again.
        ''')
        except ValueError:
            print('''
        Invalid input. Try again.
        ''')

# 1. Add product to database
def add_new_item():
    with open(filename) as product_db:
        product_data = json.load(product_db)
        sku_generator = random.randint(10000, 99999)
        product_category = input('''
        Product category:
        ''').capitalize()
        product_name = input('''
        Product Name:
        ''').capitalize()
        
        while True:
            try:
                product_price = int(input('''
        Product price (NUMBERS ONLY. NO SPECIAL CHARACTERS):
        '''))
                break
            except ValueError:
                print('''
        Invalid input! Try again.
        ''')
        
        vendor = input('''
        Vendor:
        ''').capitalize()
        vendor_phone = input('''
        Vendor Phone No.:
        ''')

        while True:
            try:
                items_in_stock = int(input('''
        No. of items (NUMBERS ONLY. NO SPECIAL CHARACTERS):
        '''))
                break
            except:
                print('''
        Invalid input! Try again.
        ''')

        new_product = Product(sku_generator, product_category, product_name, product_price, vendor, vendor_phone, items_in_stock)
        p_details = new_product.__dict__
        product_data.append(p_details)
    
    with open(filename, "w") as f:
        json.dump(product_data, f, indent=4)
    print(f'''
        Product {sku_generator} added successfully!
        ''')

# 2. Delete product from database
def delete_item():
    with open(filename) as product_db:
        product_data = json.load(product_db)
        while True:
            try:
                p_ref = int(input('''
                Enter product SKU:
                '''))
                break
            except ValueError:
                print("Invalid value. Try again.")

        j = 0

        # iterate over product_data list
        for i in product_data:
            if i["sku"] == p_ref:
                for key, value in i.items():
                    print("{} : {}".format(key, value))
                warning = input('''
                Are you sure?
                ***THIS ACTION IS IRREVERSIBLE*** (Y/N)
                ''').upper()
                if warning == "Y":
                    product_data.pop(j)
                    print(f'''
                Product {p_ref} deleted successfully!
                ''')
                    break
                elif warning == "N":
                    print('''
                No changes made!
                ''')
                    break
                else:
                    print('''
                Invalid input!
                ''')
                    break
            j += 1
        else:
            print('''
            Product not found!
            ''')
            

    with open(filename, "w") as f:
        json.dump(product_data, f, indent=4)

# 3. Update product details

def update_product():
    with open(filename) as product_db:
        product_data = json.load(product_db)

        while True:
            try:
                update_p = int(input('''
            Which product would you like to update?
            Enter product SKU:
            '''))
                break
            except:
                print('''
            Invalid value. Try again!
            ''')

        for i in product_data:
            p = Product(i["sku"], i["product_category"], i["product_name"], i["product_price"], i["product_vendor"], i["vendor_phone"], i["stock_capacity"])
            q = p.__dict__

            if q["sku"] == update_p:
                print(p)

                print('''
                [1] SKU
                [2] Product Category
                [3] Product Name
                [4] Product Price
                [5] Product Vendor
                [6] Vendor Phone No.
                [7] Stock Capacity
                ''')
                # update attribute
                while True:
                    try:
                        update_a = int(input('''
                Which attribute would you like to update?
                '''))
                        break
                    except ValueError:
                        print('''
                Invalid Value. Try again.
                ''')
                # Product SKU update
                if update_a == 1:
                    new_sku = random.randint(10000, 99999)
                    confirm = input('''
                    Are you sure of this action? (Y/N)
                    *** THIS ACTION IS IRREVERSIBLE! ***
                    ''').upper()
                    if confirm == "Y":
                        i["sku"] = new_sku
                        print(f'''
                        Product updated successfully! New SKU: {new_sku}.
                        ''')
                        break
                    elif confirm == "N":
                        print('''
                        No changes made!
                        ''')
                        break
                    else:
                        print('''
                        Invalid input!
                        ''')
                        break
                # Product category update
                if update_a == 2:
                    new_pc = input('''
                    Enter new category:
                    ''').capitalize()
                    confirm = input('''
                    Are you sure of this action? (Y/N)
                    *** THIS ACTION IS IRREVERSIBLE! ***
                    ''').upper()
                    if confirm == "Y":
                        i["product_category"] = new_pc
                        print(f'''
                        Product updated successfully! New product category: {new_pc}.
                        ''')
                        break
                    elif confirm == "N":
                        print('''
                        No changes made!
                        ''')
                        break
                    else:
                        print('''
                        Invalid input!
                        ''')
                        break
                
                # Product name update
                if update_a == 3:
                    new_pn = input('''
                    Enter new name:
                    ''').capitalize()
                    confirm = input('''
                    Are you sure of this action? (Y/N)
                    *** THIS ACTION IS IRREVERSIBLE! ***
                    ''').upper()
                    if confirm == "Y":
                        i["product_name"] = new_pn
                        print(f'''
                        Product updated successfully! New name:{new_pn}.
                        ''')
                        break
                    elif confirm == "N":
                        print('''
                        No changes made!
                        ''')
                        break
                    else:
                        print('''
                        Invalid input!
                        ''')
                        break
                
                # Product price update
                if update_a == 4:
                    new_pp = input('''
                    Enter new price:
                    (NUMBERS ONLY. NO SPECIAL CHARACTERS)
                    ''')
                    confirm = input('''
                    Are you sure of this action? (Y/N)
                    *** THIS ACTION IS IRREVERSIBLE! ***
                    ''').upper()
                    if confirm == "Y":
                        i["product_price"] = new_pp
                        print(f'''
                        Product updated successfully! New price: {new_pp}.
                        ''')
                        break
                    elif confirm == "N":
                        print('''
                        No changes made!
                        ''')
                        break
                    else:
                        print('''
                        Invalid input!
                        ''')
                        break

                # Product vendor update
                if update_a == 5:
                    new_pv = input('''
                    Enter new vendor:
                    ''').capitalize()
                    confirm = input('''
                    Are you sure of this action? (Y/N)
                    *** THIS ACTION IS IRREVERSIBLE! ***
                    ''').upper()
                    if confirm == "Y":
                        i["product_vendor"] = new_pv
                        print(f'''
                        Product updated successfully! New vendor: {new_pv}.
                        ''')
                        break
                    elif confirm == "N":
                        print('''
                        No changes made!
                        ''')
                        break
                    else:
                        print('''
                        Invalid input!
                        ''')
                        break
                
                # Vendor Phone No. update
                if update_a == 6:
                    new_phn = input('''
                    Enter new Phone No.:
                    ''')
                    confirm = input('''Are you sure of this action? (Y/N)
                    *** THIS ACTION IS IRREVERSIBLE! ***
                    ''').upper()
                    if confirm == "Y":
                        i["vendor_phone"] = new_phn
                        print(f'''
                        Product updated successfully. New Phone No.: {new_phn}
                        ''')
                        break
                    elif confirm == "N":
                        print('''
                        No changes made!
                        ''')
                        break
                    else:
                        print('''
                        Invalid input!
                        ''')
                        break
                
                # Stock capacity update
                if update_a == 7:
                    action = input('''
                    Do you want to clear previous stock, add to existing stock,
                    or subtract from existing stock? (C/A/S/E)
                    [C] Clear
                    [A] Add
                    [S] Subtract
                    [E] Exit
                    ''').upper()

                    if action == "C":
                        while True:
                            try:
                                new_sc = int(input('''
                        New capacity:
                        '''))
                                break   
                            except:
                                print('''
                        Invalid input. Try again.
                        ''')

                        confirm = input('''
                        Are you sure of this action? (Y/N)
                        *** THIS ACTION IS IRREVERSIBLE! ***
                        ''').upper()
                        if confirm == "Y":
                            i["stock_capacity"] = new_sc
                            print(f'''
                            Product updated successfully. Stock amount: {new_sc}.
                            ''')
                            break
                        elif confirm == "N":
                            print('''
                            No changes made!
                            ''')
                            break
                        else:
                            print('''
                            Invalid input!
                            ''')
                            break

                    elif action == "A":
                        while True:
                            try:
                                new_sc = int(input('''
                        No. of items to add
                        ***WHOLE NUMBERS ONLY***:
                        '''))   
                                break
                            except ValueError:
                                print('''
                                Invalid value. Try again.''')
                        confirm = input('''
                        Are you sure of this action? (Y/N)
                        *** THIS ACTION IS IRREVERSIBLE! ***
                        ''').upper()
                        if confirm == "Y":
                            i["stock_capacity"] += new_sc
                            print(f'''
                            Product updated successfully! Stock capacity: {i["stock_capacity"]}.
                            ''')
                            break
                        elif confirm == "N":
                            print('''
                            No changes made!
                            ''')
                            break
                        else:
                            print('''
                            Invalid input!
                            ''')
                            break
                    elif action == "S":
                        while True:
                            try:
                                new_sc = int(input('''
                        No. of items to remove
                        ***WHOLE NUMBERS ONLY***:'''))
                                break
                            except ValueError:
                                print("Invalid input! Try again.")

                        confirm = input('''
                        Are you sure of this action? (Y/N)
                        *** THIS ACTION IS IRREVERSIBLE! ***
                        ''').upper()

                        if confirm == "Y":
                            i["stock_capacity"] -= new_sc
                            print(f'''
                            Product updated successfully! Stock capacity: {i["stock_capacity"]}
                            ''')
                            break
                        elif confirm == "N":
                            print('''
                            No changes made!
                            ''')
                            break
                        else:
                            print('''
                            Invalid input!
                            ''')
                            break
                    elif action == "E":
                        print('''
                        Exiting...
                        ''')
                        break
                    else:
                        print('''
                        Invalid input!
                        ''')
                        break
        else:
            print('''
            Product not found!
            ''')
    
    with open(filename, "w") as f:
        json.dump(product_data, f, indent=4)

# 4. View product
def view_item():
    with open(filename) as product_db:
        product_data = json.load(product_db)
        while True:
            try:
                sku_view = int(input('''
                Enter Product SKU:
                '''))
                break
            except ValueError:
                print('''
                Invalid value. Try again.
                ''')
        j = 0

        for i in product_data:
            p = Product(i["sku"], i["product_category"], i["product_name"], i["product_price"], i["product_vendor"], i["vendor_phone"], i["stock_capacity"])
            p_dict = p.__dict__
            if i["sku"] == sku_view:
                print(p)
                return p_dict
        else:
            print('''
            Product not available!
            ''')

# 5. View product database
def view_product_db():
    with open(filename) as product_db:
        product_data = json.load(product_db)

        while True:
            try:
                view = int(input('''
                [1] View All
                [2] Sort by Product SKU
                [3] Sort by Product Name
                '''))
                break
            except ValueError:
                print('''
                Invalid input! Try again.''')

        for i in product_data:
            p = Product(i["sku"], i["product_category"], i["product_name"], i["product_price"], i["product_vendor"], i["vendor_phone"], i["stock_capacity"])
            if view == 1:
                print(p)
            elif view == 2:
                order = input('''
                Sort:
                [A] Ascending
                [D] Descending
                (ENTER A/D)
                ''').upper()
                if order == "A":
                    sorted_by_sku  = sorted(product_data, key = lambda j: j["sku"])
                    for s in sorted_by_sku:
                        print(f'''
                            SKU: {s["sku"]}
                            Product Category: {s["product_category"]}
                            Product Name: {s["product_name"]}
                            Product Price: {s["product_price"]}
                            Product Vendor: {s["product_vendor"]}
                            Vendor Phone: {s["vendor_phone"]}
                            Stock Capacity: {s["stock_capacity"]}
                            ''')
                    break
                elif order == "D":
                    sorted_by_sku  = sorted(product_data, key = lambda j: j["sku"], reverse=True)
                    for s in sorted_by_sku:
                        print(f'''
                            SKU: {s["sku"]}
                            Product Category: {s["product_category"]}
                            Product Name: {s["product_name"]}
                            Product Price: {s["product_price"]}
                            Product Vendor: {s["product_vendor"]}
                            Vendor Phone: {s["vendor_phone"]}
                            Stock Capacity: {s["stock_capacity"]}
                            ''')
                    break
                else:
                    print('''
                    Invalid input! Exiting...
                    ''')
                    break
            elif view == 3:
                prod_search = input('''
                Sort:
                [A] Ascending
                [D] Descending
                (Enter A/N)
                ''').upper()
                if prod_search == "A":
                    sorted_by_name = sorted(product_data, key = lambda n: n["product_name"])
                    for s in sorted_by_name:
                        print(f'''
                            SKU: {s["sku"]}
                            Product Category: {s["product_category"]}
                            Product Name: {s["product_name"]}
                            Product Price: {s["product_price"]}
                            Product Vendor: {s["product_vendor"]}
                            Vendor Phone: {s["vendor_phone"]}
                            Stock Capacity: {s["stock_capacity"]}
                            ''')
                    break
                elif prod_search == "D":
                    sorted_by_name = sorted(product_data, key = lambda n: n["product_name"], reverse=True)
                    for s in sorted_by_name:
                        print(f'''
                            SKU: {s["sku"]}
                            Product Category: {s["product_category"]}
                            Product Name: {s["product_name"]}
                            Product Price: {s["product_price"]}
                            Product Vendor: {s["product_vendor"]}
                            Vendor Phone: {s["vendor_phone"]}
                            Stock Capacity: {s["stock_capacity"]}
                            ''')
                    break
                else:
                    print('''
                    Invalid input! Exiting...
                    ''')
                    break 
            else:
                print('''
                Invalid selection! Exiting...
                ''')
                break            

# Query no of products in db

def query_no_items():
    with open(filename) as product_db:
        product_data = json.load(product_db)
        j = 0

        for i in product_data:
            j += 1
        
        print(f'''
        There are {j} products in the database!
        ''')
if __name__ == "__main__":
    product_menu()