# GUI imports
from Tkinter import Tk, Frame, BOTH, Checkbutton, Listbox,END
import tkFileDialog 
from ttk import Button, Style
import tkMessageBox as box
# Backend imports
from Queue import Queue
from threading import Thread
from queue import runPool
import ntpath


class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.files = []
        self.lb = None
        self.should_decompress = False
        self.initUI()
        self.update_idletasks()
    
    def initUI(self):
        ''' Create the UI '''
        # Name the window
        self.parent.title("oZip")
        self.pack(fill=BOTH, expand=1)
        
        # 'Add File' button
        addFileButton = Button(self, text="Add File",
            command=self.onOpen)
        addFileButton.place(x=225, y=30)
        
        # 'Go' button
        goButton = Button(self, text="Go",
            command=self.onClick)
        goButton.place(x=225, y=100)
        
        # 'Quit' button
        quitButton = Button(self, text="Quit",
            command=self.quit)
        quitButton.place(x=225, y=160)
        
        # Decompression checkbox
        self.cb = Checkbutton(self, text="Should decompress",
            command=self.checkboxClick)
        self.cb.place(x=20, y=195)
        
        # Selected files list
        lb = Listbox(self)
        self.lb = lb   
        lb.place(x=20, y=20)

    def checkboxClick(self):
        ''' Update the variable that stores the action that will be done on the files '''
        # Update the GUI
        self.cb.update_idletasks()
        # Update the backend
        self.should_decompress = not self.should_decompress

    def onClick(self):
        ''' 'Go' button pressed '''
        # Create a queue for any error messages that may rise
        err_q = Queue()
        # Run the processing on another thread and use the current thread to display errors if occured
        worker = Thread(target=runPool, args=(self.files, err_q, self.should_decompress))
        worker.setDaemon(True)
        worker.start()

        # Display error messages if needed
        while True:
            # Get the next error message
            var = err_q.get()
            # If it's a tuple, display the error from the tuple
            if isinstance(var, tuple):
                self.showError(var[0], var[1])
            # If it's a string it means that the processing is done
            elif isinstance(var, str):
                break
            # Remove the error from the queue
            err_q.task_done()
        # When all the files are done, inform the user
        box.showinfo("Done", 'Processing completed.')
        # Quit
        self.quit()

    def showError(self, filename, error_msg):
        ''' Show an error msg if needed '''
        box.showerror("Error on file %s" % filename, error_msg)

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
    root.geometry("350x225+300+300")
    app = MainWindow(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  