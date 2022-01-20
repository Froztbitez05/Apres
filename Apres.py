import math
import tkinter as tk
from tkinter import Text

root = tk.Tk()
root.title("Apresiasi")

def calculate ():
    apres()

def apres ():
    Nilai = float(Entry_nilai.get())

    if Nilai >= 94:
        label_predikat['text'] = f"Predikat : Summa Cum Laude"

    elif Nilai >= 91:
        label_predikat['text'] = f"Predikat : Magna Cum Laude"
    
    elif Nilai >= 88:
        label_predikat['text'] = f"Predikat : Cum Laude"

    else :
        label_predikat['text'] = f"Predikat : Tidak Memenuhi Kriteria"

canvas = tk.Canvas(root, height = 800, width = 800, bg = "#506f75")
canvas.pack()

Frame = tk.Frame(root, bg = "white")
Frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

label_nama = tk.Label(Frame, text = "Nama :")
label_nama.grid(column = 0, row = 1)

label_nilai = tk.Label(Frame, text = "Nilai :")
label_nilai.grid(column = 0, row = 2)

label_predikat = tk.Label(Frame, text = "Predikat :")
label_predikat.grid(column = 0, row = 3)

Entry_nama = tk.Entry(Frame)
Entry_nama.grid(column = 1, row = 1)

Entry_nilai = tk.Entry(Frame)
Entry_nilai.grid(column = 1, row = 2)

button_kalkulasi = tk.Button(root, text = "Calculate", command=calculate)
button_kalkulasi.pack()

root.mainloop()