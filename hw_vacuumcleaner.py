
def left():
    print("The vacuum has turned to the left side\n")

def right():
    print("The vacuum has turned to the right side\n")

def dock():
    print("The vacuum is at rest\n")

def main():
    while True:
        print("""    1. Start
    2. Left
    3. Right
    4. Dock
    5. Stop""")
        
        choice = int(input("Choose the command to be instructed: "))
        if choice == 1:
            start()
        elif choice == 2:
            left()
        elif choice == 3:
            right()
        elif choice == 4:
            dock()
        elif choice == 5:
            print("The vacuum has stopped")
            break
        else:
            print("Invalid choice, please try again.")

main(
