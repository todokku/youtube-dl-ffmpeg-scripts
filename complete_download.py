#!/usr/bin/env python3
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
    run_cmd(cmd, "Formats available:\n")


    video_format = input("\nEnter video format: ")
    audio_format = input("\nEnter audio format: ")

    cmd = f"youtube-dl -f {video_format} {URL} -o %(title)s.%(ext)s"
    run_cmd(cmd,"\nDownloading video...")

    cmd = f"youtube-dl -f {video_format} --get-filename -o %(title)s.%(ext)s {URL}"
    out = subprocess.check_output(cmd.split())
    video = out.decode("utf-8").strip()

    cmd = f"youtube-dl -f {audio_format} {URL} -o %(title)s.%(ext)s"
    run_cmd(cmd, "\nDownloading audio...")

    cmd = f"youtube-dl -f {audio_format} --get-filename -o %(title)s.%(ext)s {URL}"
    out = subprocess.check_output(cmd.split())
    audio = out.decode("utf-8").strip()

    #STITCH


    cmd = f"ffmpeg -i -i -c:v copy -c:a aac -strict experimental"
    cmd = cmd + " -loglevel panic"
    cmd = cmd + " -hide_banner"
    cmd = cmd.split()
    cmd.insert(2, video)
    cmd.insert(4, audio)
    output_name = "DL - " + video
    cmd.append(output_name)

    run_cmd(cmd,"\nStitching video & audio...")

    run_cmd(['rm', video, audio], "\nRemoving leftover files...")

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

if __name__ == "__main__":
    main()
