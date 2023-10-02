import tkinter as tk

class PasswordManagerGUI:

    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.init_gui()

    def init_gui(self):
        # Frames
        self.input_frame = tk.Frame(self.master)
        self.output_frame = tk.Frame(self.master)
            
        # Input widgets
        self.website_label = tk.Label(self.input_frame, text="Website:")  
        self.website_entry = tk.Entry(self.input_frame)
        self.username_label = tk.Label(self.input_frame, text="Username:")
        self.username_entry = tk.Entry(self.input_frame)
        self.password_label = tk.Label(self.input_frame, text="Password:")
        self.password_entry = tk.Entry(self.input_frame, show="*")
        
        # Output widgets
        self.output_label = tk.Label(self.output_frame, text="Saved Passwords:")
        self.output_text = tk.Text(self.output_frame)
        
        # Input frame layout
        self.website_label.grid(row=0, column=0)
        self.website_entry.grid(row=0, column=1)
        
        self.username_label.grid(row=1, column=0)
        self.username_entry.grid(row=1, column=1)
        
        self.password_label.grid(row=2, column=0)  
        self.password_entry.grid(row=2, column=1)

        # Output frame layout
        self.output_label.grid(row=0, column=0)
        self.output_text.grid(row=1, column=0)
        
        # Frame packing 
        self.input_frame.pack()
        self.output_frame.pack()