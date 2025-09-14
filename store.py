balance = 200
cart = []

store = {"cup": 18, "trousers": 80, "shirt": 65}
prices = {"cup": 5, "trousers": 30, "shirt": 15,}

while True:
    choice = input("Type 'store' or 'exit': ")

    if choice == "exit":
        print("Cart:", cart)
        print("Balance:", balance)
        break

    if choice == "store":
        print("Store:", store)
        print("Prices:", prices)
        item = input("What do you want to buy? ")

        if item in store:
            if store[item] > 0 and balance >= prices[item]:
                cart.append(item)
                balance -= prices[item]
                store[item] -= 1
                print("Added:", item)
                print("Cart:", cart)
                print("Balance:", balance)
            else:
                print("No items left or not enough money!")
        else:
            print("No such item in store!")
