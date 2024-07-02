import tkinter

def addTask():
    print("Task added!")

def main():
    window = tkinter.Tk()
    window.geometry("420x720")
    window.title("ToDoListApp")
    menuBar = tkinter.Menu(window)
    window.config(background="#1D54B6", menu=menuBar)
    label = tkinter.Label(window, text="Todo for today:", font=("Arial",40), fg="#1D54B6", relief=tkinter.SUNKEN, bd=10)
    label.grid(row=0, column=5)
    entry1 = tkinter.Entry(window, font=20)
    entry1.insert(0,"Add new task...")
    entry1.grid(row=3, column=2)
    entry2 = tkinter.Entry(window, font=20)
    entry2.insert(0,"Add new task...")
    entry2.grid(row=6, column=2)
    checkButton1 = tkinter.Checkbutton(window)
    checkButton1.grid(row=3, column=0)
    checkButton2 = tkinter.Checkbutton(window)
    checkButton2.grid(row=6, column=0)
    fileMenu = tkinter.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="Save")
    addMenu = tkinter.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Add", menu=addMenu)
    addMenu.add_command(label="New task", command=addTask)
    window.mainloop()
    


if __name__ == "__main__":
    main()
