#!/usr/bin/env python3
import sys
import os

new_lim = sys.argv[1]

fout = open("POWERLIMIT.shx", "w")
with open("POWERLIMIT.sh") as f:
    for line in f:
        if "power_limit" in line:
            split = line.split()
            split[1] = new_lim + "000000"
            new_line = "\t" + " ".join(split) + "\n"
            fout.write(new_line)
        else:
            fout.write(line.rstrip()+"\n")
fout.close()

os.replace("POWERLIMIT.shx","POWERLIMIT.sh")


