# ========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialize the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    '''
        Add the code to return the cost of the shoe in this method.
    '''

    def get_cost(self):
        return self.cost

    '''
        Add the code to return the quantity of the shoes.
    '''

    def get_quantity(self):
        return self.quantity

    '''
        Add a code to return a string representation of a class.
    '''

    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n"


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''

# Read from a file
file = open("inventory.txt", "r")
file2 = open("inventory.txt", "a+")

shoe_obj = []
shoe_list = []

# ==========Functions outside the class==============
'''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
'''


def read_shoes_data():

    try:
        # Read the file from the second line
        for line in file:
            row = line.strip("\n")
            split_line = row.split(",")
            shoe_list.append(split_line)

        # Creating a Shoe object
        for i in range(1, len(shoe_list)):
            array = shoe_list[i]
            new_row = Shoe(array[0], array[1], array[2], array[3], int(array[4]))
            shoe_obj.append(new_row)
    except FileNotFoundError:
        print("File inventory.txt not available")
        file.close


'''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
 '''


def capture_shoes():
    try:
        # request input from the user
        new_country = input("Please enter the country of your product:\n")
        new_code = input("Please enter the code of your product:\n")
        new_product = input("Please enter the name of your product:\n")
        new_cost = int(input("Please enter the cost of your product:\n"))
        new_quantity = int(input("Please enter the quantity of your product :\n"))
        shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)
        shoe_obj.append(shoe)

        file2.write(f'\n{new_country},{new_code},{new_product},{new_cost},{new_quantity}')
        print("\n New  product has been loaded!\n")
        file2.close()

    except ValueError:
        print("Please enter a valid number ")
        file2.close()


'''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organize your data in a table format
    by using Python’s tabulate module.
'''

'''
Define the function view all  and get shoes from the shoe object then display using tabulate
'''


def view_all():
    table = []
    for line in shoe_obj:
        table.append([line.country, line.code, line.product, line.cost, line.quantity])
    # Print the data in a table format
    for row in table:
        print(','.join(map(str, row)))
    file.close()


'''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
'''

'''   Define the lowest quantity that will display the lowest quantity from the text file,
      Set an empty list Append the value the list, and print on the console using min to get 
      the minimum value Ask the user if they want to update the shoe quantity and update the new quantity 
 '''


def restock():
    try:
        lowest_qty = min(shoe_obj, key=lambda x: x.quantity)
        print(f"{lowest_qty.country}, {lowest_qty.code}, {lowest_qty.product}, {lowest_qty.cost}, {lowest_qty.quantity}")

        choice = input("Do you want to restock this shoe? (y/n) ")
        if choice.lower() == 'n':
            print("No restock needed items ! ")
            return
        elif choice.lower() == 'y':
            quantity = int(input(f"Enter quantity to add (currently {lowest_qty.quantity} available): "))
            lowest_qty.quantity += quantity
            with open('inventory.txt', 'r+') as file2:
                lines = file2.readlines()

                # sets the file's current position
                file2.seek(0)
                file2.write(lines[0])

                # Read the file from the second line
                for line in lines[1:]:
                    data = line.strip().split(',')
                    if data[1] == lowest_qty.code:
                        data[4] = str(lowest_qty.quantity)
                        line = ','.join(data) + '\n'
                    file2.write(line)

    except ValueError:
        print("Please enter a valid number ")
    file.close()


'''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
'''


def search_shoe():
    search_code = input("\nPlease enter the code you are searching for:\n\n")
    with open("inventory.txt", "r") as file:
        lines = file.readlines()[1:]
    for shoe in lines:
        if shoe.find(search_code) != -1:
            print(shoe)
    else:
        print("This code does not exist on inventory.txt")
    file.close()


'''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
'''


def value_per_item():
    table = []
    for line in shoe_obj:
        value = int(line.get_cost()) * int(line.get_quantity())
        table.append([line.country, line.product, value])
    # Print the data in a table format
    for row in table:
        print(','.join(map(str, row)))
    file.close()


'''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
'''


def highest_quantity():
    # Mark item as sale
    print("\n This item is on sale!! ")
    print(max(shoe_obj, key=lambda item: item.quantity))

 #==========Main Menu=============
'''
    Create a menu that executes each function above.
    This menu should be inside the while loop. Be creative!
'''


read_shoes_data()
while True:
    try:
        menu = int(input(
                "\n1. Capture Shoes"
        "\n2. View All"
        "\n3. Restock "
        "\n4. Search"
        "\n5. View Item Values"
        "\n6. View Sale Items"
        "\n  Choose any number greater than 6 to EXIT! "
        "\nPlease select from the menu above:"
                
        )
        
        )
        

        if menu == 1:
                capture_shoes()

        elif menu == 2:
                view_all()

        elif menu == 3:
                restock()

        elif menu == 4:
                search_shoe()

        elif menu == 5:
                value_per_item()

        elif menu == 6:
                highest_quantity()
        elif menu > 6:
             print("You can no longer make changers on inventory.txt")
             break
  
    except ValueError:
         print("\nYou have selected an invalid option. ")
           
               
