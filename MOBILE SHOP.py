import random
import time

# Define a dictionary to store the user's cart
cart = {}

# Function to print text slowly
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

# Welcome screen function
def welcome_screen():
    print_slow('\t\t\tCartCrafters Online Shop')
    print_slow('\t\t  Your one-stop shop for all things online')

# Show the main menu and get the user's choice
def show_menu():
    print("1. Welcome\n2. Our Mission\n3. Categories\n4. View Cart\n5. Check-out\n6. Exit\n")
    return int(input("Enter Choice: "))

# Function to display a welcome message
def welcome_message():
    welcome_text = (
        '\t\t\tWelcome!!\n\n'
        'Welcome To CartCrafters Online Mobile Shop\n\n'
        'Are you new here?\n\n'
        'Sign Up or Log in to get the latest deals, info, address saving, and the latest scoop on your favorite products!'
    )
    print_slow(welcome_text)
    time.sleep(3)

# Function to display the mission statement
def mission_message():
    mission_text = (
        '\t\t\tOur Mission\n\n'
        'We hope to empower the common man to be able to use technology that they would not be able to normally get...\n'
        '40% of all our profits go to the Child Help Foundation in Velachery'
    )
    print_slow(mission_text)
    time.sleep(3)

# Show the categories menu and get the user's choice
def show_categories():
    print("1. Groceries\n2. Cooking essentials\n3. Tech")
    return int(input("Enter Choice: "))

# Function to display and handle the tech category
def show_tech():
    print("Loading...")
    time.sleep(1)
    print("ID|\t\t\t|Name|\t\t\t\t|Price|\t\t|Specs|")
    
    tech_list = {
        '1': ['HP Pavilion x360 Convertible', 25000, '4GB RAM, Intel Pentium Silver Processor'],
        '2': ['Acer Laptop 001', 64000, '8GB RAM, Intel Core i3'],
        '3': ['Dell Laptop 002', 100000, '256GB RAM, AMD Ryzen 360 Series']
    }

    for key, value in tech_list.items():
        print(f'|{key}|\t\t|{value[0]}|\t\t|{value[1]}|-|\t{value[2]}|')

    while True:
        ch1 = input("Enter Product to buy: [N to exit] ")
        if ch1.upper() == 'N':
            break
        elif ch1 in tech_list:
            product = tech_list[ch1]
            prod = product[0]
            price = product[1]
            n = int(input(f"How many {prod} would you like to buy?: "))
            tot = price * n
            time.sleep(2)
            print(f"The price of {n} {prod} laptops is {tot}")
            time.sleep(2)
            con = input("Would you like to buy?\n1. Y for Yes\n2. N for no\nEnter Choice: ")
            if con.upper() == 'Y' or con == '1':
                cart[prod] = [price, n, tot]
        else:
            print("Invalid Choice")
            time.sleep(3)

# Function to display and handle the groceries category
def show_groceries():
    print("loading...")
    time.sleep(3)
    print("\t\t\t\tGROCERIES")
    print('ID\tNAME\tWeight\t\tCOMPANY\t\tTYPE')
    
    grocery_list = {
        '1': ['Rice', '1 KG', '$2', 'SONA MASOORI'],
        '2': ['APPLE', '1 KG', '$2', 'KING APPLE'],
        '3': ['ORANGE', '1 KG', '$1.5', 'KING ORANGE'],
        '4': ['ONIONS', '1 KG', '$0.5', 'ONIONS- By The Bulk'],
        '5': ['TOMATO', '1 KG', '$2', 'TOMATO-By The Bulk']
    }

    for key, value in grocery_list.items():
        print(f'|{key}|\t{value[0]}\t{value[1]}\t{value[2]}\t{value[3]}|')

    while True:
        choice = input("Please Enter Product to buy (N to exit): ")
        if choice.upper() == 'N':
            break
        elif choice in grocery_list:
            product = grocery_list[choice]
            prod = product[0]
            weight = product[1]
            price = float(product[2].replace('$', ''))
            n = int(input(f"How many {prod} ({weight}) would you like to buy?: "))
            tot = price * n
            time.sleep(2)
            print(f"The price of {n} {prod} ({weight}) is {tot}")
            time.sleep(2)
            con = input(f"Would you like to buy {prod}?\n1. Y for Yes\n2. N for no\nEnter Choice: ")
            if con.upper() == 'Y' or con == '1':
                cart[prod] = [price, n, tot]
        else:
            print("Invalid Choice")
            time.sleep(3)

# Function to display and handle the cooking essentials category
def show_cooking_essentials():
    print("|SNo|\t|Name\t|Weight\t|Price|\t|Company|")
    print("-----------------------------------------")
    
    essentials_list = {
        '1': ['Khayam', '100gms', '$3.50', 'HingRaj'],
        '2': ['Salt', '1Kg', '$2.00', 'TataSalt'],
        '3': ['Sugar', '1KG', '$2.00', 'TataSugar'],
        '4': ['CHILLI', '100g', '$6.00', 'EVEREST']
    }

    for key, value in essentials_list.items():
        print(f'|{key}|\t{value[0]}\t{value[1]}\t{value[2]}\t{value[3]}|')

    while True:
        choice2 = input("Enter Choice [N to exit]: ")
        if choice2.upper() == 'N':
            break
        elif choice2 in essentials_list:
            product = essentials_list[choice2]
            prod = product[0]
            price = float(product[2].replace('$', ''))
            n = int(input(f"Enter the number of units of {prod}: "))
            tot = price * n
            print(f"Price of {n} units of {prod} is: {tot}")
            con = input(f"Would you like to buy {prod}?\n1. Y for Yes\n2. N for no\nEnter Choice: ")
            if con.upper() == 'Y' or con == '1':
                cart[prod] = [price, n, tot]
        else:
            print("Invalid Choice")
            time.sleep(3)

# Function to display the user's cart
def view_cart():
    if not cart:
        print("Cart is empty. Go fill it up!")
    else:
        print("Loading...")
        time.sleep(3)
        print("\t\t\t\tYour Cart")
        print("Name\tNo of items\tPrice per unit\tBuying Price")
        for k, a in cart.items():
            print(k, end='\t')
            for i in a:
                print(i, end='\t\t')
            print()

# Function to handle the checkout process
def checkout():
    print("Checking Out..")
    total_cost = 0
    for item in cart.values():
        total_cost += item[2]
    print(f"You have to pay ${total_cost:.2f}")



# Main function to run the program
def main():
    while True:
        welcome_screen()
        choice = show_menu()
        if choice == 1:
            welcome_message()
        elif choice == 2:
            mission_message()
        elif choice == 3:
            category_choice = show_categories()
            if category_choice == 1:
                show_groceries()
            elif category_choice == 2:
                show_cooking_essentials()
            elif category_choice == 3:
                show_tech()
        elif choice == 4:
            view_cart()
        elif choice == 5:
            checkout()
            while True:
                print("Please Enter Payment Details", end='')
                payment = input(": ")
                if payment == '':
                    pass
                else:
                    break
            print("Your payment is confirmed!!!")
            while True:
                address = input("Enter Address: ")
                if address == '':
                    pass
                else:
                    break
            print("We will ship your products to your address")
            a = random.randrange(1, 4)
            print("Please expect your products to come within", a, "business days")
            time.sleep(3)
            print()
            cart= { }
        elif choice == 6:
            print("Exiting...")
            time.sleep(3)
            print("Exited")

# Run the program if this script is executed
if __name__ == "__main__":
    main()
