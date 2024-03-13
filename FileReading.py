file_object = open('test.txt', 'r')

for lines in file_object:
    each_line = lines.split('.')
  

    try:
        print(each_line[7])
    except:
        print(" Error. No index at line 7")

