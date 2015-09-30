#!/usr/bin/python

import re
import sys

def main():
    if len(sys.argv) != 3:
        print "Usage: extract.py <lang>[ger|eng] <src>"
        return 1
    
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
            
            print mm

if __name__ == "__main__":
    main()

