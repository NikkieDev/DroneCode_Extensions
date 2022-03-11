import dc_files as files

# Documentation for DroneCode extension: dc_files

files.create_file(file_name="", file_extension="", file_location="./")
# Creates a file, no need to put a '.' in the file_extensions parameter. This is done automatically
# The default values are "list", "txt", "./"

file = files.open_file(path_to_file="./example/directory/example.txt", perms="a")
# Opens file, and binds it to the desired variable name. 
# The 'perms' parameter let's you open the file with the correct permissions for your actions.
# w = write
# a = append
# r = read
# t = Text mode
# b = Binary mode
# t + b are combined with defaults

string_array = ["This", "is", "an", "array"]
files.edit_file(file_variable_name=file, data_to_write=str(string_array))
# Writes/Appends the data from variable 'string_array' to the file specified with 'file_variable_name', that was opened in the previous command

files.close_file(file_variable_name=file)
# Closes the file specified with 'file_variable_name'

file = files.open_file(path_to_file="./example/directory/example.txt", perms="r") # Necessary for the next step
file_data = files.read_file(file_variable_name=file) # Stores the data of the file specified by 'file_variable_name' in the new variable 'file_data'
print(file_data) # Prints the data from 'file_variable_name' to the console

files.close_file(file_variable_name=file)


############################
# MADE                     #
# BY                       #
# NikkieDev Software       #
# https://nikkiedev.com    #
############################