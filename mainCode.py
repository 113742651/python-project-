import random

print("\033[5;37;40m Guess the Song\033[0;37;40m \n")
print ("""
 _                 _
| |               (_)
| |     ___   __ _ _ _ __
| |    / _ \ / _` | | '_ \\
| |___| (_) | (_| | | | | |
\_____/\___/ \__, |_|_| |_|
              __/ |
             |___/

                                                                                                                                                """)
def write(file_write, usernames):
    with open(file_write, "a+") as file:
        file.write(usernames)
"""
Is this even used?
def Enter(file_write, userpassword):
   with open(file_write, "a+") as file:        
       file.write(userpassword)
"""

#this runs the first inputs for the start menu
def start_menu():
    print ("""
        A)Start Normally
        B)Skip to test
        """)
    selection = input ("Choose if you would like to start or leave\n> ")

    if selection.lower() == 'a':
        menu_A()
    elif selection.lower() == 'b':
        music()


#basic menu interface for userdetails
def menu_A():
    username = input ("enter your username: ")
    password = input ("enter your password: ")
    print ("Correct details")
    usernamesWrite = username + "," + "\n"
    write("userdetails.txt", usernamesWrite)
    userpasswordEnter = password + "," + "\n"
    write("userpassword.txt", userpasswordEnter)
    start = input ("Ready to start?")

    if start.lower() == 'yes':
        music()
    elif start.lower() == 'no':
        start_menu()

#the second part of the menu curretnly running under the test section until later changes
def music():

    with open("artists.txt", 'r') as file:
       all_lines = file.readlines()

    song = random.choice(all_lines).split(",")

    print(song[0][0])
    print (song[1])
    
start_menu()
