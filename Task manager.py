# Task manager 
class Task :
    def __init__(self,title):
        self.title = title
        self.completed = False

    def toggle(self):
        self.completed = not self.completed

class TaskManager :
    def __init__(self):
        self.all_tasks = []

    def get_task_number(self):
        if self.all_tasks :
            while True:
                try:
                    task_number = int(input("enter the number of the task :"))
                    if 1 <= task_number <= len(self.all_tasks):
                        return task_number
                    else:
                        print("invalid input ,enter the number of the task 📛")
                except ValueError:
                    print("invalid input 📛 ,enter a number ")
        else :
            print("you don't have tasks yet ")
            return None

    def add_task(self):
        while True :
            task = input("enter your task (q to quit):")
            if task == "" :
                print("invalid input ,you need to enter something ")
            elif task.isdigit() :
                print("invalid input ,task can't be numbers")
            elif task=="q" or task=="Q" :
                break
            else :
                self.all_tasks.append(Task(task))

    def show_tasks(self):
        if self.all_tasks :
            print("\n---- your tasks ----")
            for index,task in enumerate(self.all_tasks , start=1) :
                statu = "✅" if task.completed else "❌"
                print(f"{index} - {task.title} {statu}")
            print("--------------------\n")
        else :
            print("you don't have tasks yet ")

    def mark_task_as_done(self,index):
        new_index = index -1
        self.all_tasks[new_index].toggle()

    def delete_task(self,index) :
        new_index = index -1
        task = self.all_tasks.pop(new_index)
        print(f"you successfully deleted task number '{index}:{task.title}'")

def main():
    my_task = TaskManager()
    is_running = True
    while is_running :
        print("----- Task Manager -----")
        print("1 - Add a task")
        print("2 - Show all tasks")
        print("3 - Mark a task as completed")
        print("4 - Delete a task ")
        print("5 - Exit")
        print("-------------------------")
        choice = input("enter your choice :")
        print("-------------------------")
        if choice == "1" :
            my_task.add_task()
        elif choice == "2" :
            my_task.show_tasks()
        elif choice == "3" :
            number_of_tasks = my_task.get_task_number()
            if number_of_tasks is not None :
                my_task.mark_task_as_done(number_of_tasks)
        elif choice == "4" :
            number_of_tasks = my_task.get_task_number()
            if number_of_tasks is not None :
                my_task.delete_task(number_of_tasks)
        elif choice == "5" :
            print("goodbye")
            is_running = False
        else :
            print("invalid input 📛")

if __name__ == '__main__':
    main()
