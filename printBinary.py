import os
import array
import getopt
import sys

def usage() :
   print "Usage :"
   print "   printBinary.py -f [filename] > save.txt"
   print
   print "Option : "
   print "   -f : input file path"
   print "   -n : show number line"   
   print "   -m : limit file size(bytes)"
    
def printHexString(nStr) :
   if nStr >=65 and nStr <= 126 :
      return chr(nStr)
   return "."
def main_run(filename, numline, sizeLimit) :
   line = ''

   f = open(filename, 'rb')
   wd = f.read(1)
   cnt = 0
   lineHex = ''
   lineAsc = ''
   while wd :
      hexTemp = array.array("B",wd)
      lineHex += "%02x "%hexTemp[0]
      lineAsc += printHexString(hexTemp[0])
      wd = f.read(1)
      cnt += 1
      if sizeLimit!=0 and sizeLimit<=cnt :
         lineSpace = ""
         if (16 - cnt%16)!=0 :
            for i in range(0, 16- cnt%16) :
               lineSpace = lineSpace + "   "
         if numline :
            print "%06x "%( (cnt-16) + (16 - (cnt%16) ) ),
         print lineHex+lineSpace, lineAsc
         f.close()
         return;
      if (cnt > 0) and (cnt % 16 == 0) :
         if numline :
            print "%06x "%(cnt-16),
         print lineHex, lineAsc
         lineHex = ''
         lineAsc = ''
   if numline :
      print "%06x "%( (cnt-16) + (16 - (cnt%16) ) ),
   lineSpace = ""
   if (16 - cnt%16)!=0 :
      for i in range(0, 16- cnt%16) :
         lineSpace = lineSpace + "   "
	  
   print lineHex+lineSpace, lineAsc
   f.close()

if __name__ == "__main__":
   bRun = True
   filename = ""
   sizeLimit = 0
   numline = False
   try:
       optlist, list = getopt.getopt(sys.argv[1:],'f:m:n')
       if len(optlist) == 0 :
           usage()
           bRun = False
       for o, a in optlist:
           if o == "-f":
               filename = a
           elif o == "-n":
               numline = True
           elif o == "-m":
               sizeLimit = int(a)
           else :
               usage()
               bRun = False
   except getopt.GetoptError:
       usage()
       bRun = False
   
   if bRun :
       if filename!="":
           main_run(filename, numline, sizeLimit)
       else :
           usage()