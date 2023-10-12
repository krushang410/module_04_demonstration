"""
Description: This program will provide salary increases of 20% to all 
executives at PiXELL-River Financial.  Prior to implementing this change, 
the program will see how many executives will end up with salaries greater than 
the high-salary mark.
Author: ACE Faculty
Edited by: {Student Name}
Date: oct 12th 2023
Usage: 
"""

#raise Exception("An eroor has occured")
"""""
try:
     # code that may raise an exception
    denominator = int(input("Enter a numeric value for a denominator: "))
    quotient = 10 / denominator
    print(f"Quotient is {quotient}")
except ZeroDivisionError:
    # code to handle the exception
    print("Cannot divide by zero.")
    
print("Next line of code...")    


# Initialize file to None (null).
file = None
try:
    # Open the file in read mode.
    file = open('module_4_data.txt', 'r')

    # Read the contents of the file.
    content = file.read()

    # Some exception that may occur unrelated to the input file.
    10 / 0

    # Print the contents.
    print(content)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("A general exception occurred:", e)
finally:
    # Close the file in the finally block
    if file is not None:
        file.close()
        print("File closed.")

numeric_list = [1, 2, 3, 'four', 5, 6, 7, 'eight', 10, 11, 'twelve']
valid_list = []
for number in numeric_list:
    try:
        number = int(number)
        valid_list.append(number)
    except:
        print(valid_list)

# continue with program using valid_list
"""""

import logging

logging.debug('Debug level message.')
logging.info('Info level message')
logging.warning('Warning level message')
logging.error('Error level message')
logging.critical('Critical level message')

logging.basicConfig(level=logging.DEBUG,
                    filename='app.log', 
                    filemode='w', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('This debug message will get logged to a file')


numerator = 5
denominator = 0

logger = logging.getLogger()
try:
    quotient = numerator / denominator
except Exception:
    logging.exception("An exception has occurred: ")        
logger.error("An error has occured")


logger.error("An error has occured")