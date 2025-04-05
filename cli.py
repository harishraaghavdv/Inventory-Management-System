from inventory import Inventory, Product

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Product")
        print("4. Search Product")
        print("5. Generate Inventory Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            try:
                price = float(input("Enter Price: "))
                quantity = int(input("Enter Quantity: "))
                product = Product(product_id, name, price, quantity)
                inventory.add_product(product)
                print(" Product added successfully!")
            except Exception as e:
                print(" Error:", e)

        elif choice == "2":
            product_id = input("Enter Product ID to remove: ")
            try:
                inventory.remove_product(product_id)
                print(" Product removed successfully!")
            except Exception as e:
                print(" Error:", e)

        elif choice == "3":
            product_id = input("Enter Product ID to update: ")
            new_price = input("Enter new price (leave blank to skip): ")
            new_quantity = input("Enter new quantity (leave blank to skip): ")

            try:
                inventory.update_product(
                    product_id,
                    float(new_price) if new_price else None,
                    int(new_quantity) if new_quantity else None
                )
                print(" Product updated successfully!")
            except Exception as e:
                print(" Error:", e)

        elif choice == "4":
            keyword = input("Enter Product ID or Name: ")
            print(" Search Result:")
            print(inventory.search_product(keyword))

        elif choice == "5":
            print("\n Inventory Report:")
            print(inventory.generate_report())

        elif choice == "6":
            print(" Exiting program. Goodbye!")
            break

        else:
            print(" Invalid choice, please try again.")

if __name__ == "__main__":
    main()
