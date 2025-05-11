class ItemToPurchase:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self, customer_name, current_date):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, name):
        self.cart_items = [item for item in self.cart_items if item.name != name]

    def modify_item(self, item):
        for cart_item in self.cart_items:
            if cart_item.name == item.name:
                if item.description != 'none':
                    cart_item.description = item.description
                if item.price != 0:
                    cart_item.price = item.price
                if item.quantity != 0:
                    cart_item.quantity = item.quantity

    def print_descriptions(self):
        print("Item Descriptions:")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")

    def print_total(self):
        total_cost = sum(item.price * item.quantity for item in self.cart_items)
        print(f"Total: ${total_cost:.2f}")

def print_menu(cart):
    menu = """
    MENU
    a - Add item to cart
    r - Remove item from cart
    c - Change item quantity
    i - Output items' descriptions
    o - Output shopping cart
    q - Quit
    Choose an option:
    """
    while True:
        print(menu)
        choice = input().strip()
        if choice == 'q':
            break
        elif choice == 'a':
            print("ADD ITEM TO CART")
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = float(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(name, description, price, quantity)
            cart.add_item(item)
        elif choice == 'r':
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove: ")
            cart.remove_item(name)
        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")  # Added prompt for changing item quantity
            name = input("Enter the item name: ")  # Prompt for item name
            quantity = int(input("Enter the new quantity: "))  # Prompt for new quantity
            item = ItemToPurchase(name, 'none', 0, quantity)  # Create new ItemToPurchase object with updated quantity
            cart.modify_item(item)
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        else:
            print("Invalid option. Please choose again.")

def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)

if __name__ == "__main__":
    main()
