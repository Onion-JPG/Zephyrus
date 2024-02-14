import customtkinter
import login

class Zephyrus(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Zephyrus")
        self.geometry("1400x800")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        login.Login(self).grid(row=0, column=0, padx=10, pady=10)

# Configuring the theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = Zephyrus()
root.mainloop()