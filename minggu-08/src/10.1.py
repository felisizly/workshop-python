import os
os.getcwd()
os.chdir('/server/accesslogs')   
os.system('mkdir today')

import os
dir(os)
help(os)

import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')