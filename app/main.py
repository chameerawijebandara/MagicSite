import os

def createFolders(folders):
	for folder in folders:
		if not os.path.exists(folder):
			os.makedirs(folder)
			
def createFiles(files):
	for file in files:
		open(file, 'a').close()

folders = {"build/public", "build/src"}	
files = {"build/index.md"}

createFolders(folders)	
createFiles(files)
	




