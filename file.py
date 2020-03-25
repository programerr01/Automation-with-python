""" importing the modules require 
note: when you first run it will not work immediately. u need to change a lit of folder to work 
you can also run it like normal python script if you want it to work once
"""
import os,time
import shutil

directory = '/home/yogesh/Downloads'
os.chdir(directory) #changing the directory to downloads to work from there 

st = os.stat(directory).st_mtime #it will check for any modification in folder


while True:
    st1 = os.stat(directory).st_mtime #getting the modification file
    if st != st1: #if modified is equal to the previous one then it is not modified
        st = st1 #changing the previous file to new and then again loop through
        for files in os.listdir():
            
            if files.endswith(".mkv", ): #ext of the file for ex mp3 , mp4 etc to move it
                shutil.move(files , "/home/yogesh/Videos") #path to where you want to paste it
            elif files.endswith(".jpg"):
                shutil.move(files , "/home/yogesh/Pictures")
            elif files.endswith(".pdf"):
                shutil.move(files , "/home/yogesh/Documents")
            
            elif files.endswith(".mp3"):
                shutil.move(files , "/home/yogesh/Music")
                
    else:
        time.sleep(10) #checking after 10 seconds so it don't take too much process
