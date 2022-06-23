from tkinter import *
from tkinter import messagebox
import pytube
import tqdm

FOLDER = 'C:/Audio'


def youtube_download():
    yt = pytube.YouTube(y_t_enter.get())
    audio = yt.streams.get_audio_only()
    yt.register_on_progress_callback(progress_download)
    audio.download(FOLDER)
    # audio.title
    display_end_download()




def progress_download(stream, chunk, bytes_remaining):
    for i in tqdm.tqdm(range(stream.filesize)):
        ''


def display_end_download():
    messagebox.showinfo("End download", f"End download\nFile sawed C:/Audio")


window = Tk()
window.geometry('680x150')
window.title("MP3 from You Tube")

x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2 - 340
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2 - 75
window.wm_geometry("+%d+%d" % (x, y))
lbl = Label(window, text="                                                Insert You Tube address",
            font=("Arial Bold", 14))
lbl.grid(column=0, row=0)
y_t_enter = Entry(window, width=50, font=("Arial Bold", 14))
y_t_enter.place(x=70, y=30)
txt1 = y_t_enter.get()
btn_start = Button(window, text="                      START                     ", font=("Arial Bold", 12),
                   command=youtube_download)
btn_start.place(x=220, y=75)
window.mainloop()
