import os

class IOHandler():
	"""This class handle all the IO functions"""	
	
	@staticmethod	
	def __createFolder(folder):
		"""Create folder in given path with given name"""		
		if not os.path.exists(folder):
			os.makedirs(folder)
	
	@staticmethod			
	def __createFile(filename):
		"""Create file in given path with given name"""
		open(filename, 'a').close()
	
	@staticmethod
	def createFolderStructure(folders, files):
		"""Create file structure according to the e given files and folder details"""
		for folder in folders:
			IOHandler.__createFolder(folder)
		for filename in files:		
			IOHandler.__createFile(filename)
	
class MagicSite():
	"""This is main class of the Magic"""
	
	def __init__(self):
		"""intitlaization of the magic """
		self.folders = {"build/public", "build/src"}
		self.files = {"build/index.md"}	
	
	def boostreap(self):
		"""This method is call when the new site is bootstrapping"""
		IOHandler.createFolderStructure(self.folders, self.files)




