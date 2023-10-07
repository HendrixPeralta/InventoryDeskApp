import DB
import menu

#DB.delete_all_items()
#DB.create_db()

# Map user input to corresponding functions
options = {
    '1': menu.add_item,
    '2': menu.delete_item,
    '3': menu.add_quantity,
    '4': menu.subtract_quantity,
    '5': menu.edit_item,
    '6': menu.search_item,
    '7': menu.filter_by,
    '98': menu.delete_table_content,
    '99': menu.delete_database,
}

button = None

# Main menu loop
while button != '0':
    print(
        """
        1 = Add new item
        2 = Delete an item
        3 = Add quantity
        4 = Subtract quantity
        5 = *** Edit item ***
        6 = Search item 
        7 = Filter by ...
        ---------------------------
        98 = DELETE TABLE CONTENTS
        99 = *** Delete database ***
        0 = QUIT
        """
    )
    button = input("Enter your choice: ")

    # Get the corresponding action based on user input
    action = options.get(button)
    if action:
        print("button selected: ", button)
        print(options[button])
        action()

    elif button == '0':
        # Quit the program
        print("Quitting the program...")
        # Add any necessary cleanup or exit code here
    else:
        # Handle invalid input
        print("Invalid choice. Please enter a valid option.")

    print("Program exited.")


