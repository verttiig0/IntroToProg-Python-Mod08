# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# GShay,5.31.2021,Modified code to complete assignment 8
# GShay,5.31.2021,Added functions for menu and to get inputs
# GShay,5.31.2021,Added functions for reading and writing to the file
# GShay,5.31.2021,Added getter and setter for product and price
# GShay,6.1.2021,Updated code to use product class
# GShay,6.1.2021,Updated docstrings
#
#    Github: https://github.com/verttiig0/IntroToProg-Python-Mod08
#
# ------------------------------------------------------------------------ #


# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strChoice = ''


class Product:
    """
    Stores data about a product:

    properties:
        product_name: (string) with the products' name
        product_price: (float) with the products' standard price

    methods:
        __init__(self, product_name, product_price):
        __str__(self)
        product_name(self)
        product_name(self, name)
        product_price(self)
        product_price(self, value)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        GShay,5.31.2021,Modified code to complete assignment 8
        GShay,5.31.2021,Added getter and setter for product and price
        GShay,6.1.2021,Added
    """

    # -- Constructor --
    def __init__(self, product_name, product_price):
        self.__product_name = product_name
        self.__product_price = product_price

    def __str__(self):
        """
        Defines how the class prints the string
        """
        return 'Product = ' + str(self.__product_name) + ', $' + str(self.__product_price)

    # -- Properties --
    @property
    def product_name(self):
        """
        Returns the product name
        """
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, name):
        """
        Verifies the product not a number and sets the value
        :param name: (string) name of the product
        """
        if not str(name).isnumeric():
            self.__product_name = name
        else:
            raise Exception("Names can not be numbers")

    @property
    def product_price(self):
        """
        Returns the product price
        """
        return self.__product_price

    @product_price.setter
    def product_price(self, value):
        """
        Verifies the price is a float and sets the value
        :param value: (string) price of the product
        """
        try:
            float(value)
            self.__product_price = value
        except ValueError:
            raise Exception("Price must be numbers")

# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """
    Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        GShay,5.31.2021,Modified code to complete assignment 8
        GShay,5.31.2021,added functions to read and save the data
        GShay,6.1.2021,updated list to use Product class
    """

    @staticmethod
    def read_data_from_file(file_name):
        """
        Reads data from a file into list of objects
        :param file_name: (string) with name of file:
        :return: (list) of objects
        """
        try:
            list_of_objects = []
            file = open(file_name, "r")
            for line in file:
                product, price = line.split(",")
                obj1 = Product(product.strip(), price.strip())
                list_of_objects.append(obj1)
            file.close()
            return list_of_objects
        except FileNotFoundError as e:
            print('File not found')
            return []

    @staticmethod
    def save_data_to_file(file_name, list_of_objects):
        """
        Writes data from the list to the file
        :param file_name: (string) name of file
        :param list_of_objects: (list) list of objects
        """
        file = open(file_name, 'w')
        for obj in list_of_objects:
            file.write(obj.product_name + ',' + str(obj.product_price) + '\n')
        file.close()
        print('Writing data to file')

# Processing  ------------------------------------------------------------- #


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """
    Displays a menu, gets inputs from user, and displays a list of product objects:

    methods:
        print_menu():
        input_menu_choice()
        print_current_data_in_list(list_of_objects)
        input_new_product():

    changelog: (When,Who,What)
        GShay,5.31.2021,Modified code to complete assignment 8
        GShay,5.31.2021,added functions to print the menu and get input from user
        GShay,6.1.2021,updated print to use objects
    """

    @staticmethod
    def print_menu():
        """
        Display a menu to the user
        """
        print('''
        Menu of Options
        1) Show Current Data
        2) Add new Product
        3) Save Data to File and Exit       
        ''')

    @staticmethod
    def input_menu_choice():
        """
        Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option? [1 to 3] - ")).strip()
        return choice

    @staticmethod
    def print_current_data_in_list(list_of_objects):
        """
        Shows the current data in the list
        :param list_of_objects: (list) display the list to the user
        """
        print("\nThe Current Data is:")
        for obj in list_of_objects:
            print(obj)
        print("--------------")

    @staticmethod
    def input_new_product():
        """
        Gets the input from the user for a new product and price
        :return: (string) product and price
        """
        product = ''
        price = ''
        while not product:
            product = str(input('Enter a product: '))
        while not price:
            price = float(input('Enter a price: '))
        return product, price

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #


lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

while True:
    IO.print_menu()
    strChoice = IO.input_menu_choice()
    if strChoice.strip() == '1':
        IO.print_current_data_in_list(lstOfProductObjects)
        continue

    elif strChoice.strip() == '2':
        product, price = IO.input_new_product()
        objP1 = Product(product, price)
        lstOfProductObjects.append(objP1)
        continue

    elif strChoice.strip() == '3':
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        exit()

# Main Body of Script  ---------------------------------------------------- #
