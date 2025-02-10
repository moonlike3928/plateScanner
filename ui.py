from tkinter import Tk, Label

root = Tk()
root.title("Plate Scanner")
lbl = Label(root, text="Waiting for Plates...", font=("Arial", 16))
lbl.pack()

def update_display(plate):
    lbl.config(text=f"Detected: {plate}")

root.mainloop()
