import Eye4AnEye
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image


class Main:
    def __init__(self):
        self.root = tk.Tk(className=" Eye4anEye")
        self.root.geometry("800x700")
        self.root.iconphoto(False,tk.PhotoImage(file = "icon.png"))


        self.text = tk.StringVar()
        self.image = Image.open("resized-icon.png")
        self.text.set("e.g C:/Users/User/Pictures/Saved Pictures/cataract.png")

        self.icon = ImageTk.PhotoImage(self.image)
        self.panel = tk.Label(self.root, image=self.icon, width=192,height=108)

        self.title = tk.Label(self.root, font=("Times", 50), text="Eye4AnEye")
        self.subtitle = tk.Label(self.root, font=("Courier", 20), text="A tool for asynchronous eye diagnosis")
        self.gap = tk.Label(self.root, font=("Times", 60), text=" ")
        self.label1 = tk.Label(self.root, font=("Helvetica", 30), text="Image Directory:")
        self.label2= tk.Label(self.root, font=("Helvetica", 22), textvariable=self.text)
        self.button1 = tk.Button(self.root, font=("Helvetica", 12) , text='Select File', width = 20, height= 2 ,command=self.print_path)

        self.button2 = tk.Button(self.root, font=("Helvetica", 12), text='Start', width=20, height=2, command=self.parser)
        self.CreateMsg = tk.Label(self.root, font=("Helvetica", 12), text="A file named results.csv has been created or edited in the current directory and is ready with the results")

        self.panel.pack()
        self.title.pack()
        self.subtitle.pack()
        self.gap.pack()
        self.label1.pack()
        self.label2.pack()

        self.button1.pack()
        self.button2.pack()
        self.root.mainloop()

    def print_path(self):
        self.f = tk.filedialog.askopenfilename(
            parent=self.root, initialdir='C:/',
            title='Choose file',
            filetypes=[('png images', '.png'), ('jpg image', '.jpg'),('jpeg images', '.jpeg')]
        )
        self.CreateMsg.pack_forget()
        self.text.set(self.f)
        print(self.text.get())
    def parser(self):
        self.CreateMsg.pack_forget()
        self.fa = "no file selected"
        handler = open("results.csv", "a+")
        self.newtext = self.text.get().split("/")
        print(self.newtext[-1])
        if self.text.get() == "" or self.text.get() == "e.g C:/Users/User/Pictures/Saved Pictures/cataract.png" :
            self.text.set(self.fa)
        else:
            myObj = Eye4AnEye.cataract(self.text.get())
            print(myObj.proc())
            if myObj.proc() <= 70:
                handler.write(self.newtext[-1] + ", " + str(myObj.proc()) + "%" + " | Insufficent evidence of cataract" + "\n")
                print("Insufficent evidence of cataract")

            else:
                handler.write(self.newtext[-1] + ", " + str(myObj.proc()) + "%" + " | Cataract detected" + "\n")
                print("Cataract detected")
            self.CreateMsg.pack()




app = Main()






