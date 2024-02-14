import customtkinter
from CTkTable import *

def buildShipyard(self):
    shipyard_frame = customtkinter.CTkFrame(self, corner_radius=0)

    value = [["Name", "Type", "Location", "Mode",  "Mission"],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5]]

    shipTable = CTkTable(master=shipyard_frame, row=5, column=5, values=value, corner_radius=0)
    shipTable.pack(expand=True, fill="both", padx=20, pady=20)

    return shipyard_frame