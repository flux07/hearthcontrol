'''
This script simply reads the Hearthstone log in real time,
and prints it out to sytem out.

First, you have to enable logging in hearthstone:
https://github.com/jleclanche/fireplace/wiki/How-to-enable-logging
Note!  Rather than use the log config file suggest there, use the one in this repo.

Second, you need to point this script towards your log directoy.  We may need an automated way of finding that.
The script scans that directory for the most recent log file, and starts printing it out.
Eventually, this should be in a thread feeding info to the main program.
'''

import glob
import os
log_path = "/Users/justin/Library/Preferences/Blizzard/Hearthstone/Logs/"
list_of_files = glob.glob(log_path+'*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print "Opening",latest_file

import time
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    logfile = open(latest_file,"r")
    loglines = follow(logfile)
    for line in loglines:
        print line,

print "done"