# lspy
lspy is a Python 3  script that allows you to list the contents of a directory every 5 seconds in a format that looks very much like ls -la

## command line options
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
Since I'm not really familiar with Python, I used ChatGPT to help me generate most of the script. I've tweaked a few things here or there and have actually learned a lot from looking and how ChatGPT did a lot of the logic.
