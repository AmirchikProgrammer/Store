balance = 5000
cart = []

store = {"cup": 20, "trousers": 60, "shirt": 40}
prices = {"cup": 50, "trousers": 200, "shirt": 150,}

restoraunt = {"xingal": 20, "crab": 60, "fish": 40}
prices1 = {"xingal": 20, "crab": 40, "fish": 30,}

tech_store = {"samsung": 5, "apple": 2, "hp": 3, "xiaomi": 10, "macbook": 1}
prices2 = {"samsung": 700, "apple": 2000, "hp": 1500, "xiaomi": 500, "macbook": 2500}
while True:
    choice = input("Type 'store', 'restoraunt', 'tech store' or 'exit': ")

    if choice == "exit":
        print("Cart:", cart)
        print("Balance:", balance)
        break

    if choice == "store":
        print("Store:", store)
        print("Prices:", prices)
        item = input("What do you want to buy in store? ")

        if item in store:
            if store[item] > 0 and balance >= prices[item]:
                cart.append(item, prices2[item])
                balance -= prices[item]
                store[item] -= 1
                print("Added:", item)
                print("Cart:", cart)
                print("Balance:", balance)
            else:
                print("No items left or not enough money!")
        else:
            print("No such item in store!")
    elif choice == "restoraunt":
        print("Restoraunt:", restoraunt)
        print("Prices:", prices1)
        item = input("What do you want to buy in restoraunt? ")

        if item in restoraunt:
            if restoraunt[item] > 0 and balance >= prices1[item]:
                cart.append(item, prices2[item])
                balance -= prices1[item]
                restoraunt[item] -= 1
                print("Added:", item)
                print("Cart:", cart)
                print("Balance:", balance)
            else:
                print("No items left or not enough money!")
        else:
            print("No such item in restoraunt!")
    elif choice == "tech store":
        print("TechStore:", tech_store)
        print("Prices:", prices2)
        item = input("What do you want to buy in TechStore? ")

        if item in tech_store:
            if tech_store[item] > 0 and balance >= prices2[item]:
                cart.append(item, prices2[item])
                balance -= prices2[item]
                tech_store[item] -= 1
                print("Added:", item)
                print("Cart:", cart)
                print("Balance:", balance)
            else:
                print("No items left or not enough money!")
        else:
            print("No such item in TechStore!")
