print("Bridgend Ravens Till System")

total = 0

while True:
    print("\nMenu")
    print("1. Pepsi Max - £2.50")
    print("2. Guinness - £5.20")
    print("3. Cheese and Onion Walkers - £2.00")
    print("4. Smarties - £2.00")
    print("5. Double Vodka and Pepsi - £6.20")
    print("6. Finish Order")

    choice = input("Choose an option: ")

    if choice == "1":
        total += 2.50
        print("Pepsi Max added")

    elif choice == "2":
        total += 5.20
        print("Guinness added")

    elif choice == "3":
        total += 2.00
        print("Cheese and Onion Walkers added")

    elif choice == "4":
        total += 2.00
        print("Smarties added")

    elif choice == "5":
        total += 6.20
        print("Double Vodka and Pepsi added")

    elif choice == "6":
        break

    else:
        print("Invalid option")

print("\nOrder Complete")
print(f"Total Cost: £{total:.2f}")
