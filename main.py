from pytube import YouTube
from pytube import Playlist
import re
from tkinter import *
from tkinter import ttk
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from tkinter import messagebox as MessageBox
import ttkbootstrap as ttkb
import moviepy.editor as mp

def center_window(window):

    window.update_idletasks()
    width = window.winfo_width()
    frm_width = window.winfo_rootx() - window.winfo_x()
    win_width = width + 2*frm_width
    height = window.winfo_height()
    titlebar_height = window.winfo_rooty() - window.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = window.winfo_screenwidth()//2 - win_width//2
    y = window.winfo_screenheight()//2 - win_height//2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.deiconify()

def poup():
    MessageBox.showinfo("Sobre el software","Programa creado para descaragr videos de youtube con el link")


def funcion():
    Otraventana.state(newstate = "normal")
    root.state(newstate = "withdraw")

def funcion2():
    Otraventana.state(newstate = "withdraw")
    root.state(newstate = "normal") #state(newstate = "withdraw")root.deiconify, zoomed()

def actionmp4():
    link = video.get()
    direct = video_carpeta.get()

    if len(link) == 0:
        MessageBox.showinfo("Campo vacío","Debe ingresar un link")
    else:
        if len(direct) == 0:
             MessageBox.showinfo("Campo vacío","Debe ingresar un nombre para crear una carpeta")
        else:
            Youtubevideo = YouTube(link)
            downloads = Youtubevideo.streams.get_highest_resolution()
            downloads.download(direct)
            MessageBox.showinfo("Estado de descarga","La descarga se realizó con exito")

def actionmp4playlist():
    link = video_playlist.get()
    direct = video_carpeta_playlist.get()

    if len(link) == 0:
        MessageBox.showinfo("Campo vacío","Debe ingresar un link")
    else:
        if len(direct) == 0:
             MessageBox.showinfo("Campo vacío","Debe ingresar un nombre para crear una carpeta")
        else:
            Youtubevideo = Playlist(link)
            # this fixes the empty playlist.videos list
            Youtubevideo._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
            print(len(Youtubevideo.video_urls))
            for url in Youtubevideo.video_urls:
                print(url)
            # physically downloading the audio track
            for video in Youtubevideo.videos:
                downloads = video.streams.get_highest_resolution()
                downloads.download(direct)
            MessageBox.showinfo("Estado de descarga","La descarga del playlist mp4 se realizó con exito")

def actionmp3():
    link = video.get()
    direct = video_carpeta.get()

    if len(link) == 0:
        MessageBox.showinfo("Campo vacío","Debe ingresar un link")
    else:
        if len(direct) == 0:
             MessageBox.showinfo("Campo vacío","Debe ingresar un nombre para crear una carpeta")
        else:
            YOUTUBE_STREAM_AUDIO = '140'
            Youtubevideo = YouTube(link)
            downloads = Youtubevideo.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
            downloads.download(direct)
            MessageBox.showinfo("Estado de descarga","La descarga se realizó con exito")

def actionmp3playlist():
    link = video_playlist.get()
    direct = video_carpeta_playlist.get()

    if len(link) == 0:
        MessageBox.showinfo("Campo vacío","Debe ingresar un link")
    else:
        if len(direct) == 0:
             MessageBox.showinfo("Campo vacío","Debe ingresar un nombre para crear una carpeta")
        else:
            YOUTUBE_STREAM_AUDIO = '140'
            Youtubevideo = Playlist(link)
            # this fixes the empty playlist.videos list
            Youtubevideo._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
            print(len(Youtubevideo.video_urls))
            for url in Youtubevideo.video_urls:
                print(url)
            # physically downloading the audio track
            for video in Youtubevideo.videos:
                downloads = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
                downloads.download(direct)
            MessageBox.showinfo("Estado de descarga","La descarga se realizó con exito")


root = Tk()
root.state(newstate = "normal")
root.geometry("350x400")
root.resizable(0, 0)
root.title("Ventana 1")
root.iconbitmap("img/logo_youtube.ico")
center_window(root)

##menu principal
menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Para Más información", menu=helpmenu)
helpmenu.add_command(label="Acerca de programa", command=poup)
menubar.add_command(label="Playlist", command=funcion)
menubar.add_command(label="salir", command=root.destroy)

#Imagen de youtube
image = PhotoImage(file="img/logo_youtube.png")
foto = Label(root, image=image, bd=0)
foto.pack()

#label
text_link = Label(root, text="Link de descarga")
text_link.pack()

# input link
video = Entry(root)
video.pack(pady=12, padx=10)

#label
text_carpeta = Label(root, text="Nombre de carpeta del la descarga")
text_carpeta.pack()

# input link
video_carpeta = Entry(root)
video_carpeta.pack(pady=12, padx=10)

btn_mp4 = Button(root, text="Descargar a mp4", font= ("Times New Roman", 12), command=actionmp4)
btn_mp4.pack(pady=12, padx=10)

btn_mp3 = Button(root, text="Descargar a mp3", font= ("Times New Roman", 12), command=actionmp3)
btn_mp3.pack(pady=12, padx=10)

Otraventana = Toplevel()
Otraventana.state(newstate = "withdraw")
Otraventana.geometry("350x400")
Otraventana.title("Ventana 2")
Otraventana.iconbitmap("img/logo_youtube.ico")

##menu principal
menubar = Menu(Otraventana)
Otraventana.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Para Más información", menu=helpmenu)
helpmenu.add_command(label="Acerca de programa", command=poup)
menubar.add_command(label="Video unico", command=funcion2)
menubar.add_command(label="salir", command=Otraventana.destroy)

#Imagen de youtube ventana dos
image1 = PhotoImage(file="img/logo_youtube.png")
foto1 = Label(Otraventana, image=image1, bd=0)
foto1.pack()

#label
text_link_playlist = Label(Otraventana, text="Link de descarga del playlist")
text_link_playlist.pack()

# input link
video_playlist = Entry(Otraventana)
video_playlist.pack(pady=12, padx=10)

#label
text_carpeta_playlist = Label(Otraventana, text="Nombre de carpeta del las descargas")
text_carpeta_playlist.pack()

# input link
video_carpeta_playlist = Entry(Otraventana)
video_carpeta_playlist.pack(pady=12, padx=10)


btn_mp4_playlist = Button(Otraventana, text="Descargar a mp4", font= ("Times New Roman", 12), command=actionmp4playlist)
btn_mp4_playlist.pack(pady=12, padx=10)

btn_mp3_playlist = Button(Otraventana, text="Descargar a mp3", font= ("Times New Roman", 12), command=actionmp3playlist)
btn_mp3_playlist.pack(pady=12, padx=10)

Otraventana.mainloop()
root.mainloop()