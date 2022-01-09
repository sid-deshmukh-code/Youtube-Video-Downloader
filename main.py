# Importing required modules

# ---------------------------------------------------------------------------------------
from tkinter import *
from tkinter import filedialog
# ---------------------------------------------------------------------------------------


def download():
    from pytube import YouTube
    yt = YouTube(link_.get())
    title = str(yt.title)
    Label(root, text=title).pack()
    path_ = filedialog.askdirectory()
    yt.streams.filter(file_extension='mp4', res="720p").first().download(str(path_))

# ---------------------------------------------------------------------------------------


root = Tk()
root.title("Youtube Video Downloader")
link_ = StringVar()
Label(root, text="Enter Your Video link here").pack()
e1 = Entry(root, textvariable=link_, font="SegoeUI 10 bold", borderwidth=3, relief=SUNKEN).pack(padx=3, pady=3)
Button(root, command=download, text="Download").pack()
root.mainloop()
# ---------------------------------------------------------------------------------------
