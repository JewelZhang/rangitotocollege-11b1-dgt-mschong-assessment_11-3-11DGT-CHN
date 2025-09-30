import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.font import Font#So I can use fonts in the games and menu
import random#For hangman and blackjack



root = tk.Tk()

root.geometry("1000x900")#The size of the window

root.resizable(False, False)  # stop the resizing of the window

root.configure(bg="#FAF0CA")#The background color of the window

pixel_font_title = Font(family = "VT323", size = 70)
pixel_font_buttons = Font(family = "VT323", size = 30)
pixel_font_labels = Font(family = "VT323", size = 40)
pixel_font_buttons_hangman = Font(family = "VT323", size = 20)
pixel_font_buttons_small = Font(family = "VT323", size = 15)
scary_font_label = Font(family = "Nosifer", size = 20)


Title = tk.Label(root, text = "Game compedium", font = (pixel_font_title), fg = "#0D3B66", bg = "#FAF0CA").grid(row=0, column=0, columnspan=2, pady=20, padx = 200)#Stand in for the title, I willl change later

#Limiting the amount of windows that can be opened at once for each game
#I learnt this from codemy.com on yt
hm_counter = 0
TTT_counter = 0
memory_counter = 0
blackjack_counter = 0

def hangman():
    global hm_counter
    #Using a hangman tut from Data Science with Onur
    hm_counter +=1
    if hm_counter < 2:

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

        scores = {}

        lives = 10#Number of lives user has

        score = 0#The users score

        print(score)





        hangman = tk.Toplevel(root)#A new window for hangman
        hangman.title("Hangman")
        hangman.geometry("800x800")
        hangman.resizable(False, False)  # stop the resizing of the window
        hangman.configure(bg="#FAF0CA")#The background color of the window

        head = tk.Label(hangman, text = "Guess the word, \nor the man gets hanged", font=scary_font_label, fg = "#CC0000", bg = "#FAF0CA")#heading

        head.pack(pady = 10 )


        difficulty = random.choice(list(words))#Choosing a random difficulty first
        word = random.choice(words[difficulty])#Then choosing a random word
        guessed = ["_ "] * len(word)#Number of lines = number of letters in word for user to guess, each line will be replaced when user guesses correctly






        enter = tk.Entry(hangman, font = ("comicsans", 20), bg = "#FAF0CA")#A textbox where the user can enter their guesses(single line)
        enter.pack(pady = 20)



        label = tk.Label(hangman, text = "_ " * len(word), font = ("comic sans", 40), bg = "#FAF0CA")#the lines to show how many letters are in the word
        label.pack(pady = 10)



        letters = tk.Label(hangman, text = f"Wrong Letters/Words guessed: ", font = ("comic sans", 20), bg = "#FAF0CA")#To show the user what letters they have guessed wrong
        letters.pack(pady = 10)



        liveslabel = tk.Label(hangman, text = f"Lives left until the man gets hanged: {lives}", font = ("comic sans", 20), bg = "#FAF0CA")
        liveslabel.pack(pady = 10)



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

                    if difficulty == "AAA":
                        score += 1
                    elif difficulty == "BBBB":
                        score += 2
                    elif difficulty == "CC":
                        score += 3



            else:

                lives = lives - 1

                liveslabel.config(text = f"Lives left until the man gets hanged: {lives}")

                liveslabel.pack(pady = 10)

                if guess not in letters_guessed:

                    letters_guessed.append(guess)#Adding the wrong guess to the list

                    letters.config(text = f"Wrong Letters/Words guessed: {', '.join(letters_guessed)}")#Showing the user what they guessed wrong

                drawman(lives)#Draw the man!!

            if lives == 0:

                drawman(lives)#Draw the man!!

                print(score)

                head.config(text = f"Uh oh!! The man is dead...\n The word was {word}", font=scary_font_label, fg = "#CC0000", bg = "#FAF0CA")

                checkbutton.pack_forget()#I learnt this from the yt channel Tkinter.com

                enter.pack_forget()#pack_forget removes the wiget from the window so the player cant keep guessing after they lose

                scores.append(score)



        def nextword(event = None):

            nonlocal word

            nonlocal guessed

            nonlocal difficulty

            checkbutton.config(command = check, text = "Check letter")#Changing back the button

            head.config(text = "Guess the word,\n or the man gets hanged", font=scary_font_label, fg = "#CC0000", bg = "#FAF0CA")

            difficulty = random.choice(list(words))#Choosing a random difficulty first

            word = random.choice(words[difficulty])#Then choosing a random word

            guessed = ["_ "] * len(word)#Number of lines = number of letters in word for user to guess, each line will be replaced when user guesses correctly

            label.config(text = "_ " * len(word))#Resetting the lines

            letters.config(text = f"Wrong Letters/Words guessed: ")#Resetting the wrong letters guessed

            letters_guessed.clear()#Clearing the list of wrong letters guessed



        hangman.bind('<Return>', check)#So user can also presses enter to check their guess

        hangman.bind("<Right>", nextword)

        checkbutton = tk.Button(hangman, text = "Check letter", font = pixel_font_buttons_hangman, command = lambda:check(), pady = 0, padx = 20)#To check the users guesses
        #lambda is like a one off function. We can use the function name again elsewhere in the code without being affected by this function

        checkbutton.pack(pady = 5)






        """To draw the man.



        we will draw the man using canvas with lines and coordinates.

        There will be 6 strokes each corresponding to a life the player has.

        When the player guesses wrong a stroke will be added.

        """



        canvas = tk.Canvas(hangman, width = 400, height = 400, bg =  "#FAF0CA", highlightthickness = 0)

        canvas.pack(pady = 5)



        def drawman(lives):

            if lives == 9:

                canvas.create_line(100, 300, 100, 50)#Pole
            elif lives == 8:

                canvas.create_line(50, 300, 300, 300)#Basecanvas.create_line(100, 50, 300, 50)#Bottom frame

            elif lives == 7:

                canvas.create_line(100, 50, 300, 50)#high frame

            elif lives == 6:

                canvas.create_line(200, 50, 200, 100)#String

            elif lives == 5:

                canvas.create_oval(180, 100, 220, 140)#Head

            elif lives == 4:

                canvas.create_line(200, 140, 200, 240)#body

            elif lives == 3:

                canvas.create_line(200, 140, 260, 200)#arm1

            elif lives == 2:

                canvas.create_line(200, 140, 140, 200)#arm2

            elif lives == 1:

                canvas.create_line(200, 240, 260, 290)#leg1

            elif lives == 0:

                canvas.create_line(200, 240, 140, 290)#leg2





    hangman.mainloop()




def Stictactoe():
    global TTT_counter
    
    if TTT_counter < 1:
        TTT_counter += 1
        current_player = "X"#X is the current player
        #I am using a tutorial by Alina Chudnova
        TTT = tk.Toplevel(root)#A new window for Tictactoe
        TTT.title("Tic Tac Toes")
        TTT.geometry("800x620")
        TTT.resizable(False, False)  # stop the resizing of the window
        TTT.configure(bg="#FAF0CA")#The background color of the window

        #Giving our board a value
        board = [["", "", "",] for i in range(3)]#duplicating this three times to make a grid


        def make_move(row, col):#the code so the player can click a button to make a move
            nonlocal current_player
            nonlocal board
            nonlocal buttons
            #The [row][col] si the coords of the button clicked
            if board[row][col] == "":#First check if the button is empty
                board[row][col] = current_player#Then change the button the whatever the current player is
                buttons[row][col].config(text = current_player)#changing the text of the button to the current player
                check_winner()#Check winner after each turn
                if current_player == "X":#Changing the current player after each turn
                    current_player = "O"
                else:
                    current_player = "X"

        #Buttons for the game
        buttons = []
        for i in range(3):#Three rows for buttons
            row = []#Button rows
            for r in range(3):#Three columns per row for the buttons
                button = tk.Button(TTT, text = "", font = pixel_font_buttons, width = 15, height = 3, padx= 4,
                                    command = lambda i = i, r = r: make_move(i, r))#Creating the buttons with I and R being the coordinates
                #this is so we know which button was pressed
                button.grid(row = i, column = r, padx = 5, pady = 5)#Place the buttons in a grid, the padding is the lines
                row.append(button)#Adding the button to the row
            buttons.append(row)#Adding the rows to the buttons so they are now in a list so we can keep track of them

        def check_winner():#Checking if there is a winner
            nonlocal board
            nonlocal current_player
            winning = (board[0], 
                        board[1], 
                        board[2],#checking the rows
                        [board[i][0] for i in range(3)],#column one
                        [board[i][0] for i in range(3)],#columnc 2
                        [board[i][0] for i in range(3)],#Column 3
                        [board[i][i] for i in range(3)],#Diagonal
                        [board[i][2-i] for i in range(3)])
            
            for win in winning:
                if win[0] == win[1] == win[2] != "":#If all three values in a row are the same and not empty
                    print(f"wins")
            if all(board[i][r] != "" for i in range(3) for r in range(3)):#If all buttons are filled but no winner
                print("Tie")

        TTT.mainloop()



def Memory():
    global memory_counter
    memory = tk.Toplevel(root)
    memory.title("Memory Mania")
    root.geometry("900x800")
    root.resizable(False, False)  # stop the resizing of the window
    if memory_counter < 1:
        memory_counter += 1



    memory.mainloop()

def blackjack():

    blackjack = tk.Toplevel(root)
    blackjack.title("Memory Mania")
    root.geometry("900x800")
    root.resizable(False, False)  # stop the resizing of the window



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
        "You can either enter one letter or a whole word \nBUT the letters in the word are not counted as guessed\n" \
        "so consider  very carefully.\n" \
        "You have 10 lives, and everytime you get a word or letter wrong, \nyou will lose a life\n" \
        "and the man gets one step closer to being hanged...\n" \
        "Lose all your lives and the man DIES!!!(dun dun dun)\n" \
        "Guess the word correctly and you can move on to the next word!!(yay!!)\n" \
            "The words are divided into 3 difficulties: easy, medium and hard.\n" \
                "each difficulty gives you a different amount of points:\n" \
                    "easy = 1 point, medium = 2 points, hard = 3 points\n" \
                        "The points will then be counted and put on a leaderboard.\n" \
                            "Good luck and don't let the man die...", font = pixel_font_buttons_small, 
                                fg = "#0D3B66", bg = "#FAF0CA", justify = "center")
    def TTT_help():
        nonlocal changing_label
        changing_label.config(text = "sdlkhflskdjf", font = pixel_font_buttons_small, 
                            fg = "#0D3B66", bg = "#FAF0CA", justify = "center")

    help_label = tk.Label(help, text = "What do you need help with?", font = pixel_font_buttons_hangman, 
                          fg = "#0D3B66", bg = "#FAF0CA")
    changing_label = tk.Label(help, text = "Click the buttons below to get help with each game", 
                             font = pixel_font_buttons_small, fg = "#0D3B66", bg = "#FAF0CA")
    hangman_help_button = tk.Button(help, text = "Hangman help?", 
                                    command=hangman_help, 
                                      font = pixel_font_buttons_hangman, 
                                      fg = "#FAF0CA", bg = "#0D3B66", 
                                      relief = "flat")
    TTT_help_button = tk.Button(help, text = "Tic Tac Toe help?", 
                                   command=TTT_help, 
                                     font = pixel_font_buttons_hangman, 
                                     fg = "#FAF0CA", bg = "#0D3B66", 
                                     relief = "flat")
    memory_help_button = tk.Button(help, text = "Memory Game help?", 
                                   command=TTT_help, 
                                     font = pixel_font_buttons_hangman, 
                                     fg = "#FAF0CA", bg = "#0D3B66", 
                                     relief = "flat")
    blackjack_help_button = tk.Button(help, text = "Black Jack help?", 
                                   command=TTT_help, 
                                     font = pixel_font_buttons_hangman, 
                                     fg = "#FAF0CA", bg = "#0D3B66", 
                                     relief = "flat")
    help_label.pack(pady = 10)
    changing_label.pack(pady = 10)
    TTT_help_button.pack(pady = 20, padx = 20)
    hangman_help_button.pack(pady = 20, padx = 20)
    memory_help_button.pack(pady = 20, padx = 20)
    blackjack_help_button.pack(pady = 20, padx = 20)



root.title("Main Menu")

hangman_image = Image.open("Python/hangyman.jpg").resize((200, 200))
hangman_image = ImageTk.PhotoImage(hangman_image)

help_button = tk.Button(root, text = "?", command = help, 
                        font = pixel_font_buttons_small, fg = "#FAF0CA",
                        bg = "#0D3B66", height = 1, width = 1).grid(
                            row = 0, column=2, sticky = "ne", padx = 10, pady = 10
                        )

frame_hangman = tk.Frame(root, bg = "#000000", borderwidth=5, relief="raised")
frame_hangman.grid(row = 1, column = 0, pady = 50, padx = 10)
hangman_button = tk.Button(frame_hangman, image = hangman_image, command = hangman, 
                           font = pixel_font_buttons , 
                           fg = "#FAF0CA", bg = "#0D3B66", 
                           borderwidth= 0, relief="raised",
                           padx = 10, pady = 10)
hangman_button.pack()

frame_ttt = tk.Frame(root, bg = "#000000")
frame_ttt.grid(row = 1, column = 1, pady = 50, padx = 10)
Stictactoe_image = tk.Label(frame_ttt, image = hangman_image)
Stictactoe_image.pack()
Stictactoe_button = tk.Button(frame_ttt, text = "Super Tic Tac Toe",
                               command = Stictactoe, 
                               font = pixel_font_buttons, fg = "#FAF0CA", 
                               bg = "#0D3B66", borderwidth = 0, 
                               pady = 10, padx = 10)
Stictactoe_button.pack()

Memory_button = tk.Button(root, text = "Memory Mania", command = Memory, 
                          font = pixel_font_buttons, fg = "#FAF0CA", 
                          bg = "#0D3B66", borderwidth = 0, 
                          padx = 45, pady = 10).grid(row = 4, 
                                                     column = 0, rowspan = 2, 
                                                     pady = 50, padx = 85)

blackjack_button = tk.Button(root, text = "BlackJack", command = blackjack, 
                             font = pixel_font_buttons, fg = "#FAF0CA",
                               bg = "#0D3B66", borderwidth = 0, padx = 75, pady = 10).grid(row = 4, column = 1, pady = 50, padx = 5)



root.mainloop()