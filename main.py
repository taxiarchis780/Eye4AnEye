import Eye4AnEye #import our pixel identifier
import tkinter as tk #gui library
from tkinter.filedialog import askopenfilename #file selection window
from PIL import ImageTk, Image #manage the logo in the app


class Main:
    def __init__(self):
        self.root = tk.Tk(className=" Eye4anEye") #instatiate our app
        self.root.geometry("800x700") #set it's borders
        self.root.iconphoto(False,tk.PhotoImage(file = "icon.png")) #misc decorations (this is the header icon)


        self.text = tk.StringVar() # it is used to update a label later
        self.image = Image.open("resized-icon.png") #load the eye logo for in app use
        self.text.set("e.g C:/Users/User/Pictures/Saved Pictures/cataract.png") # set a draft example of what a file directory might look like

        self.icon = ImageTk.PhotoImage(self.image) #make our image a PhotoImage object
        self.panel = tk.Label(self.root, image=self.icon, width=192,height=108) #make a container for our image

        #format for the following line of code:
        # {varName} = {type of element e.g Label or Button} ( parent, font=("FontName", size), text="message")

        self.title = tk.Label(self.root, font=("Times", 50), text="Eye4AnEye")
        self.subtitle = tk.Label(self.root, font=("Courier", 20), text="A tool for asynchronous eye diagnosis")
        self.gap = tk.Label(self.root, font=("Times", 60), text=" ")
        self.label1 = tk.Label(self.root, font=("Helvetica", 30), text="Image Directory:")
        self.label2= tk.Label(self.root, font=("Helvetica", 22), textvariable=self.text)
        self.button1 = tk.Button(self.root, font=("Helvetica", 12) , text='Select File', width = 20, height= 2 ,command=self.print_path) #when this button is pressed it called the function print_path

        self.button2 = tk.Button(self.root, font=("Helvetica", 12), text='Start', width=20, height=2, command=self.parser)#when pressed it calls the function parser
        self.CreateMsg = tk.Label(self.root, font=("Helvetica", 12), text="A file named results.csv has been created or edited in the current directory and is ready with the results") # is going to be displayed after our algorithm is done processing the image

        #Load all of the previous elements in our app
        self.panel.pack()
        self.title.pack()
        self.subtitle.pack()
        self.gap.pack()
        self.label1.pack()
        self.label2.pack()

        self.button1.pack()
        self.button2.pack()
        self.root.mainloop() #start the window's main loop

    def print_path(self):
        self.f = tk.filedialog.askopenfilename( #initialise the file selection window
            parent=self.root, initialdir='C:/', #starting from the root of our C: drive
            title='Choose file',# with the title "choose file"
            filetypes=[('png images', '.png'), ('jpg image', '.jpg'),('jpeg images', '.jpeg'), ('jfif images', '.jfif')] #all the supported and allowed file formats
        )
        self.CreateMsg.pack_forget() #make CreateMsg disapear
        self.text.set(self.f) #set label2 to the selected firectory
        #print(self.text.get()) //ignore
    def parser(self):
        self.CreateMsg.pack_forget() #make CreateMsg disapear
        self.fa = "no file selected" #create the no file selected message
        handler = open("results.csv", "a+") #load our output file
        self.newtext = self.text.get().split("/") #split the text with the delimiter "/" and assign the split parts into an array
        #print(self.newtext[-1]) //ignore
        if self.text.get() == "" or self.text.get() == "e.g C:/Users/User/Pictures/Saved Pictures/cataract.png": #check if no file is selected
            self.text.set(self.fa) #and display the warning message
        else:
            myObj = Eye4AnEye.cataract(self.text.get()) #call the cataract function with the file directory as input
            myObj2 = Eye4AnEye.BloodInChamber(self.text.get())
            print(myObj2.BDetector())
            if myObj.CDetector() <= 70: #70 is the threshold
                handler.write(self.newtext[-1] + ", " + str(myObj.CDetector()) + "%" + " | Insufficent evidence of cataract" + ", " ) # write the first part starting from the name fo the file the ‰ and the more readable result
                if myObj2.BDetector() <= 200: # write to the file the second part
                    handler.write(str(myObj2.BDetector()) + "%" + " | Insufficent evidence of blood presense" "\n")
                else: # --"-- if the ‰ is bigger than the threshold
                    handler.write(str(myObj2.BDetector()) + "%" + " | Blood detected" "\n")

                #print("Insufficent evidence of cataract") //ignore

            elif myObj2.BDetector() > 200:
                if myObj.CDetector() > 70:
                    handler.write(self.newtext[-1] + ", " + str(myObj.CDetector()) + "%" + " | Cataract detected" + ", " + str(myObj2.BDetector()) + "%" + " | Possible blood presense" "\n")
                else:
                    handler.write(self.newtext[-1] + ", " + str(myObj.CDetector()) + "%" + " | Insufficent evidence of cataract" + ", "+ str(myObj2.BDetector()) + "%" + " | Possible blood presense" "\n")
            self.CreateMsg.pack()




app = Main() #start our app






