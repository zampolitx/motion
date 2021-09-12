#import section
import os, subprocess
from os.path import expanduser
import configure
#exit import section
home = expanduser("~")
l = subprocess.run(['ls', '-l'])
print(home)