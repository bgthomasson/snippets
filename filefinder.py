#! python3

'''
1: Search DIR for FILETYPE

2: GUI: option to open directly, a button by each name, or hyperlink style

3: preview snippet would be useful

-------------------------
DONE:
. dir to search is automatically found- user's home dir on WIN or UNIX
. valid file path on WIN or UNIX
. succesfully searches for RTF and retrieves basic metadata
. returns file size (fuzzy)
. returns date modified (but not time because of space)

I think anything more advanced is better in GUI
(if only have CLI can just use BASH commands)

#TODO: allow choice of dir to search
#TODO: choose filetype to find
#TODO: choose program to open files with 
#TODO: preview contents 

'''

import os
from time import localtime, strftime

# create a variable for current user's home dir found via os.environ
userhome = os.environ['HOME']

for folder, subfolders, files in os.walk(userhome):
    for filename in files:
        if filename.endswith('.rtf'):
            # create a valid path on any OS-
            url = os.path.join(folder, filename)

            # now grab file info- statinfo requires full valid path- 
            statinfo = os.stat(url)

            # fuzzy file sizes- 
            bytesize = statinfo.st_size
            if bytesize < 1000:
                humansize = str(bytesize) + ' B'
            elif bytesize >= 1000 and bytesize < 1000000:
                humansize = str(bytesize // 1000) + ' KB'
            else:
                humansize = str(bytesize // 1000000) + ' MB'

            # time last modified- pay attention to nesting order- 
            last_modified = strftime("%Y %B %d", localtime(statinfo.st_mtime))

            # output-
            print(url + ' ~' + humansize + ' * ' + last_modified)
            
