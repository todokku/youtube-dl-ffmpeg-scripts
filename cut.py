#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
import subprocess

def main():
    n_of_arguments = len(sys.argv)
    if n_of_arguments != 4:
        exit(f"Must have 3 arguments! {n_of_arguments-1} given. To omit end type \"end\" ")

    name = sys.argv[1]
    from_ = sys.argv[2]
    to = sys.argv[3]

    if to == "end":
        cmd = f"ffmpeg -i -ss {from_} -async 1 -strict -2 -qscale 0"
    else:
        cmd = f"ffmpeg -i -ss {from_} -to {to} -async 1 -strict -2 -qscale 0"

    cmd = cmd.split()
    cmd.insert(2, name)
    cmd.append( "CUT - " + name)


    start = time.time()
    print("Running ffmpeg...")
    subprocess.run(cmd)
    end = time.time()
    print(f"Time elapsed: {end - start:.2f} seconds")



if __name__ == "__main__":
    main()
