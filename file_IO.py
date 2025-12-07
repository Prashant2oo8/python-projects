# file = open("file.txt", "r")
# data1 = file.readline()
# print(data1)
# data = file.read()
# print(data)
# file.close()


# file = open("file.txt", "w")
# file.write("it will overwrite the file")
# file.close()
# file = open ("file.txt", "r+")
# file.write("\n this will add in last in file, (APPEND)")
# file.seek(0)
# new = file.read()
# print(new)
# file.close()
# f = open("file1.txt", "a+")
# f.write("appending something")
# f.close()
# with open ("file1.txt", "r") as f:
#     data = f.read()
#  print(data)
# with open("newfile.txt","r") as f:
#     f.write("hi everyone \n we are learning file I/O \n using java \n i like peogramming in java")


# def find_word ():
#     with open("newfile.txt","r") as f:
#         data = f.read()
#         if(data.find("learning")== 1 ):
#             print("found")
#         else:
#             print("notfound")


# def check_line():
#     data = True
#     lineNo = 1
#     with open("newfile.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if not data:
#                 break
#             if ("learning" in data):
#                 print(lineNo)
#             lineNo += 1

# with open ("something.txt", "r") as f:
#     valuse = f.read()

# new_valuse = valuse.replace("java", "python")
# with open ("something.txt", "w") as f:
#         f.write(new_valuse) 

# with open ("something.txt", "r") as f:
#     val = f.read()
#     if "simple" in val:
#         print("exist")
#     else:
#         print("not exist")

def check_lines():
    lineNo = 1
    with open("something.txt", "r") as f:
        data = f.readline()
        while data:
            if "language" in data:
                print (f"word found in line number {lineNo}")
                break
            data = f.readline()
            lineNo += 1
