import os
import os.path
import fnmatch

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return file_info
#need to target the folder that contains all the resort folders
subfolders = [f.path for f in os.scandir('/Users/c_evasquez/Pictures/pythontest/') if f.is_dir() ] 

for y in subfolders:
	newPath = (y+'/Approved Photos/JPEG')
	os.chdir(newPath)
	a,b,c,d,e, pathSplit = y.split('/') #takes the folder name into a variable
	nameSplit = pathSplit.split(" ") 
	codeFilter = fnmatch.filter(nameSplit, '(???)')
	resortCode =  ''.join(x for x in codeFilter if x != [])
	if (resortCode != ''):
		if (resortCode in s for s in nameSplit ):
			pathName = '-'.join(nameSplit[:-1])
	else:
		pathName = '-'.join(nameSplit)
	counter = (0)

	for x in os.listdir():
		if x.endswith(".jpg"):
			counter +=1
			fileNum = counter
			fileThumb = "th"
			file_name, file_ext = os.path.splitext(x)
			new_name = '{}-{}{}'.format(pathName,fileNum,file_ext)
			os.rename(x,new_name)
#this section does the thumbnails after PS has created them 
	thumbPath = (y+'/Approved Photos/JPEG/JPEG')
	os.chdir(thumbPath)
	counter = (0)

	for x in os.listdir():
		if x.endswith(".jpg"):
			counter +=1
			fileNum = counter
			fileThumb = "th"
			file_name, file_ext = os.path.splitext(x)
			new_name = '{}-{}-{}{}'.format(pathName,fileNum,fileThumb,file_ext)
			os.rename(x,new_name)

	

	# for x in os.listdir():
	# 	if x.endswith(".jpg"):
	# 		counter +=1
	# 		fileNum = counter
	# 		fileThumb = "th"
	# 		file_name, file_ext = os.path.splitext(x)
	# 		print(file_size(x))
	# 		if file_size(x).st_size < 100000:
	# 			new_name = '{}-{}-{}{}'.format(pathName,fileNum,fileThumb,file_ext)
	# 			os.rename(x,new_name)
	# 		else:
	# 			new_name = '{}-{}{}'.format(pathName,fileNum,file_ext)
	# 			os.rename(x,new_name)
		
