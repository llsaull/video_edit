#!/usr/bin/env python3

import sys 
import os


def read_menu():
    opt = ["c","j","t","x"]
    x = ""
    while not x in opt:
        print(
        "  Choose an option:         \n"+
        "      c - cut a video       \n"+
        "      j - join videos       \n"+
        "      t - add text to video \n"+
        "      x - exit"
        )
        x = input()
    return x

def choose_files():
    print("  From these files:")
    l = get_files()

    opt = []
    for i in range(0,len(l)):
        opt.append(i)

    exit = False
    while not exit:
        for i in range(0,len(l)):
            print(f"      {i+1} - {l[i]}")
        print("  choose multiple files to join (separated by spaces): ",end="")

        # Check input
        exit = True
        x = input().split()
        ifiles = []
        for n in x:
            v = int(n)-1
            if not v in opt:
                exit = False
                print("  Invalid choice, try again:")
                break
            else:
                ifiles.append(v)
    return [l[i] for i in ifiles]

def join_videos(fs):
    concat_file = open(".concat.txt","w")
    for f in fs:
        concat_file.write(f"file '{f}'\n")
    concat_file.close()
    fout = get_fout(f,"j")
    txt = f"ffmpeg -f concat -safe 0 -i .concat.txt -c copy fout"
    print(txt)
    #os.system(txt)
    print(f"  [DONE] output saved to {fout}")
    print("-"*30+"\n"*2)

def choose_file():
    print("  Choose a file to edit:")
    l = get_files()
    opt  = []
    for i in range(0,len(l)):
        opt.append(i)

    x = ""
    while not x in opt:
        for i in opt:
            print(f"      {i+1} - {l[i]}")
        x = int(input())-1

    return l[x]

def get_files():
    l = []
    for f in os.listdir("."):
        if not os.path.isdir(f):
            if f.endswith(".mkv") or f.endswith(".mp4"):
                l.append(f)
    return l

def get_fout(f,ext):
    f1 = os.path.splitext(f)[0]
    f2 = os.path.splitext(f)[1]
    fout = f"{f1}[{ext}]{f2}"
    return fout

def cut_video(f):
    ss = input(" beginning (hh:mm:ss): ")
    to = input(" end       (hh:mm:ss): ")
    fout = get_fout(f,"c")
    txt = f"ffmpeg -i {f} -ss {ss} -to {to} -c copy {fout}"
    print(txt)
    #os.system(txt)
    print(f"  [DONE] output saved to {fout}")
    print("-"*30+"\n"*2)

def add_text(f):
    ss   = input(" beginning (hh:mm:ss): ")
    d    = input(" duration      (secs): ")
    text = input(" display text: ")
    hh, mm, ss = ss.split(":")
    bsecs = int(hh)*60**2 + int(mm)*60 + int(ss)
    esecs = bsecs + int(d)

    font = "fontfile=/usr/share/fonts/TTF/DejaVuSans.ttf"
    cmd  = f"drawtext=enable='between(t,{bsecs},{esecs})':{font}:text='{text}'"+\
           f":fontcolor=white: fontsize=24: box=1: boxcolor=black@0.5"+\
           f":boxborderw=5: x=(w-text_w)/2: y=(h-text_h)/2"
    fout = get_fout(f,"t")
    txt  = f"ffmpeg -i {f} -vf \"{cmd}\" -max_muxing_queue_size 9999 -acodec copy {fout}"

    print(txt)
    os.system(txt)
    print(f"  [DONE] output saved to {fout}")
    print("-"*30+"\n"*2)


exit = False
while not exit:
    x = read_menu()
    if x == "c":
        cut_video(choose_file())
    elif x == "j":
        join_videos(choose_files())
    elif x == "t":
        add_text(choose_file())
    elif x == "x":
        exit = True
    else:
        print("Not implemented yet")