#mapper.py


#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import re
import sys

regex='([(\d\.)]+) - - \[(.*?)\] "(/*?)" (\d+) - "(.*?)" "(.*?)"'

for line in sys.stdin:
  data = line.strip().split("\t")
  if len(data) == 6:
  ip, identity, username, time, method, status, size= re.match(regex,data).groups()
    if(methog)
    print "{0}\t{1}".format(item, cost)
