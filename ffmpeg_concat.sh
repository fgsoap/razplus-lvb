#!/bin/bash  

ffmpeg -safe 0 -f concat -i 'mylist.txt'' -c copy output.mp4