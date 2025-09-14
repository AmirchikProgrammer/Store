balance = 2000
cart = []

store = {"cup": 20, "trousers": 60, "shirt": 40}
prices = {"cup": 50, "trousers": 200, "shirt": 150,}

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
