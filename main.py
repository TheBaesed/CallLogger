def show_menu():
    print("\nEPB Call Logger")
    print("---------------")
    print("1. Log a new call")
    print("2. View recent calls")
    print("3. Searh calls")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("Log a call - coming soon")
        elif choice == "2":
            print("View calls - coming soon")
        elif choice == "3":
            print("Search calls - coming soon")
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print ("Invalid choice, Try again")

main()
