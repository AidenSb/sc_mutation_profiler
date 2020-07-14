import sys
import os
fl = open("filelist.txt", "w")
files=os.listdir()
for f in files:
    if f[-4:] ==".bam":
        job = "./bash " + f+"\n"
        fl.write(job)

