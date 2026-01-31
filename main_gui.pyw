import tkinter
import tkinter.filedialog
import tkinter.ttk as TTK
import ParseSTDF_main as main

def BrowsePath():
	stdpath = tkinter.filedialog.askopenfilename()
	folder_path.set(stdpath)

def ParseData():
	main.parsing(pathEntry.get())

#Reference to mainwindow
mainwindow = tkinter.Tk()

#Rename the title of the window
mainwindow.title("J800 STDF Parser")

#set window size
mainwindow.geometry("500x250")

#Welcome Label in Main window
tkinter.Label(mainwindow, text = "J800 STDF Parser", font=("Arial Bold",25)).pack()

#Create path frame and label
pathframe = tkinter.Frame(mainwindow, width = 100, height = 50)
pathframe.pack()
tkinter.Label(pathframe, text = "Enter std file path", font=("Arial Bold", 12)).pack(side = 'left')

#Create path frame and entry and button for path
folder_path = tkinter.StringVar()
inputframe = tkinter.Frame(mainwindow, width = 100, height = 50)
inputframe.pack()
pathEntry = tkinter.Entry(inputframe, font = ('arial', '10'), width = 50, textvariable = folder_path)
pathEntry.grid(column = 1, padx = 4)
pathBt = tkinter.Button(inputframe, text=".....", command = BrowsePath)
pathBt.grid(column = 2, row = 0, padx = 4)

#Create parse frame and button
parseframe = tkinter.Frame(mainwindow, width = 100, height = 50)
parseframe.pack()
parseBt = tkinter.Button(parseframe, text = "PARSE DATA", font = ("Arial Bold", 15), width = 20, height = 1, bg = '#43B7C8', fg = 'white', command = ParseData)
parseBt.grid(pady = 4)

mainwindow.mainloop()
