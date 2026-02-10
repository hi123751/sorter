from glob import glob
import shutil
import os
home = os.environ['USERPROFILE']
jpg = glob(home + '/Downloads/*.jpg')
des = 'jpg/'
for file in jpg:
  shutil.move(file, des)
py = glob(home + '/Downloads/*.py')
des2 = 'python/'
for file1 in py:
  shutil.move(file1, des2)
exe = glob(home + '/Downloads/*.exe')
des3 = 'exe/'
for file2 in exe:
    shutil.move(file2, des3)
txt = glob(home + '/Downloads/*.txt')
des4 = 'txt/'
for file3 in txt:
    shutil.move(file3, des4)
