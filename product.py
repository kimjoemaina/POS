import json
import random

filename = "products.json"

class Product:
    def __init__(self, sku, product_category, product_name, product_vendor, vendor_phone):
        self.sku = int(sku)
        self.product_category = product_category
        self.product_name = product_name
        self.product_vendor = product_vendor
        self.vendor_phone = vendor_phone
        # self.stock_capacity = int(stock_capacity)
    
    def item(self):
        p_details = {"SKU": self.sku, "Product Category": self.product_category, "Product Name": self.product_name, "Vendor": self.product_vendor, "Vendor Phone No.": self.vendor_phone}
        return p_details
    
    def __str__(self):
        p_info = (f"""
        SKU: {self.sku}
        Product Category: {self.product_category}
        Product Name: {self.product_name}
        Vendor: {self.product_vendor}
        Vendor Phone No.: {self.vendor_phone}
        """)

        return p_info

        

def product_menu():
    while True:
        print("Select a Product Operation.")
        print(" (1) Add New Item ")
        print(" (2) Delete Item ")
        print(" (3) Update Existing Item ")
        print(" (4) View Existing Item ")
        print(" (5) View Product Database ")
        # print(" (6) Go back ")

        selection = int(input("Enter product operation: \n"))

        if selection == 1:
            add_new_item()
            break
        elif selection == 2:
            delete_item()
            break
        elif selection == 3:
            update_item()
            break
        elif selection == 4:
            view_item()
            break
        elif selection == 5:
            view_product_db()
            break
        else:
            print("Invalid selection! Please try again.")

def add_new_item():
    with open(filename) as product_db:
        product_data = json.load(product_db)
        sku_generator = random.randint(10000, 99999)
        product_category = input("Product category:\n").capitalize()
        product_name = input("Product Name:\n").capitalize()
        vendor = input("Vendor:\n")
        vendor_phone = input("Vendor Phone No.:\n")
        # items_in_stock : add later

        p = Product(sku_generator, product_category, product_name, vendor, vendor_phone)
        product_data.append(p.item())
    
    with open(filename, "w") as f:
        json.dump(product_data, f, indent=4)
    print(f"Product {sku_generator} added successfully!")

def delete_item():
    with open(filename) as product_db:
        product_data = json.load(product_db)
        p_ref = int(input("Enter product SKU:\n"))
        j = 0

        for i in product_data:
            if i["SKU"] == p_ref:
                product_data.pop(j)
            j += 1
    
    with open(filename, "w") as f:
        json.dump(product_data, f, indent=4)
    print(f"Customer {p_ref} deleted successfully!")

def view_item():
    with open(filename) as product_db:
        product_data = json.load(product_db)
        sku_view = int(input("Enter Product SKU to view:\n"))
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
    product_menu()