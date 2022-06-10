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
                print("\n\tInvalid selection! Please try again.\n\t")
        except ValueError:
            print("\n\tInvalid input. Try again.\n\t")

# 1. Add product to database
def add_new_item():
    with open(filename) as product_db:
        product_data = json.load(product_db)
        sku_generator = random.randint(10000, 99999)
        product_category = input("\n\tProduct category:\n\t").capitalize()
        product_name = input("\n\tProduct Name:\n\t").capitalize()
        
        while True:
            try:
                product_price = int(input("\n\tProduct price (NUMBERS ONLY. NO SPECIAL CHARACTERS):\n\t"))
                break
            except ValueError:
                print("\n\tInvalid input! Try again.\n\t")
        
        vendor = input("\n\tVendor:\n\t").capitalize()
        vendor_phone = input("\n\tVendor Phone No.:\n\t")

        while True:
            try:
                items_in_stock = int(input("\n\tNo. of items (NUMBERS ONLY. NO SPECIAL CHARACTERS):\n\t"))
                break
            except:
                print("\n\tInvalid input! Try again.\n\t")

        new_product = Product(sku_generator, product_category, product_name, product_price, vendor, vendor_phone, items_in_stock)
        p_details = new_product.__dict__
        product_data.append(p_details)
    
    with open(filename, "w") as f:
        json.dump(product_data, f, indent=4)
    print(f"\n\tProduct {sku_generator} added successfully!\n\t")

# 2. Delete product from database
def delete_item():
    with open(filename) as product_db:
        product_data = json.load(product_db)
        while True:
            try:
                p_ref = int(input("\n\tEnter product SKU:\n\t"))
                break
            except ValueError:
                print("\n\tInvalid value. Try again.\n\t")

        j = 0

        # iterate over product_data list
        for i in product_data:
            if i["sku"] == p_ref:
                for key, value in i.items():
                    print("\t{} : {}\t".format(key, value))
                warning = input("\n\tAre you sure?\n\t***THIS ACTION IS IRREVERSIBLE*** (Y/N)\n\t").upper()
                if warning == "Y":
                    product_data.pop(j)
                    print(f"\n\tProduct {p_ref} deleted successfully!\n\t")
                    break
                elif warning == "N":
                    print("\n\tNo changes made!\n\t")
                    break
                else:
                    print("\n\tInvalid input!\n\t")
                    break
            j += 1
        else:
            print("\n\tProduct not found!\n\t")
            

    with open(filename, "w") as f:
        json.dump(product_data, f, indent=4)

# 3. Update product details

def update_product():
    with open(filename) as product_db:
        product_data = json.load(product_db)

        while True:
            try:
                update_p = int(input("\n\tWhich product would you like to update?\n\tEnter product SKU:\n\t"))
                break
            except:
                print("\n\tInvalid value. Try again!\n\t")

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
                        update_a = int(input("\n\tWhich attribute would you like to update?\n\t"))
                        break
                    except ValueError:
                        print("\n\tInvalid Value. Try again.\n\t")
                # Product SKU update
                if update_a == 1:
                    new_sku = random.randint(10000, 99999)
                    confirm = input("\n\tAre you sure of this action? (Y/N)\n\t*** THIS ACTION IS IRREVERSIBLE! ***\n\t").upper()
                    if confirm == "Y":
                        i["sku"] = new_sku
                        print(f"\n\tProduct updated successfully! New SKU: {new_sku}.\n\t")
                        break
                    elif confirm == "N":
                        print("\n\tNo changes made!\n\t")
                        break
                    else:
                        print("\n\tInvalid input!\n\t")
                        break
                # Product category update
                if update_a == 2:
                    new_pc = input("\n\tEnter new category:\n\t").capitalize()
                    confirm = input("\n\tAre you sure of this action? (Y/N)\n\t*** THIS ACTION IS IRREVERSIBLE! ***\n\t").upper()
                    if confirm == "Y":
                        i["product_category"] = new_pc
                        print(f"\n\tProduct updated successfully! New product category: {new_pc}.\n\t")
                        break
                    elif confirm == "N":
                        print("\n\tNo changes made!\n\t")
                        break
                    else:
                        print("\n\tInvalid input!\n\t")
                        break
                
                # Product name update
                if update_a == 3:
                    new_pn = input("\n\tEnter new name:\n\t").capitalize()
                    confirm = input("\n\tAre you sure of this action? (Y/N)\n\t*** THIS ACTION IS IRREVERSIBLE! ***\n\t").upper()
                    if confirm == "Y":
                        i["product_name"] = new_pn
                        print(f"\n\tProduct updated successfully! New name:{new_pn}.\n\t")
                        break
                    elif confirm == "N":
                        print("\n\tNo changes made!\n\t")
                        break
                    else:
                        print("\n\tInvalid input!\n\t")
                        break
                
                # Product price update
                if update_a == 4:
                    new_pp = input("\n\tEnter new price:\n\t(NUMBERS ONLY. NO SPECIAL CHARACTERS)\n\t")
                    confirm = input("\n\tAre you sure of this action? (Y/N)\n\t*** THIS ACTION IS IRREVERSIBLE! ***\n\t").upper()
                    if confirm == "Y":
                        i["product_price"] = new_pp
                        print(f"\n\tProduct updated successfully! New price: {new_pp}.\n\t")
                        break
                    elif confirm == "N":
                        print('\n\tNo changes made!\n\t')
                        break
                    else:
                        print("\n\tInvalid input!\n\t")
                        break

                # Product vendor update
                if update_a == 5:
                    new_pv = input("\n\tEnter new vendor:\n\t").capitalize()
                    confirm = input("\n\tAre you sure of this action? (Y/N)\n\t*** THIS ACTION IS IRREVERSIBLE! ***\n\t").upper()
                    if confirm == "Y":
                        i["product_vendor"] = new_pv
                        print(f"\n\tProduct updated successfully! New vendor: {new_pv}.\n\t")
                        break
                    elif confirm == "N":
                        print("\n\tNo changes made!\n\t")
                        break
                    else:
                        print("\n\tInvalid input!\n\t")
                        break
                
                # Vendor Phone No. update
                if update_a == 6:
                    new_phn = input("\n\tEnter new Phone No.:\n\t")
                    confirm = input("\n\tAre you sure of this action? (Y/N)\n\t*** THIS ACTION IS IRREVERSIBLE! ***\n\t").upper()
                    if confirm == "Y":
                        i["vendor_phone"] = new_phn
                        print(f"\n\tProduct updated successfully. New Phone No.: {new_phn}\n\t")
                        break
                    elif confirm == "N":
                        print("\n\tNo changes made!\n\t")
                        break
                    else:
                        print("\n\tInvalid input!\n\t")
                        break
                
                # Stock capacity update
                if update_a == 7:
                    action = input("\n\tDo you want to clear previous stock, add to existing stock,\n\tor subtract from existing stock? (C/A/S/E)\n\t[C] Clear\n\t[A] Add\n\t[S] Subtract\n\t[E] Exit\n\t").upper()

                    if action == "C":
                        while True:
                            try:
                                new_sc = int(input("\n\tNew capacity:\n\t"))
                                break   
                            except:
                                print("\n\tInvalid input. Try again.\n\t")

                        confirm = input("\n\tAre you sure of this action? (Y/N)\n\t*** THIS ACTION IS IRREVERSIBLE! ***\n\t").upper()
                        if confirm == "Y":
                            i["stock_capacity"] = new_sc
                            print(f"\n\tProduct updated successfully. Stock amount: {new_sc}.\n\t")
                            break
                        elif confirm == "N":
                            print("\n\tNo changes made!\n\t")
                            break
                        else:
                            print("\n\tInvalid input!\n\t")
                            break

                    elif action == "A":
                        while True:
                            try:
                                new_sc = int(input("\n\tNo. of items to add\n\t***WHOLE NUMBERS ONLY***:\n\t"))   
                                break
                            except ValueError:
                                print("\n\tInvalid value. Try again.\n\t")
                        confirm = input("\n\tAre you sure of this action? (Y/N)\n\t*** THIS ACTION IS IRREVERSIBLE! ***\n\t").upper()
                        if confirm == "Y":
                            i["stock_capacity"] += new_sc
                            print(f'\n\tProduct updated successfully! Stock capacity: {i["stock_capacity"]}.\n\t')
                            break
                        elif confirm == "N":
                            print("\n\tNo changes made!\n\t")
                            break
                        else:
                            print("\n\tInvalid input!\n\t")
                            break
                    elif action == "S":
                        while True:
                            try:
                                new_sc = int(input("\n\tNo. of items to remove\n\t***WHOLE NUMBERS ONLY***:\n\t"))
                                break
                            except ValueError:
                                print("\n\tInvalid input! Try again.\n\t")

                        confirm = input("\n\tAre you sure of this action? (Y/N)\n\t*** THIS ACTION IS IRREVERSIBLE! ***\n\t").upper()

                        if confirm == "Y":
                            i["stock_capacity"] -= new_sc
                            print(f'\n\tProduct updated successfully! Stock capacity: {i["stock_capacity"]}\n\t')
                            break
                        elif confirm == "N":
                            print("\n\tNo changes made!\n\t")
                            break
                        else:
                            print("\n\tInvalid input!\n\t")
                            break
                    elif action == "E":
                        print("\n\tExiting...\n\t")
                        break
                    else:
                        print("\n\tInvalid input!\n\t")
                        break
        else:
            print("\n\tProduct not found!\n\t")
    
    with open(filename, "w") as f:
        json.dump(product_data, f, indent=4)

# 4. View product
def view_item():
    with open(filename) as product_db:
        product_data = json.load(product_db)
        while True:
            try:
                sku_view = int(input("\n\tEnter Product SKU:\n\t"))
                break
            except ValueError:
                print("\n\tInvalid value. Try again.\n\t")
        j = 0

        for i in product_data:
            p = Product(i["sku"], i["product_category"], i["product_name"], i["product_price"], i["product_vendor"], i["vendor_phone"], i["stock_capacity"])
            p_dict = p.__dict__
            if i["sku"] == sku_view:
                print(p)
                return p_dict
        else:
            print("\n\tProduct not available!\n\t")

# 5. View product database
def view_product_db():
    with open(filename) as product_db:
        product_data = json.load(product_db)

        while True:
            try:
                view = int(input("\n\t[1] View All\n\t[2] Sort by Product SKU\n\t[3] Sort by Product Name\n\t"))
                break
            except ValueError:
                print("\n\tInvalid input! Try again.\n\t")

        if product_data == []:
            print("\n\tNo products found! Database empty!\n\t")
        for i in product_data:
            p = Product(i["sku"], i["product_category"], i["product_name"], i["product_price"], i["product_vendor"], i["vendor_phone"], i["stock_capacity"])
            if view == 1:
                print(p)
            elif view == 2:
                order = input("\n\tSort:\n\t[A] Ascending\n\t[D] Descending\n\t(ENTER A/D)\n\t").upper()
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
                    print("\n\tInvalid input! Exiting...\n\t")
                    break
            elif view == 3:
                prod_search = input("\n\tSort:\n\t[A] Ascending\n\t[D] Descending\n\t(Enter A/N)\n\t").upper()
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
                    print("\n\tInvalid input! Exiting...\n\t")
                    break 
            else:
                print("\n\tInvalid selection! Exiting...\n\t")
                break            

# Query no of products in db

def query_no_items():
    with open(filename) as product_db:
        product_data = json.load(product_db)
        j = 0

        for i in product_data:
            j += 1
        
        print(f"\n\tThere are {j} products in the database!\n\t")
if __name__ == "__main__":
    product_menu()