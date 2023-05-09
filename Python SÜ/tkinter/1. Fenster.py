#erstelle ein fenster für tkinter
from tkinter import *


root = Tk()
root.title("KiddoBot")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg="black")

#zeige das fenster an
root.mainloop()