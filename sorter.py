from glob import glob
import shutil
import os
home = os.environ['USERPROFILE']
jpg = glob(home / 'Downloads/*.jpg')
des = 'jpg/'
for file in jpg:
  shuthil.move(file, des)
py = glob(home / 'Downloads/*.py')
des2 = 'python/'
for file1 in py:
  shutil.move(file1, des2)
exe = glob(home / 'Downloads/*.exe)
