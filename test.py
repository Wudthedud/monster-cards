from tkinter import *
import customtkinter as tk

tk.set_appearance_mode("system")

root = tk.CTk()
root.geometry("300x400")

button = tk.CTkButton(root, text="test")
button.place(relx= 0.5, rely= 0.5, anchor=CENTER)

root.mainloop()

card_name = input("Enter new card name: ")
card_stats = input("Enter stats: ")
stats_list = list(map(int, str(card_stats[0])))
add_card(card_name, stats_list)
return_cards()