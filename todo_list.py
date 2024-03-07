import csv

todos = []

#Add todos from file into todos list
with open("todo_list.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        todos.append({"Todo": row["Todo"], "Priority": row["Priority"], "Completed": row["Completed"]})

#Functions for sorting
def get_priority(todo):
    return todo["Priority"]
def get_completed(todo):
    return todo["Completed"]

#Function to all todos
def get_list(choice): 
 
    if not todos:
        print("\n")
        print("There are no tasks in your list")
    else:
        if int(choice) == 2:
            for index, todo in enumerate(sorted(todos, key=get_completed)):
                if todo['Completed'] == "False":
                    print(f"{index + 1}: {todo['Todo']}") 

        elif int(choice) == 3:
            for index, todo in enumerate(sorted(todos, key=get_priority, reverse=True)):
                if (todo['Priority'] == "True") and (todo['Completed'] == "False"):
                    print(f"{index + 1}: {todo['Todo']}") 

        elif int(choice) == 4:
            count = 0
            for index, todo in enumerate(sorted(todos, key=get_completed)):
                if todo['Completed'] == "False":
                    count += 1
                    print(f"{index + 1}: {todo['Todo']}") 
            print("\n")
            delete = input("Select the Todo you've completed: ")
            if (0 < int(delete) <= int(count)):
                for index, todo in enumerate(sorted(todos, key=get_completed)):
                    if (index + 1) == int(delete):
                        todo.update({"Priority":"False","Completed":"True"})
                        print("\n")
                        print(f"{todo['Todo']} has been completed!")
            else:
                print("\n")
                print("Invalid Choice")

        elif int(choice) == 5:
            for todo in todos:
                if todo['Completed'] == "True":
                    print(todo['Todo']) 
        else: 
            pass            

#Add todo
def add_todo():
    task = input("Add a new task: ")
    priority = set_priority()
    completed = "False"
    todos.append({"Todo": task, "Priority": priority, "Completed": completed})
    return task

#Set Priority
def set_priority():
    while True:
        priority_input = input("Is this a priority? (Y/N) ")
        try:
            if priority_input.upper() == "Y":
                priority = "True"
                return priority
            elif priority_input.upper() == "N":
                priority = "False"
                return priority
        except:
            pass

#Mark as completed
def set_completed(todo):
    ...

#Exit and update save file
def exit():
    with open("todo_list.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["Todo", "Priority", "Completed"])
        writer.writeheader()
        for todo in todos:
            task = todo['Todo']
            priority = todo['Priority']
            completed = todo['Completed']
            writer.writerow({"Todo": task, "Priority": priority, "Completed": completed})

#Interface
def main():
    while True:
        print("Welcome to your Todo list:")
        print("1. Add new Todo")
        print("2. View all your incomplete Todos")
        print("3. View all your priority incomplete Todos")
        print("4. Mark a Todo as completed")
        print("5. View all completed Todos")
        print("6. Exit")
        print("---------------------------")
        print("\n")
        choice = input("Please select an option (1,2,3,4,5 or 6): ").upper()
        try:
            if choice == "1":
                task = add_todo()
                print("\n")
                print(f"{task} was sucessfully added!")
                print("\n")
            elif choice == "2":
                print("\n")
                print("Current Todos:")
                get_list(choice)
                print("\n")
            elif choice == "3":
                print("\n")
                print("Priority Todos:")
                get_list(choice)
                print("\n")
            elif choice == "4":
                print("\n")
                get_list(choice)
                print("\n")
            elif choice == "5":
                print("\n")
                print("Completed Todos:")
                get_list(choice)
                print("\n")
            elif choice == "6":
                exit()
                print("\n")
                print("Goodbye!")
                print("\n")
                break
        except:
            print("Invalid choice")
    
if __name__ == "__main__":
    main()