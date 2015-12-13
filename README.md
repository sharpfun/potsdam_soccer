# Potsdam Soccer Project

## Overview
Using natural language processng and answer set solving techniques this project reads in multiple tickers and by information extraction and merging them in an intelligent way we output a comprehensive summary of the given tickers.

## Usage
```
python2 run.py [-h] [--verbose VERBOSE] [--kicktionary KICKTIONARY]
              [--verbnet VERBNET] [--tickers TICKERS] [--luorder LUORDER]

optional arguments:
  -h, --help            show this help message and exit
  --verbose VERBOSE     print helpful messages about the progress
  --kicktionary KICKTIONARY
                        location of kicktionary xml file
  --verbnet VERBNET     location of folder with verbnet xml files
  --tickers TICKERS     location of tickers folder (by default it's "data/input", so you can put tickers inside)
  --luorder LUORDER     location of folder with lexical unit order file
```

## Requirements
- **Python 2.7**
- **Anna Dependency Parser**: We use the well known anna dependency parser. This parser needs to be placed in the parser folder as well as its models for parsing, tagging and lemmatizing. We used anna-3.3 for the english ticker messages. The tool can be downloaded here: https://code.google.com/p/mate-tools/
- **Gringo Python Lib**: For merging different tickers into one ticker we use answer set programming. Therefore we decided for using the asp solver developed by the Potassco group. It provides an easy integration of ASP into Python. The python library and further instructions on the compilation process are found on http://potassco.sourceforge.com and especially for the version we used under http://sourceforge.net/projects/potassco/files/clingo/4.5.3/
```
project_folder
├── run.py
├── data
|     └── ...
├── parser
│     ├── anna-3.3.jar
│     ├── models.de
│     │   ├── lemmatizer.model
│     │   ├── mtag.model
│     │   ├── parser.model
│     │   └── tagger.model
│     ├── models.en
│     │   ├── lemmatizer.model
│     │   ├── parser.model
│     │   └── tagger.model
│     ├── parse.sh
├── extracting
|     └── ...
├── preprocessing
|     └── ...
├── reasoning
      └── ...
```

## Input Format
All ticker files need to be placed in the same directory. The directory is easily selected using the commandline argument `-- tickers DIR`.

## Output Format
The results are stored in the data/output folder. Each run gets its own subdir named by a timestamp.
