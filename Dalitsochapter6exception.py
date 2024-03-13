try:
    file_object = open('MeDescription.txt','r')
    for lines in file_object:
        print(lines)
except  FileNotFoundError:
    print("use the correct path of your file")    

x = 5
print(x)
