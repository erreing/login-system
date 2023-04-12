import customtkinter as ctk
import json
import tkinter as tk
from time import sleep

print("###########################\nTHIS ZONE IS FOR DEBBUGGING\n###########################")

class MyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Widgets

        self.label = ctk.CTkLabel(self, font=("Arial", 32), text="Login System")
        self.label.grid(padx=235, pady=(50, 30))

        self.keyCheckerText = self.label = ctk.CTkLabel(self, text="", font=("Arial", 20))
        self.label.grid(padx=0, pady=(10, 20))

        self.keyInserBox = self.entry = ctk.CTkEntry(self, placeholder_text="Key here", width=190)
        self.entry.grid(padx=0, pady=0)

        self.button = ctk.CTkButton(master=self, command=self.login, text="Login", width=80)
        self.button.grid(padx=0, pady=50)

    def login(self):
        # Checker

        print(self.entry.get())
        with open("data.json", "r") as r:
            data = json.load(r)
            for item in data: # checker
                if item['key'] == self.entry.get(): # if valid
                    self.keyCheckerText.configure(text="Correct! Welcome.")
                    print("Correct! Welcome.")
                    self.keyInserBox.delete(0, tk.END)
                    self.after(1000, self.quit)

                elif self.entry.get() == "": # if no given key
                    self.keyCheckerText.configure(text="No given key.")
                    print("No given key.")

                else:
                    self.keyCheckerText.configure(text="Incorrect key. Make sure you don't put spaces.")
                    print("Incorrect key.")
                    self.keyInserBox.delete(0, tk.END)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Appearance

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Window {geometry, center calc}

        window_x = int((App.winfo_screenwidth(self) - 700) / 2)
        window_y = int((App.winfo_screenheight(self) - 400) / 2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.geometry(f"700x400+{window_x}+{window_y}")
        self.title("Key Test")
        self.resizable(False, False)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


if __name__ == "__main__":
    try:
        app = App()
        app.mainloop()
    except KeyboardInterrupt:
        print("Canceled by user.")
