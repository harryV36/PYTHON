# File Handling

# Modes:
# 'r' -> Read
# 'w' -> Write (clears existing contents)
# 'a' -> Append (keeps existing contents)
# 'x' -> Create new file (fails if it already exists)

# Methods:
# read()      -> Reads data
# readline()  -> Reads one line
# readlines() -> Reads all lines into a list
# write()     -> Writes text
# close()     -> Closes the file

# Important:
# There is NO append() method for files.
# Appending is done by opening the file in 'a' mode and then using write().