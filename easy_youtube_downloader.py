''' 
Most simple and flexible youtube video downloader
It's free and always will be :)
Power of open source code
currently supporting videos upto 720p

Features to add in future version:
1080p support
mp3 support
playlist support
extract link to a txt file.

requirements : pytube
To install pytube use command 'pip install pytube'
'''

import os,subprocess
from pytube import YouTube,Playlist

MB = 1048576 #  (1024*1024)

def convert_to_mb(num):
    #function to convert bytes into MB
    a = num/MB
    print("%.2f MB" % a)

quality = {'360p':18, '720p':22,'mp3':140,'240p':36,'144p':17,'1080p':137}

support = ['720p','480p','360p','240p','144p',]

avail = []

def ask_quality():
    print("Enter from the above available resolutions")
    quality = str(input('Enter the quality in which you want to download the video: '))
    while quality not in avail:
        print("please provide correct input like '360p' and hit enter")
        quality = str(input('Enter the quality in which you want to download the video: '))
    return quality

def download_singlefile(link):
    q = ask_quality()
    yt = YouTube(link)
    print("please wait....")
    if q=='1080p':
        print("1080p is not supported! ")
    else:
        z = yt.streams.get_by_itag(quality[q])
        print(z.default_filename)
        convert_to_mb(z.filesize)
        print('downloading....')
        z.download()
        print("download complete :)")

def query_all(link):
    yt = YouTube(link)
    print(yt.streams.first().default_filename)
    videoavail = []
    videos = yt.streams.filter(progressive=True).all()
    
    for video in videos:
        videoavail.append(video.resolution)
        print(video.resolution, end=' ')
        convert_to_mb(video.filesize)
    avail[:] = videoavail

    
#main program
link = str(input("Enter the link of a video: "))
query_all(link)
download_singlefile(link)

dirpath = os.getcwd()
print("saved in ",end = ' ')
print(dirpath)
