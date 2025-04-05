
#  Inventory Management System - Python Task 

A simple yet powerful Inventory Management System built with **Python** that stores data in an **Excel file** using `pandas` and `openpyxl`. This system lets users manage products in a store with options to add, update, delete, search, and generate inventory reports — all via a **Command-Line Interface (CLI)**.

---

##  Project Structure

```
Inventory-Management-System/
│── inventory.py          # Product & Inventory classes (Excel-based)
│── cli.py                # Command-line interface
│── inventory.xlsx        # Inventory data stored in Excel (auto-created)
│── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

---

##  Features

-  Add new products (with unique IDs)
-  Remove products by ID
-  Update price or quantity of products
-  Search products by ID or name
-  Generate inventory report in tabular format
-  Data is stored in an Excel file (`inventory.xlsx`) automatically
-  Input validation and error handling

---

## 🔧 Requirements

- Python 3 or higher  
- Install required libraries:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```
pandas
openpyxl
```

---

##  How to Run

1. Clone or download this repo.

```bash
git clone https://github.com/harishraaghavdv/Inventory-Management-System.git
cd inventory-management-system
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the CLI:

```bash
python cli.py
```

---

##  CLI Menu Options

```
1. Add Product
2. Remove Product
3. Update Product
4. Search Product
5. Generate Inventory Report
6. Exit
```

---

##  Sample Operations

### Add Product
- Input: `product_id=P001`, `name=Pen`, `price=10.5`, `quantity=100`

### Search Product
- Input: `P001` or `Pen`
- Output: Displays matching product info from Excel

### Report Generation
- Output: Prints a table of all products in the inventory

---

##  Data Storage Format (Excel)

The file `inventory.xlsx` will automatically store your inventory like this:

| product_id | name   | price | quantity |
|------------|--------|-------|----------|
| P001       | Pen    | 10.5  | 100      |
| P002       | Book   | 50.0  | 30       |

---

##  Error Handling

-  Duplicate product IDs not allowed
-  Cannot remove/update non-existent product
-  Validations for price (float) and quantity (integer)


---

##  Author

**Harish Raaghav**  

---

