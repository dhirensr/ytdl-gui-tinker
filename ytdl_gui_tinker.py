from tkinter import *
from tkinter import messagebox
import requests
import json
import os
import sys
import youtube_dl


class App (object):
  def __init__(self):
    self.root = Tk ()
    self.root.geometry ("600x400")
    self.root.wm_title ("Youtube-DL Gui")
    self.audio = IntVar()
    Checkbutton(self.root, text="Audio", variable=self.audio).pack()
    self.video = IntVar()
    Checkbutton(self.root, text="Video", variable=self.video).pack()
    self.directory_label = Label (self.root, text= "Enter the Directory to be saved in.")
    self.directory_label.pack ()
    self.directory = StringVar ()
    Entry(self.root, textvariable = self.directory).pack ()
    self.label = Label (self.root, text= "Enter the video link.")
    self.label.pack ()
    self.entrytext = StringVar ()
    Entry(self.root, textvariable = self.entrytext).pack ()
    self.buttontext = StringVar ()
    self.buttontext.set ("Download")
    Button(self.root, textvariable = self.buttontext, command = self.clicked_button).pack ()
    self.label = Label (self.root, text = "")
    self.label.pack ()
    self.root.mainloop ()
  def clicked_button (self):
    video_link = str (self.entrytext.get ())
    directory=str(self.directory.get())
    def download_hook(d):
        self.label.configure (text = d['status'])
        if d['status'] == 'finished':
            messagebox.showinfo('Status',"Download Completed !")

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        "outtmpl" : str(directory) + "/%(title)s.%(ext)s'" ,
        'progress_hooks': [download_hook],
    }
    try:
        if not os.path.exists(directory):
          messagebox.showinfo("Message","Path does not exists!")
        elif [int(self.audio.get()),int(self.video.get())].count(1) > 1:
            messagebox.showinfo("Message","Multiple Options Selected")
        else:
          if (int(self.video.get())==1):
            with youtube_dl.YoutubeDL() as ydl:
                ydl.download(video_link.split(","))
          else:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(video_link.split(","))
    except KeyError:
    	messagebox.showinfo("Sorry","Unable to download the video!")



App ()
