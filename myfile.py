# L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
  
# # Writing to file
# with open("myfile.txt", "w+") as file1:
#     # Writing data to a file
#     file1.write("Hello\n")
#     file1.write("Hello\n")

#     print(file1.tell())
#     file1.seek(0)
#     print(file1.read())

f = open('my_file', 'w+b')
byte_arr = [120, 3, 255, 0, 100]
binary_format = bytearray(byte_arr)
f.write(binary_format)
f.close()