import os
from colorama import init, Fore, Style
from pyfiglet import Figlet
import json

init(autoreset=True)

banner = Figlet(font='slant', justify='center')

to_do_list = {

}

def add_task():
    os.system('cls' if os.name == 'nt' else 'clear')
    task = input(Fore.WHITE + "Description : ")
    to_do_list[task] = "not done yet"
    print(Fore.GREEN + "Task Added!")
    print()

def view_task():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + Style.BRIGHT + banner.renderText("To Do List"))
    count = 1
    for task,status in to_do_list.items():
        if status == "not done yet":
            print("❌ "+ Fore.BLUE + str(count) + ". " + Fore.WHITE + task)
        else:
            print("✅ " + Fore.BLUE + str(count) + ". " + Fore.WHITE + task)
        count += 1
        
    print()

def mark_task():
    view_task()
    while True :
        try:
            n = int(input("Enter task number to mark as complete: "))
            task = list(to_do_list.keys())[n-1]
            to_do_list[task] = "done"
            print(Fore.GREEN + "Task marked as complete!")
            print()
            break
        except Exception:
            print(Fore.RED + "Invalid Value! ")
        
def remove_task():
    view_task()
    while True:
        try:
            n = int(input("Enter task number to remove : "))
            task = list(to_do_list.keys())[n-1]
            del to_do_list[task]
            print("Task removed!")
            print()
            break
        except Exception:
            print(Fore.RED + "Invalid Value! ")

def save():
    name = input("File Name : ")
    with open(name + ".json", "w", encoding="utf-8") as file:
        json.dump(to_do_list, file, indent=4)
    print("File Path : " + os.getcwd())

def load():
    while(True):
        try:
            name = input("File name : ")
            with open(name + ".json", "r", encoding="utf-8") as file:
                to_do_list.clear()
                to_do_list.update(json.load(file))
                view_task()
                break
        except FileNotFoundError:
         print("File not found!")

def main():
    while True:
        print(Fore.BLUE + "1. "+Fore.YELLOW + "Add " + Fore.WHITE + "Task")
        print(Fore.BLUE + "2. "+Fore.YELLOW + "View " + Fore.WHITE + "Task")
        print(Fore.BLUE + "3. "+Fore.YELLOW + "Mark " + Fore.WHITE + "Task")
        print(Fore.BLUE + "4. "+Fore.YELLOW + "Remove " + Fore.WHITE + "Task")
        print(Fore.BLUE + "5. "+Fore.YELLOW + "Save " + Fore.WHITE + "File")
        print(Fore.BLUE + "6. "+Fore.YELLOW + "Load " + Fore.WHITE + "File")
        print(Fore.BLUE + "7. "+Fore.YELLOW + "Exit")
        option = input("Choose an option : ")
        if(option == "1"):
            add_task()
        elif(option == "2"):
            view_task()
        elif(option == "3"):
            mark_task()
        elif(option == "4"):
            remove_task()
        elif(option == "5"):
            save()
        elif(option == "6"):
            load()
        elif(option == "7"):
            break
        else:
            print("Invalid Input!")

main()
