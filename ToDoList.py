def create() :
    print("Create your To-Do List ",end="\n")
    print("Enter tasks(Seperated by commas) : ",end="")
    To_Do_List=[task.upper() for task in input().split(",")]
    return To_Do_List
def update(To_Do_List,response):
    if response.upper()=="ADD" :
        print("Enter your new task : ",end="")
        To_Do_List.append(input().upper())
        print("Update To-Do List : ",end="\n")
        display(To_Do_List)
    elif response.upper()=="DEL" :
        print("Enter the task name for deletion : ",end="")
        task_del=input().upper()
        To_Do_List.remove(task_del)
    else :
        print("Invalid input. Input should be add or del")

def display(To_Do_List) :
    for i in To_Do_List:
        print(i)


To_Do_List=create()
while 1 :
    print("Do you wanna update To-Do List(Yes/No) : ", end="")
    response = input()
    if response.upper()=="YES" :
        print("Add or Delete a task (add/del) : ",end="")
        upt=input()
        update(To_Do_List,upt)
    elif response.upper()=="NO" :
        print("Your left over To-Do List taks : ")
        display(To_Do_List)
        break
    else :
        print("Invalid input. Input should be yes or no")