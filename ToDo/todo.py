print("Add your tasks or retrieve them as u want :D")
a=0
while a<3:
    print("Press 1 to add tast and 2 to retrieve tasks and 3 to leave")
    a=int(input())
    if a==1:
        task=input("Enter the task")
        with open("tasks.txt","a") as f:
            f.write(task+"\n")
    if a==2:
        with open("tasks.txt","r") as f:
            data=f.read()
            print(data)
