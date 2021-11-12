#!/bin/bash

ls *.mp4 | sort -n | awk '{printf "file \"%s\"\n", $1}' > mylist.txt

ffmpeg -safe 0 -f concat -i 'mylist.txt' -c copy output.mp4