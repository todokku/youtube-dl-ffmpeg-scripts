#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Crop height/width of a video
#Reference: https://video.stackexchange.com/questions/4563/how-can-i-crop-a-video-with-ffmpeg
import sys



def main():
    #ffmpeg -i in.mp4 -filter:v "crop=out_w:out_h:x:y" out.mp4
    n_of_arguments = len(sys.argv)
    if n_of_arguments != 2:
        exit(f"Must have 1 argument (File to crop)! {n_of_arguments-1} given.")
    print("Insert width and height for the output: ")
    out_w, out_h = take_two_ints()
    print(out_w, out_h)
    
        

def take_two_ints():
    #practice: take_n_ints (recursion: take_n-1_ints...)
    try:
        first_line = input().split() #performance? Go to only second whitespace?
        print("first line debug: " + str(first_line))
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
        return take_two_ints() # Tail recursion? No stack overflow?



if __name__ == "__main__":
    main()
