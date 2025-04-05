import pandas as pd
import os

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    def display_details(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"


class Inventory:
    def __init__(self, filename='inventory.xlsx'):
        self.filename = filename
        self.columns = ['product_id', 'name', 'price', 'quantity']
        self._load_data()

    def _load_data(self):
        if os.path.exists(self.filename):
            self.df = pd.read_excel(self.filename)
        else:
            self.df = pd.DataFrame(columns=self.columns)
            self.df.to_excel(self.filename, index=False)

    def _save_data(self):
        self.df.to_excel(self.filename, index=False)

    def add_product(self, product):
        if product.product_id in self.df['product_id'].values:
            raise ValueError("Product ID already exists.")
        self.df = pd.concat([self.df, pd.DataFrame([product.to_dict()])], ignore_index=True)
        self._save_data()

    def remove_product(self, product_id):
        if product_id not in self.df['product_id'].values:
            raise ValueError("Product not found.")
        self.df = self.df[self.df['product_id'] != product_id]
        self._save_data()

    def update_product(self, product_id, new_price=None, new_quantity=None):
        if product_id not in self.df['product_id'].values:
            raise ValueError("Product not found.")

        if new_price is not None:
            self.df.loc[self.df['product_id'] == product_id, 'price'] = new_price
        if new_quantity is not None:
            self.df.loc[self.df['product_id'] == product_id, 'quantity'] = new_quantity

        self._save_data()

    def search_product(self, keyword):
        result = self.df[
            (self.df['product_id'].astype(str) == str(keyword)) |
            (self.df['name'].str.contains(str(keyword), case=False))
        ]
        if result.empty:
            return "Product not found."
        return result.to_string(index=False)

    def generate_report(self):
        if self.df.empty:
            return "Inventory is empty."
        return self.df.to_string(index=False)
