import magicsite
import sys, getopt

def main(argv):
   #inputfile = ''
   #outputfile = ''
   site = magicsite.MagicSite()
   site.boostreap()    
   """
   try:
      opts, args = getopt.getopt(argv,"hi:o:b:",["ifile=","ofile=","boostreap="])
   except getopt.GetoptError:
      print 'main.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
         
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()   
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("-b", "--boostreap"):  
            site.boostreap()    
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile
   
   """
if __name__ == "__main__":
    main(sys.argv[1:])
	
	