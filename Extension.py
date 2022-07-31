#Python program to accept a filename from the user and print the extension of that
filename = input("Input the Filename: ")
file_extension = filename.split(".")
#print(file_extension)
if file_extension[1]=="py":
    print("python")
if file_extension[1] =="c":
    print("c language")
if file_extension[1]=="java":
    print("java file")
if file_extension[1]=="docx":
    print("word file")
if file_extension[1] == "xlsx":
    print("excel file")
if file_extension[1] == "csv":
    print("Comma-separated values file")
