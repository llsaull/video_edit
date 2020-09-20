## About

This is a simple script to wrap ffmpeg calls to edit videos. I wrote this to
prepare lectures for my classes, since the process of running ffmpeg from the command
line is tedious. It involves remembering long command arguments and knowing the
name of your files.

Currenlty this is what it does:
```
   Choose an option:        
         c - cut a video   
         j - join videos   
         t - add text to video
         v - increase volume   
```
Curretly the script only looks for .mkv and .mp4 files, you may change this in the script
if needed. For the text option, you have to set the path to a valid font in the variable
```
PATH_TO_FONT = "<<YOUR FONT HERE>>"
```
defined in the beginning of the script.
   
## How to run:

Run the script from the folder where you videos are located.
