# -------------------------------------------------------------------------
# GenericHeader.py - V0.1 - 27 June 2014
# -------------------------------------------------------------------------
# This work is licensed under a:
# Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
# http://creativecommons.org/licenses/by-nc-sa/3.0/us/
#
# by:
# D. Calvin Andrus, Ph.D.
# Sterling, VA 20164
# calvin.andrus@gmail.com
#--------------------------------------------------------------------------
# developed on:
# Enthought Python Distribution (EPD) free version -- www.enthought.com
# Python 2.7.3 |EPD_free 7.3-2 (32-bit)| (default, Apr 12 2012, 11:28:34) 
# [GCC 4.0.1 (Apple Inc. build 5493)] on darwin
#
# using:
# The Google Python Style Guide
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html
#-------------------------------------------------------------------------
# Give an overall description of what this program does
#
# Explain any unusual libraries or data that is needed
#
# Program based on:
# Cite the source of the original code, or the source of the inspiration,
# textbook chapter, blog posting, web course, etc.
# http://playground.arduino.cc/interfacing/python
#
#-------------------------------------------------------------------------
# Clean up memory
#-------------------------------------------------------------------------

# Delete all global, but non-system, variables
all = [var for var in globals() if (var[:2], var[-2:]) != ("__", "__")]
for var in all:
    del globals()[var]

del all
del var

# See what is left
globals()

#-------------------------------------------------------------------------
# Load basic libraries from the "Standard Library"
#-------------------------------------------------------------------------

# Python Interpreter Functions (sys)
# Operating System Functions (os)
# Information about the machine and os (platform)
# Manage system memory (resource)
# Functions for time (time)

import sys
import os
import platform
import resource
import time

#-------------------------------------------------------------------------
# Describe the environment
#-------------------------------------------------------------------------

# Clear the console (doesn't work in Spyder)
# os.system('clear')

# Current date and time
time.strftime("%c")

# Info about the machine and os
platform.uname()

# See who is logged in (doesn't work in Spyder)
# os.getlogin()

# Currently used memory (for OSX returns in bytes)
resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

# Total memory limit;  5 = RLIMIT_RSS
# This is operating system limit, not physical machine memoryos.popen()
resource.getrlimit(5)

# About Python -- don't be surprised if you are running
# a 32-bit Python on a 64-bit machine
platform.python_implementation()
platform.python_version()
platform.architecture()
sys.getdefaultencoding()
sys.getfilesystemencoding()

# Set the default directory and see what is in there

path = "/Users/Calvin/Google Drive/Projects/Python/Ard"
os.chdir(path)
os.getcwd()
os.listdir(path)
cmd = "ls -l"
os.system(cmd)

#-------------------------------------------------------------------------
# Load other libraries 
#-------------------------------------------------------------------------

# Functions for dates and times (datetime)
import datetime

#-------------------------------------------------------------------------
# Define functions
#-------------------------------------------------------------------------

# The make_dir() function creates a new directory
# This funtion requires the 'os' module to be previously imported
# Caller must pass an argument that is a character string
# It first checks to see if the directory already exists
# If not, then it makes the directory

def make_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)
	print "Directory '", d, "' created!"
    else:
	print "Directory already exists!"


# The make_fil() function creates a file then closes it
# The "with open()" command sequence both opens the file and then
# automatically closes the file when the 'with' operation is complete.
# Otherwise, we would have to explicitly close the file as follows
#     f = open('myfile.dat', 'w+')
#     f.close()

def make_fil(f):
	if os.path.exists(f):
		with open(f,'r+') as f1:
			print "File '", f, "' already existed."
	else:
		with open(f,'w') as f1:
			print "File '", f, "' now created."

#-------------------------------------------------------------------------
# Define constants
#-------------------------------------------------------------------------

# Load the years, months, days into lists
# The s_ at the begining of the variables means "seminary" and
# disambiguates the variables from package functions

s_year = [2013, 2014]
s_month = [9, 10, 11, 12, 1, 2, 3, 4, 5]
s_day = [d+1 for d in range(31)]

# number of days per month for the 9 seminary months (Sep-Jun)

day_month = [30, 31, 30, 31, 31, 28, 31, 30, 31]

# Day names as a list

day_name = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Month names as a list and as a dict (key-value pair)

mth_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
	     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] 
mth_nam_d = {'09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec',
	     '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May'}

#-------------------------------------------------------------------------
# Now, see what globals we are starting with
#-------------------------------------------------------------------------
globals()

#-------------------------------------------------------------------------
# Begin Executable Statements
#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
# End of executable statements
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Backup material
#-------------------------------------------------------------------------

