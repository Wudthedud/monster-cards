from tkinter import *
import customtkinter as tk

tk.set_appearance_mode("system")

root = tk.CTk()
root.geometry("300x400")

button = tk.CTkButton(root, text="test")
button.place(relx= 0.5, rely= 0.5, anchor=CENTER)

root.mainloop()
