import json
import random

filename = "products.json"

class Product:
    def __init__(self, sku, product_category, product_name, product_price, product_vendor, vendor_phone, stock_capacity):
        self.sku = sku
        self.product_category = product_category
        self.product_name = product_name
        self.product_price = int(product_price)
        self.product_vendor = product_vendor
        self.vendor_phone = vendor_phone
        self.stock_capacity = int(stock_capacity)
    
    def __str__(self):
        p_info = (f"""
        SKU: {self.sku}
        Product Category: {self.product_category}
        Product Name: {self.product_name}
        Price: {self.product_price}
        Vendor: {self.product_vendor}
        Vendor Phone No.: {self.vendor_phone}
        Stock Capacity: {self.stock_capacity}
        """)

        return p_info

        

def product_menu():
    while True:
        print("Select a Product Operation.")
        print(" [1] Add New Item ")
        print(" [2] Delete Item ")
        print(" [3] Update Existing Item ")
        print(" [4] View Existing Item ")
        print(" [5] View Product Database ")
        print(" [6] Back to main menu")
        # print(" (6) Go back ")

        selection = int(input("Enter product operation: \n"))

        if selection == 1:
            add_new_item()
            break
        elif selection == 2:
            delete_item()
            break
        elif selection == 3:
            update_product()
            break
        elif selection == 4:
            view_item()
            break
        elif selection == 5:
            view_product_db()
            break
        elif selection == 6:
            from main import menu
            menu()
            break
        else:
            print("Invalid selection! Please try again.")

# 1. Add product to database
def add_new_item():
    with open(filename) as product_db:
        product_data = json.load(product_db)
        sku_generator = random.randint(10000, 99999)
        product_category = input("Product category:\n").capitalize()
        product_name = input("Product Name:\n").capitalize()
        product_price = input("Product price (NO SPECIAL CHARACTERS):\n")
        vendor = input("Vendor:\n").capitalize()
        vendor_phone = input("Vendor Phone No.:\n")
        items_in_stock = (input("No of items (NO SPECIAL CHARACTERS):\n"))

        new_product = Product(sku_generator, product_category, product_name, product_price, vendor, vendor_phone, items_in_stock)
        p_details = new_product.__dict__
        product_data.append(p_details)
    
    with open(filename, "w") as f:
        json.dump(product_data, f, indent=4)
    print(f"Product {sku_generator} added successfully!")
    product_menu()

# 2. Delete product from database
def delete_item():
    with open(filename) as product_db:
        product_data = json.load(product_db)
        p_ref = input("Enter product SKU:\n")

        j = 0

        # iterate over product_data list
        for i in product_data:
            if i["sku"] == p_ref:
                for key, value in i.items():
                    print("{} : {}".format(key, value))
                warning = input("\nAre you sure? ***THIS ACTION IS IRREVERSIBLE*** (Y/N)\n").upper()
                if warning == "Y":
                    product_data.pop(j)
                    print(f"Product {p_ref} deleted successfully!\n")
                    break
                elif warning == "N":
                    print("\nNo changes made!\n")
                    break
                else:
                    print("\nInvalid input!\n")
                    break
            j += 1
        else:
            print("\nProduct not found!\n")
            

    with open(filename, "w") as f:
        json.dump(product_data, f, indent=4)
    product_menu()

# 3. Update product details

def update_product():
    with open(filename) as product_db:
        product_data = json.load(product_db)
        update_p = input("Which product would you like to update?\nEnter product SKU:\n")

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
                update_a = int(input("Which attribute would you like to update?\n"))
                # Product SKU update
                if update_a == 1:
                    new_sku = str(random.randint(10000, 99999))
                    confirm = input("\nAre you sure of this action? (Y/N)\n*** THIS ACTION IS IRREVERSIBLE! ***\n").upper()
                    if confirm == "Y":
                        i["sku"] = new_sku
                        print(f"\nProduct updated successfully! New SKU: {new_sku}.\n")
                        break
                    elif confirm == "N":
                        print("\nNo changes made!\n")
                        break
                    else:
                        print("\nInvalid input!\n")
                        break
                # Product category update
                if update_a == 2:
                    new_pc = input("Enter new category:\n").capitalize()
                    confirm = input("\nAre you sure of this action? (Y/N)\n*** THIS ACTION IS IRREVERSIBLE! ***\n").upper()
                    if confirm == "Y":
                        i["product_category"] = new_pc
                        print(f"\nProduct updated successfully! New product category: {new_pc}.\n")
                        break
                    elif confirm == "N":
                        print("\nNo changes made!\n")
                        break
                    else:
                        print("\nInvalid input!\n")
                        break
                
                # Product name update
                if update_a == 3:
                    new_pn = input("Enter new name:\n").capitalize()
                    confirm = input("\nAre you sure of this action? (Y/N)\n*** THIS ACTION IS IRREVERSIBLE! ***\n").upper()
                    if confirm == "Y":
                        i["product_name"] = new_pn
                        print(f"Product updated successfully! New name:{new_pn}.\n")
                        break
                    elif confirm == "N":
                        print("\nNo changes made!\n")
                        break
                    else:
                        print("\nInvalid input!\n")
                        break
                
                # Product price update
                if update_a == 4:
                    new_pp = input("Enter new price: (NUMBERS ONLY. NO SPECIAL CHARACTERS)\n")
                    confirm = input("\nAre you sure of this action? (Y/N)\n*** THIS ACTION IS IRREVERSIBLE! ***\n").upper()
                    if confirm == "Y":
                        i["product_price"] = new_pp
                        print(f"Product updated successfully! New price: {new_pp}.\n")
                        break
                    elif confirm == "N":
                        print("\nNo changes made!\n")
                        break
                    else:
                        print("\nInvalid input!\n")
                        break

                # Product vendor update
                if update_a == 5:
                    new_pv = input("Enter new vendor:\n").capitalize()
                    confirm = input("\nAre you sure of this action? (Y/N)\n*** THIS ACTION IS IRREVERSIBLE! ***\n").upper()
                    if confirm == "Y":
                        i["product_vendor"] = new_pv
                        print(f"Product updated successfully! New vendor: {new_pv}.\n")
                        break
                    elif confirm == "N":
                        print("\nNo changes made!\n")
                        break
                    else:
                        print("\nInvalid input!\n")
                        break
                
                # Vendor Phone No. update
                if update_a == 6:
                    new_phn = input("Enter new Phone No.:\n")
                    confirm = input("\nAre you sure of this action? (Y/N)\n*** THIS ACTION IS IRREVERSIBLE! ***\n").upper()
                    if confirm == "Y":
                        i["vendor_phone"] = new_phn
                        print(f"Product updated successfully. New Phone No.: {new_phn}\n")
                        break
                    elif confirm == "N":
                        print("\nNo changes made!\n")
                        break
                    else:
                        print("\nInvalid input!\n")
                        break
                
                # Stock capacity update
                if update_a == 7:
                    action = input("Do you want to clear previous stock, add to existing stock, or subtract from existing stock? (C/A/S/E)\n[C] Clear\n[A] Add\n[S] Subtract\n[E] Exit\n").upper()

                    if action == "C":
                        new_sc = int(input("New capacity:\n"))
                        confirm = input("\nAre you sure of this action? (Y/N)\n*** THIS ACTION IS IRREVERSIBLE! ***\n").upper()
                        if confirm == "Y":
                            i["stock_capacity"] = new_sc
                            print(f"\nProduct updated successfully. Stock amount: {new_sc}.\n")
                            break
                        elif confirm == "N":
                            print("\nNo changes made!\n")
                            break
                        else:
                            print("\nInvalid input!\n")
                            break
                    elif action == "A":
                        new_sc = int(input("No. of items to add\n***WHOLE NUMBERS ONLY***:\n"))
                        confirm = input("\nAre you sure of this action? (Y/N)\n*** THIS ACTION IS IRREVERSIBLE! ***\n").upper()
                        if confirm == "Y":
                            i["stock_capacity"] += new_sc
                            print(f'Product updated successfully! Stock capacity: {i["stock_capacity"]}\n')
                            break
                        elif confirm == "N":
                            print("\nNo changes made!\n")
                            break
                        else:
                            print("\nInvalid input!\n")
                            break
                    elif action == "S":
                        new_sc = int(input("No. of items to remove\n***WHOLE NUMBERS ONLY***:\n"))
                        confirm = input("\nAre you sure of this action? (Y/N)\n*** THIS ACTION IS IRREVERSIBLE! ***\n").upper()
                        if confirm == "Y":
                            i["stock_capacity"] -= new_sc
                            print(f'Product updated successfully! Stock capacity: {i["stock_capacity"]}\n')
                            break
                        elif confirm == "N":
                            print("\nNo changes made!\n")
                            break
                        else:
                            print("\nInvalid input!\n")
                            break
                    elif action == "E":
                        break
                    else:
                        print("\nInvalid input!\n")
                        break
        else:
            print("\nProduct not found!\n")
    
    with open(filename, "w") as f:
        json.dump(product_data, f, indent=4)
    product_menu()

# 4. View product
def view_item():
    with open(filename) as product_db:
        product_data = json.load(product_db)
        sku_view = int(input("Enter Product SKU:\n"))
        j = 0

        for i in product_data:
            p = Product(i["SKU"], i["Product Category"], i["Product Name"], i["Vendor"], i["Vendor Phone No."])
            if i["SKU"] == sku_view:
                print(p)

def view_product_db():
    with open(filename) as product_db:
        product_data = json.load(product_db)

        for i in product_data:
            p = Product(i["SKU"], i["Product Category"], i["Product Name"], i["Vendor"], i["Vendor Phone No."])
            print(p)


if __name__ == "__main__":
    delete_item()