import customtkinter
import os
from PIL import Image
import mission_control

class Login(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Zephyrus.png")), size=(800, 200))

        logo_label = customtkinter.CTkLabel(master=self, text="", image=logo_image)
        logo_label.grid(row=0, column=0, padx=10, pady=12)

        self.tabview = customtkinter.CTkTabview(master=self, width=250, height=350)
        self.tabview.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.tabview.add("Saved Login")
        self.tabview.add("New Login")
        self.tabview.add("Create")
        self.tabview.set("New Login")

        self.tabview.tab("Saved Login").grid_columnconfigure(0, weight=1)  
        self.tabview.tab("New Login").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Create").grid_columnconfigure(0, weight=1)

        # Saved Login tab
        scrollable_frame = customtkinter.CTkScrollableFrame(master=self.tabview.tab("Saved Login"), width=775, height=290, fg_color="transparent")
        scrollable_frame.grid(row=0, column=0, padx=0, pady=0)

        # New Login tab
        label = customtkinter.CTkLabel(master=self.tabview.tab("New Login"), text="Login", font=("Roboto", 24))
        label.grid(row=1, column=0, padx=10, pady=12)
        self.callsign = customtkinter.CTkEntry(master=self.tabview.tab("New Login"), placeholder_text="Callsign")
        self.callsign.grid(row=2, column=0, padx=10, pady=12)
        self.API_key = customtkinter.CTkEntry(master=self.tabview.tab("New Login"), placeholder_text="API Key")
        self.API_key.grid(row=3, column=0, padx=10, pady=12)
        checkbox = customtkinter.CTkCheckBox(master=self.tabview.tab("New Login"), text="Remember Login")
        checkbox.grid(row=4, column=0, padx=10, pady=12)
        login_button = customtkinter.CTkButton(master=self.tabview.tab("New Login"), text="Login", command=self.loginButton)
        login_button.grid(row=5, column=0, padx=10, pady=12)

        # Create tab
        label = customtkinter.CTkLabel(master=self.tabview.tab("Create"), text="Login", font=("Roboto", 24))
        label.grid(row=1, column=0, padx=10, pady=12)
        self.callsign = customtkinter.CTkEntry(master=self.tabview.tab("Create"), placeholder_text="Choose A Callsign")
        self.callsign.grid(row=2, column=0, padx=10, pady=12)
        create_button = customtkinter.CTkButton(master=self.tabview.tab("Create"), text="Create Agent", command=self.createAgentButton)
        create_button.grid(row=3, column=0, padx=10, pady=12)

    def loginButton(self):
        print("Loging in")
        self.destroy()
        mission_control.MissionControl(self.master).pack(expand=True, fill="both")

    def createAgentButton(self):
        print("Creating Agent")
