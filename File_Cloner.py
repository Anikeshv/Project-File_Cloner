def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'rb') as source:
            with open(destination_file, 'wb') as destination:
                destination.write(source.read())
        print("File copied successfully!")
    except IOError:
        print("Error: Unable to copy the file.")

# Example usage
source_file = ""
destination_file = ""

copy_file(source_file, destination_file)

#Code with file path
def File_Cloner(Original_file_with_path,Copy_file_with_path):
    f1=open(Original_file_with_path,'rb')
    f2=open(Copy_file_with_path,'wb')
    try:
        f2.write(f1.read())
        print("File cloned successfully!")
    except IOError:
        print("Error occurred: Unable to copy file.")

Fpath=''
Fname=''
Cpath=''
Cname=''
Original_file_with_path=f"{Fpath}/{Fname}"
Copy_file_with_path=f"{Cpath}/{Cname}"

File_Cloner(Original_file_with_path,Copy_file_with_path)



file_path = "D:\CS\Python/Datatype- Dictionaries.txt"
try:
    with open(file_path, 'r') as file:
        file_contents = file.read()
        print(file_contents)
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Unable to read the file.")
















