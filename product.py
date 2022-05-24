import json
import random

filename = "products.json"
def product_menu():
    while True:
        print("Select a Product Operation.")
        print(" (1) Add New Item ")
        print(" (2) Search Item ")
        print(" (3) Delete Item ")
        print(" (4) Update Existing Item ")
        print(" (5) View Stock Database ")
        # print(" (6) Go back ")

        selection = int(input("Enter product operation: \n"))

        if selection == 1:
            add_new_item()
            break
        elif selection == 2:
            search_item()
            break
        elif selection == 3:
            delete_item()
            break
        elif selection == 4:
            update_item()
            break
        elif selection == 5:
            view_stock_database()
        else:
            print("Invalid selection! Please try again.")

def add_new_item():
    with open(filename) as product_db:
        product_data = json.load(product_db)
        item_name = input("Enter item name:\n")
        sku = str(random.randint(100000, 999999))
        category = input("Product Category:\n")
        # inventory = 
        vendor = input("Enter the product vendor:\n")
        vendor_phone = input("Vendor Phone No.:\n")
        new_product = {"product_name": item_name, "sku": sku, "product_category": category, "vendor": vendor, "vendor_phone": vendor_phone}
        product_data.append(new_product)

    with open(filename, "w") as f:
        json.dump(product_data, f, indent=4)
    print(f"{item_name} added successfully!")

def search_item():
    

        


if __name__ == "__main__":
    product_menu()