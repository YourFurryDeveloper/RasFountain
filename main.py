import tkinter as tk
import tkinter.font as tkFont
import drinkMixer
import os

if os.name == "nt":
    print("WOMP WOMP >:3")
else:
    print("Go ahead! :3")
    os.system("sudo pigpiod")

drinkMixer.init()

root = tk.Tk()
root.title("The RasFountain")
root.geometry("800x480")

bgimage = tk.PhotoImage(file="bg.png")
bg = tk.Label(image=bgimage)
bg.place(x=0, y=0, relwidth=1, relheight=1)

mainFont = tkFont.Font(family="DejaVu Sans Mono", size=20, weight="bold")
btnFont = tkFont.Font(family="Carlito", size=20, weight="bold")


topbar = tk.Frame()
topbar.pack(padx=10, pady=10)

title = tk.Label(topbar, font=mainFont, text="The RasFountain", bg="#20a8bd")
title.grid(row=0, column=0)

mainContent = tk.Frame()
mainContent.pack(pady=25)

drinks = {
    "Water": [tk.PhotoImage(file="btnImgs/water.png"), "#002491"],
}

btns = 0
row = 0
for drinkName, btnAttribs in drinks.items():
    drinkBtn = tk.Button(mainContent, width=100, height=84, text=drinkName, font=btnFont, fg=btnAttribs[1], compound="center", image=btnAttribs[0], command=lambda: drinkMixer.mix(drinkName))
    drinkBtn.grid(row=row, column=btns, padx=5, pady=5)
    
    if not btns >= 5:
        btns += 1
    else:
        btns = 0
        row += 1

root.protocol("WM_DELETE_WINDOW", drinkMixer.stopPumpD)
root.mainloop()