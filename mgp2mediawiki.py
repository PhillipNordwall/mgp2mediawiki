"""mgp2mediawiki converts a magicpoint file to mediawiki syntax
"""
import sys
import re
from optparse import OptionParser

def mgp2mediawiki(fin):
  """Read the contents of fin, convert to mediawiki syntax and return string"""
  page = fin.read()
  page = re.sub(r"\n%page\n\n([^\n]*)\n", r"\n==\1==\n", page)
  page = re.sub(r"^%[^\n]*", r"", page)
  page = re.sub(r"\n%[^\n]*", r"", page)
  page = re.sub(r"\t", r"*", page)
  page = re.sub(r"\n\n\*", r"\n*", page)
  page = re.sub(r"\\\n", r"", page)
  #page = re.sub(r"  +", r" ", page)
  return page

def main(argv=None):
  use = """Usage: python %prog [options] [INPUTFILENAME]

 Default input is STDIN
 Default output is STDOUT
 Author: Phillip.Nordwall+mpg2mediawiki@gmail.com"""
  ver = "%prog 0.1"
  parser = OptionParser(usage=use, version=ver)
  parser.add_option("-o", "--output-file",
                    dest = "OUTPUTFILENAME",
                    help = "write output to OUTPUTFILENAME")
  (options, args) = parser.parse_args()

  # use standard in if no arguments are passed
  if len(args) > 1:
    parser.error("incorrect number of arguments")
  elif len(args) == 1:
    ifh = open(args[0], "rb")
  else:
    ifh = sys.stdin
  
  # use standard out if no out argument is passed
  if options.OUTPUTFILENAME:
    ofh = open(options.OUTPUTFILENAME, "wb")
  else:
    ofh = sys.stdout

  # do the conversion and output the results
  ofh.write(mgp2mediawiki(ifh))
  
  # close the file handles
  ifh.close()
  ofh.close()

if __name__ == "__main__":
  sys.exit(main())
