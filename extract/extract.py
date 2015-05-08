#!/usr/bin/python
#
# author:
# 
# date: 
# description:
#
import re
import sys

# Procedures

# Main
def main():
    if len(sys.argv) != 2:
        print "Usage: extract.py <src>"
        return 1
    srcFile = sys.argv[1]
    with open(srcFile, "r") as fh:
        matches = re.findall("([+0-9]*)'\s*([^\n]*)", fh.read())
        matches.sort(key=lambda x: eval(x[0]))
        for m in matches:
            mm = re.sub(r"([0-9]+):([0-9]+)",r"\1 zu \2",m[1])
            mm = mm.replace(". ", ".\n")
            mm = mm.replace("! ", "!\n")
            mm = mm.replace("? ", "?\n")
            print mm

if __name__ == "__main__":
    main()
