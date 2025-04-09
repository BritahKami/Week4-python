def message(message):
    x = f'\n\n***\n{message}\n***\n\n'
    print(x)

def errorhandler(e):
    with open ('logs.txt', 'w') as err:
        err.write(str(e))
    
    print("An error occured. Try again later")
    

def modify_text(text):
    return text.upper()

def read_and_modify_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Original file read successfully.")

            modified_content = modify_text(content)

            new_filename = "modified_" + filename
            try:
                with open(new_filename, 'w') as new_file:
                    new_file.write(modified_content)
                    print(f"Modified content written to '{new_filename}'.")
            except Exception as e:
                errorhandler(e)

    except Exception as e:
        errorhandler(e)

read_and_modify_file()
