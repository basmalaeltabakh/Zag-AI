# List contains admins
admins = ["Basmala", "Tahany", "Tasnim", "Aml", "Abdelrahman"]

# Login
name = input("Please Enter Your name: ").strip().capitalize()

if name in admins:
    print(f"Hello {name}, Welcome Back.")
    option = input("Delete (d) or Update (u) Your name? ").strip().lower()
    
    # Update option
    if option == 'update' or option == 'u':
        new_name = input("Enter your new name: ").strip().capitalize()
        admins[admins.index(name)] = new_name  # Update the name
        print("Name Updated.")
        print("New Admins List:")
        print(admins)
    
    # Delete Option
    elif option == 'delete' or option == 'd':
        admins.remove(name) # Remove the name
        print("Name Deleted.")
        print("New Admins List:")
        print(admins)
    
    else:
        print("Wrong Option Chosen.")
else:
    status = input("You are not Admin. Add you Yes (y) or No (n)? ").strip().lower()
    if status == 'yes' or status == 'y':
        admins.append(name)  # Add the name
        print("You have been Added.")
        print("New Admins List:")
        print(admins)
    else:
        print("You have not been Added.")
