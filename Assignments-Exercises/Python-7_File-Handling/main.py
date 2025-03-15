try:
    with open('sample.txt', 'r') as file:
        file_contents = file.read()
        print("\nCurrent file content:")
        print(file_contents)
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")

with open('newfile.txt', 'w') as file:
    file.write("This is a new file, like New Year New Me XD.\n")
    print("\nNewly created file and its content:")

with open('newfile.txt', 'r') as file:
    new_contents = file.read()
    print(new_contents)