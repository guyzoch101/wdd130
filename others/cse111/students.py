import csv

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
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}
    
    with open(filename, "rt") as csv_file:
        
        reader = csv.reader(csv_file)
        next(reader)
        
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                
                dictionary[key] = row_list[1]
    
    return dictionary

def main():
    
    student_dictionary = read_dictionary("students.csv", 0)
    
    i_number = input("Please enter an I-number (xxxxxxxxx): ")
    
    i_number_clean = i_number.replace("-", "")
    
    if not i_number_clean.isdigit():
        print("Invalid I-Number")        
    
    elif len(i_number_clean) < 9:
        print("Invalid I-Number: too few degits")
        
    elif len(i_number_clean) > 9:
        print("Invalid I-Number: too many digits")
    
    if i_number_clean in student_dictionary:
        student_name = student_dictionary[i_number_clean]
        print(student_name)
    
    elif i_number_clean not in student_dictionary and i_number_clean.isdigit():
        print("No such student")
    
    pass

if __name__ == "__main__":
    main()