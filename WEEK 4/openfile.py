#file = open('newFile.pdf', 'w')
#content ="Hello world, this is amazing\n"

#file.write(content.upper())
# Reading a file
#file = open('newFile.pdf', 'r')
#data = file.readlines()
#print(data)

# Appending content to a file
#file = open('newFile.pdf', 'a')
#file.write("Invite JsMammie to the party\n")

# Error handling with try-except
#file = open('newFile.pdf', 'r')
#data = file.readlines()
#print(data)

try:
    file = open('newFile.pdf', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    print("File operation completed")
    file.close()