# lspy
lspy is a Python 3  script that allows you to list the contents of a directory every 5 seconds in a format that looks very much like `ls -la` . This is very handy for seeing how file sizes in a directory may be changing or for checking which files have been modified most recently. 

## Command Line Options
Output from lspy.py --help
```
List directory contents sorted by size, name, or last edited time. The screen with updated contents is refreshed every 5 seconds.

positional arguments:
  path              Directory path to list

optional arguments:
  -h, --help        show this help message and exit
  --size, -s        Sort by file size
  --name, -n        Sort by file name
  --lastedited, -e  Sort by last edited time

```

## Why did I write this script?
My Apache webserver was being pounded with requests and I wanted to be able to easily see which log file was growing the fastest so I could tell which VHOST to modify, disable, etc to stave off the traffic. (I have since setup mod_evasive to keep the out of control AI scrapers at bay, but I digress). I am now able to easily see which log file is growing the fastest. 

## I used ChatGPT for much of the script
Since I'm not really familiar with Python, I used ChatGPT to help me generate most of the script. I've tweaked a few things here or there and have actually learned a lot from looking at how ChatGPT did a lot of the logic.

## System Requirements
This script only works with **Python 3.x**. On my Ubuntu server where I use it most, I had to explicity state `python3` to make sure it was using 3, since just typing `python` was running it with Python 2.x .

## lspy.py Permissions
I have my permissions for lspy.py set to `755`. After doing that, you can omit having to type `python3` to execute the command because I have the `#!/usr/bin/env python3` statement at the top of the file. (*Note:* On your system, python3 may not be stored in the same place. Use `which python3` to determine where exactly your python interpreter is stored)
