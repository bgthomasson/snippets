# CSS MINZIP 
# Quick and dirty tool to minimize (and gzip??) CSS files 
# step 1. Open file and copy the contents
# [can we check to see if it's in an unsaved state!?]
# step 2. Remove all whitespace 
# step 3. join() with no spaces in between
# step 4. remove comments, leaving no spaces
# step 5. GZIP!? I tihnk this would only be easy on *nix. 
# step 6. Write minimized-zipped code to filename.css.zip
# option: compare filesize of source to final, X kb vs Y kb
# -----------------------------------------------------------------------------
# maybe best to put all imports first 

import re, sys

def bassomatic(): 
    # Not sure best way to input so I'll default to CLI style for testing.
    print("(Use sample.css for testing purposes)")
    filename = input("Enter a file name to make a minimized copy: ")

    # We need to pull out the guts- err, content.
    raw = open(filename, 'r')

    # Then chop it up along newlines, and split() removes the whitespace.
    # So this is absurdly easy, while the regex is absurdly hard.
    diced = raw.read().split()

    # now we jam it all back together 
    spliced = "".join(diced)

    return spliced


def rex(diced):

    pattern = r'/\*(.+)\*/'
    # OK learned 2 things here, first, don't leave spaces in regex.
    # second, it skips all the way to the very last */ in the string.
    # Thus, -everything- in the file is selected since I have a comment
    # at the end... oops. At least I got the regex right.

    regex = re.compile(pattern)

    commentless_output = re.sub(regex, '', diced)

    return commentless_output


def write_to_file(final_output): 
    # IF (filename exists) prompt to save a copy like file2 OR overwrite
    # ELSE-
    output = open("filename.min.css.zip", "w")
    output.writelines(final_output)
    output.close()
    # success/fail dialogue 


def write_to_cli(output):
    print(output)


def main():
    final_output = bassomatic()
    write_to_cli(final_output)


# With everything encapsulated and digestable we just run 
main()
