from tkinter import  messagebox
from tkinter import *
from pytube import YouTube
root=Tk()
root.geometry("325x200")
root.title("Youtube downloader")
root['bg']="#51E1DC"
#heading
Label(text="Youtube Video Download",fg="gold",pady=20,padx=30,font=("Times", "10", "bold italic"),borderwidth = 5,relief="sunken",bg="black").place(x=40,y=40)
link = StringVar()
#label for heading
Label( text = 'Paste video Link Here:', fg="red",font =("Helvetica",9,"bold italic") ,bg="white").place(x= 170, y = 190)
#text input
link_enter = Entry(root, width = 30,fg="blue",font=("Helvetica",8,"bold italic"),textvariable = link).place(x = 60, y = 300)



#function for downloading
def YouTubeDownloader():
    #applying validation
    if link.get()!="":
     #getting url
     url =YouTube(str(link.get()))
     video = url.streams.first()
     #download video
     video.download()

     #show messsage
     messagebox.showinfo("Downloaded","Download Sucessfully")
    else:
        messagebox.showwarning("Warning", "Please Add The Link")
#button
Button(root,text = 'Download', font = 'arial 12 bold italic' ,pady=20,bg = 'green',fg="white", padx = 10, borderwidth = 5,relief="sunken",command = YouTubeDownloader).place(x=240 ,y = 420)
root.mainloop()