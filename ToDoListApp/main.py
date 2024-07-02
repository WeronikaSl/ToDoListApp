import tkinter
import TaskManager


def main():
    window = tkinter.Tk()
    window.geometry("420x720")
    window.title("ToDoListApp")
    menu_bar = tkinter.Menu(window)
    window.config(background="#1D54B6", menu=menu_bar)
    
    label = tkinter.Label(window, text="Todo:", font=("Arial",30), fg="#1D54B6", relief=tkinter.SUNKEN, bd=10)
    label.pack()

    file_menu = tkinter.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Save")
    
    adding_menu = tkinter.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Add", menu=adding_menu)
    
    task_manager = TaskManager.TaskManager(window)
    
    adding_menu.add_command(label="New task", command=task_manager.add_task) #adding a callback
    
    window.mainloop()
    


if __name__ == "__main__":
    main()
