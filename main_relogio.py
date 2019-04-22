import tkinter as tk
from tkinter import ttk
from datetime import datetime as dt
import hora

#now = dt.now()
#h1 = hora.Hora(now.hour, now.minute, now.second)
#h2 = hora.Hora(7, 16, 33)
#
#print(h1)
#print(h2)
#print(50*'-')
#h1.mais_um_segundo()
#h2.mais_um_segundo()
#print(h1)
#print(h2)
#
#main_window = tk.Tk()
#main_window.title('Relógio')
#
#lblHora = ttk.Label(main_window, text=h1.__str__())
#lblHora.grid(column=0, row=0, padx=5)
#lblMinuto = ttk.Label(main_window, text=h1.get_minuto)
#lblMinuto.grid(column=1, row=0, padx=5)
#lblSegundo = ttk.Label(main_window, text=h1.get_segundo)
#lblSegundo.grid(column=2, row=0, padx=5)

main_window = tk.Tk()
main_window.title('Relógio')
now = dt.now()
h1 = hora.Hora(now.hour, now.minute, now.second)
lblHora = ttk.Label(main_window, text=h1.__str__())
lblHora.grid(column=0, row=0, padx=5)

main_window.mainloop()