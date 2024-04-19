# with

#with open("example.txt", "r") as file:
#    content = file.read()
#    print(content)




file = None
try:
    file = open("example.xlsx", "r")
    content = file.read()
    print(content)
except Exception as e:
    print("Error occurred: {}".format(e))
    file = open("example.xlsx", "w")
    file.write('Hello, world')
finally:

    if file is not None:
        print('Closing the file')
        file.close()
