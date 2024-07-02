import tkinter
import FileHandler

class TaskManager:
    
    def __init__(self, window):
        self.frame_for_tasks = tkinter.Frame(window)
        saved_data = FileHandler.FileHandler().read_from_file()
        for line in saved_data:
            self.add_task(line)
    
    def get_current_tasks(self):
        current_tasks = []
        for inner_frame in self.frame_for_tasks.winfo_children():
            current_tasks.append(inner_frame.winfo_children()[1].get())
        return current_tasks
    
    def add_task(self, task_text):
        self.frame_for_tasks.pack(pady = 10)
        
        inner_frame = tkinter.Frame(self.frame_for_tasks)
        inner_frame.pack()
        
        checkButton = tkinter.Checkbutton(inner_frame, command=lambda:self.remove_task(inner_frame)) #adding a callback
        checkButton.pack(side=tkinter.LEFT)
        
        task_content = tkinter.Entry(inner_frame, font=20, width=30)
        task_content.insert(0,task_text)
        task_content.pack(side=tkinter.RIGHT)
        
    def remove_task(self, task_frame):
        task_frame.destroy()
        