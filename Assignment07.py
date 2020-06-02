# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with pickling and structured error handling
# ChangeLog (Who,When,What):
# KOdland,5.31.2020,created file
# KOdland,5.31.2020,added code with pickling example
# KOdland,6.1.2020,added code with error handling
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
import pickle
lstBills = []

class FileNotDATError(Exception):
    """ File extension must end with .dat """
    def __str__(self):
        return 'File extension not .dat'


# Processing  --------------------------------------------------------------- #
def write_to_file(file_name, list_of_bills):
    """ Pickles data and saves it to file

    :param file_name: (string) of dat file
    :param list_of_bills: (list) of dictionary rows
    :return: nothing
    """
    open_file = open(file_name, "wb")
    pickle.dump(list_of_bills, open_file)
    open_file.close()


def read_from_file(file_name):
    """ Unpickles data from file

    :param file_name: (string) of dat file
    :return: (list) of dictionary rows from file
    """
    open_file = open(file_name, "rb")
    list_of_bills = pickle.load(open_file)
    open_file.close()
    return list_of_bills


# Presentation (Input/Output)  -------------------------------------------- #
def input_new_bill(list_of_bills):
    """ Asks the user to input a new bill, the cost, and the due date

    :param list_of_bills: (list) of dictionary rows
    :return: (list) of dictionary rows
    """
    bill = input("Enter a bill: ")
    cost = float(input("Enter the amount owed [$]: "))
    due = input("Enter due date [MM/DD]: ")
    dic_row = {"Bill": bill, "Cost": cost, "Due": due}
    list_of_bills.append(dic_row)
    return list_of_bills


def enter_file_name(read_write):
    """ Asks the user to input a .dat file name

    :param read_write: (string) to show whether file is to read or write
    :return: (string) of file name
    """
    file = ""
    if read_write == "w":
        file = input("Please type a file name to save bills data [.dat]: ")
    elif read_write == "r":
        file = input("Please type a file name to read bills data [.dat]: ")

    if not file.endswith("dat"):
        raise FileNotDATError
    return file


def more_bills():
    """ Asks the user to choose to continue or quit

    :return: (string) of user choice
    """
    choice = input("Press 1 to continue program or 2 to save and quit: ")
    return choice


# Main Body of Script  ------------------------------------------------------ #
strFileName = enter_file_name("w")
while True:
    try:
        lstBills = input_new_bill(lstBills)
    except ValueError:
        print("Please only enter a number for the cost of the bill\n")
        continue
    userChoice = more_bills()
    if userChoice == "1":
        continue
    else:
        write_to_file(strFileName, lstBills)
        print("Data saved\n")
        break

# get data from file and print it
while True:
    try:
        strFileName = enter_file_name("r")  # get file name to read from
        print(read_from_file(strFileName))  # print contents of file
    except FileNotFoundError:
        print("File does not exist\n")
    else:
        break  # if no error, break out of while loop
