import tkinter as tk
from pytube import YouTube



def download_video():
    url = e.get()
    try:
        YouTube(url).streams.get_highest_resolution().download()   
        status.config(text="Download Successful!")
    except:
        status.config(text="Download Failed!")
        
#Create the GUI window
window = tk.Tk()
window.title("YouTube Downloader")

#Create the input text box
tk.Label(window, text=" Enter YouTube URL: ").grid(row=0, column=0 )
e = tk.Entry(window, width=40, borderwidth=5 )
e.grid(row=0, column=1)

#Create the download button
download_btn = tk.Button(window, text="Download", command=download_video)
download_btn.grid( row=1, column=0, columnspan=2, pady=10 )


#Create the status message label
status = tk.Label(window, text="", font=("Courier",12))
status.grid( row=2, column=0, columnspan=2 )

#run the GUI window
window.mainloop()


