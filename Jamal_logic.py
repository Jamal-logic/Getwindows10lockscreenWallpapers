import os
import shutil
currentUser = os.environ['USERNAME']

src = "C:\\Users\\"+currentUser+"\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
dest = os.path.dirname(os.path.abspath( __file__ ))
os.makedirs(dest + '\\winpics')
dest = dest + '\\winpics\\'
src_files = os.listdir(src)
minSize = 400000
for file_name in src_files:
	full_file_name = os.path.join(src, file_name)
	x = os.path.getsize(full_file_name)
	if(x > minSize):		
		if (os.path.isfile(full_file_name)):
			shutil.copy(full_file_name, dest)

path = dest
files = os.listdir(path)
i = 1
for file in files:
    x = os.path.getsize(path+file)
    os.rename(os.path.join(path, file), os.path.join(path, str(x) + str(i)+'.jpg'))
    i = i+1

