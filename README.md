# Potsdam Soccer Project

## Overview
Using natural language processng and answer set solving techniqzes this project reads in multiple tickers and by information extraction and merging them in an intelligent way we output a comprehensive summary of the given tickers.

## Usage
```
python run.py [-h] [--verbose VERBOSE] [--kicktionary KICKTIONARY]
              [--verbnet VERBNET] [--tickers TICKERS] [--luorder LUORDER]

optional arguments:
  -h, --help            show this help message and exit
  --verbose VERBOSE     print helpful messages about the progress
  --kicktionary KICKTIONARY
                        location of kicktionary xml file
  --verbnet VERBNET     location of folder with verbnet xml files
  --tickers TICKERS     location of tickers folder
  --luorder LUORDER     location of folder with lexical unit order file
```

## Requirements
We assume to have a running python verion 2.7 on the system. Further we use the well known anna dependecy parser. This parser needs to be placed in the parser folder. We used anna-3.3 for the english ticker messages. Following structure will be assumed that the program works correctly.
```
parser
├── anna-3.3.jar
├── anna-3.61.jar
├── models.de
│   ├── lemmatizer.model
│   ├── mtag.model
│   ├── parser.model
│   └── tagger.model
├── models.en
│   ├── lemmatizer.model
│   ├── parser.model
│   └── tagger.model
├── parse2.sh
├── parse.sh
```

## Data
### Input
All ticker files need to be placed in the same directory. The directory is easily selected using the commandline argument `-- tickers DIR`.

### Output
The results are stored in the data/output folder. Each run gets its own subdir named by a timestamp.
