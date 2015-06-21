import os
from shutil import copytree, ignore_patterns

class IOHandler():
	"""This class handle all the IO functions"""
	
	@staticmethod	
	def copytree(src, dst, symlinks=False, ignore=None):
		names = os.listdir(src)
	 	if ignore is not None:
			ignored_names = ignore(src, names)
		else:
			ignored_names = set()
	
		os.makedirs(dst)
		errors = []
		for name in names:
			if name in ignored_names:
				continue
			srcname = os.path.join(src, name)
			dstname = os.path.join(dst, name)
			try:
				if symlinks and os.path.islink(srcname):
					linkto = os.readlink(srcname)
					os.symlink(linkto, dstname)
				elif os.path.isdir(srcname):
					copytree(srcname, dstname, symlinks, ignore)
				else:
					copy2(srcname, dstname)
				# XXX What about devices, sockets etc.?
			except (IOError, os.error) as why:
				errors.append((srcname, dstname, str(why)))
			# catch the Error from the recursive copytree so that we can
			# continue with other files
			except Error as err:
				errors.extend(err.args[0])
		try:
			copystat(src, dst)
		except WindowsError:
			# can't copy file access times on Windows
			pass
		except OSError as why:
			errors.extend((src, dst, str(why)))
		if errors:
			raise Error(errors)
	
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
		self.base = "src"
		self.output = "build/src"	
	
	def boostreap(self):
		"""This method is call when the new site is bootstrapping"""
		#self.output = ofilepath
		IOHandler.createFolderStructure(self.folders, self.files)
		IOHandler.copytree(self.base, self.output)
		




