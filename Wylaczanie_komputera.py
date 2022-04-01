import tkinter
from tkinter import *
import time
import datetime
import os


def wylaczenie(ustaw_czas_wylaczenia):
    while True:
        time.sleep(1)
        czas = datetime.datetime.now()
        aktualny_czas = czas.strftime("%H:%M:%S")
        print('Aktualny czas: ' + str (aktualny_czas),",", 'Czas wyłączenia: ',ustaw_czas_wylaczenia)
        if aktualny_czas == ustaw_czas_wylaczenia:
            os.system('shutdown -s')
            break

def pobierz_czas_alarmu():
    ustaw = f"{godz.get()}:{min.get()}:{sek.get()}"
    wylaczenie(ustaw)

def wyswietlanie():
    obecna = datetime.datetime.now().strftime("%H:%M:%S")
    l2.config(text = obecna)
    l2.after(100, wyswietlanie)
        
root = tkinter.Tk()
root.title("Wyłączenie komputera")
root.geometry('340x200')
root.resizable(width=False,height=False)

godz = StringVar()
min = StringVar()
sek = StringVar()

l = tkinter.Label(root, text = 'Aktualna godzina: ', font = ('Calibri', 12), width = '20')
l.pack()
l2 = tkinter.Label(root, text = wyswietlanie, font=('Calibri', 25) ,bg = 'black', fg = 'green', height = '1', width = '10')
l2.place(x = 80, y = 25)
l3 = tkinter.Label(root, text = 'Wyłączenie \n komputera: \n godz. min. sek.', font = ('Calibri', 8), fg = 'red', width = '12')
l3.place(x = 8 , y = 71)
l4 = tkinter.Label(root, text = 'Podaj wszystkie wartości (format 24 godz.)', font = ('Calibri', 8), width = '40')
l4.place(x = 48, y = 115)
egodziny = tkinter.Entry(root, textvariable = godz, bg = 'white', fg = 'black', font = 15, width = 4)
egodziny.place(x = 94, y = 79) 
eminuty = tkinter.Entry(root, textvariable = min, bg = 'white', fg = 'black', font = 15, width = 4)
eminuty.place(x = 144, y = 79)
esekundy = tkinter.Entry(root, textvariable = sek, bg = 'white', fg = 'black', font = 15, width = 4)
esekundy.place(x = 194, y = 79)

b = tkinter.Button(root, command = pobierz_czas_alarmu, text = 'Zatwierdź', font = ('Calibri', 16), bg = 'grey', fg = 'white')
b.place(x = 117, y = 140)

wyswietlanie()
root.mainloop()