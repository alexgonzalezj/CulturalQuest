import tkinter
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk

ventana = Tk()
ventana.title("CulturalQuest v1.0 By Dreamers - IED Comunitaria Metropolitana")
ventana.minsize(width=800, height=480)
ventana.maxsize(width=800, height=480)
imgBack = PhotoImage(file = 'Images\ondo.png')
titulo = Label(ventana, text="CulturalQuest v1.0 || By DREAMERS")
titulo.pack(anchor=CENTER)
titulo.config(fg="white",bg="black")
titulo.place(x = 10, y = 200)
titulo.pack()
background = Label(image = imgBack)
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
ventana.config(padx= 35, pady= 1, background="black")

def winBrasil() :    
    tkinter.messagebox.showinfo(title=None, message="Listo Brasil")
    
def winSpain() :    
    tkinter.messagebox.showinfo(title=None, message="Listo España")

def winUSA() :    
    tkinter.messagebox.showinfo(title=None, message="Listo USA")

def winKorea() :    
    tkinter.messagebox.showinfo(title=None, message="Listo Korea")

def winGermany() :    
    tkinter.messagebox.showinfo(title=None, message="Listo Alemania")
    
def winJapan() : 
    ventana.withdraw()   
    tkinter.messagebox.showinfo(title=None, message="Listo Japón")
    ventana.deiconify()

def winChinese() : 
    ventana.withdraw()   
    tkinter.messagebox.showinfo(title=None, message="Listo China")
    ventana.deiconify()

def winFrench() : 
    ventana.withdraw()   
    tkinter.messagebox.showinfo(title=None, message="Listo Francia")
    ventana.deiconify()

def winRussia() : 
    ventana.withdraw()   
    tkinter.messagebox.showinfo(title=None, message="Listo Rusia")
    ventana.deiconify()

def winItaly() : 
    ventana.withdraw()   
    tkinter.messagebox.showinfo(title=None, message="Listo Italia")
    ventana.deiconify()

def winArabia() : 
    ventana.withdraw()   
    tkinter.messagebox.showinfo(title=None, message="Listo Arabia")
    ventana.deiconify()

def winSwedish() : 
    ventana.withdraw()   
    tkinter.messagebox.showinfo(title=None, message="Listo Suecia")
    ventana.deiconify()

#Botón Brasil
imgBrasil = Image.open("Images\Flags\Brazil.png")
imgBrasil = imgBrasil.resize((96,96))
renderBrasil = ImageTk.PhotoImage(imgBrasil)
btnBrasil = tkinter.Button(text="Español", width=100, height=100, image = renderBrasil, command=winBrasil)
btnBrasil.place(x = 295, y = 30)

#Botón España
imgSpain = Image.open("Images\Flags\Spain.png")
imgSpain = imgSpain.resize((96,96))
renderSpain = ImageTk.PhotoImage(imgSpain)
btnSpain = tkinter.Button(text="Español", width=100, height=100, image = renderSpain, command = winSpain)
btnSpain.place(x = 405, y = 30)

#Botón USA
imgUSA = Image.open("Images\Flags\eua.png")
imgUSA = imgUSA.resize((96,96))
renderUSA = ImageTk.PhotoImage(imgUSA)
btnUSA = tkinter.Button(text="Español", width=100, height=100, image = renderUSA, command = winUSA)
btnUSA.place(x = 515, y = 30)

#Botón Korea
imgKorea = Image.open("Images\Flags\Korea.png")
imgKorea = imgKorea.resize((96,96))
renderKorea = ImageTk.PhotoImage(imgKorea)
btnKorea = tkinter.Button(text="Español", width=100, height=100, image = renderKorea, command = winKorea)
btnKorea.place(x = 625, y = 30)

#Botón Germany
imgGermany = Image.open("Images\Flags\Germany.png")
imgGermany = imgGermany.resize((96,96))
renderGermany = ImageTk.PhotoImage(imgGermany)
btnGermany = tkinter.Button(text="Español", width=100, height=100, image = renderGermany, command=winGermany)
btnGermany.place(x = 295, y = 140)

#Botón Japón
imgJapan = Image.open("Images\Flags\Japan.png")
imgJapan = imgJapan.resize((96,96))
renderJapan = ImageTk.PhotoImage(imgJapan)
btnJapan = tkinter.Button(text="Español", width=100, height=100, image = renderJapan, command=winJapan)
btnJapan.place(x = 405, y = 140)

#Botón China
imgChinese = Image.open("Images\Flags\China.png")
imgChinese = imgChinese.resize((96,96))
renderChinese = ImageTk.PhotoImage(imgChinese)
btnChinese = tkinter.Button(text="Español", width=100, height=100, image = renderChinese, command = winChinese)
btnChinese.place(x = 515, y = 140)

#Botón Francia
imgFrench = Image.open("Images\Flags\France.png")
imgFrench = imgFrench.resize((96,96))
renderFrench = ImageTk.PhotoImage(imgFrench)
btnFrench = tkinter.Button(text="Español", width=100, height=100, image = renderFrench, command=winFrench)
btnFrench.place(x = 625, y = 140)

#Botón Russia
imgRussia = Image.open("Images\Flags\Russia.png")
imgRussia = imgRussia.resize((96,96))
renderRussia = ImageTk.PhotoImage(imgRussia)
btnRussia = tkinter.Button(text="Español", width=100, height=100, image = renderRussia, command=winRussia)
btnRussia.place(x = 295, y = 250)

#Botón Italy
imgItaly = Image.open("Images\Flags\Italy.png")
imgItaly = imgItaly.resize((96,96))
renderItaly = ImageTk.PhotoImage(imgItaly)
btnItaly = tkinter.Button(text="Español", width=100, height=100, image = renderItaly, command=winItaly)
btnItaly.place(x = 405, y = 250)

#Botón Arabia
imgArabia = Image.open("Images\Flags\Arabia.png")
imgArabia = imgArabia.resize((96,96))
renderArabia = ImageTk.PhotoImage(imgArabia)
btnArabia = tkinter.Button(text="Español", width=100, height=100, image = renderArabia, command=winArabia)
btnArabia.place(x = 515, y = 250)

#Botón Swedish
imgSwedish = Image.open("Images\Flags\Sweden.png")
imgSwedish = imgSwedish.resize((96,96))
renderSwedish = ImageTk.PhotoImage(imgSwedish)
btnSwedish = tkinter.Button(text="Español", width=100, height=100, image = renderSwedish, command=winSwedish)
btnSwedish.place(x = 625, y = 250)

ventana.mainloop()