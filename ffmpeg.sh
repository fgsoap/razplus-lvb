#!/bin/bash  
  
for i in $(seq 3 10)  
do   
ffmpeg -safe 0 -loop 1 -i $i.jpg -i $i.mp3 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -x264-params keyint=1:scenecut=0 -c:a copy -shortest $i.mp4
done

find . -type f -name '*.mp4' -printf "file '$PWD/%p'\n" | sort > 'mylist.txt'
ffmpeg -safe 0 -f concat -i 'mylist.txt'' -c copy output.mp4