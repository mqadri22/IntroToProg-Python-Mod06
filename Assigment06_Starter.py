# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# MQadri,8.15.2023,Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()                                            # clear current data
        file = open(file_name, "r")                                     # opens file file_name with read permissions
        for line in file:                                               # for each row in file_name
            task, priority = line.split(",")                            #   split the comma separated elements of current line into two strings
            row = {"Task": task.strip(), "Priority": priority.strip()}  #   create a dictionary object consisting of these two strings
            list_of_rows.append(row)                                    #   append the dictionary object to the list_of_rows list object
        file.close()                                                    # close the file once all lines are looped through
        return list_of_rows                                             # return the list_of_rows list object as an output

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want to add more data to:
        :return: (list) of dictionary rows
        """
        row = {"Task": str(task).strip(), "Priority": str(priority).strip()}    # create a dictionary object using the provided string parameters
        # TODO: Add Code Here!
        list_of_rows.append(row)                                                # append dictionary object to list_of_rows list parameter

        return list_of_rows                                                     # returns appended list parameter as an output

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes data from a list of dictionary rows

        :param task: (string) with name of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # TODO: Add Code Here!
        taskExistCheck = False                                                          # create a boolean to track whether the task to be removed was found
        for row in list_of_rows:                                                        # for each row in the list of tasks and priorities
            if row["Task"].strip().lower() == task.lower():                             #   check if the task to be removed matches the task in the current row
                list_of_rows.remove(row)                                                #       if it matches, then remove the current row
                taskExistCheck = True                                                   #       mark tracking boolean to true (task was found)

        if taskExistCheck:                                                              # if the task was found
            print("The task was successfully removed. Returning to option menu... ")    #   inform user
        else:                                                                           # if the task was not found
            print("Sorry, that task could not be found. Returning to option menu... ")  #   inform user

        return list_of_rows # return edited list of tasks and priorities as output

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # TODO: Add Code Here!
        saveSelection = str(input("Would you like to save this data? [y/n]: ")).strip().lower() # ask user if they'd like to save
        if saveSelection == "y":                                                                # if user elects to save
            objFile = open(file_name,"w")                                                       #   open file file_name with write permissions
            for row in list_of_rows:                                                            #   for each row in the list of tasks & priorities
                objFile.write(row["Task"]+","+row["Priority"]+"\n")                             #       write task and priority from current line to file
            objFile.close()                                                                     #   close file when loop completes
            print("The file was saved successfully. Returning to option menu...")               #   print empty line for looks
        elif saveSelection == "n":                                                              # if user elects not to save
            print("File was not saved. Returning to option menu... ")                           #   state so for clarity
        else:                                                                                   # if user provides invalid input
            print("Invalid input. Returning to option menu... ")                                #   state so for clarity

        return list_of_rows                                                                     # return list of task and priorities as output


# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        ''')     # displays a menu to the user
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()  # prompts user to make a selection from the menu
        print()         # Add an extra line for looks
        return choice   # returns user selection as output

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current tasks ToDo are: *******")    # displays descriptor for data about to be shown
        for row in list_of_rows:                                # for each row in the list of tasks and priorities
            print(row["Task"] + " (" + row["Priority"] + ")")   #   display task and priority in current row as printed, comma separated concatenated string
        print("*******************************************")    # display divider to readability
        print()                                                 # Add an extra line for looks

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        inputTask = str(input("Please enter a task: ")).strip()                                                          # prompt user for name of a task to add
        inputPriority = str(input("Please enter the priority for '"+inputTask.strip()+"' [high|medium|low]: ")).strip()  # prompt user for priority of input task
        return inputTask, inputPriority                                                                                  # return user provided task and priority as outputs

    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list

        :return: (string) with task
        """
        taskToRemove = str(input("Enter the name of the task you would like to remove: ")).strip()  # prompt user for the name of a task to remove
        return taskToRemove                                                                         # return user provided task name as output


# Main Body of Script  ------------------------------------------------------ #


# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file( file_name=file_name_str, list_of_rows=table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()                                   # Shows menu
    choice_str = IO.input_menu_choice()                      # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':                                                                       # Add a new Task
        task, priority = IO.input_new_task_and_priority()                                               # execute function to prompt user for new task and its priority, returning both
        table_lst = Processor.add_data_to_list(task=task, priority=priority, list_of_rows=table_lst)    # execute function to add new task and priority to list
        continue                                                                                        # to show the menu

    elif choice_str == '2':                                                             # Remove an existing Task
        task = IO.input_task_to_remove()                                                # execute function prompting user for a task to remove
        table_lst = Processor.remove_data_from_list(task=task, list_of_rows=table_lst)  # execute function removing user defined task from list
        continue                                                                        # to show the menu

    elif choice_str == '3':                                                                         # Save Data to File
        table_lst = Processor .write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)  # execute function to save list to file
        # print("Data Saved!")                                                                      # commented out for improved functionality
        continue                                                                                    # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")    # bid user farewell
        break                # by exiting loop
