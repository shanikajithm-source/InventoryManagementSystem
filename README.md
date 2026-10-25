# Inventory Management System

A Python-based Inventory Management System developed using Object-Oriented Programming (OOP).

This project allows users to manage products, update stock quantities and prices, delete products, and calculate total inventory value.

## Features

- Add new products
- View available inventory
- Update product quantities
- Update product prices
- Delete products with confirmation
- Calculate total inventory value
- Automatically save and load products using JSON
- Prevent duplicate product names
- Validate user inputs

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON File Handling

## Project Structure

```text
InventoryManagementSystem/
├── inventory.py
├── inventory.json
└── README.md
```

## How to Run

1. Install Python 3.
2. Clone or download the repository.
3. Open the project folder in a terminal.
4. Run:

```bash
python inventory.py
```

## Menu Options

```text
1. Add Product
2. View Inventory
3. Update Product Quantity
4. Update Product Price
5. Delete Product
6. Total Inventory Value
7. Exit
```

## OOP Concepts Used

- **Classes and Objects:** Product and Inventory classes
- **Constructors:** Initialize objects using `__init__()`
- **Encapsulation:** Organize product data and inventory operations within classes
- **Methods:** Perform inventory operations through class methods

## Data Storage

The application uses `inventory.json` to store product information. Changes are saved automatically and loaded when the application restarts.

## Future Improvements

- Product search
- Low-stock alerts
- Graphical user interface
- Database integration

## Author

Shanika Jith

GitHub: https://github.com/shanikajithm-source