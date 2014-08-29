# GUI imports
from Tkinter import Tk, Frame, BOTH, Checkbutton, IntVar, Listbox,END
import tkFileDialog 
from ttk import Button, Style
import tkMessageBox as box
# Backend imports
from queue import runPool
import ntpath


class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.files = []
        self.lb = None
        self.initUI()
    
    def initUI(self):
        ''' Create the UI '''
        # Name the window
        self.parent.title("oZip")
        self.pack(fill=BOTH, expand=1)
        
        # 'Add File' button
        addFileButton = Button(self, text="Add File",
            command=self.onOpen)
        addFileButton.place(x=250, y=50)
        
        # 'Go' button
        goButton = Button(self, text="Go",
            command=self.onClick)
        goButton.place(x=250, y=210)
        
        # 'Quit' button
        quitButton = Button(self, text="Quit",
            command=self.quit)
        quitButton.place(x=10, y=210)
        
        # Decompression checkbox
        self.should_decompress = IntVar()
        cb = Checkbutton(self, text="Should decompress",
            variable=self.should_decompress)
        cb.place(x=200, y=175)
        
        # Selected files list
        lb = Listbox(self)
        self.lb = lb   
        lb.place(x=20, y=20)

    def onClick(self):
        ''' 'Go' button pressed '''
        # TODO: Display an error message
        # Run the pool
        runPool(self.files, bool(self.should_decompress))
        # Show a message box
        msg = 'Processing completed.'
        box.showinfo("Done", msg)
        # Quit
        self.quit()

    def onOpen(self):
        ''' 'Add File' button was clicked '''
        # Get a tuple with the user's selected files
        selected_files = tkFileDialog.askopenfilenames()
        for path in selected_files:
            # Append the selected files to the list and to the list view (filename only in the GUI, path in backend)
            self.files.append(path)
            self.lb.insert(END, ntpath.split(path)[-1])
            # Update the GUI
            self.lb.update_idletasks()

def main():
    ''' Main GUI Function '''
    root = Tk()
    root.geometry("350x250+300+300")
    app = MainWindow(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  