class Inventory:
    def __init__(self):
        self.items = []

    def create_item(self, name, quantity, price):
        new_item = {"name": name, "quantity": quantity, "price": price}
        self.items.append(new_item)
        print(f"Item '{name}' added to inventory.")

    def read_items(self):
        print("Inventory:")
        for item in self.items:
            print(f"  {item['name']} - Quantity: {item['quantity']}, Price: {item['price']}")

    def update_item(self, name, quantity=None, price=None):
        for item in self.items:
            if item["name"] == name:
                if quantity:
                    item["quantity"] = quantity
                if price:
                    item["price"] = price
                print(f"Item '{name}' updated.")
                return
        print(f"Item '{name}' not found.")

    def delete_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                print(f"Item '{name}' deleted.")
                return
        print(f"Item '{name}' not found.")

    def sort_items(self, by="name"):
        if by == "name":
            self.items.sort(key=lambda x: x["name"])
        elif by == "quantity":
            self.items.sort(key=lambda x: x["quantity"])
        elif by == "price":
            self.items.sort(key=lambda x: x["price"])
        print(f"Inventory sorted by {by}.")

    def search_item(self, name):
        for item in self.items:
            if item["name"] == name:
                print(f"Item '{name}' found:")
                print(f"  Quantity: {item['quantity']}, Price: {item['price']}")
                return
        print(f"Item '{name}' not found.")

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Create Item")
        print("2. Read Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Sort Items")
        print("6. Search Item")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            inventory.create_item(name, quantity, price)
        elif choice == "2":
            inventory.read_items()
        elif choice == "3":
            name = input("Enter item name: ")
            quantity = int(input("Enter new quantity (or leave blank): ") or 0)
            price = float(input("Enter new price (or leave blank): ") or 0)
            inventory.update_item(name, quantity, price)
        elif choice == "4":
            name = input("Enter item name: ")
            inventory.delete_item(name)
        elif choice == "5":
            by = input("Sort by (name, quantity, price): ")
            inventory.sort_items(by)
        elif choice == "6":
            name = input("Enter item name: ")
            inventory.search_item(name)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()