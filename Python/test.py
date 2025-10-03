import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.font import Font#So I can use fonts in the games and menu
import random#For hangman and blackjack



root = tk.Tk()

root.geometry("950x850")#The size of the window

root.resizable(False, False)  # stop the resizing of the window

root.configure(bg="#FAF0CA")#The background color of the window

pixel_font_title = Font(family = "VT323", size = 70)
pixel_font_buttons = Font(family = "VT323", size = 30)
pixel_font_buttons_TTT = Font(family = "VT323", size = 26)
pixel_font_labels = Font(family = "VT323", size = 40)
pixel_font_buttons_hangman = Font(family = "VT323", size = 20)
pixel_font_buttons_small = Font(family = "VT323", size = 15)
scary_font_label = Font(family = "Nosifer", size = 20)


Title = tk.Label(root, text = "Game compedium", font = (pixel_font_title), 
                 fg = "#0D3B66", bg = "#FAF0CA").grid(row=0, 
                                                      column=0, columnspan=3,
                                                        pady=5, padx = 210)
#Stand in for the title, I willl change later


scores = {}
def hangman():
    global scores
    #Using a hangman tut from Data Science with Onur
    words = {"easy":["memento", "jewel", "killer", "common", "season", 
                        "theater", "garden", "holiday", "morning", "mother"],

            "medium":["jinx", "kayak", "yuna", "macabre", "partner",
                        "prediction", "lounge", "strength", "whiskey", 
                        "zombie"],

            "hard":["jazz", "klutz", "convoluted", "sphinx", "zealous", 
                    "executioner", "mimikyu", "frequency", "jewelzhang", 
                    "xylophone"]

            }

    letters_guessed = []#Storing letters guessed

    lives = 12#Number of lives user has

    score = 0#The users score

    print(score)





    hangman = tk.Toplevel(root)#A new window for hangman
    hangman.title("Hangman")
    hangman.geometry("800x900")
    hangman.resizable(False, False)  # stop the resizing of the window
    hangman.configure(bg="#FAF0CA")#The background color of the window

    head = tk.Label(hangman, text = "Guess the word, \nor the man gets hanged", 
                    font=scary_font_label, fg = "#CC0000", 
                    bg = "#FAF0CA")#heading

    head.pack(pady = 5 )


    difficulty = random.choice(list(words))#Choosing a random difficulty first
    word = random.choice(words[difficulty])#Then choosing a random word
    guessed = ["_ "] * len(word)
    #Number of lines = number of letters in word for user to guess, 
    #each line will be replaced when user guesses correctly






    enter = tk.Entry(hangman, font = pixel_font_buttons, bg = "#FAF0CA")
    #A textbox where the user can enter their guesses(single line)
    enter.pack(pady = 10)
 


    label = tk.Label(hangman, text = "_ " * len(word), 
                     font = pixel_font_labels, bg = "#FAF0CA")
    #the lines to show how many letters are in the word
    label.pack(pady = 5)



    letters = tk.Label(hangman, text = f"Wrong Letters/Words guessed: ",
                        wraplength = 700,
                       font = pixel_font_buttons, bg = "#FAF0CA")
    #To show the user what letters they have guessed wrong
    letters.pack(pady = 5)



    liveslabel = tk.Label(hangman, text = f"Lives left until the man gets hanged: {lives}", font = pixel_font_buttons, bg = "#FAF0CA")
    liveslabel.pack(pady = 5)



    def check(event = None):#To check if the user guessed a letter in the word

        nonlocal lives#Accessing lives outside the function
        nonlocal guessed
        nonlocal score
        nonlocal head
        nonlocal difficulty
        nonlocal word
        nonlocal letters_guessed

        guess = enter.get()#Getting the letter/word guessed by the user
        guess = guess.lower()

        enter.delete(0, "end")#clearing the Entrybox thing after each use

        if guess in letters_guessed:
            return

        if guess in word.lower():

            for i in range(len(word)):

                if word[i] == guess:

                    guessed[i] = guess#Replace the line with the letter if they gusses correctly

                    label.config(text = "".join(guessed))#to join all the letters and lines together + updating the label

            if guess == word.lower() or "".join(guessed) == word:#If the user guesses the whole word or all the letters

                guessed = guess#Replace the line with the letter if they guesses correctly

                label.config(text = "".join(word))#to join all the letters and lines together + updating the label

                checkbutton.config(command = nextword, text = "Next word")#giving the option to change the word

                head.config(text = f"You guessed the word!!\n Click next word to continue playing")#Changing the text to show they won

                if difficulty == "easy":
                    score += 1
                elif difficulty == "medium":
                    score += 2
                elif difficulty == "hard":
                    score += 3
                print(score)



        if guess not in word.lower() and guess not in letters_guessed:

            lives = lives - 1

            liveslabel.config(text = f"Lives left until the man gets hanged: {lives}")

            if guess not in letters_guessed:

                letters_guessed.append(guess)#Adding the wrong guess to the list

                letters.config(text = f"Wrong Letters/Words guessed: {', '.join(letters_guessed)}")#Showing the user what they guessed wrong


            drawman(lives)#Draw the man!!

        if lives == 0:

            drawman(lives)#Draw the man(last time...)

            print(score)

            head.config(text = f"Uh oh!! The man is dead...\n The word was {word}", font=scary_font_label, fg = "#CC0000", bg = "#FAF0CA")
            enter.config(state = "disabled")
            #Disabling the entry box so the player can't keep guessing
            hangman.unbind("<Return>")#Unbinding the enter key so it cant be pressed
            #Unbinding the button so it cant be clicked
            checkbutton.pack_forget()
            #I learnt this from the yt channel Tkinter.com
            #Disabling the button so the player can't keep losing lives 
            letters.pack_forget()
            enter.pack_forget()#pack_forget removes the wiget from the window so the player cant keep guessing after they lose
            leaderboard = tk.Label(hangman, text = "Do you want to add your score to the leaderboard?", 
                                   font = pixel_font_buttons_hangman, bg = "#FAF0CA", 
                                   fg = "#0D3B66")
            leaderboard.pack(pady = 5)

            seeLB = tk.Button(hangman, command = scoreboard, 
                              text = "Open leaderboard", 
                              font = pixel_font_buttons_hangman,
                              fg = "#FAF0CA", bg = "#0D3B66")
            seeLB.pack(pady = 5)


    def nextword(event = None):

        nonlocal word

        nonlocal guessed

        nonlocal difficulty

        checkbutton.config(command = check, text = "Check letter")
        #Changing back the button

        head.config(text = "Guess the word,\n or the man gets hanged", font=scary_font_label, fg = "#CC0000", bg = "#FAF0CA")

        difficulty = random.choice(list(words))
        #Choosing a random difficulty first

        word = random.choice(words[difficulty])#Then choosing a random word

        guessed = ["_ "] * len(word)
        #Number of lines = number of letters in word for user to guess, 
        # #each line will be replaced when user guesses correctly

        label.config(text = "_ " * len(word))#Resetting the lines

        letters.config(text = f"Wrong Letters/Words guessed: ")
        #Resetting the wrong letters guessed

        letters_guessed.clear()#Clearing the list of wrong letters guessed



    hangman.bind('<Return>', check)#So user can also presses enter to check their guess


    checkbutton = tk.Button(hangman, text = "Check letter", 
                            font = pixel_font_buttons_hangman, 
                            bg = "#0D3B66", fg = "#FAF0CA",
                            command = lambda:check(), pady = 0, 
                            padx = 20)#To check the users guesses
    #lambda is like a one off function. We can use the function name again 
    #elsewhere in the code without being affected by this function

    checkbutton.pack(pady = 5)



    def scoreboard():
        scoreboard_window = tk.Toplevel(hangman)
        scoreboard_window.title("Hangman scores")
        scoreboard_window.geometry("500x800")
        scoreboard_window.resizable(False, False)  
        # stop the resizing of the window
        scoreboard_window.configure(bg="#FAF0CA")
        #The background color of the window

        name_label = tk.Label(scoreboard_window, 
                              text = "Please enter a new name", 
                              fg = "#0D3B66",
                               bg = "#FAF0CA", font = pixel_font_labels)
        name_label.pack()
        nameEnter = tk.Entry(scoreboard_window,  bg = "#FAF0CA", 
                        font = pixel_font_labels)
        nameEnter.pack()
        name_warning = tk.Label(scoreboard_window, 
                                text = "Please enter a name under 7 letters", 
                                fg = "#0D3B66",
                               bg = "#FAF0CA", 
                               font = pixel_font_buttons_hangman)
        name_warning.pack(pady = 5)

        def get_name():
            #I used a tutorial by Tutorialspoint for the scroll bar
            value = nameEnter.get()
            if len(value) <= 6:
                confirmNamewin = tk.Toplevel(hangman)
                confirmNamewin.title("Hangman scores")
                confirmNamewin.geometry("400x800")
                confirmNamewin.resizable(False, False)  
                confirmNamewin.grid()

                scrollframe = tk.Frame(confirmNamewin, bg = "#FAF0CA")
                scrollframe.grid(row = 0, column = 0, sticky="nsew")

                canvasScroll = tk.Canvas(scrollframe, bg = "#FAF0CA")
                #yview makes the scroll bar control canvas vertical scroll
                scrollbar = tk.Scrollbar(scrollframe
                                         , orient="vertical", 
                                         command=canvasScroll.yview)
                scrollbar.grid(row = 0, column = 1, sticky = "ns")
                canvasScroll.configure(yscrollcommand = scrollbar.set)

                content = tk.Frame(canvasScroll, bg = "#FAF0CA")
                content.grid(row = 0, column = 0, sticky = "nsew")
                content.rowconfigure(0, weight = 1)
                content.columnconfigure(0, weight = 1)

                #Allow for other widgets to be in the canvas
                canvasScroll.create_window((0, 0), window = content, 
                                           anchor = "nw")
                canvasScroll.grid(row = 0, column = 0, sticky = "nsew")
                #make scroll bar expand to fit to window
                scrollframe.bind("<Configure>", lambda e: 
                                   canvasScroll.configure(scrollregion=canvasScroll.bbox("all")))


                # stop the resizing of the window
                confirmNamewin.configure(bg="#FAF0CA")
                scoreboard_window.destroy()
                scores[value] = score
                #save the scores to a dictionary with a name and score
                title_score_UN = tk.Label(content, text = "Name",
                font = pixel_font_labels, 
                                        fg = "#0D3B66", bg = "#FAF0CA")
                #spot where name is
                title_score_S = tk.Label(content, text = "Score", 
                                        font = pixel_font_labels, 
                                        fg = "#0D3B66", bg = "#FAF0CA")
                title_score_UN.grid(row = 0, column = 0, padx = 40, pady = 5)
                title_score_S.grid(row = 0, column = 1, padx = 40, pady = 5)
                #putting them in a grid so they can stack like a leaderboard
                line = 1
                #The row the name and score are on
                for i, r in scores.items():
                    #putting the score and name in dict into labels so the player
                    #can see them 
                    scorey = tk.Label(content, text = r, bg = "#FAF0CA", 
                                    fg = "#0D3B66", font = pixel_font_labels)
                    namey = tk.Label(content, text = i, bg = "#FAF0CA", 
                                    fg = "#0D3B66", font = pixel_font_labels)
                    scorey.grid(row = line, column = 1, padx = 40, pady = 5)
                    namey.grid(row = line, column = 0, padx = 40, pady = 5)
                    line += 1

                    #make it enlarge into the window
                    confirmNamewin.columnconfigure(0, weight=1)
                    confirmNamewin.rowconfigure(0, weight=1)
                    scrollframe.columnconfigure(0, weight=1)
                    scrollframe.rowconfigure(0, weight=1)
            else:
                name_warning.config(fg = "#FF0000")


        confirmName = tk.Button(scoreboard_window, text = "Confirm name", 
                                command = get_name, bg = "#0D3B66", 
                                fg = "#FAF0CA")
        confirmName.pack(pady = 10)





        



    """To draw the man.



    we will draw the man using canvas with lines and coordinates.

    There will be 6 strokes each corresponding to a life the player has.

    When the player guesses wrong a stroke will be added.

    """



    canvas = tk.Canvas(hangman, width = 400, height = 350, bg =  "#FAF0CA", highlightthickness = 0)

    canvas.pack(pady = 2)



    def drawman(lives):

        if lives == 11:#rim

            canvas.create_line(150, 100, 240, 100)

        elif lives == 10:#hat

            canvas.create_rectangle(180, 75, 220, 100)

        elif lives == 9:

            canvas.create_line(100, 300, 100, 50)#Pole

        elif lives == 8:

            canvas.create_line(50, 300, 300, 300)#Base

        elif lives == 7:

            canvas.create_line(100, 50, 300, 50)#high frame

        elif lives == 6:

            canvas.create_line(200, 50, 200, 75)#String

        elif lives == 5:

            canvas.create_oval(180, 100, 220, 140)#Head

        elif lives == 4:

            canvas.create_line(200, 140, 200, 220)#body

        elif lives == 3:

            canvas.create_line(200, 140, 260, 200)#arm1

        elif lives == 2:

            canvas.create_line(200, 140, 140, 200)#arm2

        elif lives == 1:

            canvas.create_line(200, 220, 260, 240)#leg1

        elif lives == 0:

            canvas.create_line(200, 220, 140, 240)#leg2





def Stictactoe():
    TTT = tk.Toplevel(root)
    TTT.title("Choose your gamemode")
    TTT.title("Tic Tac Toes")
    TTT.geometry("490x300")
    TTT.configure(bg="#FAF0CA")#The background color of the window
    TTT_title = tk.Label(TTT, text = "Choose your gamemode", 
                         font = pixel_font_labels, 
                         fg = "#0D3B66", bg = "#FAF0CA")
    TTT_title.grid(row = 0, column = 0, columnspan = 3, pady = 10, padx = 10)

    def Stictactoe_friend():
        global pixel_font_buttons_TTT
        global pixel_font_labels
        FTTT = tk.Toplevel(TTT)
        FTTT.title("Tic Tac Toes but you aren't lonely!")
        FTTT.geometry("805x875")
        FTTT.resizable(False, False)  # stop the resizing of the window
        FTTT.configure(bg="#FAF0CA")#The background color of the window
        current_player = "X"#X is the current player
        #I am using a tutorial by Alina Chudnova but I modified it to make it super
        #I used codingspots ultimate tictactoe video for the nested list board

        FTTT_title = tk.Label(FTTT, text = "Super Tic Tac Toe with a buddy!!",
                                font = pixel_font_labels, 
                                fg = "#0D3B66", bg = "#FAF0CA")
        FTTT_title.grid(row = 0, column = 0, columnspan = 3, pady = 10, 
                        padx = 10)
        #Giving our board a value
        board = [[[["" for i in range(3)] for r in range (3)] 
                for j in range(3)] for k in range(3)]
        #I creates the first row, r creates the first subboard, 
        # j creates the first row of subboards, k creates the bigger board
        subboard_winner = [["" for i in range(3)] for r in range(3)]
        #Creating a way to store all the winners of the subboard
        #These subboards function as a section in tic tac toe

        allowed_frame_coords_x = ""
        allowed_frame_coords_y = ""
        #The coordinates of the only frame the user is able to move in

        def make_move(mainrow, maincol, subrow, subcol):
            #the code so the player can click a button to make a move
            nonlocal current_player
            nonlocal board
            nonlocal buttons
            nonlocal allowed_frame_coords_x
            nonlocal allowed_frame_coords_y
            nonlocal subboard_winner
            #The the mainrow maincol determines which frame the button picked is
            #The subrow subcol determines which button inside the frame was clicked
            if allowed_frame_coords_x == "" and allowed_frame_coords_y == "" and board[mainrow][maincol][subrow][subcol] == "":
                board[mainrow][maincol][subrow][subcol] = current_player
                #Turning all the subboards blue except those that are won
                #or the one that we are moving in
                check_winner_sub(mainrow, maincol)
                #check if the subboard fo these coords wins
                check_winner_main()#Check if main board wins
                for i in range(3):
                    for r in range(3):
                        if subboard_winner[i][r] == "":
                            subboards[i][r].config(bg = "#EE964B")
                if subboard_winner[subrow][subcol] == "":
                    allowed_frame_coords_x = subrow
                    allowed_frame_coords_y = subcol
                    if subboard_winner[subrow][subcol] == "":
                        #If the target board was not won then...
                        subboards[subrow][subcol].config(bg = "#0D3B66")
                        #Change color of target
                else:
                    allowed_frame_coords_x = ""
                    allowed_frame_coords_y = ""
                    #If the subboard is won highlight all not won subboards
                    for i in range(3):
                        for r in range(3):
                            if subboard_winner[i][r] == "":
                                subboards[i][r].config(bg = "#0D3B66")
                                
                #Then change the button the whatever the current player is
                if current_player == "O":#Changing the color of the square
                    buttons[mainrow][maincol][subrow][subcol].config(text=current_player, bg = "#0000FF")
                else:
                    buttons[mainrow][maincol][subrow][subcol].config(text=current_player, bg = "#FF0000")
                #changing the text of the button to the current player
                if current_player == "X":#Changing the current player after each turn
                    current_player = "O"
                else:
                    current_player = "X"


                    #First check if the button is empty
                    #Then check if the button is in the allowed frame
            elif board[mainrow][maincol][subrow][subcol] == "" and \
                allowed_frame_coords_x == mainrow and\
                      allowed_frame_coords_y == maincol:
                #Turning all the subboards blue except those that are won
                #or the one that we are moving in
                for i in range(3):
                    for r in range(3):
                        if subboard_winner[i][r] == "":
                            subboards[i][r].config(bg = "#EE964B")
                if subboard_winner[subrow][subcol] == "":
                    #If the target board was not won then...
                        subboards[subrow][subcol].config(bg = "#0D3B66")

                    #Change color of target

                board[mainrow][maincol][subrow][subcol] = current_player
                #Check if the next subboard is 
                check_winner_sub(mainrow, maincol)
                #check if the subboard fo these coords wins
                check_winner_main()#Check if main board wins
                if subboard_winner[subrow][subcol] == "":
                    #If it isn't then change the allowed coords to the next subboard
                    allowed_frame_coords_x = subrow
                    allowed_frame_coords_y = subcol
                else:
                    #If it is then allow the player to move anywhere
                    allowed_frame_coords_x = ""
                    allowed_frame_coords_y = ""
                    #If the subboard is won highlight all not won subboards
                    for i in range(3):
                        for r in range(3):
                            if subboard_winner[i][r] == "":
                                subboards[i][r].config(bg = "#0D3B66")
                #Then change the button the whatever the current player is
                if current_player == "O":#Changing the color of the square
                    buttons[mainrow][maincol][subrow][subcol].config(text=current_player, bg = "#0000FF")
                else:
                    buttons[mainrow][maincol][subrow][subcol].config(text=current_player, bg = "#FF0000")
                #changing the text of the button to the current player
                if current_player == "X":#Changing the current player after each turn
                    current_player = "O"
                else:
                    current_player = "X"


        def check_winner_main():#Checking if there is a winner
            nonlocal board
            nonlocal current_player
            nonlocal subboard_winner
            winning = (subboard_winner[0], 
                        subboard_winner[1], 
                        subboard_winner[2],#checking the rows
                        [subboard_winner[i][0] for i in range(3)],#column one
                        [subboard_winner[i][1] for i in range(3)],#columnc 2
                        [subboard_winner[i][2] for i in range(3)],#Column 3
                        [subboard_winner[i][i] for i in range(3)],#Diagonal
                        [subboard_winner[i][2-i] for i in range(3)])#another diagonal
            
            for win in winning:
                if win[0] == win[1] == win[2] != "":#If all three values in a row are the same and not empty
                    FTTT_title.config(text = f"{win[0]} wins!")
                    if win[0] == "O":
                        FTTT.config(bg = "#0000FF")
                    else:
                        FTTT.config(bg = "#FF0000")
                    for i in range(3):
                        for r in range(3):
                            for j in buttons[i][r]:#Iterating through the list
                                for k in j:#go through and disble all buttons 1 by 1
                                    k.config(state = "disabled")
                                    #Making each button in that frame dissabled
            if all(subboard_winner[i][r] != "" for i in range(3) for r in range(3)):#If all buttons are filled but no winner
                FTTT_title.config(text = "Tie!!")
                for i in range(3):
                    for r in range(3):
                        for j in buttons[i][r]:#Iterating through the list
                            for k in j:#go through and disble all buttons 1 by 1
                                k.config(state = "disabled")
                                #Making each button in that frame dissabled
            #Iterating through each square
        def check_winner_sub(mainrow, maincol):#Checking if there is a winner for sub
            #These coords are used for the subboard_check var
            nonlocal current_player
            nonlocal board
            nonlocal subboard_winner
            subboard_check = board[mainrow][maincol]
            #Coordinates of subboard of the button that was just clicked
            winning = (subboard_check[0], 
                        subboard_check[1], 
                        subboard_check[2],#checking the rows
                        [subboard_check[i][0] for i in range(3)],#column one
                        [subboard_check[i][1] for i in range(3)],#columnc 2
                        [subboard_check[i][2] for i in range(3)],#Column 3
                        [subboard_check[i][i] for i in range(3)],#Diagonal
                        [subboard_check[i][2-i] for i in range(3)])#Diagonal2
            
            for win in winning:
                if win[0] == win[1] == win[2] != "":#If all three values in a row are the same and not empty
                    #take note of who won the subboard in the nested list
                    subboard_winner[mainrow][maincol] = current_player
                    if subboard_winner[mainrow][maincol] == "X":
                        subboards[mainrow][maincol].config(bg = "#FF0000")
                    else:#Changing the colors to match the winners
                        subboards[mainrow][maincol].config(bg = "#0000FF")
                    #Taking note of who won
                    for i in buttons[mainrow][maincol]:#Iterating through the list
                        #Or 3rd list inside the buttons(row list)nested list
                        for r in i:#Inside the list I iterate through each button
                            r.config(state = "disabled")
                            #Making each button in that frame dissabled
                    return
            if all(subboard_check[i][r] != "" for i in range(3) for r in range(3)):#If all buttons are filled but no winner
                subboard_winner[mainrow][maincol] = "T"
                #To make confirm the board can no longer be played in
                subboards[mainrow][maincol].config(bg = "grey")


        #Buttons for the game
        subboards = [["" for i in range(3)] for r in range(3)]
        #Store buttons in a frame to keep the seperate from other subboards
        buttons = [["" for i in range(3)] for r in range(3)]
        #These act as place holders as they are lists with sub lists inside
        #These allow us to determine coords of our buttons and stuff
        for d in range(3):#creating the first row
            board_button_row = []#Stores the row of buttons created this iteration
            for r in range(3):#creating the 3x3 grid structure
                #frame like divclass
                subboard_frame = tk.Frame(FTTT, bg = "#EE964B",)
                subboard_frame.grid(row=d + 1, column=r, pady = 5, padx = 5)
                subboards[d][r] = subboard_frame
                """
                Creating the frame the buttons are gonna go inside
                And then putting the frame into a grid structure
                then add that to a nested list that stores it 
                and lets us edit exact frames through coords
                """
                button_subboard = []#Where we append the button rows for 3x3 grid
                #buttons inside the subboard
                for j in range(3):#Three rows for buttons
                    buttons_row = []#One row of three buttons
                    for k in range(3):#Three columns per row for the buttons
                        #Put the buttons into the frame
                        button = tk.Button(subboard_frame, text = "",
                                            font = pixel_font_buttons_TTT, 
                                            width = 5, height = 1, borderwidth=0,
                                            bg = "#F4D35E",
                                            command = lambda d=d, r=r, j=j,
                                            k=k: make_move(d, r, j, k))
                        #providing numbers for the make move function
                        #when we make a move we take into consideration the subboard and button pressed
                        #this is so we know which button was pressed
                        """Button coords.

                        The first 2, D and R or m(main)row and m(main)col
                        determine the frame the button is on and the second 2 
                        bb(baby)row and bb(baby)col determine the coords of the 
                        button inside the frame.
                        """
                        button.grid(row = j, column = k, padx = 5, pady = 5)
                        #Place the buttons in a grid, the padding is the lines
                        buttons_row.append(button)#Adding the button to a row
                    button_subboard.append(buttons_row)#Adding the row to a 3x3 grid
                buttons[d][r] = button_subboard
                #changing the "" from the nested list into our button 3x3 grid



    def Stictactoe_bot():
        global pixel_font_buttons_TTT
        global pixel_font_labels
        BTTT = tk.Toplevel(TTT)
        BTTT.title("Tic Tac Toes but you ARE lonely!")
        BTTT.geometry("805x875")
        BTTT.configure(bg="#FAF0CA")#The background color of the window

        current_player = "X"#X is the current player
        #I am using a tutorial by Alina Chudnova but I modified it to make it super
        #I used codingspots ultimate tictactoe video for the nested list board

        #Giving our board a value
        board = [[[["" for i in range(3)] for r in range (3)] 
                for j in range(3)] for k in range(3)]
        #I creates the first row, r creates the first subboard, 
        # j creates the first row of subboards, k creates the bigger board
        subboard_winner = [["" for i in range(3)] for r in range(3)]
        #Creating a way to store all the winners of the subboard
        #These subboards function as a section in tic tac toe


        game_finished = False


        STTT_title = tk.Label(BTTT, text = "Super Tic Tac Toe, with a bot!", 
                            font = pixel_font_labels, 
                            fg = "#0D3B66", bg = "#FAF0CA")
        STTT_title.grid(row = 0, column = 0, columnspan = 3, pady = 10)

                #Buttons for the game
        subboards = [["" for i in range(3)] for r in range(3)]
        #Store buttons in a frame to keep the seperate from other subboards
        buttons = [["" for i in range(3)] for r in range(3)]
        #These act as place holders as they are lists with sub lists inside
        #These allow us to determine coords of our buttons and stuff
        for d in range(3):#creating the first row
            board_button_row = []#Stores the row of buttons created this iteration
            for r in range(3):#creating the 3x3 grid structure
                #frame like divclass
                subboard_frame = tk.Frame(BTTT, bg = "#EE964B",)
                subboard_frame.grid(row=d+1, column=r, pady = 5, padx = 5)
                subboards[d][r] = subboard_frame
                """
                Creating the frame the buttons are gonna go inside
                And then putting the frame into a grid structure
                then add that to a nested list that stores it 
                and lets us edit exact frames through coords
                """
                button_subboard = []#Where we append the button rows for 3x3 grid
                #buttons inside the subboard
                for j in range(3):#Three rows for buttons
                    buttons_row = []#One row of three buttons
                    for k in range(3):#Three columns per row for the buttons
                        #Put the buttons into the frame
                        button = tk.Button(subboard_frame, text = "",
                                            font = pixel_font_buttons_TTT, 
                                            width = 5, height = 1, borderwidth=0,
                                            bg = "#F4D35E",
                                            command = lambda d=d, r=r, j=j,
                                            k=k: make_move(d, r, j, k))
                        #providing numbers for the make move function
                        #when we make a move we take into consideration the subboard and button pressed
                        #this is so we know which button was pressed
                        """Button coords.

                        The first 2, D and R or m(main)row and m(main)col
                        determine the frame the button is on and the second 2 
                        bb(baby)row and bb(baby)col determine the coords of the 
                        button inside the frame.
                        """
                        button.grid(row = j, column = k, padx = 5, pady = 5)
                        #Place the buttons in a grid, the padding is the lines
                        buttons_row.append(button)#Adding the button to a row
                    button_subboard.append(buttons_row)#Adding the row to a 3x3 grid
                buttons[d][r] = button_subboard
                #changing the "" from the nested list into our button 3x3 grid

        fm_mainrow = random.randint(0,2)
        fm_maincol = random.randint(0,2)
        fm_subrow = random.randint(0,2)
        fm_subcol = random.randint(0,2)
        #Making the bot make the first move to prevent any freezes when there
        #is only one avaliable space for the bot to move
        #fm stands for first move

        board[fm_mainrow][fm_maincol]\
            [fm_subrow][fm_subcol] = "O"
        buttons[fm_mainrow][fm_maincol]\
            [fm_subrow][fm_subcol].config(text="O", 
                                          bg = "#0000FF")
        allowed_frame_coords_x = fm_subrow
        allowed_frame_coords_y = fm_subcol
        subboards[allowed_frame_coords_x][allowed_frame_coords_y].config(bg = "#0D3B66")


        def make_move(mainrow, maincol, subrow, subcol):
            #the code so the player can click a button to make a move
            nonlocal current_player
            nonlocal board
            nonlocal buttons
            nonlocal allowed_frame_coords_x
            nonlocal allowed_frame_coords_y
            nonlocal subboard_winner
            #The the mainrow maincol determines which frame the button picked is
            #The subrow subcol determines which button inside the frame was clicked
            if allowed_frame_coords_x == "" and allowed_frame_coords_y == "" \
                and board[mainrow][maincol][subrow][subcol] == "":
                board[mainrow][maincol][subrow][subcol] = current_player
                #Turning all the subboards blue except those that are won
                #or the one that we are moving in
                for i in range(3):
                    for r in range(3):
                        if subboard_winner[i][r] == "":
                            subboards[i][r].config(bg = "#EE964B")
                check_winner_sub(mainrow, maincol)
                #check if subboard wins using the coordinates
                check_winner_main()#Check if main board wins
                if subboard_winner[subrow][subcol] == "":
                    allowed_frame_coords_x = subrow
                    allowed_frame_coords_y = subcol
                    if subboard_winner[subrow][subcol] == "":
                        #If the target board was not won then...
                        subboards[subrow][subcol].config(bg = "#0D3B66")
                        #Change color of target
                else:
                    allowed_frame_coords_x = ""
                    allowed_frame_coords_y = ""
                    #If the subboard is won highlight all not won subboards
                    for i in range(3):
                        for r in range(3):
                            if subboard_winner[i][r] == "":
                                subboards[i][r].config(bg = "#0D3B66")
                #Then change the button the whatever the current player is
                if current_player == "O":#Changing the color of the square
                    buttons[mainrow][maincol][subrow][subcol].config(text=current_player, bg = "#0000FF")
                else:
                    buttons[mainrow][maincol][subrow][subcol].config(text=current_player, bg = "#FF0000")
                #changing the text of the button to the current player
                if current_player == "X":#Changing the current player after each turn
                    current_player = "O"
                    if game_finished == False:
                    #The bot making a move if its O
                        BTTT.after(100, TTT_bot_move, allowed_frame_coords_x,
                                    allowed_frame_coords_y)
                        #delaying the bot by 0.1 secconds to make it seem more natural
                        #and give the winning function to calculate the winner before
                        #the bot makes a move
                else:
                    current_player = "X"


                    #First check if the button is empty
                    #Then check if the button is in the allowed frame
            elif board[mainrow][maincol][subrow][subcol] == "" and\
                  allowed_frame_coords_x == mainrow and \
                    allowed_frame_coords_y == maincol:
                #MAKE MOVE FIRST
                board[mainrow][maincol][subrow][subcol] = current_player
                #Turning all the subboards blue except those that are won
                #or the one that we are moving in
                for i in range(3):
                    for r in range(3):
                        if subboard_winner[i][r] == "":
                            subboards[i][r].config(bg = "#EE964B")
                #Check if the next subboard is won
                check_winner_sub(mainrow, maincol)
                #check if the subboard fo these coords wins
                check_winner_main()#Check if main board wins
                if subboard_winner[subrow][subcol] == "":
                    #If the target board was not won then...
                        subboards[subrow][subcol].config(bg = "#0D3B66")
                    #Change color of target
                if subboard_winner[subrow][subcol] == "":
                    #If it isn't then change the allowed coords to the next subboard
                    allowed_frame_coords_x = subrow
                    allowed_frame_coords_y = subcol
                else:
                    #If it is then allow the player to move anywhere
                    allowed_frame_coords_x = ""
                    allowed_frame_coords_y = ""

                #Then change the button the whatever the current player is
                if current_player == "O":#Changing the color of the square
                    buttons[mainrow][maincol][subrow][subcol].config(text=current_player, bg = "#0000FF")
                else:
                    buttons[mainrow][maincol][subrow][subcol].config(text=current_player, bg = "#FF0000")
                #changing the text of the button to the current player
                if current_player == "X":#Changing the current player after each turn
                    current_player = "O"
                    if game_finished == False:
                    #The bot only moves if its O
                        BTTT.after(100, TTT_bot_move, allowed_frame_coords_x,\
                                allowed_frame_coords_y)#Make the bot move
                    #delay to the bots movements
                else:
                    current_player = "X"

        def TTT_bot_move\
            (bot_allowed_frame_coords_x, bot_allowed_frame_coords_y):
            nonlocal board
            nonlocal current_player
            bot_coord_X = random.randint(0,2)
            bot_coord_Y = random.randint(0,2)
            nonlocal buttons
            nonlocal subboards
            nonlocal subboard_winner
            nonlocal allowed_frame_coords_x
            nonlocal allowed_frame_coords_y
            if allowed_frame_coords_x != "" and allowed_frame_coords_y != "":
                while board[allowed_frame_coords_x][allowed_frame_coords_y]\
                    [bot_coord_X][bot_coord_Y] != "":
                    bot_coord_X = random.randint(0,2)
                    bot_coord_Y = random.randint(0,2)
                    #Rabdomise the coords until we find an empty button
                if board[allowed_frame_coords_x][allowed_frame_coords_y]\
                    [bot_coord_X][bot_coord_Y] == "":
                    #Change the button to the current player or whatever player the but is
                    board[allowed_frame_coords_x][allowed_frame_coords_y]\
                        [bot_coord_X][bot_coord_Y] = current_player
                    #Changing the color of the square depedning on the player
                    buttons[allowed_frame_coords_x][allowed_frame_coords_y]\
                        [bot_coord_X][bot_coord_Y].config(text=current_player, 
                                                          bg = "#0000FF")
                    check_winner_sub(allowed_frame_coords_x, 
                                     allowed_frame_coords_y)
                    check_winner_main()
                    for i in range(3):
                        for r in range(3):
                            if subboard_winner[i][r] == "":
                                subboards[i][r].config(bg = "#EE964B")
                    current_player = "X"

                    if subboard_winner[bot_coord_X][bot_coord_Y] == "":
                        allowed_frame_coords_x = bot_coord_X
                        allowed_frame_coords_y = bot_coord_Y
                        #if target board isn't won then change color
                        subboards[bot_coord_X][bot_coord_Y].config(bg = "#0D3B66")
                    else:
                        allowed_frame_coords_x = ""
                        allowed_frame_coords_y = ""
                        #If the subboard is won highlight all not won subboards
                        for i in range(3):
                            for r in range(3):
                                if subboard_winner[i][r] == "":
                                    subboards[i][r].config(bg = "#0D3B66")
            else:#If allowed frame coords are either empty or the subboard is won
                #Choose a random frame that isn't won
                allowed_frame_coords_x = random.randint(0,2)
                allowed_frame_coords_y = random.randint(0,2)
                bot_coord_X = random.randint(0,2)
                bot_coord_Y = random.randint(0,2)
                #First choose a random frame and random button
                #Then check random frames until we find one that isn't won
                while True:
                    allowed_frame_coords_x = random.randint(0,2)
                    allowed_frame_coords_y = random.randint(0,2)
                    #If the frame isn't won then break the loop
                    if subboard_winner[allowed_frame_coords_x]\
                        [allowed_frame_coords_y] == "":
                        break
                    #And choose a random button in that frame
                    #Then check random buttons until we find an empty one
                while True:
                    bot_coord_X = random.randint(0,2)
                    bot_coord_Y = random.randint(0,2)
                    #If the button is empty then break the loop
                    if board[allowed_frame_coords_x][allowed_frame_coords_y]\
                        [bot_coord_X][bot_coord_Y] == "":
                        break
                #Then make the bot make a move in the button
                
                #Make a move in the selected button
                board[allowed_frame_coords_x][allowed_frame_coords_y]\
                    [bot_coord_X][bot_coord_Y] = current_player
                buttons[allowed_frame_coords_x][allowed_frame_coords_y]\
                    [bot_coord_X][bot_coord_Y].config(text=current_player, 
                                                      bg = "#0000FF")
                check_winner_sub(allowed_frame_coords_x, allowed_frame_coords_y)
                check_winner_main() 
                for i in range(3):
                    for r in range(3):
                        if subboard_winner[i][r] == "":
                            subboards[i][r].config(bg = "#EE964B")
                current_player = "X"

                if subboard_winner[bot_coord_X][bot_coord_Y] == "":
                    #If it isn't then change the allowed coords to the next subboard
                    allowed_frame_coords_x = bot_coord_X
                    allowed_frame_coords_y = bot_coord_Y
                    subboards[bot_coord_X][bot_coord_Y].config(bg = "#0D3B66")
                else:
                    #If it is then allow the player to move anywhere
                    allowed_frame_coords_x = ""
                    allowed_frame_coords_y = ""
                    for i in range(3):
                        for r in range(3):
                            if subboard_winner[i][r] == "":
                                subboards[i][r].config(bg = "#0D3B66")
                #change allowed coords and color



        def check_winner_main():#Checking if there is a winner
            nonlocal board
            nonlocal current_player
            nonlocal subboard_winner
            nonlocal game_finished
            winning = (subboard_winner[0], 
                        subboard_winner[1], 
                        subboard_winner[2],#checking the rows
                        [subboard_winner[i][0] for i in range(3)],#column one
                        [subboard_winner[i][1] for i in range(3)],#columnc 2
                        [subboard_winner[i][2] for i in range(3)],#Column 3
                        [subboard_winner[i][i] for i in range(3)],#Diagonal
                        [subboard_winner[i][2-i] for i in range(3)])#another diagonal
            
            for win in winning:
                if win[0] == win[1] == win[2] != "":#If all three values in a row are the same and not emptyF
                    game_finished = True
                    STTT_title.config(text = f"{win[0]} wins!")
                    if win[0] == "O":
                        BTTT.config(bg = "#0000FF")
                    else:
                        BTTT.config(bg = "#FF0000")
                    for i in range(3):
                        for r in range(3):
                            for j in buttons[i][r]:#Iterating through the list
                                for k in j:#go through and disble all buttons 1 by 1
                                    k.config(state = "disabled")
                                    #Making each button in that frame dissabled
                    return
                #prevent checking for a tie when winner is already found.
            if all(subboard_winner[i][r] != "" for i in range(3) for r in range(3)):
                #If all buttons are filled but no winner
                game_finished = True
                STTT_title.config(text = "Tie!!")
                for i in range(3):
                    for r in range(3):
                        for j in buttons[i][r]:#Iterating through the list
                            for k in j:#go through and disble all buttons 1 by 1
                                k.config(state = "disabled")
                                    #Making each button in that frame dissabled
        #Iterating through each square
        def check_winner_sub(mainrow, maincol):#Checking if there is a winner for sub
            #These coords are used for the subboard_check var
            nonlocal current_player
            nonlocal board
            nonlocal subboard_winner
            subboard_check = board[mainrow][maincol]
            #Coordinates of subboard of the button that was just clicked
            winning = (subboard_check[0], 
                        subboard_check[1], 
                        subboard_check[2],#checking the rows
                        [subboard_check[i][0] for i in range(3)],#column one
                        [subboard_check[i][1] for i in range(3)],#columnc 2
                        [subboard_check[i][2] for i in range(3)],#Column 3
                        [subboard_check[i][i] for i in range(3)],#Diagonal
                        [subboard_check[i][2-i] for i in range(3)])#Diagonal2
            
            for win in winning:
                if win[0] == win[1] == win[2] != "":#If all three values in a row are the same and not empty
                    #take note od who won the subboard in the nested list
                    subboard_winner[mainrow][maincol] = win[0]
                    #The winner is the first value out of the winning line
                    if subboard_winner[mainrow][maincol] == "X":
                        subboards[mainrow][maincol].config(bg = "#FF0000")
                    else:#Changing the colors to match the winners
                        subboards[mainrow][maincol].config(bg = "#0000FF")
                    #Taking note of who won
                    for i in buttons[mainrow][maincol]:
                        #Iterating through the list
                        #Or 3rd list inside the buttons(row list)nested list
                        for r in i:
                            #Inside the list I iterate through each button
                            r.config(state = "disabled")
                            #Making each button in that frame dissabled
                    return
                
            if all(subboard_check[i][r] != "" for i in range(3) \
                   for r in range(3)):#If all buttons are filled but no winner
                subboard_winner[mainrow][maincol] = "T"
                #To make confirm the board can no longer be played in
                for i in buttons[mainrow][maincol]:#Iterating through the list
                    #Or 3rd list inside the buttons(row list)nested list
                    for r in i:#Inside the list I iterate through each button
                        r.config(state = "disabled")
                subboards[mainrow][maincol].config(bg = "grey")

    friend_button = tk.Button(TTT, text = "Play with a friend", 
                              command = Stictactoe_friend,
                              font = pixel_font_buttons_hangman, 
                              bg = "#0D3B66", fg = "#FAF0CA", 
                              borderwidth = 0)
    bot_button = tk.Button(TTT, text = "Play with a bot", 
                           command = Stictactoe_bot,
                            font = pixel_font_buttons_hangman, 
                            bg = "#0D3B66", fg = "#FAF0CA", 
                            borderwidth = 0)
    friend_button.grid(row = 1, column = 0, pady = 20, padx = 20)
    bot_button.grid(row = 1, column = 2, pady = 20, padx = 20)


def blackjack():
    #I am using a tutorial by codemy.com for this blackjack game
    blackjack = tk.Toplevel(root)
    blackjack.title("Memory Mania")
    blackjack.geometry("900x500")
    blackjack.resizable(False, False)  # stop the resizing of the window
    blackjack.config(bg = "#FAF0CA")

    #resizing our images
    def resize_cards(card):
        pass

    #creating the deck list first
    deck = []

    cardnum = tk.Label(blackjack, 
                       text = f"Cards left in deck: 52", 
                       font = pixel_font_buttons_hangman, fg = "#0D3B66",
                        bg = "#FAF0CA")
    def shuffle():
        #shuffle the cards
        deck.clear()
        #making the deck
        suits = ["diamonds", "clubs", "hearts", "spades"]
        #These values range from 2 to ace
        #ace is the 15th card
        values = range(2, 15)
        #one card value for each suit
        for i in suits:
            #i is each individual suit
            for r in values:
                #r is each value
                deck.append(f"{r}_of_{i}")
                #name them like our images
        cardnum.config(text = f"Cards left in deck: {len(deck)}", 
                       fg = "#0D3B66")

    
    def dealing():
        try:  
            nonlocal deck
            #making the get card lists
            #Using these lists to keep track of what cards each person has
            dealer = []
            player = []

            #FOR DEALER
            #getting random card using random choice out of deck
            card = random.choice(deck)
            #remove card from deck
            deck.remove(card)
            #give card to dealer
            dealer.append(card)
            #show player dealer has a card
            dealer_card.config(text = card)

            #FOR PLAYER
            #getting random card using random choice out of deck
            card = random.choice(deck)
            #remove card from deck
            deck.remove(card)
            #give card to dealer
            player.append(card)
            #show player dealer has a card
            player_card.config(text = card)

            cardnum.config(text = f"Cards left in deck: {len(deck)}", 
                           fg = "#0D3B66")
        except:
            cardnum.config(fg = "#FF0000", text = "There are no more cards"\
                           " in the deck, please shuffle again")
    #add cards into the deck
    shuffle()
    #creating a deck with all the cards
    jack_title = tk.Label(blackjack, text = "Welcome to BlackJack!!", 
                          font = pixel_font_buttons_hangman, fg = "#0D3B66",
                          bg = "#FAF0CA")

    jack_title.pack()
    cardnum.pack()
    
    Mframe = tk.Frame(blackjack, bg = "green")
    Mframe.pack(pady = 20)
    #frame with text around border

    #where cards will be displayed
    Dframe = tk.LabelFrame(Mframe,text = "Dealer", bg = "green", bd = 0)
    Dframe.grid(row = 0, column = 0, padx = 20, ipady = 10)

    Pframe = tk.LabelFrame(Mframe,text = "Player", bg = "green", bd = 0)
    Pframe.grid(row = 0, column = 1, ipady = 10, padx = 20)

    #putting cards into frames
    dealer_card = tk.Label(Dframe, text = "spacefiller")
    player_card = tk.Label(Pframe, text = "playerflilielr")
    dealer_card.pack(pady = 20)
    player_card.pack(pady = 20)

    shuffle_button = tk.Button(blackjack, text = "Shuffle", 
                               font = pixel_font_buttons_TTT, 
                               command = shuffle, bg = "#0D3B66",
                          fg = "#FAF0CA")
    shuffle_button.pack(pady = 20)

    hit_button = tk.Button(blackjack, text = "Hit", 
                           font = pixel_font_buttons_TTT, command = dealing, 
                           bg = "#0D3B66", fg = "#FAF0CA")
    hit_button.pack(pady = 20)

    blackjack.mainloop()



def help():
    help = tk.Toplevel(root)
    help.title("Help")
    help.geometry("700x1000")
    help.resizable(False, False)  # stop the resizing of the window
    help.configure(bg="#FAF0CA")#The background color of the window

    def hangman_help():
        nonlocal changing_label
        changing_label.config(text = "How to play Hangman:\n" \
        "Enter the letters you think are in the word inside the text box.\n" \
        "You can either enter one letter or a whole word \nBUT the letters" \
        "in the word are not counted as guessed\n" \
        "so consider  very carefully.\n" \
        "You have 10 lives, and everytime you get a word or letter wrong,"\
        "\nyou will lose a life\n" \
        "and the man gets one step closer to being hanged...\n" \
        "Lose all your lives and the man DIES!!!(dun dun dun)\n" \
        "Guess the word correctly and you can move on to the next word!!(yay!!)\n" \
            "The words are divided into 3 difficulties: easy, medium and hard.\n" \
                "each difficulty gives you a different amount of points:\n" \
                    "easy = 1 point, medium = 2 points, hard = 3 points\n" \
                        "The points will then be counted and put on a leaderboard.\n" \
                            "Good luck and don't let the man die...", 
                            font = pixel_font_buttons_small, 
                                fg = "#0D3B66", bg = "#FAF0CA", 
                                justify = "center")
    def TTT_help():
        nonlocal changing_label
        changing_label.config(text = "sdlkhflskdjf", 
                              font = pixel_font_buttons_small, 
                            fg = "#0D3B66", bg = "#FAF0CA", 
                            justify = "center")
    def blackjack_help():
        nonlocal changing_label
        changing_label.config(text = "sdlkhflskdjf", 
                              font = pixel_font_buttons_small, 
                            fg = "#0D3B66", bg = "#FAF0CA", 
                            justify = "center")

    help_label = tk.Label(help, text = "What do you need help with?", font = pixel_font_buttons_hangman, 
                          fg = "#0D3B66", bg = "#FAF0CA")
    changing_label = tk.Label(help, text = "Click the buttons below to get help with each game", 
                             font = pixel_font_buttons_small, fg = "#0D3B66", bg = "#FAF0CA")
    hangman_help_button = tk.Button(help, text = "Hangman help?", 
                                    command=hangman_help, 
                                      font = pixel_font_buttons_hangman, 
                                      fg = "#FAF0CA", bg = "#0D3B66", 
                                      relief = "flat", padx=25)
    TTT_help_button = tk.Button(help, text = "Tic Tac Toe help?", 
                                   command=TTT_help, 
                                     font = pixel_font_buttons_hangman, 
                                     fg = "#FAF0CA", bg = "#0D3B66", 
                                     relief = "flat")
    blackjack_help_button = tk.Button(help, text = "Black Jack help?", 
                                   command=TTT_help, 
                                     font = pixel_font_buttons_hangman, 
                                     fg = "#FAF0CA", bg = "#0D3B66", 
                                     relief = "flat", padx = 15)
    help_label.pack(pady = 10)
    changing_label.pack(pady = 10)
    TTT_help_button.pack(pady = 20, padx = 20)
    hangman_help_button.pack(pady = 20, padx = 20)
    blackjack_help_button.pack(pady = 20, padx = 20)



root.title("Main Menu")

hangman_image = Image.open("Python/hangyman.jpg").resize((270, 200))
hangman_image = ImageTk.PhotoImage(hangman_image)

TTT_image = Image.open("Python/TTT.jpeg.jpeg").resize((300, 300))
TTT_image = ImageTk.PhotoImage(TTT_image)

help_button = tk.Button(root, text = "?", command = help, 
                        font = pixel_font_buttons_small, fg = "#FAF0CA",
                        bg = "#0D3B66", height = 1, width = 1).grid(
                            row = 0, column=2, sticky = "ne", padx = 10, pady = 10
                        )

frame_hangman = tk.Frame(root, bg = "#FAF0CA", borderwidth=0,)
frame_hangman.grid(row = 1, column = 0, pady = 40, padx = 10)
hangman_button_image = tk.Button(frame_hangman, image = hangman_image, 
                                 command = hangman, 
                           font = pixel_font_buttons , 
                           fg = "#FAF0CA", 
                           borderwidth= 0,
                           padx = 10, pady = 10)
hangman_button = tk.Button(frame_hangman, text = "Hangman", command = hangman, 
                             font = pixel_font_buttons, fg = "#FAF0CA",
                               bg = "#0D3B66", borderwidth = 0, padx = 80, 
                               pady = 5)
hangman_button_image.pack()
hangman_button.pack()

frame_ttt = tk.Frame(root, bg = "#FAF0CA", borderwidth=0)
frame_ttt.grid(row = 1, column = 2, rowspan=2, pady = 0, padx = 0)
Stictactoe_image = tk.Button(frame_ttt, image = TTT_image, 
                            command=Stictactoe, borderwidth=0,)
Stictactoe_image.pack()
Stictactoe_button = tk.Button(frame_ttt, text = "Super Tic Tac Toe",
                               command = Stictactoe, 
                               font = pixel_font_buttons, fg = "#FAF0CA", 
                               bg = "#0D3B66", borderwidth = 0, 
                               pady = 5, padx = 5)
Stictactoe_button.pack()

blackjack_frame = tk.Frame(root, bg = "#FAF0CA", borderwidth=0)
blackjack_frame.grid(row = 4, column = 1, rowspan=2, pady = 5, padx = 10)
blackjack_image = tk.Button(blackjack_frame, image = hangman_image, 
                            command=blackjack, borderwidth=0)

blackjack_button = tk.Button(blackjack_frame, text = "BlackJack", command = blackjack, 
                             font = pixel_font_buttons, fg = "#FAF0CA",
                               bg = "#0D3B66", borderwidth = 0, padx = 75, 
                               pady = 5)
blackjack_image.pack()
blackjack_button.pack()


root.mainloop()