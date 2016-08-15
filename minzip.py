# CSS MINZIP
# a tool to minimize and gzip CSS files
# step 1. Open filename.css and copy the contents
# [can we check to see if it's in an unsaved state!?]
# step 2. remove all whitespace- split() does this nicely 
# step 3. Remove comments which may take some thinking
# step 4. join() with no spaces in between
# step 5. GZIP!?
# step 6. write minimized-zipped code to filename.css.zip
# [check to see if that filename already exists]

# Not sure best way to input so I'll default to CLI style for testing.
# Use sample.css for your convenience

filename = input("Enter a file name to minimize: ")

raw = open(filename, 'r')

diced = raw.read().split()

# Remove comments 

# put it back together
spliced = "".join(diced)

# GZIP!?

# IF (filename exists) prompt to rename OR overwrite ELSE-
# output = open("filename.min.css.zip", "w")
# output.writelines(spliced)
# output.close()
# success/fail dialogue 

# here is our test output until then: 
print(spliced)
