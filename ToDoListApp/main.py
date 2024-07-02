import tkinter
import TaskManager
import FileHandler


def main():
    window = tkinter.Tk()
    window.geometry("420x720")
    window.title("ToDoListApp")
    menu_bar = tkinter.Menu(window)
    window.config(background="#1D54B6", menu=menu_bar)
    
    label = tkinter.Label(window, text="Todo:", font=("Arial",30), fg="#1D54B6", relief=tkinter.SUNKEN, bd=10)
    label.pack()
    
    task_manager = TaskManager.TaskManager(window)

    file_menu = tkinter.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Save", command=lambda: FileHandler.write_to_file(task_manager.get_current_tasks()))
    
    adding_menu = tkinter.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Add", menu=adding_menu)
    
    adding_menu.add_command(label="New task", command=lambda: task_manager.add_task("New task...")) #adding a callback
    
    window.mainloop()
    


if __name__ == "__main__":
    main()
