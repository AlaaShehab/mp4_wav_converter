import os
from os import listdir

def convert():
    files = [f for f in listdir() if f.endswith(".mp4")]
    print(len(files))
    [os.system("ffmpeg -i " + files[i] +" -vn audio" + str(i) + ".wav") for i in range(len(files))]
convert()