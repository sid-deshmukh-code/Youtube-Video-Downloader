# Importing required modules

# ---------------------------------------------------------------------------------------
from tkinter import *
from tkinter import filedialog, messagebox, ttk


# ---------------------------------------------------------------------------------------
# Backend

def download():
    try:
        from pytube import YouTube
        yt = YouTube(link_.get())
        video_title = str(yt.title)
        Label(root, text=video_title).pack(pady=8)
        path_ = filedialog.askdirectory()
        if format_is_video.get():
            file_name = str(video_title+'_'+resolution_var.get()+'_'+'_ssd.mp4')
            print(file_name)
            yt.streams.filter(file_extension="mp4", res=str(resolution_var.get())).first().download(str(path_), filename=file_name)
        else:
            yt.streams.filter(only_audio=True).first().download(str(path_), filename=video_title+"_ssd.mp3")

        messagebox.askokcancel("Success", "Successfully Downloaded")
    except Exception as ee:
        messagebox.showerror("Error", "Something went wrong" + str(ee))
        print(ee)


# ---------------------------------------------------------------------------------------


root = Tk()
root.title("Youtube Video Downloader")
root.geometry("470x420")
# ---------------------------------------------------------------------------------------

link_ = StringVar()
format_is_video = BooleanVar()
resolution_var = StringVar()

# ---------------------------------------------------------------------------------------

Label(root, text="Youtube Video Downloader", bg='skyblue', font="SegoeUI 15 bold", borderwidth=5).pack()
frame_ = Frame(root).pack()
frame2 = Frame(root).pack(fill=BOTH, side=LEFT)
frame3 = Frame(root).pack(fill=BOTH, side=LEFT)

# ---------------------------------------------------------------------------------------

Label(frame_, text="Enter Your Video link here").pack(pady=4, padx=5)
Entry(frame_, textvariable=link_, font="SegoeUI 10 bold", borderwidth=4, relief=SUNKEN).pack(padx=4, pady=3)

# ---------------------------------------------------------------------------------------

Label(frame2, text="Select Format").pack()
Radiobutton(frame2, text='mp3', variable=format_is_video, value=False).pack()
Radiobutton(frame2, text='mp4', variable=format_is_video, value=True).pack()

# ---------------------------------------------------------------------------------------
# Selecting resolution
Label(frame3, text="Select Resolution").pack()
res_combo = ttk.Combobox(frame3, width=27, textvariable=resolution_var)
res_combo['values'] = ('144p',
                       '240p',
                       '360p',
                       '480p',
                       '720p',
                       '1080p')
res_combo['state'] = 'readonly'
res_combo.pack()
# Download button
Button(root, command=download, text="Download", relief=RIDGE, font="Helvetica 16 bold").pack(side=RIGHT)
# ---------------------------------------------------------------------------------------
root.mainloop()
# ---------------------------------------------------------------------------------------
