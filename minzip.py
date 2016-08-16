# CSS MINZIP
# a tool to minimize and gzip CSS files
# step 1. Open filename.css and copy the contents
# [can we check to see if it's in an unsaved state!?]
# step 2. Remove all whitespace  
# step 3. join() with no spaces in between
# step 4. run regex pattern to remove comments
# step 5. GZIP!?
# step 6. Write minimized-zipped code to filename.css.zip
# [check to see if that filename already exists]

import re

# Not sure best way to input so I'll default to CLI style for testing.
# Use sample.css for your convenience
filename = input("Enter a file name to make a minimized copy: ")

# We need to pull out the guts- err, content.
raw = open(filename, 'r')

# Then chop it up along newlines, and split() removes the whitespace easily.
diced = raw.read().split()

# now we jam it all back together so we can use regex on it
spliced = "".join(diced)

# OF COURSE I'm having problems with getting it to work
# Even putting the "r" in front isn't escaping the *
# Also I can't find a pattern that works just reading basic how-to stuff
# Problem is we have /* and */ as delimiters, with a variable amount between. 

pattern = r'/\* [.]+ \*/'

regex = re.compile(pattern)

final = re.sub(regex, '', spliced)

# GZIP!?

# IF (filename exists) prompt to rename OR overwrite ELSE-
# output = open("filename.min.css.zip", "w")
# output.writelines(spliced)
# output.close()
# success/fail dialogue 

# here is our test output until then: 
print(spliced)
print(final) 
