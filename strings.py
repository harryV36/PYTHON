# STRINGS AND TYPE CONVERSION 
# In string we can save multiple things characters so it takes extra space then othet datatypes.
# every value stored in string has unicode.
# string takes extra space cauz every character it stores has special unicode that's why.

""" STRINGS """
a = "A"
print(ord(a)) # getting unicode of any character
b = "B"
print(ord(b))

c = 65 
print(chr(c)) # getting character of an unicode.

# INDEXING 
d = "SHER"
# INDEXING STARTS WITH 0 AND ALSO INCLUDE SPACE IN IT AND SPACE ALSO HAS AN INDEX NUMBER IN IT. INDEXING ALWAYS START FROM ZERO.
# NEGATIVE INDEXING STARTS FROM -1. AND POSITIVE INDEXING STARTS FROM ZERO.
print(d[1]) # gives E as result.
print(d[-1])
print(d[-1],d[3])

# STRING SLICING  d[start : stop : steps], at stop point always write stop point + 1.
d = "sher coder"
print(d[0:4:1])
print(d[5:10:1])
print(d[0:6:2])
