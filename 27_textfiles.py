# there are two types of files: text files and binary files. text files are human readable data like plain text, xmli json or even a source code. binary files are used for storing compiled code, app data and media files. 

# to open a file in python 
f = open("guido_bio.txt")

# to read th econtents of the file, call the read method
text = f.read() # this will return all the text in the file
f.close() # finally, close the file

print(text)

# what if sth happens to the text before you close the file
# to aviod this problem, there is a shorter and better method which is opening a file using the with keyword

with open("guido_bio.txt") as fobj:
	bio = fobj.read()

# this way you do not need to close the file, python does it itself

# if we're not sure whether there is a file like that:

try:
	with open("future_lottery_numbers.txt") as f:
		text = f.read()
except FileNotFoundError:
	text = None
print(text)

# gives None, if the file was not found

# how to write a file
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

with open(oceans.txt", "w") as f:
	for ocean in oceans:
		f.write(ocean)
		f.write("\n")
# if the file already exists, python will overwrite it

# there is also another way to write each name in a separate line

with open(oceans.txt", "w") as f:
        for ocean in oceans:
		print(ocean, file=f)

# to write to a file without overwriting any existing texts
with open("oceans.txt", "a") as f:
	print(23*"=", file=f)
	print("These are the 5 oceans.", file=f)



















