# CSS MINZIP
# a tool to minimize and gzip CSS files
# step 1. Open filename.css and copy the contents
# [can we check to see if it's in an unsaved state!?]
# step 2. Remove all whitespace  
# step 3. join() with no spaces in between
# step 4. remove comments, leaving no spaces
# step 5. GZIP!?
# step 6. Write minimized-zipped code to filename.css.zip
# -----------------------------------------------------------------------------

# maybe best to put all imports first C style

import re, sys

def bassomatic(): 
    # Not sure best way to input so I'll default to CLI style for testing.
    # Use sample.css for your convenience
    filename = input("Enter a file name to make a minimized copy: ")

    # We need to pull out the guts- err, content.
    raw = open(filename, 'r')

    # Then chop it up along newlines, and split() removes the whitespace.
    diced = raw.read().split()

    # now we jam it all back together so we can use regex on it
    spliced = "".join(diced)

    return spliced

# OF COURSE I'm having problems with getting it to work
# Even putting the "r" in front isn't escaping the *
def rex(spliced):

    # pattern = r'/\* [.]+ \*/'
    # I'm not understandin the logic here, whatever it may be, so a test-

    pattern = r'regex'

    regex = re.compile(pattern)

    final_output = re.sub(regex, 'VOODOO', spliced)

    return final_output


def write_to_file(final_output): 
    # IF (filename exists) prompt to rename OR overwrite ELSE-
    output = open("filename.min.css.zip", "w")
    output.writelines(final_output)
    output.close()
    # success/fail dialogue 

def write_to_cli(final_output):
    print(final_output)


def main():
    spliced = bassomatic()
    final_output = rex(spliced)
    write_to_cli(final_output)

# With everything encapsulated and digestable we just run 
main()
