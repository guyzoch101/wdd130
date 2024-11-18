# Tristan Wong
# 3/13/2024
"""A local grocery store subscribes to an online service that enables its customers
    to order groceries online. After a customer completes an order, the online service
    sends a CSV file that contains the customer’s requests to the grocery store. The
    store needs you to write a program that reads the CSV file and prints to the terminal
    window a receipt that lists the purchased items and shows the subtotal, the sales tax
    amount, and the total."""


# import csv library to read csv files
import csv

# for products_dictionary
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

# for row_list in request.csv
PRODUCT_CODE_INDEX = 0
PRODUCT_QUANTITY_INDEX = 1

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

def get_date_time(form):
    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()
    
    # long: full date and time
    if form == "long":
        current_date_and_time = f"{current_date_and_time:%a %b %d %H:%M:%S %Y}"
    
    # only outputting hour
    elif form == "hour":
        current_date_and_time = f"{current_date_and_time:%H}"
    
    return current_date_and_time


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    # create an empty dictionary to store data from csv files
    dictionary = {}
    
    with open(filename, "rt") as csv_file:
        
        # use csv.reader to read through the file
        reader = csv.reader(csv_file)
        
        # skip the title line in the csv file
        next(reader)
        
        # using a for loop to iterate each line of the csv file
        for row_list in reader:
            
            # skip the row if the row is empty
            if len(row_list) != 0:
                
                """Dictionary:
                    key: [row_list]"""
                key = row_list[key_column_index]
                
                dictionary[key] = row_list
    
    return dictionary


def discount_decider():
    
    """Determining if this invoice is eligible for discount
        
        Parameters: none
        Return: True or False"""
    
    # get full date and time
    current_date_and_time = get_date_time("long")
    
    # only getting the hour
    hour = int(get_date_time("hour"))
    
    if ("Tue" or "Wed" in current_date_and_time) or (hour < 11):
        return True
    else:
        return False


def main():

    try:
        # calling discount_decider function to determine if the invoice is eligible to discounts\
        discount = discount_decider()
        
        # calls the read_dictionary function to read the file: products.csv    
        products_dict = read_dictionary("products.csv", 0)
        
        # Store name
        print()
        print("Tristan's Place")
        
        print()
        print("Purchased Items:")
    
        # reads the file: request.csv
        with open("request.csv", "rt") as request_csv:
            
            # use csv.reader to read through the file
            request_reader = csv.reader(request_csv)
            
            # skip the title line in the csv file
            next(request_reader)
            
            # for invoice
            subtotal = 0
            number_of_items = 0
            
            # using a for loop to iterate each line of the csv file
            for row_list in request_reader:
                
                # skip the row if the row is empty
                if len(row_list) != 0:
                    
                    
                    product_code = row_list[PRODUCT_CODE_INDEX]
                    
                    # define quantity_requested to calculate sum of requested_quantity for a product
                    # resets to 0 every time it finished obtaining info for 1 product
                    quantity_requested = 0
                    quantity_requested = int(row_list[PRODUCT_QUANTITY_INDEX])
                    
                    product_info = products_dict[product_code]
                    product_name = product_info[PRODUCT_NAME_INDEX]
                    product_price = float(product_info[PRODUCT_PRICE_INDEX])

                # Invoiced items
                print(f"{product_name}: {quantity_requested} @ {product_price}")
                
                # calculating the subtotal
                subtotal = subtotal + product_price * quantity_requested
                
                # calculating the number of items
                number_of_items = number_of_items + quantity_requested
            
            # subtotal is stored in the corresponding variable, uses the return value from
            # the discount function to calculate the new subtotal if discount is awarded    
            if discount:
                subtotal = 0.9 * subtotal
                
                print()
                print("You are eligible for a 10% discount!")
                
            # calculating the amount of sales tax
            sales_tax = subtotal * 0.06
                
            # calculating the total amount
            total_amount = subtotal + sales_tax
            
            # printing the data: 1) Number of Items; 2) Subtotal; 3) Sales Tax; 4) Total
            print()
            print(f"Number of Items: {number_of_items}")
            print(f"Subtotal: ${round(subtotal, 2)}")
            print(f"Sales Tax (6%): ${round(sales_tax, 2)}")
            print(f"Total: ${round(total_amount, 2)}")
            
            print()
            print("Thank you for shopping at Tristan's Place.")
            
            # calling get_date_time function to get current date and time
            current_date_and_time = get_date_time("long")
            
            # displaying date time: day of the week month/day time year
            print(current_date_and_time)
        
    except KeyError as unknown_key:
        print("Error: unknown product ID in the request.csv file\n", unknown_key)
    except FileNotFoundError as unknown_file:
        print("Error: missing file")
        print(unknown_file)

    pass


if __name__ == "__main__":
    main()