#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import subprocess


def main():
    n_of_arguments = len(sys.argv)
    if n_of_arguments != 2:
        exit(f"Must have 1 argument (File to crop)! {n_of_arguments-1} given.")
    in_file = sys.argv[1]
    print("Insert width and height for the output: ")
    out_w, out_h = take_two_ints()
    print("Insert start x and y coords: ")
    x, y = take_two_ints()
    #bash command
    cmd = f'ffmpeg -i -filter:v "crop={out_w}:{out_h}:{x}:{y}"'.split()
    cmd.insert(2, in_file)
    cmd.append("CROPPED - " + in_file)
    subprocess.run(cmd)
    
        

def take_two_ints():
    try:
        first_line = input().split() #performance? Go to only second whitespace?
        if len(first_line) < 1:
            raise(ValueError)
        elif len(first_line) == 1:
            num1 = first_line[0]
            num2 = int(input())
            return num1, num2
        elif len(first_line) > 1:
            num1 = first_line[0]
            num2 = first_line[1]
            return num1, num2
    except ValueError as e:
        print("Error parsing. Try again: ")
        return take_two_ints()



if __name__ == "__main__":
    main()
