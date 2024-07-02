import tkinter

class TaskManager:
    
    def __init__(self, window):
        self.frame_for_tasks = tkinter.Frame(window)
        
    def add_task(self):
        self.frame_for_tasks.pack(pady = 10)
        
        part_of_frame = tkinter.Frame(self.frame_for_tasks)
        part_of_frame.pack()
        
        task_content = tkinter.Entry(part_of_frame, font=20, width=30)
        task_content.insert(0,"New task...")
        task_content.pack(side=tkinter.RIGHT)
    
        checkButton = tkinter.Checkbutton(part_of_frame, command=lambda:self.remove_task(part_of_frame)) #adding a callback
        checkButton.pack(side=tkinter.LEFT)
    
    def remove_task(self, task_frame):
        task_frame.destroy()
        