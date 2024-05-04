#! /bin/bash
#
#
while :
do

xwd -root -out test.xwd
convert test.xwd test.png
python main.py

done

