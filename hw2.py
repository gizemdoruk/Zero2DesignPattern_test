customers = {}
orders = {}

def add_new_customer():
    name = input("Customer Name: ")
    surname = input("Customer Surname: ")
    email = input("Email: ")
    phone = input("Phone Number: ")
    customer_id = len(customers) + 1
    customer = {
        "Name": name,
        "Surname": surname,
        "Email": email,
        "Phone": phone
    }
    customers[customer_id] = customer
    print(name, surname, "has been added.")

def create_new_order():
    print("Customers:")
    for customer_id, customer in customers.items():
        print("customer_id:",customer_id,":",customer['Name'], customer['Surname'])
    customer_id = int(input("Enter Customer ID (press 0 to add new customer): "))
    if customer_id == 0:
        add_new_customer()
        customer_id = len(customers)
    order_name = input("Order Name: ")
    order_quantity = int(input("Order Quantity: "))
    order_date = input("Order Date: ")
    order_id = len(orders) + 1
    order = {
        "Customer ID": customer_id,
        "Order Name": order_name,
        "Order Quantity": order_quantity,
        "Order Date": order_date
    }
    orders[order_id] = order
    print("Order has been created. Order ID: ", order_id)

def order_status_check():
    order_id = int(input("Enter order ID: "))
    if order_id in orders:
        order = orders[order_id]
        customer = customers[order["Customer ID"]]
        print("Order Info:")
        print("Order ID:", order_id)
        print("Order Name: ",order['Order Name'])
        print("Order Quantity: ",order['Order Quantity'])
        print("Order Date: ",order['Order Date'])
        print("Customer Name: ", customer['Name'], customer['Surname'])
        print("Email: ", customer['Email'])
        print("Phone: ",customer['Phone'])
    else:
        print("Invalid Order ID!")

def customer_list():
    print("Customer List:")
    for customer_id, customer in customers.items():
        print("Customer ID: ", customer_id)
        print("Name: ",customer['Name'])
        print("Surname: ",customer['Surname'])
        print("Email: ",customer['Email'])
        print("Phone: ",customer['Phone'])
        print()

while True:
    print("Options:")
    print("1. Add New Customer")
    print("2. Create New Order")
    print("3. Order Status Check")
    print("4. Customer List")
    print("5. Exit")
    
    selection = input("Enter an option (1,2,3,4,5): ")
    
    if selection == "1":
        add_new_customer()
    elif selection == "2":
        create_new_order()
    elif selection == "3":
        order_status_check()
    elif selection == "4":
        customer_list()
    elif selection == "5":
        print("Exiting.")
        break
    else:
        print("Invalid selection ! Please try again.")
        