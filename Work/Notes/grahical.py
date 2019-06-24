import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self, text="Give me COFFFFFF!!!!", fg="green", command=self.say_hi)
        self.quit = tk.Button(self, text="QUIT", 
                                fg="red", 
                                command=self.master.destroy)
        self.hi_there.pack(side="right")                        
        self.quit.pack(side="left")

    def say_hi(self):
        print("NOM NOM NOM NOM !")


root = tk.Tk()
app = Application(master=root)
app.master.title("My great coffee program ")
app.master.minsize(500,200)
app.master.maxsize(1000,400)
app.mainloop()

 
