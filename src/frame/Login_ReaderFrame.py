from tkinter import Tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

class Login_ReaderFrame:
    def __init__(self):
        root = Tk()

        #Setting the Title
        root.title("Library Management System")

        #Setting the icon
        root.iconbitmap('src\\picture\\library.ico')

        #Get the screen resolution
        x = root.winfo_screenwidth()
        y = root.winfo_screenheight()

        #Get the value for windows size
        x1 = x * (13/20)
        y1 = y * (0.81)

        #Get the value for Starting point for windows
        x2 = x * (1.1/6)
        y2 = y * (1/12)

        root.geometry("%dx%d+%d+%d" % (x1, y1, x2, y2))
        root.resizable(False, False)

        #Easy for configure within attribute
        x1 = int(x1)
        y1 = int(y1)

        x_nav = int(x1*0.3)
        y_nav = int(y1*0.8)

        style = ttk.Style()
        style.configure("Title.TFrame", foreground="black", background="brown1")
        style.configure("Content.TFrame", foreground="black", background="LightSkyBlue2")
        style.configure("Nav.TFrame",foreground="black", background="SeaGreen1")
        
        title_frame = ttk.Frame(root, style="Title.TFrame")
        title_frame.place(relwidth=1, relheight=0.2)

        content_frame = ttk.Frame(root, style="Content.TFrame")
        content_frame.place(relx=0.3,rely=0.2,relwidth=1,relheight=0.8)

        nav_frame = ttk.Frame(root, style="Nav.TFrame")
        nav_frame.place(rely=0.2,relwidth=0.3,relheight=0.8)
        
        #Resize the Image
        Nav_image = Image.open("src\\picture\\Nav.jpg")
        Nav_image = Nav_image.resize((x_nav, y_nav), Image.ANTIALIAS)
        Nav_image = ImageTk.PhotoImage(Nav_image)

        # (highlightthickness = 0) is for remove the border for the Canvas 
        Nav_label = Canvas(nav_frame, width=x_nav, height=y_nav, highlightthickness=0)
        Nav_label.pack()
        Nav_label.create_image(0, 0, anchor=NW, image=Nav_image)

        root.mainloop()

if __name__ == "__main__":
    frame = Login_ReaderFrame()
