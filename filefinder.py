#! python3

'''
DONE:
. dir to search is automatically found- user's home dir on WIN or UNIX
. valid file path on WIN or UNIX
. succesfully searches for RTF and retrieves basic metadata
. returns file size (fuzzy)
. returns date modified (but not time because of space)

#TODO: allow choice of dir to search 
#TODO: choose filetype to find (dropmenu?)
#TODO: choose program to open files with (button? menu?)  
#TODO: preview contents
#TODO: better to split output up so can put into tabular form-

FILE | SIZE | EDITED | OPEN | Preview 

'''

import os
from time import localtime, strftime


userhome = os.environ['HOME']

def finder(): 
    for folder, subfolders, files in os.walk(userhome):
        for filename in files:
            if filename.endswith('.rtf'):
                # create a valid path on any OS-
                url = os.path.join(folder, filename)

                # now grab file info- statinfo requires valid path- 
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
                edited = strftime("%Y %B %d", localtime(statinfo.st_mtime))

                # output-
                print(url + ' ~' + humansize + ' * ' + edited)
            

finder()
