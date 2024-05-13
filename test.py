import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Monster Cards")
        self.geometry(f"{300}x{400}")

root = tk.CTk()
root.geometry("300x400")

button = tk.CTkButton(root, text="test")
button.place(relx= 0.5, rely= 0.5, anchor=CENTER)

root.mainloop()





# card_name = input("Enter new card name: ")
# card_stats = input("Enter stats: ")
# stats_list = list(map(int, str(card_stats[0])))
# add_card(card_name, stats_list)
# return_cards()