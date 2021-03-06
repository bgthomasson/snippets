#! python3

'''
GOALS:
I'm trying to standardize my workflow: all writing should be in ODT,
so any RTF or DOC files should be saved as such, and the original trashed.

#TODO: allow choice of dir to search
#bonus: check if RTF files have eponymous ODT/DOC/etc versions already
#TODO: choose program to open files with. import subprocess
?: subprocess.run(['/usr/bin/libreoffice', url])
?: CLI: /usr/bin/libreoffice -o url
#TODO: preview contents
# DELETE os.remove(url)

'''
# imports
import os
from time import localtime, strftime
from tkinter import *
from tkinter import ttk
import subprocess

# global vars (oh noes)
userhome = os.environ['HOME']

# functions
def finder():
    for folder, subfolders, files in os.walk(userhome):
        for filename in files:
            if filename.endswith(filetype):
                url = os.path.join(folder, filename)
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

                # CLI output-
                # print(url + ' ~' + humansize + ' * ' + edited)



def open_in_editor(url):
    subprocess.run(['/usr/bin/libreoffice', url])

    

def nukem(url):
    try:
        os.remove(url)
    except:
        return "Where is it?"
            


def previewer(url):
    try:
        fp = open("url")
    except PermissionError:
        return "I kinna do that cap'n!"
    else:
        with fp:
            return fp.read()



# GUI -------------------------------------------------------------------

root = Tk()
root.title("File Ferret")
# root.option_add('*tearOff', FALSE)

self = ttk.Frame(root, padding="3 3 12 12")
self.grid(column=0, row=0, sticky=(N, S, E, W))
# make it resizable- I know switch from root to self is weird but it works 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
self.rowconfigure(1, weight=3)
self.columnconfigure(0, weight=3)
self.columnconfigure(1, weight=3)
self.columnconfigure(2, weight=3)
self.columnconfigure(3, weight=3)
self.columnconfigure(4, weight=3)
self.columnconfigure(5, weight=3)

home_label = ttk.Label(self, text=userhome)
home_label.grid(row=0, column=0, sticky=W)

filetypes = [ 'rtf', 'txt', 'doc' ]
filetype = StringVar()
# some bullshit about not passing variables directly so get/set

opt_rtf = ttk.Radiobutton(self, text='RTF', variable=filetype, value='rtf')
opt_rtf.grid(row=0, column=1)
opt_txt = ttk.Radiobutton(self, text='TXT', variable=filetype, value='txt')
opt_txt.grid(row=0, column=2)
opt_doc = ttk.Radiobutton(self, text='DOC', variable=filetype, value='doc')
opt_doc.grid(row=0, column=3)

search_button = ttk.Button(self, text="Search", command=finder)
search_button.grid(row=0, column=5, sticky=E)
filetype.set('')

sep = ttk.Separator(root, orient=HORIZONTAL) 
sep.grid(row=1, columnspan=5, sticky=EW)

# menu header
filename_label = ttk.Label(self, text="Filename") 
filesize_label = ttk.Label(self, text="Size")
edited_label = ttk.Label(self, text="Edited")
preview_panel = ttk.Label(self, text="Preview")

filename_label.grid(row=2, column=0)
filesize_label.grid(row=2, column=1)
edited_label.grid(row=2, column=2)
preview_panel.grid(row=2, column=3, columnspan=2, sticky=E)

# text = Text(self, width=30, height=100)
# use this as preview pane??

# $filename = ttk.Button(self, text=filename, command=open_in_editor)
# $filename.grid(row=3+i, column=0)

for child in self.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()









