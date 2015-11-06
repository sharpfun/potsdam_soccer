#!/usr/bin/python

## tickerscrape.py
## Scrapes lines from a ticker. In the future, will be integrated into overall 
## system and then passed to parser.
##
## Usage: extract.py <lang>[ger|eng] <src> <outputname>
##

import sys
import re

def main():
    if len(sys.argv) != 4:
        print "Usage: extract.py <lang>[ger|eng] <src> <outputname>"
        return 1

    outfile = open("scraped/%s" % sys.argv[3], "w")
    
    srcFile = sys.argv[2]
    with open(srcFile, "r") as fh:
        matches = re.findall("([\+\s0-9]+\')\s*([^\n\r]*)", fh.read())
        matches.reverse()
        for m in matches:
            mm = m[1]
            if sys.argv[1] == "ger":
                mm = re.sub(r"([0-9]+):([0-9]+)",r"\1 zu \2",mm)
            elif sys.argv[1] == "eng":
                mm = re.sub(r"([0-9]+):([0-9]+)",r"\1 to \2",mm)
                mm = mm.replace("min.", "minutes")
            mm = mm.replace("-", " ")
            mm = re.sub(r"([\.\!\?])$",r" \1",mm)
            
            mm = mm.replace(". ", " .\n")
            mm = mm.replace("! ", " !\n")
            mm = mm.replace("? ", " ?\n")
            mm = mm.replace(", ", " , ")
            
            outfile.write(mm + "\n")
    
    outfile.close()

if __name__ == "__main__":
    main()

