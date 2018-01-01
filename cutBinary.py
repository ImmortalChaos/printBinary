import os
import array
import getopt
import sys

def usage() :
   print "Usage :"
   print "   cutBinary.py -f [filename] -o [filename] -n [cut size]"
   print "   cutBinary.py -f [filename] -o [filename] -s [start offset]"
   print "   cutBinary.py -f [filename] -o [filename] -s [start offset] -n [cut size]"
   print
   print "Option : "
   print "   -f : input file path"
   print "   -o : output file path"   
   print "   -n : cut file size(bytes)"
   print "   -s : file start offset"
    
def main_run(filename, outfile, startOffset, sizeLimit) :
   line = ''

   f = open(filename, 'rb')
   fo = open(outfile, 'wb')
   cnt = 0
   if startOffset>0 :
      f.read(startOffset)
   wd = f.read(1)
   while wd :
      fo.write(wd)
      wd = f.read(1)
      cnt += 1
      if sizeLimit>0 and sizeLimit<=cnt :
         f.close()
         fo.close()
         return;
   f.close()
   fo.close()

if __name__ == "__main__":
   bRun = True
   filename = ""
   destFilename = ""
   startOffset = 0
   sizeLimit = 0
   numline = False
   try:
       optlist, list = getopt.getopt(sys.argv[1:],'f:o:n:s:')
       if len(optlist) == 0 :
           usage()
           bRun = False
       for o, a in optlist:
           if o == "-f":
               filename = a
           elif o == "-n":
               sizeLimit = int(a)
           elif o == "-o":
               destFilename = a
           elif o == "-s":
               startOffset = int(a)
           else :
               usage()
               bRun = False
   except getopt.GetoptError:
       usage()
       bRun = False
   
   if bRun :
       if filename!="":
           main_run(filename, destFilename, startOffset, sizeLimit)
       else :
           usage()