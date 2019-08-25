#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
import subprocess


n_of_arguments = len(sys.argv)
if n_of_arguments != 3:
    exit(f"Must have 2 arguments (video + audio)! {n_of_arguments-1} given.")

video = sys.argv[1]
audio = sys.argv[2]

cmd = f"ffmpeg -i -i -c:v copy -c:a aac -strict experimental"
cmd = cmd + " -loglevel panic"
cmd = cmd + " -hide_banner"
cmd = cmd.split()
cmd.insert(2, video)
cmd.insert(4, audio)

output_name = "STITCHED - " + video
cmd.append(output_name)

start = time.time()
print("Running ffmpeg...")

subprocess.run(cmd)

end = time.time()
print(f"Time elapsed: {end - start:.2f} seconds")
