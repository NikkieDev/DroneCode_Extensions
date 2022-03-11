import os

def create_file(file_name="file", file_extension="txt", file_location="./"):
    file = open(f"{file_location}/{file_name}.{file_extension}", "w")
    file.close()
    print(f"Created file: {file_name}.{file_extension} in {file_location}")

def delete_file(path_to_file=None):
    if path_to_file is None:
        print("ERROR: Missing required argument: 'You need to select a file to delete!'")

    elif path_to_file is not None:
        try:
            os.remove(path_to_file)
            print("File Succesfully deleted")
        except FileNotFoundError:
            print(f"ERROR! Wrong path: 'Couldn't find {path_to_file}'")

def open_file(path_to_file=None, perms=None):
    if path_to_file is None:
        print("ERROR: Missing required argument: 'You need to select a file to delete!'")
    elif perms is None:
        print("ERROR: Missing required argument: 'You need to select one of the following file modes: \n1. w (write)\n2. a (append)\n3. r (read)\n4. t (Text mode) COMBINED WITH THE FIRST 3\n5. b (Binary mode) COMBINED WITH THE FIRST 3'")
    elif path_to_file is not None and perms is not None:
        try:
            file = open(path_to_file, perms)
            # w = write
            # a = append
            # r = read
            # t = Text mode
            # b = Binary mode
            # t + b are combined with defaults

            print(f"Opened: {path_to_file}")

            return file
            
        except FileNotFoundError:
            return print(f"ERROR! Wrong path: 'Couldn't find {path_to_file}'")

def close_file(file_variable_name=None):
    if file_variable_name is None:
        print("ERROR! No file selected!")
    elif file_variable_name is not None:
        try:
            file_variable_name.close()
        except FileNotFoundError:
            return print(f"ERROR! Wrong path: 'Couldn't find {file_variable_name}'")

def edit_file(file_variable_name=None, data_to_write=None):
        if file_variable_name is None:
            print("You need to select a valid opened file!")
        elif file_variable_name is not None:
            if (file_variable_name.mode == 'w' or file_variable_name.mode == 'wt' or file_variable_name.mode == 'wb' or file_variable_name.mode == 'a' or file_variable_name.mode == 'ab' or file_variable_name.mode == 'at'):
                try:
                    file_variable_name.write(data_to_write)
                    if (file_variable_name.mode == "w"):
                        print(f"Overwrote data in '{file_variable_name}' to '{data_to_write}'")
                    elif (file_variable_name.mode == "a"):
                        print(f"Appended '{data_to_write}' to '{file_variable_name}'")
                except FileNotFoundError:
                    return print(f"ERROR! Wrong path: 'Couldn't find {file_variable_name}'")
                except PermissionError:
                    return print(f"ERROR! Wrong file permissions for file '{file_variable_name}'")

def read_file(file_variable_name=None):
    if file_variable_name is None:
        print("ERROR! No file selected!")
    elif file_variable_name is not None:
        if (file_variable_name.mode == 'r' or file_variable_name.mode == 'rt' or file_variable_name.mode == 'rb'):
            try:
                data = file_variable_name.read()

                return data
            except FileNotFoundError:
                return print(f"ERROR! Wrong path: 'Couldn't find {file_variable_name}'")
            except PermissionError:
                return print(f"ERROR! Wrong file permissions for file '{file_variable_name}'")
                
############################
# MADE                     #
# BY                       #
# NikkieDev Software       #
# https://nikkiedev.com    #
############################