#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
import subprocess


def main():
    n_of_arguments = len(sys.argv)
    if n_of_arguments != 2:
        exit(f"Must have 1 argument (URL)! {n_of_arguments-1} given.")

    # ampersand problemi! Izbegevaj zbog shell-a
    URL = sys.argv[1]
    amp_pos = URL.find('&')
    if amp_pos > 0:
        #URL = URL[0:amp_pos]
        exit("URL can't have ampersands! (Shell issues)")
    cmd = f"youtube-dl -F {URL}"
    run_cmd(cmd, "formats:\n")


    video = input("\nEnter video format: ")
    audio = input("\nEnter audio format: ")

    cmd = f"youtube-dl -f {video} {URL} -o %(title)s.%(ext)s"
    run_cmd(cmd)

    cmd = f"youtube-dl -f {audio} {URL} -o %(title)s.%(ext)s"
    run_cmd(cmd)

    return


def run_cmd(cmd = "echo 'No command!'", msg = ""):
    start = time.time()
    print(msg)
    if isinstance(cmd, str):
        cmd = cmd.split()
    #print(cmd)
    subprocess.run(cmd)
    end = time.time()
    print(f"Time elapsed: {end - start:.2f} seconds")
    return


def check_output(file_name):
    tmp = file_name
    suffix = 1
    while os.path.exists(tmp):
        tmp = file_name + str(suffix)
        suffix = suffix + 1
    return tmp

if __name__ == "__main__":
    main()
