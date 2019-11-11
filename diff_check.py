import os
from subprocess import check_output
#p = os.Popen('diff a.txt b.txt')
p = os.popen('diff a.txt b.txt')

fp=open("diff.txt","w")

for line in p.read():
	fp.write(line)
fp.close()

q = os.popen('patch a.txt diff.txt')

