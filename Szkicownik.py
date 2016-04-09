import os
with open(os.path.join('/path/to/Documents',completeName), "w") as file1:
    toFile = raw_input("Write what you want into the field")
    file1.write(toFile)
