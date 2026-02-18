from calls import log_call, view_recent_calls, search_calls, view_call_detail

def show_menu():
    print("\nEPB Call Logger")
    print("---------------")
    print("1. Log a new call")
    print("2. View recent calls")
    print("3. Search calls")
    print("4. View full call detail")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            log_call()
        elif choice == "2":
            view_recent_calls()
        elif choice == "3":
            search_calls()
        elif choice == "4":
            view_call_detail()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print ("Invalid choice, Try again")

main()
