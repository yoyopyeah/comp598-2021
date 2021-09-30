#!/bin/bash

# number of lines
LINES=$(cat $1 | wc -l)

# error when line < 10000
if [[ LINES -lt 1000 ]];
then 
    echo "Error! The input file needs to have at least 10,000 lines." 1>&2  
    exit 1
else
    echo $LINES
fi

# header row
head -n 1 $1

# -i "potus"
echo $(tail -n 10000 $1 | grep -i "potus" | wc -l)

# "word"
echo $(sed -n '100,200p' < $1 | grep "fake" | wc -l)

