import sys
import subprocess


output = subprocess.check_output(["git", "status"])

print output

for string in output.split():
    print "shitori" + string

