#! python3
# what the RTF: find RTF files so can resave as ODT or TXT

'''
1: It needs to automatically search in current user's home dir.
(Have option to search others tho?)
(pedantically, it should have option for the filetype to find as well)

2: option to open in LO, a button by each name, or hyperlink style

3: preview snippet?

-------------------------

OOPS: I found os.stat() and tried to use it to print the file size, but-
Traceback (most recent call last):
  File "/home/ben/Documents/snippets/filefinder.py", line 32, in <module>
    statinfo = os.stat(filename)
FileNotFoundError: [Errno 2] No such file or directory: 'fizzbuzz.py'

I'm assuming it needs the whole path, which gives me an idea for abbreviating,
orignal idea was like-

statinfo = os.stat('file.rtf')
print(folder + '/' + filename + ' size = ' + statinfo.st_size + ' bytes')

statinfo.st_mtime = most recent modification, in seconds

OK using "url" helped but now it can't convert int to str. OK we can do it.
How about this-

filesize = str(statinfo.st_size) + ' bytes'

This will make our print statement even shorter, so we can add the mod time.
And it works!

Time may take some work, it's not only an integer, but in UNIX time

'''

import os

# create a variable for current user's home dir found via os.environ

userhome = os.environ['HOME']

for folder, subfolders, files in os.walk(userhome):
    for filename in files:
        if filename.endswith('.rtf'):
            # create a valid path, unfortunately is UNIX only atm-
            #TODO: use os.name to find if "nt" or "posix", insert proper slash.
            url = folder + '/' + filename

            # now grab file info using our valid on UNIX pathname-
            statinfo = os.stat(url)

            # we have to convert st_size from int for print()-
            #TODO: human readable sizes
            bytesize = str(statinfo.st_size) + ' bytes'

            print(url + ' ' + bytesize)
            
