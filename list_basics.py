tasks = []
while True:
    print("\n--- To-do List Menu---")
    print("1. Add a tasks")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("\nChoose an option (1-4):")
    if choice == "1":
        task = input("Enter the task to add: ")
        tasks.append(task)
        print("Task'"+ task + "'added!")
    elif choice == "2":
        for i in tasks:
            print(i)
    elif choice == "3":
        task = input("enter the name of task u want remove: ")
        tasks.remove(task)
        print("Task'"+ task + "'removed!") 
    elif choice == "4":
        print("Thank u For using This app")
        break
        


    
