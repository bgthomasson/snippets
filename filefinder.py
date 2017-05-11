#! python3

'''
GOALS:
I'm trying to standardize my workflow: all writing should be in ODT (or DOCX),
so any RTF or DOC files should be saved as such, and the original trashed.
You can do this in BASH or GUI but I thought this was good practice. 

#TODO: allow choice of dir to search 
#TODO: choose filetype to find (dropmenu?)
#bonus: check if RTF files have eponymous ODT/DOC/etc versions
#bonus: for TXT files, check if UTF-8 (st_mode?)
#TODO: choose program to open files with. import subprocess
?: subprocess.run(['usr/bin/libreoffice', url])
?: or libreoffice --writer %U 
#TODO: preview contents
#TODO: FILE | SIZE | EDITED
#: Preview | OPEN | DELETE os.remove(url)

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


'''
try:
    fp = open("myfile")
except PermissionError:
    return "I kinna do that cap'n!"
else:
    with fp:
        return fp.read()
'''

