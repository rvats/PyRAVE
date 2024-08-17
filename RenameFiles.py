import os
import time
from time import mktime
from datetime import datetime
target = input('Enter full directory path: ')
prefix = input('Enter prefix: ')
os.chdir(target)
allfiles = os.listdir(target)
for filename in os.listdir(target):
    os.rename(filename, datetime.fromtimestamp(os.path.getmtime(filename)).strftime('{0}%Y%m%d%H%M%S.jpg'.format(prefix)))