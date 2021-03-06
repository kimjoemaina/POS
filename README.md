# Command Line POS

## Prerequisites

- Python 3

## Introduction

This is a command line Point-Of-Sale system that allows for adding and deleting customers and products and selling these products to existing or new customers. It is written in python and uses JSON as it's data storage

Features:

- Add customer.
- Delete customer.
- Update customer.
- View customer.
- View customer database.
- Adding new stock.
- Deleting stock.
- Updating stock.
- Viewing stock.
- Viewing products.
- Search and sort using Product SKU, Product Name, Customer ID, Customer Name, Transaction ID.

## ⚑ 1. Initialization

1. Download the zipped files.
2. Extract to your folder of choice.
3. Open the extracted folder in a terminal of your choice.
4. Type `python3 main.py` to start the program and follow the on-screen prompts.

Enjoy!


## 👱 Customer Operations

Customer operations allow for the ability to add a customer, by selecting customer operations and entering `option 1`. Other operations and their key strokes are:
`[2] Delete customer`
`[3] Update customer`
`[4] View customer`
`[5] View customer database`
`[6] Main Menu`

You can delete a customer by searching them with their ID. You can also update a customer by searching them using the user ID and selecting the specific attribute you would like to update. (All attributes will be displayed on entering the Customer ID)

To view a customer's details, enter `4` and enter the Customer ID. All customer details will be displayed.

The customer database can be viewed using option `5` and can be sorted ascending or descending using the first name or ID by entering either `A` or `D`.

NB: Customer IDs are an autogenerated random number between `1000` and `9999`. Customer details contained in the JSON file are:

`Customer ID`
`First Name`
`Last Name`
`Age`
`Phone No.`
`Email`
`City`
`Registration Date` 

## 🛍 Product Operations

Similar to customer opertaions, you can carry out product opertaions by selecting `Option 2` from the `main menu`. Product operations available:

`[1] Add New Item`
`[2] Delete Item`
`[3] Update Existing Item`
`[4] View Existing Item`
`[5] View Product Database`
`[6] Back to main menu`

A product's details can be added, deleted, updated and viewed from the `products.json` file. Product operations and customer operations are similar when adding, deleting, updating, viewing, updating and also viewing the database. The reference for product operation queries is the `SKU` and `Product Name`.


NB: Product SKUs are an autogenerated random number between `10000` and `99999`.

## 🛒 Purchase operations

To sell an item, you need to enter the customer ID. If the customer does not exist, you'll get an error message, `Customer does not exist!`. If the customer is found in the database, you'll then get a prompt for the product SKU to sell.

Follow the onscreen prompts to add products to the customer's cart. After you're done selling, the total will be displayed. If the amount entered is higher than the total, the change is displayed.

You cannot sell more products than those available in the stock capacity.

All purchases are recorded in `purchases.json`. The file includes:

`Transaction ID`,
`Customer ID`,
`Customer Name`,
`Product SKU`,
`Product Names`,
`Prices`,
`Quantities`,
`Transaction Date`,
`Product Totals`,
`Grand Total`

You can view the transactions database and sort ascending by date, name or transaction ID.

NB: The transaction ID is an autogenerated number between `100000` and `9999999`.

## 📢 Contributing

All are welcome to contribute. Open a pull request and we can collaborate!



