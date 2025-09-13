balance = 4000

print(f"You are a millionare (Amir), also your balance is {balance}")

storage = {
    'cap': 18, # 5 dollars
    'trousers': 80, # 30 dollars
    'shirt': 65 # 50 dollars

}

storage_prices = {
    'cap_price': 5,
    'trousers_price': 30,
    'shirt_price': 50 

}


question = input("Do you want to buy something?")
if question == "yes":
    print("ok")
    print(f"Now, you have {balance} dollars")
    print(f"storage: {storage}, prices: {storage_prices}")
    choice_c = input("What thing do you wanna to buy?")
    if choice_c == "cap":
        print(f"Cap price is {storage_prices['cap_price']}")
        balance = balance - 5
        storage['cap'] = storage['cap'] - 1
        print(f"your balance is {balance} cap left: {storage['cap']}")
    elif choice_c == "trousers":
        print(f"trousers price is {storage_prices['trousers_price']}")
        balance = balance - 30
        storage['trousers'] = storage['trousers'] - 1
        print(f"your balance is {balance} cap left: {storage['cap']}")
elif question == "no":
    print("Command break...")