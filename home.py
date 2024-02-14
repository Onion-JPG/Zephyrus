import customtkinter


def buildHomeFrame(self):
    home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

    home_frame_large_image_label = customtkinter.CTkLabel(home_frame, text="Test")
    home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

    home_frame_button_1 = customtkinter.CTkButton(home_frame, text="")
    home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)

    home_frame_button_2 = customtkinter.CTkButton(home_frame, text="CTkButton")
    home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)

    home_frame_button_3 = customtkinter.CTkButton(home_frame, text="CTkButton")
    home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)

    home_frame_button_4 = customtkinter.CTkButton(home_frame, text="CTkButton")
    home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

    return home_frame
