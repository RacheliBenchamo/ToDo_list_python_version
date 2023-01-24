from tkinter.font import Font
from tkinter import *
from tkinter import filedialog
import pickle


class ToDoList:
    def __init__(self):

        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("My ToDo List")

        self.myFont = Font(family='Arial', size=18, weight="bold")

        self.myFrame = Frame(self.root)
        self.myFrame.pack(pady=20)

        # create a menubar
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        # create file menu
        self.fileMenu = Menu(self.menubar, tearoff=0)
        self.fileMenu.add_command(label="Save", command=self.save_list)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Open List", command=self.open_list)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Clear List", command=self.clear_list)
        # adding file menu to the menubar
        self.menubar.add_cascade(label="File", menu=self.fileMenu)

        # create a list
        self.myList = Listbox(
            self.myFrame,
            font=self.myFont,
            width=30, height=5,
            bg="SystemButtonFace",
            bd=0,
            fg="#464646",
            highlightthickness=0,
            selectbackground="#C1C1FF",
            activestyle="none"
        )
        self.myList.pack(side=LEFT, fill=BOTH)

        # Create scrollbar
        self.myScrollbar = Scrollbar(self.myFrame)
        self.myScrollbar.pack(side=RIGHT, fill=BOTH)

        # Add scrollbar
        self.myList.config(yscrollcommand=self.myScrollbar.set)
        self.myScrollbar.config(command=self.myList.yview)

        # create text box to add items to the list
        self.myEntry = Entry(self.root, font=("Helvetica", 24), width=26)
        self.myEntry.pack(pady=20)

        # Create a buttons frame
        self.myButtonsFrame = Frame(self.root)
        self.myButtonsFrame.pack(pady=20)

        # Create a buttons
        self.deleteButton = Button(self.myButtonsFrame, text="Delete task", command=self.delete_task)
        self.addButton = Button(self.myButtonsFrame, text="Add task", command=self.add_task)
        self.crossOffButton = Button(self.myButtonsFrame, text="cross off task", command=self.cross_off_task)
        self.uncrossButton = Button(self.myButtonsFrame, text="uncross task", command=self.uncross_task)
        self.delCrossedButton = Button(self.myButtonsFrame, text="delete crossed task", command=self.delete_crossed_task)

        # create grid for the buttons
        self.addButton.grid(row=0, column=0)
        self.deleteButton.grid(row=0, column=1, padx=20)
        self.crossOffButton.grid(row=0, column=2)
        self.uncrossButton.grid(row=0, column=3, padx=20)
        self.delCrossedButton.grid(row=0, column=4)

        # activate the screen
        self.root.mainloop()

    # Buttons functions
    def delete_task(self):
        self.myList.delete(ANCHOR)

    def add_task(self):
        self.myList.insert(END, self.myEntry.get())
        self.myEntry.delete(0, END)

    def cross_off_task(self):
        self.myList.itemconfig(self.myList.curselection(), fg="#dedede")
        # cancel selection bar
        self.myList.selection_clear(0, END)

    def uncross_task(self):
        self.myList.itemconfig(self.myList.curselection(), fg="#464646")
        # cancel selection bar
        self.myList.selection_clear(0, END)

    def delete_crossed_task(self):
        i = 0
        while i < self.myList.size():
            if self.myList.itemcget(i, "fg") == "#dedede":
                self.myList.delete(self.myList.index(i))
            else:
                i += 1

    # menu functions
    def save_list(self):
        file_name = filedialog.asksaveasfilename(
            initialdir="C:/gui/data",
            title="Save File",
            filetypes=(("Dat Files", "*.dat"),
                       ("All Files", "*.*")))
        if file_name:
            if file_name.endswith(".dat"):
                pass
            else:
                file_name = f'{file_name}.dat'

        # delete crossed item before saving
        self.delete_crossed_task()

        # open the output file and write the list to it
        output_file = open(file_name, 'wb')
        pickle.dump(self.myList.get(0, END), output_file)

    def open_list(self):
        file_name = filedialog.askopenfilename(
            initialdir="C:/gui/data",
            title="Open File",
            filetypes=(("Dat Files", "*.dat"),
                       ("All Files", "*.*")))

        # clear the current list
        self.clear_list()

        # open the output file and write the list to it
        input_file = open(file_name, 'rb')

        list1 = pickle.load(input_file)
        for item in list1:
            self.myList.insert(END, item)

    def clear_list(self):
        self.myList.delete(0, END)




