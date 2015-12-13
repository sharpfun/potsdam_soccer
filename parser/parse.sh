#!/bin/bash
# argument files should by whitespace-tokenized
MODELS=models.en
PARSER=anna-3.3.jar
#RAM=-Xmx1536M
RAM=-Xmx4G

for file in $*; do
    if [ -e $file.conll ] ; then echo found $file.conll 1>&2; else echo $file.conll 1>&2; java -cp $PARSER is2.util.Split $file > $file.conll; fi;
    if [ -e $file.lemma ] ; then echo found $file.lemma 1>&2; else echo $file.lemma 1>&2; java $RAM -cp $PARSER is2.lemmatizer.Lemmatizer -model $MODELS/lemmatizer.model -test $file.conll -out $file.lemma; fi;
    if [ -e $file.tagged ] ; then echo found $file.tagged 1>&2; else echo $file.tagged 1>&2; java $RAM -cp $PARSER is2.tag.Tagger -model $MODELS/tagger.model -test $file.lemma -out  $file.tagged; fi;
    if [ -e $file.parsed ] ; then echo found $file.parsed 1>&2; else echo $file.parsed 1>&2; java $RAM -classpath $PARSER is2.parser.Parser -model $MODELS/parser.model -test $file.tagged -out $file.parsed; fi;
done;
