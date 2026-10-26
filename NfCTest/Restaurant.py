class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.orders = []
        self.total_bill = 0

    def show_customer(self):
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("Total Bill:", self.total_bill)


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []
        self.customers = []
        self.total_income = 0

    def add_menu_item(self):
        name = input("Enter food name: ")
        price = float(input("Enter food price: "))

        item = MenuItem(name, price)
        self.menu.append(item)

        print("Menu item added successfully!")

    def show_menu(self):
        if len(self.menu) == 0:
            print("Menu is empty.")
        else:
            print("\n--- Restaurant Menu ---")

            for i, item in enumerate(self.menu, start=1):
                print(i, ".", item.name, "- Rs.", item.price)

    def add_customer(self):
        name = input("Enter customer name: ")
        phone = input("Enter customer phone: ")

        customer = Customer(name, phone)
        self.customers.append(customer)

        print("Customer added successfully!")

    def show_customers(self):
        if len(self.customers) == 0:
            print("No customers found.")
        else:
            print("\n--- Customer List ---")

            for customer in self.customers:
                customer.show_customer()
                print("--------------------")

    def place_order(self):
        if len(self.customers) == 0:
            print("Please add a customer first.")
            return

        if len(self.menu) == 0:
            print("Please add menu items first.")
            return

        phone = input("Enter customer phone: ")

        selected_customer = None

        for customer in self.customers:
            if customer.phone == phone:
                selected_customer = customer
                break

        if selected_customer is None:
            print("Customer not found.")
            return

        self.show_menu()

        choice = int(input("Enter menu item number: "))
        quantity = int(input("Enter quantity: "))

        if choice < 1 or choice > len(self.menu):
            print("Invalid menu choice.")
            return

        if quantity <= 0:
            print("Quantity must be positive.")
            return

        item = self.menu[choice - 1]
        bill = item.price * quantity

        selected_customer.orders.append(
            (item.name, quantity, bill)
        )

        selected_customer.total_bill += bill
        self.total_income += bill

        print("\nOrder placed successfully!")
        print("Customer:", selected_customer.name)
        print("Food:", item.name)
        print("Quantity:", quantity)
        print("Bill: Rs.", round(bill, 2))
        print(
            "Customer Total: Rs.",
            round(selected_customer.total_bill, 2)
        )

    def show_income(self):
        print("\n--- Restaurant Income ---")
        print("Total Income: Rs.", round(self.total_income, 2))

    def menu_options(self):
        while True:
            print("\n===== RESTAURANT MANAGEMENT =====")
            print("1. Add Menu Item")
            print("2. Show Menu")
            print("3. Add Customer")
            print("4. Show Customers")
            print("5. Place Order")
            print("6. Show Total Income")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_menu_item()

            elif choice == "2":
                self.show_menu()

            elif choice == "3":
                self.add_customer()

            elif choice == "4":
                self.show_customers()

            elif choice == "5":
                self.place_order()

            elif choice == "6":
                self.show_income()

            elif choice == "7":
                print("Thank you for visiting!")
                break

            else:
                print("Invalid choice!")


restaurant_name = input("Enter restaurant name: ")

restaurant = Restaurant(restaurant_name)
restaurant.menu_options()
```