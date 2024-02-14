import customtkinter

import home
import shipyard

class MissionControl(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(2, weight=1)

        # create info frame
        self.info_frame = customtkinter.CTkFrame(self, width=800, height=100, corner_radius=0)
        self.info_frame.grid(row=0, column=0,columnspan=4, sticky="new")

        self.info_frame_label = customtkinter.CTkLabel(self.info_frame, text="Credits: XXX,XXX", font=("Roboto Bold", 15))
        self.info_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.info_frame_label = customtkinter.CTkLabel(self.info_frame, text="Net Worth: XXX,XXX", font=("Roboto Bold", 15))
        self.info_frame_label.grid(row=0, column=1, padx=20, pady=20)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0, height=700)
        self.navigation_frame.grid(row=1, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Navigation", font=("Roboto Bold", 30))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=60, border_spacing=10, text="Home", font=("Roboto", 20),
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.shipyard_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=60, border_spacing=10, text="Shipyard", font=("Roboto", 20),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.shipyard_button_event)
        self.shipyard_button.grid(row=2, column=0, sticky="ew")

        self.planet_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=60, border_spacing=10, text="Planets", font=("Roboto", 20),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.planet_button_event)
        self.planet_button.grid(row=3, column=0, sticky="ew")

        self.trade_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=60, border_spacing=10, text="Trades", font=("Roboto", 20),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.trade_button_event)
        self.trade_button.grid(row=4, column=0, sticky="ew")

        self.info_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=60, border_spacing=10, text="Info", font=("Roboto", 20),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.info_button_event)
        self.info_button.grid(row=5, column=0, sticky="ew")

        # create home frame
        self.home_frame = home.buildHomeFrame(self)

        # create shipyard frame
        self.shipyard_frame = shipyard.buildShipyard(self)

        # create planet frame
        self.planet_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create trade frame
        self.trade_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create info frame
        self.info_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.shipyard_button.configure(fg_color=("gray75", "gray25") if name == "shipyard_frame" else "transparent")
        self.planet_button.configure(fg_color=("gray75", "gray25") if name == "planet_frame" else "transparent")
        self.trade_button.configure(fg_color=("gray75", "gray25") if name == "trade_frame" else "transparent")
        self.info_button.configure(fg_color=("gray75", "gray25") if name == "info_frame" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=1, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

        if name == "shipyard_frame":
            self.shipyard_frame.grid(row=1, column=1, sticky="nsew")
        else:
            self.shipyard_frame.grid_forget()

        if name == "planet_frame":
            self.planet_frame.grid(row=1, column=1, sticky="nsew")
        else:
            self.planet_frame.grid_forget()

        if name == "trade_frame":
            self.trade_frame.grid(row=1, column=1, sticky="nsew")
        else:
            self.trade_frame.grid_forget()

        if name == "info_frame":
            self.info_frame.grid(row=1, column=1, sticky="nsew")
        else:
            self.info_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def shipyard_button_event(self):
        self.select_frame_by_name("shipyard_frame")

    def planet_button_event(self):
        self.select_frame_by_name("planet_frame")

    def trade_button_event(self):
        self.select_frame_by_name("trade_frame")

    def info_button_event(self):
        self.select_frame_by_name("info_frame")