while True:
    total = 0
    customer_name = input("Enter customer name: ")
    while True:
        print("Enter item quantity and number: ")
        Item = input("Item: ")
        cost = int(input("Cost: "))
        quantity = int(input("Qty: "))
        total += quantity * cost
        repeat = input("Do you want to add more items? (y/n)")
        if repeat.lower() == 'n':
            break
    print("Customer Name:", customer_name)
    print("Total Amount:", total)
    new_customer = input("Go to the next person? (Y/y/N/n)")
    if new_customer.lower() == 'n':
        break
print("No more customers.")
input()