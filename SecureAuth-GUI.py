#Class: CPS106 Section 1
#Prof Name: Dr. Preeti Raman
#Name: Talal Malhi 
#Final Date: 29-11-2023
#Worth:  20% of finals


#--------------------------------------------------------------------------------------------------------------------
#                                                       Question
#---------------------------------------------------------------------------------------------------------------------

#Suppose that you've been assigned the responsibility of developing an authentication system for TMU's biggest project ever called "Student SecureAuth."
#However, theres just one problem, it utilizes the Tkinter package in Python. You, despite being new to Tkinter, need to complete this by November 24th hard deadline! 
#Your objective is to gain the knowledge to create the perfect authenticator from scratch. 
#How would you approach learning and implementing Tkinter for this specific purpose, considering Dr. Raman's previous use of the package?


#--------------------------------------------------------------------------------------------------------------------
#                                                       Sources + Important Notes
#---------------------------------------------------------------------------------------------------------------------

#Source: https://docs.python.org/3/library/tkinter.html
#The figma design I made for this project: 
#Login Page: https://www.figma.com/file/0tS3r3UPojCJCHdkNrsC2d/Untitled?type=design&node-id=0%3A1&mode=design&t=WaLLIzc3BmwQeDU4-1
#Resiger Page: https://www.figma.com/file/uReolZoYmdnfG1HFDqrus1/Untitled?type=design&node-id=1%3A2&mode=design&t=OK39Q7HPoZQtGzv9-1
#Home Page: 

#--------------------------------------------------------------------------------------------------------------------
#                                   Purpose of all the tkinter functions used in this project
#---------------------------------------------------------------------------------------------------------------------

#Tkinter is a GUI (Graphical User Interface) library used for desktop applications
#Label: Used to display text or images, and has a similar function to a print statement
#Button: Works under a function to display clickable buttons that trigger its command depending what the function assigns it to do
#Entry: Widget for users to enter text or numerical inputs 
#Scrollbar: Provides a more efficient way to navigate through throughout the GUI which may be larger than the visible area
#Regx: Used for matching and manipulation of strings (in my case I used it to get a realistic email from the user)
#Optionmenu: Used as a dropdown menu which allows the user to select from a list of options presented
#StringVar: A variable type in Tkinter (or GUI) which is linked to widget attributes, this can be Entrys or Labels
#DoubleVar: A variable designed for handling floating or numerical values, just like StringVar
#Messagebox: Built in module that provides a way to display various types of pop up box messages, such as alerts or successful
#PIL: Similar role to PhotoImage, expect you can resize images and modify it unlike PhotoImage (Not built for tkinter)
#PhotoImage: Similar to PTL, expect its built in tkinter, and is very limited in options

#--------------------------------------------------------------------------------------------------------------------
#                                   Types of displays 
#---------------------------------------------------------------------------------------------------------------------

#The purpose of .pack(): Declares a default position of the widgets in the GUI 
#The purpose of .place(): Allows the coder to place a widget throughout the GUI by using a x and y axis (more flexible then grid())
#The purpose of .grid(): Declared when the coder wanted to locate widgets in a 2 dimensional grid with the power of row and column (the difference in place and grid is that grid is absolute coordinates)
#The purpose of .mainloop(): Similar to functions, this tells Python to run the tkinter code, just like calling a function

#--------------------------------------------------------------------------------------------------------------------
#                                   Imports
#---------------------------------------------------------------------------------------------------------------------

import tkinter
from tkinter import ttk
import re
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import messagebox
from tkinter import OptionMenu
from tkinter import DoubleVar
from tkinter import StringVar
import random
from PIL import Image, ImageTk

#--------------------------------------------------------------------------------------------------------------------
#                                  Install the packages
#---------------------------------------------------------------------------------------------------------------------

#pip install tkinter
#pip install pillow
#pip install messagebox

name = "Talal Malhi"

print(f"Before we start! Welcome To Authentication Page By {name} \n")

#--------------------------------------------------------------------------------------------------------------------
#                                   Age Checker
#---------------------------------------------------------------------------------------------------------------------

while True:
    #Sets age number 
    age_num = 17
    #Asking user for their age, only allows a int value (cuz age can't be a float)
    age = int(input("Lets start off by asking you a few questions? What is your age?: "))
    #If the age is < then 17 then user is given the following message and the program exists 
    if age < age_num:
        print("Unfortunately, this app is only for University students\n")
        print("Thank you for trying it!\n")
        exit()
    #If the age is >= to 17 then the user is greeted with the following message and breaks the while loop
    elif age >= age_num:
        print("Great! Lets get you started up\n")
        break
    #If user adds anything other then a int value then the while loop repeats until they enter there age in a int
    else:
        print("Invaild\n")

#--------------------------------------------------------------------------------------------------------------------
#                                   Bot Checker
#---------------------------------------------------------------------------------------------------------------------

#Function name set to human_or_bot
def human_or_bot():
    #Variables
    max_attempts = 3
    attempts = 0
    #Generates 3 random numbers 
    num_1 = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    num_2 = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    num_3 = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    #Adds the 3 random
    random_num = num_1 + num_2 + num_3

    #Using the built-int-input() function to display the 3 random numbers, and allow the user to input what the end value is
    adding_values = int(input(f"When you add {num_1} + {num_2} + {num_3} together, what do you get?: "))

    # If statement that checks if the random number is equal to adding_values
    if random_num == adding_values:
        print(f'Nice, {random_num} is the correct answer!')
    else:
        # If user is incorrect, it prints the following calls the human_or_bot function again
        print("No, you're wrong")
        human_or_bot()
        return  

    
    bot_checker_2 = input(f"\n Now that you know the answer is {random_num}, would it be even or odd?: ").lower()
    # While loop with a condition which loops until attempts are done
    while attempts < max_attempts:

        # Would check whether adding_values is even
        if adding_values % 2 == 0:

            #Checks if the bot_checker_2 indicates its even or e
            if bot_checker_2 == 'even' or bot_checker_2 == 'e':
                print("Yep, that's correct!")
                break # Closes the while loop once conditions are met 
            else:
                #Allows usser to try again, and adds 1 each time they get it wrong
                print("Whoops, try again.")
                attempts += 1
                # Using recursive to call to the function human_or_bot()
                human_or_bot()
                return
        #Checks if its odd 
        else:
            if bot_checker_2 == 'odd' or bot_checker_2 == 'o':
                print("Yep, that's correct!")
                break
            else:
                print("Whoops, try again.")
                human_or_bot()
        attempts += 1
        return human_or_bot()

    if attempts == max_attempts:
        print("Max Attempts! Failed to complete")
        quit()

human_or_bot()

print("Great that works")

print("Now lets begin! \n You can't access the Authentication Page, only once you win shall you be granted access")

empty = ""

#--------------------------------------------------------------------------------------------------------------------
#                                   The Main Page
#---------------------------------------------------------------------------------------------------------------------
# Create a function for the home page (allowing me to destory and call the whole code)
def home_page_function():

    #Create the home page 
    home_window = tkinter.Tk()

    #Adjust the size of the GUI
    home_window.geometry("550x450")

    #Disabling resizing the GUI
    home_window.resizable(1,1)

    #Naming the GUI page
    home_window.title("Home Page")
    
#--------------------------------------------------------------------------------------------------------------------
#                                   Quotes
#---------------------------------------------------------------------------------------------------------------------

#Function that handles setting a random quote
    def random_quotes():
        #Using random choice to choose one of the quote randomly
        quote_of_the_day = random.choice([
            '"The man who does not read books has no advantage over the one who cannot read them.” —Mark Twain',
            '"Education is the passport to the future, for tomorrow belongs to those who prepare for it today.” —Malcolm X',
            '“Teachers can open the door, but you must enter it yourself.” —Chinese proverb',
            '“The beautiful thing about learning is that no one can take it away from you.” —B.B. King',
            '“Education is the most powerful weapon you can use to change the world.” —B.B. King',
            '“The mind is not a vessel to be filled but a fire to be ignited.” —Plutarch',
            '“Don’t let what you cannot do interfere with what you can do.” —John Wooden',
            '“A person who never made a mistake never tried anything new." —Albert Einstein',
            '“Never let the fear of striking out stop you from playing the game.” —Babe Ruth'
        ])
        #Setting the choosen quote as a text for tkinter label
        label_for_the_quote.config(text=f"\nYour Daily Quote Of The Day Is {quote_of_the_day}")
        
    #For some reason this function helps prevent an error from occuring
    def genertate_quote():
        random_quotes()
    
    #Displaying the quote using Label, and setting it to be displayed in the center of the GUI
    label_for_the_quote = tkinter.Label(home_window, text="", justify='center')
    label_for_the_quote.pack()

    # Define a function that warns the user there closing the main page
    def warning_close():
        if messagebox.askyesno("Confirm Closing The GUI?", "Are you sure you want to close this GUI?"):
            home_window.destroy()
    home_window.protocol("WM_DELETE_WINDOW", warning_close)

    # Define a function to move from login to register while hiding the main page
    def break_page_regsiter():
        home_window.withdraw()
        regsiter()

    # Define a function to move from register to login while hiding the main page
    def break_page_login():
        home_window.withdraw()
        login()

#--------------------------------------------------------------------------------------------------------------------
#                                   Regsiter Page
#---------------------------------------------------------------------------------------------------------------------
    # Register Page Function
    def regsiter():
            #New window for register page
            regsiter_window = tkinter.Toplevel(home_window)

            #Adjust the size of the GUI
            regsiter_window.geometry("550x450")

            #Naming the GUI page
            regsiter_window.title("Register Page")

            #Disabling resizing the GUI
            regsiter_window.resizable(0, 0)

            show_password_string = tkinter.BooleanVar()
            show_password_string_confirm = tkinter.BooleanVar()

            #Function that closes the Regsiter Page & opens the Login Page
            def sign_in_instead():
                regsiter_window.destroy() 
                login()

            #Function that closes the Login Page & opens the Regsiter Page
            def home_page():
                regsiter_window.destroy()
                home_page_function()

            #Function that hides or shows the password
            def hide_password():
                #If user unchecks the box, then the strings show
                if show_password_string.get():
                    password_entry.config(show=empty)
                    return True
                #If user checks the box then the stars are replaceed
                else:
                    password_entry.config(show="*")
                    return False
                
            #Function that hides or shows the password
            def hide_password_confirm():

                #If user checks the box, then the strings show
                if show_password_string_confirm.get():
                    confirm_password_entry.config(show=empty)
                    return True
                else:
                #If user unchecks the box then the stars come back
                    confirm_password_entry.config(show="*")
                    return False
                
            #Function that checks if Studnet IDs' length is equal to 7
            def check_studentID():
                studentID = studentID_name_entry.get()

                #If length is equal to 7 then a messagebox appears saying its Successful
                if len(studentID) == 7:
                    messagebox.showinfo("Successful", "The Student ID Works")
                    return True

                #If length is less or greater then 7 then a messagebox appears saying Unsuccessful
                else:
                    messagebox.showerror("Unsuccessful", "The Student ID should be 7 characters only")
                    return False
            
            #Function that checks only numeric chars and if empty 
            def number_ony(P):
                if P == empty or P.replace(".", empty).isdigit():
                    return True
                else:
                    return False
            
            #Function that checks if first and last name are empty or not
            def first_last_name():
                first_name = first_name_entry.get()
                last_name = last_name_entry.get()

                #If statement goes through first name then last name to check 
                #If the user leaves the entry empty, then a messagebox appears saying Unsuccessful and returns False
                if first_name == empty:
                    messagebox.showerror("Unsuccessful", "You Forgot To Add Your First Name")
                    return False
                elif last_name == empty:
                    messagebox.showerror("Unsuccessful", "You Forgot To Add Your Last Name")
                    return False
                #If user adds their first and last name, then a Successfully message appears
                else:
                    messagebox.showinfo("Successfully", "Your First & Last Name Are Valid!")
                    return True
                
            #Function that checks if username is empty or not
            def username_checker():
                username = username_entry.get()

                #If username is empty then a messagebox appears saying Unsuccessful
                if username == empty:
                    messagebox.showerror("Unsuccessful", "You Forgot To Add A Username")
                    return False

                #If the username is not empty then it returns a Successful message
                else:
                    messagebox.showinfo("Successful", "Great Username!")
                    return True
                
            #Checks whether email contains @, gmail, hotmail,.com...
            def checker_email():
                email = email_entry.get()

                #Email checker using regx
                pattern = r'[a-zA-Z0-9]{0,}([.]?[a-zA-Z0-9]{1,})[@](gmail.com|hotmail.com|yahoo.com)'

                #If the requirements from Regx match then sucessful
                if re.match(pattern, email):
                    messagebox.showinfo("Successfully", "Email Address Is Valid!")
                    return True

                #Else if it doesn't meet the requirements from Regx then its unsuccessful
                else:
                    messagebox.showerror("Unsuccessful", "Invalid Email Address")
                    return False
            
            #Checks if password is strong and meets the requirements 
            def password_valid():

                #Taking in the password from password entry
                password_checker = password_entry.get()

                #Taking in the confirm password from confirm password entry
                confirm_password = confirm_password_entry.get() 

                #The length of the password 
                length_of_password = 8

                #The password must contain one char
                chars_in_password = '!@#$%^&*()-_+=<>?/{},[]~' 

                #Checks if password is the same as confirm password
                if password_checker == confirm_password:

                    #Checks if password length is 8 or more
                    if len(password_checker) >= length_of_password:

                        #Checks if password contains char such as ! or @ 
                        if any(char in chars_in_password for char in password_checker):

                            #Checks if password has a lower case and upper case
                            if any(char.islower() for char in password_checker) and any(char.isupper() for char in password_checker):

                                #Checks if password has a number 
                                if any(char.isdigit() for char in password_checker):

                                    #If all requirements are complete a successful message appears
                                    messagebox.showinfo("Successfully", "Your Password Is Valid!")
                                    return True

                                #If the password does not contain a number, the user is left with an unsucessful attempt 
                                else:
                                    messagebox.showerror("Unsuccessful", "Password should have numbers.")

                            #If the password does not contain a upper or lower case, the user is left with an unsucessful attempt 
                            else:
                                messagebox.showerror("Unsuccessful", "Password should contain both upper and lower case characters.")

                        #If the password does not contain a special char (such as ! or @..), the user is left with an unsucessful attempt 
                        else:
                            messagebox.showerror("Unsuccessful", "Password should contain at least one special character.")

                    #If the password is not 8 letters or more long, the user is left with an unsucessful attempt 
                    else:
                        messagebox.showerror("Unsuccessful", "Your Password length should be at least 8 characters.")

                #If the password does not match confirm or visa vera, the user is left with an unsucessful attempt 
                else:
                    messagebox.showerror("Unsuccessful", "Your Passwords do not match! Please enter again")
                return False

#--------------------------------------------------------------------------------------------------------------------
#                                   Sign Up Page
#---------------------------------------------------------------------------------------------------------------------
            def sign_up_command():

                #Checks if registration is successful by checking if all the conditions are met in each functions
                if (check_studentID() and username_checker() and first_last_name() and
                        checker_email() and password_valid()):
                    save_data_register()
                    messagebox.showinfo("Successfully", "Registration Successful!")

            #Function is used to save the data
            def save_data_register():

                #Getting the username that the user entered within username_entry 
                username_register = username_entry.get()

                #Getting the password that the user entered within password_entry
                password_register = password_entry.get() 

                #Getting the first name that the user entered within first_name_entry
                first_register = first_name_entry.get()

                #Getting the last name that the user entered within last_name_entry
                last_register = last_name_entry.get()

                #Getting the student ID that the user entered within studentID_name_entry  
                student_register = studentID_name_entry.get()

                #Getting the email that the user entered within email_entry  
                email_register = email_entry.get()

                #Opening the Reg_data.txt and adding/writing in the info into the file
                with open("Reg_data.txt", "a") as file:

                    #Writes in what the username that the inputs (only when regsitertation is successful)
                    file.write(f"Username: {username_register}\n")

                    #Writes in what the password that the inputs (only when regsitertation is successful
                    file.write(f"Password: {password_register}\n")

                    #Writes in what the first name that the inputs (only when regsitertation is successful
                    file.write(f"First Name: {first_register}\n")

                    #Writes in what the last name that the inputs (only when regsitertation is successful
                    file.write(f"Last Name: {last_register}\n")

                    #Writes in what the student register that the inputs (only when regsitertation is successful
                    file.write(f"Student ID: {student_register}\n")

                    #Writes in what the email register that the inputs (only when regsitertation is successful
                    file.write(f"Email: {email_register}\n")

                    #Writes down a new line
                    file.write("\n")
                
                #After everything is saved, the user is left with a successful message
                messagebox.showinfo("Successfully", "Data Saved Successfully!")

            #The home button 
            home_page_button = tkinter.Button(regsiter_window, text="Home Page", padx=10, pady=20, command=home_page) #Command is setting the role of the button to the respect function

            #Displays/Packs the home back 
            home_page_button.pack()

            #Places the button in the respected location of x and y (can be written as grid(x=10,y=10) as well)
            home_page_button.place(x=10, y=10)

            #The studentID
            validate_studentID_command = regsiter_window.register(number_ony)

            #Display a entry for the user to type their respected student ID (disableing nums and only strings)
            studentID_name_entry = tkinter.Entry(regsiter_window, validate="key", validatecommand=(validate_studentID_command, "%P"))

            #Displays the entry
            studentID_name_entry.pack()

            #Prints a label the message "Enter TMU Student ID"
            studentID_name_label = tkinter.Label(regsiter_window,text="Enter TMU Student ID")
            studentID_name_label.pack()

            #Displays a entry for the user to enter in their first name in the regsiter window 
            first_name_entry = tkinter.Entry(regsiter_window)
            first_name_entry.pack()

            #Prints a label the message "Enter First Name"
            first_name_label = tkinter.Label(regsiter_window, text="Enter First Name")
            first_name_label.pack()

            #Displays a entry for the user to enter in their last name in the regsiter window 
            last_name_entry = tkinter.Entry(regsiter_window)
            last_name_entry.pack()

            #Prints a label the message "Enter Last Name"
            last_name_label = tkinter.Label(regsiter_window, text="Enter Last Name")
            last_name_label.pack()

            #Displays a entry for the user to enter in their prefered username
            username_entry = tkinter.Entry(regsiter_window)
            username_entry.pack()

            #Prints a label message called username 
            username_label = tkinter.Label(regsiter_window, text="Username")
            username_label.pack()

            #Displays a entry widget for users to input their email
            email_entry = tkinter.Entry(regsiter_window)
            email_entry.pack()

            #Displays a Label indicating the purpose of the entry which is for email address
            email_label = tkinter.Label(regsiter_window, text="Email Address")
            email_label.pack()

            #Displays a entry widget for the user to input a password (the entry displays stars by default to hide the text)
            password_entry = tkinter.Entry(regsiter_window, show="*")
            password_entry.pack()
            
            #Displays a label indicating the purpose of the entry which is for password 
            password_label = tkinter.Label(regsiter_window, text="Password")
            password_label.pack()

            #Displays a checkbutton which allows the user to show or hide the password by using the hide_password function
            show_password_checkbox = tkinter.Checkbutton(regsiter_window, text="Show Password", variable=show_password_string, command=hide_password)
            show_password_checkbox.pack()

            #Displays a entry widget for the user to input a the confirmed password (the entry displays stars by default to hide the text)
            confirm_password_entry = tkinter.Entry(regsiter_window, show="*")
            confirm_password_entry.pack()

            #Displays a label indicating the purpose of the entry which is for confirm password 
            confirm_password_label = tkinter.Label(regsiter_window, text="Confirm Password")
            confirm_password_label.pack()

            #Displays a checkbutton which allows the user to show or hide the confirmed password by using the hide_password hide_password_confirm
            show_password_checkbox_confirm = tkinter.Checkbutton(regsiter_window, text="Show Password", variable=show_password_string_confirm, command=hide_password_confirm)
            show_password_checkbox_confirm.pack()

            #Displays a button for the user to press when they feel they want to sign up, the sign_up_command function would check if all conditions are met
            sign_up_button = tkinter.Button(regsiter_window, text="Sign Up", command=sign_up_command)
            sign_up_button.pack()

            #Displays a text which is "Already have an account" to indicate that the user can login instead
            sign_in_message = tkinter.Label(regsiter_window, text="Already have an account? ")
            sign_in_message.pack()

            #Button for sign in
            sign_in_already = tkinter.Button(regsiter_window, text="Sign In Instead", command=sign_in_instead)
            sign_in_already.pack()

            #Calling the GUI
            regsiter_window.mainloop()

#--------------------------------------------------------------------------------------------------------------------
#                                   Login Page
#---------------------------------------------------------------------------------------------------------------------
    def login():

        #Adjusting the GUI for login
        #Setting the new GUI inside home_window by using Toplevel
        login_window = tkinter.Toplevel(home_window)
        login_window.geometry("550x450")
        login_window.title("Login Page")
        login_window.resizable(0,0)

        # Function that destory the login GUI and opens the regsiter GUI
        def make_an_account():
            login_window.destroy()
            regsiter() 
            
        # Function that destory the login GUI and opens the home GUI
        def home_page():
            login_window.destroy()
            home_page_function()

        show_password_string_2 = tkinter.BooleanVar()

        # Function that hides or shows the password 
        def hide_password_2():
            if show_password_string_2.get():
                password_entry.config(show="")
            else:
                password_entry.config(show="*")
                
        #Reading the resigtertion data from the reg_data.txt file and storing it into the dictionary 
        def read_info_from_resigter(name_of_the_file):

            data = {} #store the data 

            #Opens the reg_data.txt file and reads it
            with open(name_of_the_file, "r") as file:

                #reads all the lines from the reg_data.txt file
                lines = file.readlines() 

                #For loops through lines, processing every 7 lines (since there are 7 entries)
                for i in range(0, len(lines), 7):

                    #Finds and extracts the username from the i-th line and stores it within the username var
                    username = lines[i].strip().split(": ")[1]

                    #Finds and extracts from the i-th + 1 line and stores it in the password var
                    password = lines[i + 1].strip().split(": ")[1]

                    #Once done, adds the username and password into the data dictionary
                    data[username] = password
            return data
  
#--------------------------------------------------------------------------------------------------------------------
#                                   SignIn Page
#---------------------------------------------------------------------------------------------------------------------      
        def sign_in():
            #Gets the username as well as password from the entry's
            username = username_entry.get()
            password = password_entry.get()

            # Reads user information from the registration txt file with the function called read_info_from_resigter
            data = read_info_from_resigter("Reg_data.txt")

            #Check if the the information exists within the txt (checks if username and password are correct)
            if username in data and data[username] == password:
                # Messagebox that displays the successful message once the existing info is found 
                messagebox.showinfo("Login Successful", "Welcome, " + username + "!")

                #opens a new GUI after a sucessful login, which is the options GUI
                options = tkinter.Toplevel(login_window)
                options.title("Options Page")
                options.geometry("630x480")
                options.resizable(0,0)
                options.config(bg="#537C82")

#--------------------------------------------------------------------------------------------------------------------
#                                   Login Design
#---------------------------------------------------------------------------------------------------------------------
                def login_design_option():

                    login_design = tkinter.Toplevel(login_window)
                    login_design.geometry("686x686")
                    login_design.title("Talal's Login Design")
                    login_design.resizable(0, 0)

                    def make_an_account():
                        login_design.destroy()

                    def home_page():
                        login_design.destroy()
                        show_password_string_2 = tkinter.BooleanVar()

                    
                    #Background of the GUI
                    background_image = tkinter.PhotoImage(file="C:\\Users\\Talal\\Desktop\\Assign\\LoginPage.png")
                    background_label = tkinter.Label(login_design, image=background_image)
                    background_label.place(relwidth=1, relheight=1)

                    #All of the same widgets from the the login GUI
                    #Expect I use .place() to locate each entry in its correspondent box (the design I made was FROM figma, but I coded everything else including the entry's)

                    home_page_button = tkinter.Button(login_design, text="Home Page", padx=10, pady=20, command=home_page, cursor='hand2')
                    home_page_button.pack()
                    home_page_button.place(x=10, y=10)

                    username_entry_design = tkinter.Entry(login_design, width= 23, font=("Helvetica", 15), bd=0)
                    username_entry_design.grid(row=1, column=1)
                    username_entry_design.place(x=234.0, y=246.0)

                    password_entry_design = tkinter.Entry(login_design, show="*", width=12, font=("Helvetica", 15), bd=0)
                    password_entry_design.grid(row=2, column=2)
                    password_entry_design.place(x=234.0, y=355.0)

                    show_password_string_2_design = tkinter.BooleanVar()
                    show_password_checkbox_design = tkinter.Checkbutton(login_design, variable=show_password_string_2_design,cursor='hand2',borderwidth=0, bd=0, highlightthickness=0, highlightbackground="white")
                    show_password_checkbox_design.grid(row=2, column=1)
                    show_password_checkbox_design.place(x=315.0, y=410.0)

                    # Specify the path to your image
                    image_path1 = r"C:\Users\Talal\Desktop\Assign\RegInstead.png"

                    # Open the image using PIL
                    original_image1 = Image.open(image_path1)

                    # Resize the image to your desired dimensions
                    resized_image1 = original_image1.resize((120, 40))

                    # Convert the resized image to a PhotoImage object
                    image_register1 = ImageTk.PhotoImage(resized_image1)

                    # Create a label with the resized image
                    image_label = tkinter.Label(image=image_register1)

                    # Create a button with the resized image
                    sign_up_design = tkinter.Button(login_design, image=image_register1, command=make_an_account, borderwidth=0, bd=0, highlightthickness=0, highlightbackground="white", cursor='hand2')
                    sign_up_design.grid(row=5, column=1)
                    sign_up_design.place(x=435.0, y=555.0)


                    # Specify the path to your image
                    image_path_login_design = r"C:\Users\Talal\Downloads\login.png"

                    # Open the image using PIL
                    login_image2 = Image.open(image_path_login_design)

                    # Resize the image to your desired dimensions
                    resized_image_login_design = login_image2.resize((300, 50))

                    # Convert the resized image to a PhotoImage object
                    image_login2 = ImageTk.PhotoImage(resized_image_login_design)

                    # Create a label with the resized image
                    image_label = tkinter.Label(image=image_login2)

                    # Create a button with the resized image
                    login2 = tkinter.Button(login_design, image=image_login2, command=make_an_account, borderwidth=0, bd=0, highlightthickness=0, highlightbackground="white", cursor='hand2')
                    login2.grid(row=10, column=1)
                    login2.place(x=200.0, y=467.0)
                    
                    def hide_password_2():
                        pass

                    login_design.mainloop()

#--------------------------------------------------------------------------------------------------------------------
#                                   Regsiter Design
#---------------------------------------------------------------------------------------------------------------------
                def reg_design_option():
                    register_window = tkinter.Toplevel(login_window)
                    register_window.geometry("686x686")
                    register_window.title("Reg Page")
                    register_window.resizable(0, 0)

                    style = ttk.Style()

                    def make_an_account():
                        register_window.destroy()

                    def home_page():
                        register_window.destroy()

                    # Load and display the background image
                    image_path2 = r"C:\Users\Talal\Desktop\Assign\ResigterPage.png"
                    original_image2 = Image.open(image_path2)
                    resized_image2 = original_image2.resize((686, 686))
                    image_register2 = ImageTk.PhotoImage(resized_image2)
                    image_label2 = tkinter.Label(register_window, image=image_register2)
                    image_label2.grid()

                    # Create "Home Page" button
                    home_page_button2 = tkinter.Button(register_window, text="Home Page", padx=10, pady=20, command=home_page, cursor='hand2')
                    home_page_button2.place(x=10, y=10)

                    # Make a variable that sets entry settings (don't need to re)
                    var_entry_sets = {'width': 35, 'borderwidth': 0, 'bd': 0, 'highlightthickness': 0, 'highlightbackground': "white"}

                    #All of the same widgets from the the register GUI
                    #Expect I use .place() to locate each entry in its correspondent box (the design I made was FROM figma, but I coded everything else including the entry's)
                    studentID_name_entry2 = tkinter.Entry(register_window, validate="key", **var_entry_sets)
                    studentID_name_entry2.place(x=268.0, y=105.0)

                    first_name_entry2 = tkinter.Entry(register_window, **var_entry_sets)
                    first_name_entry2.place(x=268.0, y=165.0)

                    last_name_entry2 = tkinter.Entry(register_window, **var_entry_sets)
                    last_name_entry2.place(x=268.0, y=225.0)

                    username_entry2 = tkinter.Entry(register_window, **var_entry_sets)
                    username_entry2.place(x=268.0, y=285.0)

                    email_entry2 = tkinter.Entry(register_window, **var_entry_sets)
                    email_entry2.place(x=268.0, y=345.0)

                    password_entry2 = tkinter.Entry(register_window, show="*", **var_entry_sets)
                    password_entry2.place(x=268.0, y=397.0)

                    show_password_checkbox2 = ttk.Checkbutton(register_window, style="TCheckbutton")
                    show_password_checkbox2.place(x=340.0, y=425.0)

                    confirm_password_entry2 = tkinter.Entry(register_window, show="*", **var_entry_sets)
                    confirm_password_entry2.place(x=268.0, y=475.0)

                    show_password_checkbox_confirm2 = ttk.Checkbutton(register_window, style="TCheckbutton")
                    show_password_checkbox_confirm2.place(x=340.0, y=500.0)

                    # "Register" button
                    image_path_reg3 = r"C:\Users\Talal\Desktop\Assign\regbutton.png"
                    reg_image3 = Image.open(image_path_reg3)
                    resized_image_reg3 = reg_image3.resize((264, 29))
                    image_reg3 = ImageTk.PhotoImage(resized_image_reg3)
                    image_label2 = tkinter.Label(image=image_reg3)
                    login3 = tkinter.Button(register_window, image=image_reg3, command=make_an_account, borderwidth=0, bd=0, highlightthickness=0, highlightbackground="white", cursor='hand2')
                    login3.place(x=230.0, y=525.0)

                    # "Login" button
                    image_path_loginstead4 = r"C:\Users\Talal\Desktop\Assign\login2.png"
                    loginstead_image4 = Image.open(image_path_loginstead4)
                    resized_image_loginstead4 = loginstead_image4.resize((60, 19))
                    image_loginstead4 = ImageTk.PhotoImage(resized_image_loginstead4)
                    image_label3 = tkinter.Label(image=image_loginstead4)
                    login = tkinter.Button(register_window, image=image_loginstead4, command=make_an_account, borderwidth=0, bd=0, highlightthickness=0, highlightbackground="white", cursor='hand2')
                    login.place(x=470.0, y=572.0)

                    
                    style.configure("TCheckbutton", borderwidth=0, padding=0, highlightthickness=0)

                    register_window.mainloop()

#--------------------------------------------------------------------------------------------------------------------
#                                   NotePad
#---------------------------------------------------------------------------------------------------------------------
                def notepad_option():
                    #Define window
                    notepad_window = tkinter.Toplevel(login_window)
                    notepad_window.title("Talal's Notepad")
                    notepad_window.geometry("630x480")
                    notepad_window.resizable(1,1)

                    #Notepad logo
                    notepad_window.iconbitmap("notepad.ico.ico")

                    #Define functions
                    def change_font(event):
                        selected_font = font_option.get()
                        selected_size = int(size_list.get())
                        selected_style = str(font_style.get()).lower()
                        scroll.config(font=(selected_font, selected_size,selected_style))
                    
                    #Creating a new notepad
                    def new_note():
                        #Messagebox which tells the user whether they want to make a new note
                        message_1 = tkinter.messagebox.askyesno(title='New Note', message='Are you sure you want to make a new note?')
                        if message_1 == TRUE:
                            scroll.delete(1.0,END)
                        else: 
                            print('')
                    
                    #Closing the notepad function
                    def close_note():
                        #Use a messagebox to ask to close
                        message = tkinter.messagebox.askyesno(title='Closing Note', message='Are you sure you want to close your notes?')
                        if message == TRUE:
                            notepad_window.destroy()
                            #command=window.destroy
                        elif message == FALSE:
                            print('')

                    #Saving note page
                    def save_note():
                        #To get location and name of where/what to save the file as.
                        #Defaultextension saves file automatically as a .txt file
                        save1 = filedialog.asksaveasfile( mode='w',defaultextension='.txt')
                        if save1 == FALSE:
                            return
                        #write remaining text in field to the file
                        save_text=str(scroll.get(1.0,END))
                        save1.write(save_text)
                        save1.close()
                    
                    #Opening a notepad from files of your choose
                    def open_note():
                        open_1 = filedialog.askopenfile(mode='r')
                        if open_1:
                            file_info = open_1.read()
                            scroll.delete(1.0,END)
                            scroll.insert("insert", file_info)

#--------------------------------------------------------------------------------------------------------------------
#                                   #Define all the frames
#---------------------------------------------------------------------------------------------------------------------
                    grid_frame_2 = tkinter.LabelFrame(notepad_window,borderwidth=3, bg='#C4C4C4')
                    grid_frame_2.place(y=2,x=45)
                    frame_l = tkinter.Label(grid_frame_2, bg='#EF8354').grid(padx=10,pady=10)

                    frame_3 = tkinter.Label(grid_frame_2, width=75, height=2, bg='#E0E0E0').grid(row=0, column=0)

                    new_image = tkinter.PhotoImage(file='New.png')
                    new_button = tkinter.Button(notepad_window, image=new_image, command=new_note)
                    new_button.grid(row=0,column=0, padx=(50,10), pady=5)

                    open_image = tkinter.PhotoImage(file='Open.png')
                    open_button = tkinter.Button(notepad_window, image=open_image,command=open_note)
                    open_button.grid(row=0,column=2, padx=(0,10), pady=5)

                    save_image = tkinter.PhotoImage(file='Save.png')
                    save_button = tkinter.Button(notepad_window, image=save_image,command=save_note)
                    save_button.grid(row=0,column=3, padx=(0,10), pady=5)

                    close_image = tkinter.PhotoImage(file='close.png')
                    close_button = tkinter.Button(notepad_window, image=close_image,command=close_note)
                    close_button.grid(row=0,column=4, padx=(0,10), pady=5)
                    
                    #Create a list of fonts to use
                    list_font = {"MS Serif",
                    "Small Fonts",
                    "Marlett",
                    "Arial",
                    "Tempus Sans ITC",
                    "Cascadia Mono",
                    'Cascadia Code ExtraLight',
                    'Perpetua',
                    'Calibri',
                    'Times New Roman',
                    'Vivaldi'}

                    #Font optionmenu list
                    font_option = StringVar()
                    font_option.set('Times New Roman')
                    font_menu = OptionMenu(notepad_window, font_option, *list_font, command=change_font)
                    font_menu.grid(row=0, column=5, padx=(0,10), pady=5)

                    #Font size optionmenu
                    list_sizes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
                    size_list = DoubleVar()
                    size_list.set(12)
                    size_menu = OptionMenu(notepad_window,size_list, *list_sizes, command=change_font)
                    size_menu.grid(row=0, column=6, padx=(0,10), pady=5)

                    #Font style optionmenu
                    list_style = {"Normal",
                    "Bold",
                    "Italic"}
                    font_style = StringVar()
                    font_style.set('Normal')
                    style_menu = OptionMenu(notepad_window,font_style, *list_style, command=change_font)
                    style_menu.grid(row=0, column=7, padx=(0,10), pady=5)

                    #Set the width so it will fit "times new roman" and remain constant
                    font_menu.config(width=22)

                    #Set width to be constant even if its 8.
                    style_menu.config(width=8)

                    #Set the width to be constant
                    size_menu.config(width=2)

                    #Create input_text as a scrolltext so you can scroll through the text field.
                    scroll = ScrolledText(notepad_window,height=100, width=1000, font=("Times New Roman", 12), wrap=WORD,bg="#FFFDD6",insertwidth=4)
                    scroll.place(x=5,y=60)

                    #Run the root window's main loop
                    notepad_window.mainloop() 
                
                #Button for the notepad option from the options GUI
                notepad_option_button = tkinter.Button(options, text="Notepad", command=notepad_option)
                notepad_option_button.pack()

                #button for that opens the login design 
                login_design = tkinter.Button(options, text="Talal's Figma Login Design", command=login_design_option)
                login_design.pack()

                #button for that opens the register design 
                reg_design = tkinter.Button(options, text="Talal's Figma Register Design", command=reg_design_option)
                reg_design.pack()
                
            else:
                #Messagebox only appears when user fails to login
                messagebox.showerror("Login Failed", "Invalid username, password, email, or student ID. Please try again.")
        

        #Button which returns back to the home GUI
        home_page_button = tkinter.Button(login_window, text="Home Page", padx=10, pady=20, command=home_page)
        home_page_button.pack()
        home_page_button.place(x=10, y=10)


        #Label to indicate that the entry for the username
        username_label = tkinter.Label(login_window, text="Enter Your Username")
        username_label.pack()

        #Entry for the user to input their respected username
        username_entry = tkinter.Entry(login_window)
        username_entry.pack()

        #Label to indicate that the following entry is for the password
        password_label = tkinter.Label(login_window, text="Enter Your Password")
        password_label.pack()

        #Entry for the user to input their respected password (Default set to stars for privacy)
        password_entry = tkinter.Entry(login_window, show="*")
        password_entry.pack() 

        #Checkbox that takes care of showing or hiding the password
        show_password_checkbox = tkinter.Checkbutton(login_window, text="Show Password", variable=show_password_string_2, command=hide_password_2)
        show_password_checkbox.pack()

        #Button for signing in
        sign_in_button = tkinter.Button(login_window, text="Sign In", command=sign_in)
        sign_in_button.pack()

        #Label that encourages the user to register instead
        regsiter_label = tkinter.Label(login_window, text="Don't have an account yet? Don't worry You can ")
        regsiter_label.pack()

        #Button for making a new account if the user hasn't already
        sign_up = tkinter.Button(login_window, text="Make a account here", command=make_an_account)
        sign_up.pack()

        #Calling the login_window GUI
        login_window.mainloop()
    
    #Label that greets the user
    welcome = tkinter.Label(home_window, text="Welcome Back!")
    welcome.pack()

    #Button that displays quotes using the random_quotes function 
    quote_of_the_day_button = tkinter.Button(home_window, text="Quote Of The Day", command=random_quotes)
    quote_of_the_day_button.pack()

    #Label that encourages the user to login
    message_login = tkinter.Label(home_window, text="Already have a account! Login")
    message_login.pack()

    #Button that opens the login GUI
    login_button = tkinter.Button(home_window, text="Login", command=break_page_login)
    login_button.pack()

    #Label that encourages the user to register
    messsage_signup = tkinter.Label(home_window, text="Dont have an account yet, no worries lets set you up!")
    messsage_signup.pack()

    #Button that opens the registration GUI
    register_button = tkinter.Button(home_window, text="Register", command=break_page_regsiter)
    register_button.pack()

    #Calling the home_window GUI
    home_window.mainloop()


#--------------------------------------------------------------------------------------------------------------------
#                                   Ready
#---------------------------------------------------------------------------------------------------------------------

#While loop
while True:
    # User input while converting the strings into lowercase
    are_u_ready = input("Are you ready?: ").lower()

    #Statements that checks if the user is ready 
    if are_u_ready == 'yes' or are_u_ready == 'y':
        print("ok")
        #Calls the home GUI if user is ready
        home_page_function()
        break
    
    elif are_u_ready == 'no' or are_u_ready == 'n':
        print("Okay then")
        break

    else: 
        print("Invaild")