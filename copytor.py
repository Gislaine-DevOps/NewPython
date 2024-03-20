 # read a content of a file using the method "read" file
 # This method reads the whole file as a string 

# with open("Python/demo.txt", "r") as my_file:
#     content = my_file.read()
#     print(content)

 # read a content of a file using the method "readlines" file
 # This method reads each line in a form of array or list 
 # NB: readline without (s) just read the first line as a string

 
# with open("Python/demo.txt","r") as file:
#     content = file.readlines()
#     print(content)

 # the "write" method create at the same time the file if it does not exist and write inside
 # NB: the "write" method does not read the content as a list but always as a string
    
# with open("Python/demo_copy.txt" , "w") as demofile:
#     for line in content:
#         print(line)
#         demofile.write(line)
    
 # unlike "write" that only takes a string, the "writelines" is another way for the "write" method
 # to write the content as a list
       
# with open("Python/demo_copy.txt" , "w") as demofile:
#     demofile.writelines(content)

def copy(input_file: str, output_file: str) -> None:
    """
    This function copy the content of a file_source and put it in the destination file
    :param input_file: this is the source_file (the path of your local file)
    :param output_file: this one is where you want your file to be 
    """
    with open(input_file, "r") as file:
        content = file.readlines()
        print(content)

    with open(output_file , "w") as demofile:
        demofile.writelines(content)

copy("Python/demo.txt", "Python/demo_copies.txt")



