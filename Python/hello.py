"""My Game Compendium.

This is my game compedium it contains the games, Blackjack, Super Tic Tac Toe
and Hangman.
When you press play there is a button which allows you to choose which game
you want to play.
Have fun playing!!
"""

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.font import Font  # So I can use fonts in the games and menu
import random  # For hangman and blackjack
import customtkinter

root = tk.Tk()
root.geometry("955x860")  # The size of the window
root.resizable(False, False)  # stop the resizing of the window
root.configure(bg="#FAF0CA")  # The background color of the window

customtkinter.FontManager.load_font("Python/VT323/VT323-Regular.ttf")
customtkinter.FontManager.load_font("Python/Nosifer/Nosifer-Regular.ttf")

pixel_font_title = Font(family="VT323", size=70)
pixel_font_buttons = Font(family="VT323", size=30)
pixel_font_buttons_ttt = Font(family="VT323", size=26)
pixel_font_labels = Font(family="VT323", size=40)
pixel_font_buttons_hangman = Font(family="VT323", size=20)
pixel_font_buttons_small = Font(family="VT323", size=15)
scary_font_label = Font(family="Nosifer", size=20)

Title = tk.Label(
    root, text="Game compedium", font=pixel_font_title, fg="#0D3B66",
    bg="#FAF0CA"
)
Title.grid(row=0, column=0, columnspan=3, pady=0, padx=210)
# Stand in for the title, I willl change later

scores = {}


def hangman():
    """Hangman game.

    This is the hangman game.
    It is a word guessing game where the person guesses a letter or a word
    and if its right nothing will happen to the man
    if its wrong the man will lose a life
    """
    global scores
    # Using a hangman tut from Data Science with Onur
    # Create a Cool Hangman Game in Python Using TKInter – Step-by-Step Guide!
    words = {
        "easy": [
            "cat",
            "dog",
            "sun",
            "ball",
            "car",
            "big",
            "sad",
            "hot",
            "red",
            "eat",
            "tree",
            "house",
            "flower",
        ],
        "medium": [
            "memento",
            "killer",
            "common",
            "season",
            "theater",
            "garden",
            "holiday",
            "morning",
            "mother",
        ],
        "hard": [
            "macabre",
            "prediction",
            "whiskey",
            "jazz",
            "klutz",
            "sphinx",
            "executioner",
            "frequency",
            "xylophone",
        ],
    }

    letters_guessed = []  # Storing letters guessed

    lives = 12  # Number of lives user has

    score = 0  # The users score

    hangman = tk.Toplevel(root)  # A new window for hangman
    hangman.title("Hangman")
    hangman.geometry("800x850")
    hangman.resizable(False, False)  # stop the resizing of the window
    hangman.configure(bg="#FAF0CA")  # The background color of the window

    def back_to_menu():
        """Go back to the main menu."""
        root.lift()
        root.deiconify()

    back_button = tk.Button(hangman, text="See\nmenu",
                            command=back_to_menu,
                            font=pixel_font_buttons_small,
                            fg="#FAF0CA",
                            bg="#0D3B66",
                            borderwidth=0,
                            padx=10,
                            pady=0)
    back_button.pack(pady=10, padx=5, side="right", anchor="n")

    head = tk.Label(
        hangman,
        text="Guess the word, \nor the man gets hanged",
        font=scary_font_label,
        fg="#CC0000",
        bg="#FAF0CA",
    )  # heading

    head.pack(pady=5)

    difficulty = random.choice(list(words))
    # Choosing a random difficulty first
    word = random.choice(words[difficulty])
    # Then choosing a random word
    guessed = ["_ "] * len(word)
    # Number of lines = number of letters in word for user to guess,
    # each line will be replaced when user guesses correctly

    enter = tk.Entry(hangman, font=pixel_font_buttons, bg="#FAF0CA")
    # A textbox where the user can enter their guesses(single line)
    enter.pack(pady=10)

    label = tk.Label(
        hangman, text="_ " * len(word), font=pixel_font_labels, bg="#FAF0CA"
    )
    # the lines to show how many letters are in the word
    label.pack(pady=5)

    letters = tk.Label(
        hangman,
        text="Wrong Letters/Words guessed: ",
        wraplength=700,
        font=pixel_font_buttons_hangman,
        bg="#FAF0CA",
    )
    # To show the user what letters they have guessed wrong
    letters.pack(pady=5)

    liveslabel = tk.Label(
        hangman,
        text=f"Lives left until the man gets " f"hanged: {lives}",
        font=pixel_font_buttons_hangman,
        bg="#FAF0CA",
    )
    liveslabel.pack(pady=5)

    def check(event=None):
        """To check if the user guessed a letter in the word."""
        nonlocal lives  # Accessing lives outside the function
        nonlocal guessed
        nonlocal score
        nonlocal head
        nonlocal difficulty
        nonlocal word
        nonlocal letters_guessed

        guess = enter.get()
        # Getting the letter/word guessed by the user
        guess = guess.lower()

        enter.delete(0, "end")
        # clearing the Entrybox thing after each use

        if guess in letters_guessed:
            return

        if guess in word.lower():

            for i in range(len(word)):

                if word[i] == guess:

                    guessed[i] = guess
                    # Replace the line with the letter if they guess correctly

                    label.config(text="".join(guessed))
                    # to join all the letters and lines together
                    # + updating the label

            if guess == word.lower() or "".join(guessed) == word:
                # If the user guesses the whole word or all the letters

                guessed = guess
                # Replace the line with the letter if they guesses correctly

                label.config(text="".join(word))
                # to join all the letters and lines together
                # + updating the label

                checkbutton.config(command=nextword, text="Next word")
                # giving the option to change the word

                head.config(
                    text="You guessed the word!!\n"
                    "Click next word to continue playing"
                )
                # Changing the text to show they won
                enter.config(state="disabled")
                # disabling the enter box so they cant keep guessing
                # adding the score depending on what word they guess
                if difficulty == "easy":
                    score += 1
                elif difficulty == "medium":
                    score += 2
                elif difficulty == "hard":
                    score += 3

        if guess not in word.lower() and guess not in letters_guessed:

            lives = lives - 1

            liveslabel.config(text=f"Lives left until the man"
                              f" gets hanged: {lives}")

            if guess not in letters_guessed:

                letters_guessed.append(guess)
                # Adding the wrong guess to the list

                letters.config(
                    text=f"Wrong Letters/Words guessed:"
                    f"{', '.join(letters_guessed)}"
                )
                # Showing the user what they guessed wrong

            drawman(lives)  # Draw the man!!

        if lives == 0:
            drawman(lives)  # Draw the man(last time...)

            head.config(
                text=f"Uh oh!! The man is dead...\n" f"The word was {word}",
                font=scary_font_label,
                fg="#CC0000",
                bg="#FAF0CA",
            )
            enter.config(state="disabled")
            # Disabling the entry box so the player can't keep guessing
            hangman.unbind("<Return>")
            # Unbinding the enter key so it cant be pressed
            # Unbinding the button so it cant be clicked
            # I learnt this from the yt channel Tkinter.com
            # Disabling the button so the player can't keep losing lives
            letters.pack_forget()
            enter.pack_forget()
            # pack_forget removes the wiget from the window so the player
            # cant keep guessing after they lose

            liveslabel.config(text="Do you want to add your\n"
                              "score to the leaderboard?", fg="#0D3B66")
            checkbutton.config(command=scoreboard, text="Open Leaderboard")

    def nextword(event=None):
        """Go to the next word.

        This function is called on when the player wants to go to the
        next word after they have guessed the current one
        """
        nonlocal word
        nonlocal guessed
        nonlocal difficulty

        checkbutton.config(command=check, text="Check letter")
        # Changing back the button

        head.config(
            text="Guess the word,\n or the man gets hanged",
            font=scary_font_label,
            fg="#CC0000",
            bg="#FAF0CA",
        )
        enter.config(state="normal")

        difficulty = random.choice(list(words))
        # Choosing a random difficulty first
        word = random.choice(words[difficulty])
        # Then choosing a random word
        guessed = ["_ "] * len(word)
        # Number of lines = number of letters in word for user to guess,
        # each line will be replaced when user guesses correctly

        label.config(text="_ " * len(word))  # Resetting the lines

        letters.config(text=f"Wrong Letters/Words guessed: ")
        # Resetting the wrong letters guessed

        letters_guessed.clear()  # Clearing the list of wrong letters guessed

    hangman.bind("<Return>", check)
    # So user can also presses enter to check their guess

    checkbutton = tk.Button(
        hangman,
        text="Check letter",
        font=pixel_font_buttons_hangman,
        bg="#0D3B66",
        fg="#FAF0CA",
        command=lambda: check(),
        pady=0,
        padx=20,
    )  # To check the users guesses
    # lambda is like a one off function. We can use the function name again
    # elsewhere in the code without being affected by this function

    checkbutton.pack(pady=5)

    def scoreboard():
        """Display the scoreboard."""
        scoreboard_window = tk.Toplevel(hangman)
        scoreboard_window.title("Hangman scores")
        scoreboard_window.geometry("500x800")
        scoreboard_window.resizable(False, False)
        # stop the resizing of the window
        scoreboard_window.configure(bg="#FAF0CA")
        # The background color of the window

        name_label = tk.Label(
            scoreboard_window,
            text="Please enter a new name",
            fg="#0D3B66",
            bg="#FAF0CA",
            font=pixel_font_labels,
        )
        name_label.pack()
        nameEnter = tk.Entry(scoreboard_window, bg="#FAF0CA",
                             font=pixel_font_labels)
        nameEnter.pack()
        name_warning = tk.Label(
            scoreboard_window,
            text="Please enter an original name under 7 letters",
            fg="#0D3B66",
            bg="#FAF0CA",
            font=pixel_font_buttons_hangman,
        )
        name_warning.pack(pady=5)

        def get_name():
            """Get the name of the player."""
            # I used a tutorial by Tutorialspoint for the scroll bar
            checkbutton.config(state="disabled")
            value = nameEnter.get()
            if len(value) <= 6 and value not in scores.keys():
                confirmNamewin = tk.Toplevel(hangman)
                confirmNamewin.title("Hangman scores")
                confirmNamewin.geometry("400x600")
                confirmNamewin.resizable(False, False)
                confirmNamewin.grid()

                scrollframe = tk.Frame(confirmNamewin, bg="#FAF0CA")
                scrollframe.grid(row=0, column=0, sticky="nsew")

                canvasScroll = tk.Canvas(scrollframe, bg="#FAF0CA")
                # yview makes the scroll bar control canvas vertical scroll
                scrollbar = tk.Scrollbar(
                    scrollframe, orient="vertical", command=canvasScroll.yview
                )
                scrollbar.grid(row=0, column=1, sticky="ns")
                canvasScroll.configure(yscrollcommand=scrollbar.set)

                content = tk.Frame(canvasScroll, bg="#FAF0CA")
                content.grid(row=0, column=0, sticky="nsew")
                content.rowconfigure(0, weight=1)
                content.columnconfigure(0, weight=1)

                # Allow for other widgets to be in the canvas
                canvasScroll.create_window((0, 0), window=content,
                                           anchor="nw")
                canvasScroll.grid(row=0, column=0, sticky="nsew")
                # make scroll bar expand to fit to window
                scrollframe.bind(
                    "<Configure>",
                    lambda e: canvasScroll.configure(
                        scrollregion=canvasScroll.bbox("all")
                    ),
                )

                # stop the resizing of the window
                confirmNamewin.configure(bg="#FAF0CA")
                scoreboard_window.destroy()
                scores[value] = score
                sortedscores = dict(sorted(scores.items(),
                                           key=lambda item: item[1],
                                           reverse=True))
                # sorting the dictionary
                # save the scores to a dictionary with a name and score
                title_score_UN = tk.Label(
                    content,
                    text="Name",
                    font=pixel_font_labels,
                    fg="#0D3B66",
                    bg="#FAF0CA",
                )
                # spot where name is
                title_score_S = tk.Label(
                    content,
                    text="Score",
                    font=pixel_font_labels,
                    fg="#0D3B66",
                    bg="#FAF0CA",
                )
                title_score_UN.grid(row=0, column=0, padx=40, pady=5)
                title_score_S.grid(row=0, column=1, padx=40, pady=5)
                # putting them in a grid so they can stack like a leaderboard
                line = 1
                # The row the name and score are on

                for i, r in sortedscores.items():
                    # the players score
                    scorey = tk.Label(
                            content,
                            text=r,
                            bg="#FAF0CA",
                            fg="#0D3B66",
                            font=pixel_font_labels
                            )
                    # the players name
                    namey = tk.Label(
                        content,
                        text=i,
                        bg="#FAF0CA",
                        fg="#0D3B66",
                        font=pixel_font_labels
                        )
                    namey.grid(row=line, column=0, padx=40, pady=5)
                    scorey.grid(row=line, column=1, padx=40, pady=5)
                    line += 1

                    # make it enlarge into the window
                    confirmNamewin.columnconfigure(0, weight=1)
                    confirmNamewin.rowconfigure(0, weight=1)
                    scrollframe.columnconfigure(0, weight=1)
                    scrollframe.rowconfigure(0, weight=1)
            else:
                name_warning.config(fg="#FF0000")

        confirmName = tk.Button(
            scoreboard_window,
            text="Confirm name",
            command=get_name,
            bg="#0D3B66",
            fg="#FAF0CA",
        )
        confirmName.pack(pady=10)

    canvas = tk.Canvas(
        hangman, width=400, height=350, bg="#FAF0CA", highlightthickness=0
    )

    canvas.pack(pady=2)

    def drawman(lives):
        """To draw the man.

        we will draw the man using canvas with lines and coordinates.
        There will be 6 strokes each corresponding to a life the player has.
        When the player guesses wrong a stroke will be added.
        this function is called on each time the player loses a life.
        """
        if lives == 11:  # rim

            canvas.create_line(150, 100, 240, 100)

        elif lives == 10:  # hat

            canvas.create_rectangle(180, 75, 220, 100)

        elif lives == 9:

            canvas.create_line(100, 300, 100, 50)  # Pole

        elif lives == 8:

            canvas.create_line(50, 300, 300, 300)  # Base

        elif lives == 7:

            canvas.create_line(100, 50, 300, 50)  # high frame

        elif lives == 6:

            canvas.create_line(200, 50, 200, 75)  # String

        elif lives == 5:

            canvas.create_oval(180, 100, 220, 140)  # Head

        elif lives == 4:

            canvas.create_line(200, 140, 200, 220)  # body

        elif lives == 3:

            canvas.create_line(200, 140, 260, 200)  # arm1

        elif lives == 2:

            canvas.create_line(200, 140, 140, 200)  # arm2

        elif lives == 1:

            canvas.create_line(200, 220, 260, 240)  # leg1

        elif lives == 0:

            canvas.create_line(200, 220, 140, 240)  # leg2


def Stictactoe():
    """Super Tic Tac Toe game.

    When a player presses the button it will run this function and open
    up a menu giving you a choice of either playing with a friend or a bot
    """
    TTT = tk.Toplevel(root)
    TTT.title("Choose your gamemode")
    TTT.title("Tic Tac Toes")
    TTT.geometry("480x300")
    TTT.resizable(False, False)
    TTT.configure(bg="#FAF0CA")  # The background color of the window
    TTT_title = tk.Label(
        TTT,
        text="Choose your gamemode",
        font=pixel_font_labels,
        fg="#0D3B66",
        bg="#FAF0CA",
    )
    TTT_title.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

    def Stictactoe_friend():
        """Play Super Tic Tac Toe against a friend.

        The player changes each time the player makes a move and the buttons
        will change accordingly
        """
        global pixel_font_buttons_ttt
        global pixel_font_labels
        FTTT = tk.Toplevel(TTT)
        FTTT.title("Tic Tac Toes but you aren't lonely!")
        FTTT.geometry("805x875")
        FTTT.resizable(False, False)  # stop the resizing of the window
        FTTT.configure(bg="#FAF0CA")  # The background color of the window
        current_player = "X"  # X is the current player
        # I am using a tutorial by Alina Chudnova but
        # I modified it to make it super
        # I used codingspots ultimate tictactoe video
        # for ideas
        # name of the video:
        # Build a Tic-Tac-Toe Game with Python & Tkinter | Tutorial
        heading_frame = tk.Frame(FTTT, bg="#FAF0CA")
        heading_frame.grid(row=0, column=0, columnspan=5)

        def back_to_menu():
            """Go back to the main menu."""
            root.lift()
            root.deiconify()

        back_button = tk.Button(heading_frame, text="See\nmenu",
                                command=back_to_menu,
                                font=pixel_font_buttons_small,
                                fg="#FAF0CA",
                                bg="#0D3B66",
                                borderwidth=0,
                                padx=10,
                                pady=0)
        back_button.grid(row=0, column=3, columnspan=2,
                         pady=10, padx=5, sticky="ne")
        FTTT_title = tk.Label(
            heading_frame,
            text="Super Tic Tac Toe with a buddy!!",
            font=pixel_font_labels,
            fg="#0D3B66",
            bg="#FAF0CA",
        )
        FTTT_title.grid(row=0, column=0, columnspan=3, pady=10, padx=10)
        # Giving our board a value
        board = [
            [[["" for i in range(3)] for r in range(3)] for j in range(3)]
            for k in range(3)
        ]
        # I creates the first row, r creates the first subboard,
        # j creates the first row of subboards, k creates the bigger board
        subboard_winner = [["" for i in range(3)] for r in range(3)]
        # Creating a way to store all the winners of the subboard
        # These subboards function as a section in tic tac toe

        allowed_frame_coords_x = ""
        allowed_frame_coords_y = ""
        # The coordinates of the only frame the user is able to move in

        def make_move(mainrow, maincol, subrow, subcol):
            """Code so the player can click a button to make a move."""
            nonlocal current_player
            nonlocal board
            nonlocal buttons
            nonlocal allowed_frame_coords_x
            nonlocal allowed_frame_coords_y
            nonlocal subboard_winner
            # The the mainrow maincol determines which frame
            # the button picked is
            # The subrow subcol determines which button inside the
            # frame was clicked
            if (
                allowed_frame_coords_x == ""
                and allowed_frame_coords_y == ""
                and board[mainrow][maincol][subrow][subcol] == ""
            ):
                board[mainrow][maincol][subrow][subcol] = current_player
                # Turning all the subboards blue except those that are won
                # or the one that we are moving in
                check_winner_sub(mainrow, maincol)
                # check if the subboard fo these coords wins
                check_winner_main()  # Check if main board wins
                for i in range(3):
                    for r in range(3):
                        if subboard_winner[i][r] == "":
                            subboards[i][r].config(bg="#EE964B")
                if subboard_winner[subrow][subcol] == "":
                    allowed_frame_coords_x = subrow
                    allowed_frame_coords_y = subcol
                    if subboard_winner[subrow][subcol] == "":
                        # If the target board was not won then...
                        subboards[subrow][subcol].config(bg="#0D3B66")
                        # Change color of target
                else:
                    allowed_frame_coords_x = ""
                    allowed_frame_coords_y = ""
                    # If the subboard is won highlight all not won subboards
                    for i in range(3):
                        for r in range(3):
                            if subboard_winner[i][r] == "":
                                subboards[i][r].config(bg="#0D3B66")

                # Then change the button the whatever the current player is
                if current_player == "O":  # Changing the color of the square
                    buttons[mainrow][maincol][subrow][subcol].config(
                        text=current_player, bg="#0000FF"
                    )
                else:
                    buttons[mainrow][maincol][subrow][subcol].config(
                        text=current_player, bg="#FF0000"
                    )
                # changing the text of the button to the current player
                if current_player == "X":
                    # Changing the current player after each turn
                    current_player = "O"
                else:
                    current_player = "X"

                    # First check if the button is empty
                    # Then check if the button is in the allowed frame
            elif (
                board[mainrow][maincol][subrow][subcol] == ""
                and allowed_frame_coords_x == mainrow
                and allowed_frame_coords_y == maincol
            ):
                # Turning all the subboards blue except those that are won
                # or the one that we are moving in
                for i in range(3):
                    for r in range(3):
                        if subboard_winner[i][r] == "":
                            subboards[i][r].config(bg="#EE964B")
                if subboard_winner[subrow][subcol] == "":
                    # If the target board was not won then...
                    subboards[subrow][subcol].config(bg="#0D3B66")

                # Change color of target

                board[mainrow][maincol][subrow][subcol] = current_player
                # Check if the next subboard is
                check_winner_sub(mainrow, maincol)
                # check if the subboard fo these coords wins
                check_winner_main()  # Check if main board wins
                if subboard_winner[subrow][subcol] == "":
                    # If isn't then change allowed coords to next subboard
                    allowed_frame_coords_x = subrow
                    allowed_frame_coords_y = subcol
                else:
                    # If it is then allow the player to move anywhere
                    allowed_frame_coords_x = ""
                    allowed_frame_coords_y = ""
                    # If the subboard is won highlight all not won subboards
                    for i in range(3):
                        for r in range(3):
                            if subboard_winner[i][r] == "":
                                subboards[i][r].config(bg="#0D3B66")
                # Then change the button the whatever the current player is
                if current_player == "O":  # Changing the color of the square
                    buttons[mainrow][maincol][subrow][subcol].config(
                        text=current_player, bg="#0000FF"
                    )
                else:
                    buttons[mainrow][maincol][subrow][subcol].config(
                        text=current_player, bg="#FF0000"
                    )
                # changing the text of the button to the current player
                if current_player == "X":
                    # Changing the current player after each turn
                    current_player = "O"
                else:
                    current_player = "X"

        def check_winner_main():
            """Check if there is a winner on the main board."""
            nonlocal board
            nonlocal current_player
            nonlocal subboard_winner
            winning = (
                subboard_winner[0],
                subboard_winner[1],
                subboard_winner[2],  # checking the rows
                [subboard_winner[i][0] for i in range(3)],  # column one
                [subboard_winner[i][1] for i in range(3)],  # columnc 2
                [subboard_winner[i][2] for i in range(3)],  # Column 3
                [subboard_winner[i][i] for i in range(3)],  # Diagonal
                [subboard_winner[i][2 - i] for i in range(3)],
            )  # another diagonal

            for win in winning:
                if (
                    win[0] == win[1] == win[2] != ""
                ):  # If all three values in a row are the same and not empty
                    FTTT_title.config(text=f"{win[0]} wins!")
                    if win[0] == "O":
                        FTTT.config(bg="#0000FF")
                    else:
                        FTTT.config(bg="#FF0000")
                    for i in range(3):
                        for r in range(3):
                            for j in buttons[i][r]:
                                # Iterating through the list
                                for k in j:
                                    # go through and disble all buttons 1 by 1
                                    k.config(state="disabled")
                                    # Making the button in the frame dissabled
            if all(
                subboard_winner[i][r] != "" for i in range(3)
                for r in range(3)
            ):
                # If all buttons are filled but no winner
                FTTT_title.config(text="Tie!!")
                for i in range(3):
                    for r in range(3):
                        for j in buttons[i][r]:  # Iterating through the list
                            for k in j:
                                # go through and disble all buttons 1 by 1
                                k.config(state="disabled")
                                # Making each button in that frame dissabled
            # Iterating through each square

        def check_winner_sub(mainrow, maincol):
            """Check the winner in each subboard.

            Checking if there is a winner for sub
            These coords are used for the subboard_check var
            """
            nonlocal current_player
            nonlocal board
            nonlocal subboard_winner
            subboard_check = board[mainrow][maincol]
            # Coordinates of subboard of the button that was just clicked
            winning = (
                subboard_check[0],
                subboard_check[1],
                subboard_check[2],  # checking the rows
                [subboard_check[i][0] for i in range(3)],  # column one
                [subboard_check[i][1] for i in range(3)],  # columnc 2
                [subboard_check[i][2] for i in range(3)],  # Column 3
                [subboard_check[i][i] for i in range(3)],  # Diagonal
                [subboard_check[i][2 - i] for i in range(3)],
            )  # Diagonal2

            for win in winning:
                if (
                    win[0] == win[1] == win[2] != "" and win[0] != "T"
                ):  # If all three values in a row are the same and not empty
                    # take note of who won the subboard in the nested list
                    subboard_winner[mainrow][maincol] = current_player
                    if subboard_winner[mainrow][maincol] == "X":
                        subboards[mainrow][maincol].config(bg="#FF0000")
                    else:  # Changing the colors to match the winners
                        subboards[mainrow][maincol].config(bg="#0000FF")
                    # Taking note of who won
                    for i in buttons[mainrow][maincol]:
                        # Iterating through the list
                        # Or 3rd list inside the buttons(row list)nested list
                        for r in i:
                            # Inside the list I iterate through each button
                            r.config(state="disabled")
                            # Making each button in that frame dissabled
                    return
            if all(
                subboard_check[i][r] != "" for i in range(3) for r in range(3)
            ):  # If all buttons are filled but no winner
                subboard_winner[mainrow][maincol] = "T"
                # To make confirm the board can no longer be played in
                subboards[mainrow][maincol].config(bg="grey")

        # Buttons for the game
        subboards = [["" for i in range(3)] for r in range(3)]
        # Store buttons in a frame to keep the seperate from other subboards
        buttons = [["" for i in range(3)] for r in range(3)]
        # These act as place holders as they are lists with sub lists inside
        # These allow us to determine coords of our buttons and stuff
        for d in range(3):  # creating the first row
            for r in range(3):  # creating the 3x3 grid structure
                # frame like divclass
                subboard_frame = tk.Frame(
                    FTTT,
                    bg="#EE964B",
                )
                subboard_frame.grid(row=d + 1, column=r, pady=5, padx=5)
                subboards[d][r] = subboard_frame

                # Creating the frame the buttons are gonna go inside
                # And then putting the frame into a grid structure
                # then add that to a nested list that stores it
                # and lets us edit exact frames through coords

                button_subboard = []
                # Where we append the button rows for 3x3 grid
                # buttons inside the subboard
                for j in range(3):  # Three rows for buttons
                    buttons_row = []  # One row of three buttons
                    for k in range(3):
                        # Three columns per row for the buttons
                        # Put the buttons into the frame
                        button = tk.Button(
                            subboard_frame,
                            text="",
                            font=pixel_font_buttons_ttt,
                            width=5,
                            height=1,
                            borderwidth=0,
                            bg="#F4D35E",
                            command=lambda d=d, r=r, j=j, k=k: make_move(d, r,
                                                                         j, k)
                        )
                        # providing numbers for the make move function
                        # when we make a move we take into consideration
                        # the subboard and button pressed
                        # this is so we know which button was pressed

                        # The first 2, D and R or m(main)row and m(main)col
                        # determine the frame the button is on and the second
                        # 2(J and K)subrow and subcol determine the coords of
                        #  button inside the frame.

                        button.grid(row=j, column=k, padx=5, pady=5)
                        # Place the buttons in a grid, the padding is
                        # the lines
                        buttons_row.append(button)
                        # Adding the button to a row
                    button_subboard.append(buttons_row)
                    # Adding the row to a 3x3 grid
                buttons[d][r] = button_subboard
                # Adding the grid into the buttons list.
                # changing the ""
                # from the list into our button 3x3 grid

    def Stictactoe_bot():
        """Bot for Super Tic Tac Toe.

        This is a bot that will play Super Tic Tac Toe with you however it
        is a completely random bot that will loop through coordinates until
        it finds a free button.
        """
        global pixel_font_buttons_ttt
        global pixel_font_labels
        BTTT = tk.Toplevel(TTT)
        BTTT.title("Tic Tac Toes but you ARE lonely!")
        BTTT.geometry("805x875")
        BTTT.resizable(False, False)  # stop the resizing of the window
        BTTT.configure(bg="#FAF0CA")  # The background color of the window

        current_player = "X"  # X is the current player
        # I'm using a tutorial by Alina Chudnova
        # but I modified it to make it super

        # Giving our board a value
        board = [
            [[["" for i in range(3)] for r in range(3)] for j in range(3)]
            for k in range(3)
        ]
        # I creates the first row, r creates the first subboard,
        # j creates the first row of subboards, k creates the bigger board
        subboard_winner = [["" for i in range(3)] for r in range(3)]
        # Creating a way to store all the winners of the subboard
        # These subboards function as a section in tic tac toe

        game_finished = False

        heading_frame = tk.Frame(BTTT, bg="#FAF0CA")
        heading_frame.grid(row=0, column=0, columnspan=5)

        def back_to_menu():
            """Go back to the main menu."""
            root.lift()
            root.deiconify()

        back_button = tk.Button(heading_frame, text="See\nmenu",
                                command=back_to_menu,
                                font=pixel_font_buttons_small,
                                fg="#FAF0CA",
                                bg="#0D3B66",
                                borderwidth=0,
                                padx=10,
                                pady=0)
        back_button.grid(row=0, column=3, columnspan=2,
                         pady=10, padx=5, sticky="ne")

        STTT_title = tk.Label(
            heading_frame,
            text="Super Tic Tac Toe, with a bot!",
            font=pixel_font_labels,
            fg="#0D3B66",
            bg="#FAF0CA",
        )
        STTT_title.grid(row=0, column=0, columnspan=3, pady=10)

        # Buttons for the game
        subboards = [["" for i in range(3)] for r in range(3)]
        # Store buttons in a frame to keep the seperate from other subboards
        buttons = [["" for i in range(3)] for r in range(3)]
        # These act as place holders as they are lists with sub lists inside
        # These allow us to determine coords of our buttons and stuff
        for d in range(3):  # creating the first row
            for r in range(3):  # creating the 3x3 grid structure
                # frame like divclass
                subboard_frame = tk.Frame(
                    BTTT,
                    bg="#EE964B",
                )
                subboard_frame.grid(row=d + 1, column=r, pady=5, padx=5)
                subboards[d][r] = subboard_frame
                # Creating the frame the buttons are gonna go inside
                # And then putting the frame into a grid structure
                # then add that to a nested list that stores it
                # and lets us edit exact frames through coords
                button_subboard = []
                # Where we append the button rows for 3x3 grid
                # buttons inside the subboard
                for j in range(3):  # Three rows for buttons
                    buttons_row = []  # One row of three buttons
                    for k in range(3):  # Three columns per row for buttons
                        # Put the buttons into the frame
                        button = tk.Button(
                            subboard_frame,
                            text="",
                            font=pixel_font_buttons_ttt,
                            width=5,
                            height=1,
                            borderwidth=0,
                            bg="#F4D35E",
                            command=lambda d=d, r=r, j=j, k=k: make_move(d, r,
                                                                         j, k)
                        )
                        # providing numbers for the make move function
                        # when we make a move we take into consideration the
                        # subboard and button pressed
                        # this is so we know which button was pressed

                        # The first 2, D and R or m(main)row and m(main)col
                        # determine the frame the button is on and
                        # the second 2(J and K)
                        # subrow and subcol determine
                        # the coords of the button inside the frame.

                        button.grid(row=j, column=k, padx=5, pady=5)
                        # Place buttons in a grid, the padding is the lines
                        buttons_row.append(button)
                        # Adding the button to a row
                    button_subboard.append(buttons_row)
                    # Adding the row to a 3x3 grid
                buttons[d][r] = button_subboard
                # change the "" from the nested list into the button 3x3 grid

        fm_mainrow = random.randint(0, 2)
        fm_maincol = random.randint(0, 2)
        fm_subrow = random.randint(0, 2)
        fm_subcol = random.randint(0, 2)
        # Making the bot make the first move to prevent any freezes when there
        # is only one avaliable space for the bot to move
        # fm stands for first move

        board[fm_mainrow][fm_maincol][fm_subrow][fm_subcol] = "O"
        buttons[fm_mainrow][fm_maincol][fm_subrow][fm_subcol].config(
            text="O", bg="#0000FF"
        )
        allowed_frame_coords_x = fm_subrow
        allowed_frame_coords_y = fm_subcol
        subboards[allowed_frame_coords_x][allowed_frame_coords_y].config(
            bg="#0D3B66"
            )

        def make_move(mainrow, maincol, subrow, subcol):
            """Code so the player can click a button to make a move."""
            nonlocal current_player
            nonlocal board
            nonlocal buttons
            nonlocal allowed_frame_coords_x
            nonlocal allowed_frame_coords_y
            nonlocal subboard_winner
            # mainrow maincol determines which frame the button picked is
            # subrow subcol determines which button in the frame was clicked
            if (
                allowed_frame_coords_x == ""
                and allowed_frame_coords_y == ""
                and board[mainrow][maincol][subrow][subcol] == ""
            ):
                board[mainrow][maincol][subrow][subcol] = current_player
                # Turning all the subboards blue except those that are won
                # or the one that we are moving in
                for i in range(3):
                    for r in range(3):
                        if subboard_winner[i][r] == "":
                            subboards[i][r].config(bg="#EE964B")
                check_winner_sub(mainrow, maincol)
                # check if subboard wins using the coordinates
                check_winner_main()  # Check if main board wins
                if subboard_winner[subrow][subcol] == "":
                    allowed_frame_coords_x = subrow
                    allowed_frame_coords_y = subcol
                    # If the target board was not won then...
                    subboards[subrow][subcol].config(bg="#0D3B66")
                    # Change color of target
                else:
                    allowed_frame_coords_x = ""
                    allowed_frame_coords_y = ""
                    # If the subboard is won highlight all not won subboards
                    for i in range(3):
                        for r in range(3):
                            if subboard_winner[i][r] == "":
                                subboards[i][r].config(bg="#0D3B66")
                # Then change the button the whatever the current player is
                if current_player == "O":  # Changing the color of the square
                    buttons[mainrow][maincol][subrow][subcol].config(
                        text=current_player, bg="#0000FF"
                    )
                else:
                    buttons[mainrow][maincol][subrow][subcol].config(
                        text=current_player, bg="#FF0000"
                    )
                # changing the text of the button to the current player
                if current_player == "X":  # Changing the current player
                    current_player = "O"
                    if game_finished is False:
                        # The bot making a move if its O
                        BTTT.after(
                            100,
                            TTT_bot_move,
                            allowed_frame_coords_x,
                            allowed_frame_coords_y,
                        )
                        # delaying the bot by 0.1 secconds to make
                        # it seem more natural
                else:
                    current_player = "X"

                    # First check if the button is empty
                    # Then check if the button is in the allowed frame
            elif (
                board[mainrow][maincol][subrow][subcol] == ""
                and allowed_frame_coords_x == mainrow
                and allowed_frame_coords_y == maincol
            ):
                # MAKE MOVE FIRST
                board[mainrow][maincol][subrow][subcol] = current_player
                # Turning all the subboards blue except those that are won
                # or the one that we are moving in
                for i in range(3):
                    for r in range(3):
                        if subboard_winner[i][r] == "":
                            subboards[i][r].config(bg="#EE964B")
                # Check if the next subboard is won
                check_winner_sub(mainrow, maincol)
                # check if the subboard fo these coords wins
                check_winner_main()  # Check if main board wins
                if subboard_winner[subrow][subcol] == "":
                    # If no change the allowed coords to the next subboard
                    allowed_frame_coords_x = subrow
                    allowed_frame_coords_y = subcol
                    # If the target board was not won then...
                    subboards[subrow][subcol].config(bg="#0D3B66")
                    # Change color of target
                else:
                    # If it is then allow the player to move anywhere
                    allowed_frame_coords_x = ""
                    allowed_frame_coords_y = ""

                # Then change the button the whatever the current player is
                if current_player == "O":  # Changing the color of the square
                    buttons[mainrow][maincol][subrow][subcol].config(
                        text=current_player, bg="#0000FF"
                    )
                else:
                    buttons[mainrow][maincol][subrow][subcol].config(
                        text=current_player, bg="#FF0000"
                    )
                # changing the text of the button to the current player
                if current_player == "X":  # Changing the current player
                    current_player = "O"
                    if game_finished is False:
                        # The bot only moves if its O
                        BTTT.after(
                            100,
                            TTT_bot_move,
                            allowed_frame_coords_x,
                            allowed_frame_coords_y,
                        )  # Make the bot move
                    # delay to the bots movements
                else:
                    current_player = "X"

        def TTT_bot_move(bot_allowed_frame_coords_x,
                         bot_allowed_frame_coords_y):
            """Bot makes a move.

            The bot will randomly choose coordinates to move in if the
            choosen coordinates are free it will make a move
            if they aren't the bot will randomise again until it finds
            a free button.
            """
            nonlocal board
            nonlocal current_player
            bot_coord_X = random.randint(0, 2)
            bot_coord_Y = random.randint(0, 2)
            nonlocal buttons
            nonlocal subboards
            nonlocal subboard_winner
            nonlocal allowed_frame_coords_x
            nonlocal allowed_frame_coords_y
            if allowed_frame_coords_x != "" and allowed_frame_coords_y != "":
                while (board[allowed_frame_coords_x][allowed_frame_coords_y]
                       [bot_coord_X][bot_coord_Y] != ""):
                    bot_coord_X = random.randint(0, 2)
                    bot_coord_Y = random.randint(0, 2)
                    # Rabdomise the coords until we find an empty button
                if (board[allowed_frame_coords_x][allowed_frame_coords_y]
                        [bot_coord_X][bot_coord_Y] == ""):
                    # Change the button to current player or player bot
                    board[allowed_frame_coords_x][allowed_frame_coords_y][
                        bot_coord_X][bot_coord_Y] = current_player
                    # Changing the color of the square depedning on the player
                    buttons[allowed_frame_coords_x][allowed_frame_coords_y][
                        bot_coord_X][bot_coord_Y].config(text=current_player,
                                                         bg="#0000FF")
                    check_winner_sub(allowed_frame_coords_x,
                                     allowed_frame_coords_y)
                    check_winner_main()
                    for i in range(3):
                        for r in range(3):
                            if subboard_winner[i][r] == "":
                                subboards[i][r].config(bg="#EE964B")
                    current_player = "X"

                    if subboard_winner[bot_coord_X][bot_coord_Y] == "":
                        allowed_frame_coords_x = bot_coord_X
                        allowed_frame_coords_y = bot_coord_Y
                        # if target board isn't won then change color
                        subboards[bot_coord_X][bot_coord_Y].config(
                            bg="#0D3B66"
                            )
                    else:
                        allowed_frame_coords_x = ""
                        allowed_frame_coords_y = ""
                        # If the subboard is won highlight
                        # all not won subboards
                        for i in range(3):
                            for r in range(3):
                                if subboard_winner[i][r] == "":
                                    subboards[i][r].config(bg="#0D3B66")
            else:
                # If allowed frame coords are either
                # empty or the subboard is won
                # check random frames until we find one that isn't won
                while True:
                    allowed_frame_coords_x = random.randint(0, 2)
                    allowed_frame_coords_y = random.randint(0, 2)
                    # If the frame isn't won then break the loop
                    if (subboard_winner[allowed_frame_coords_x]
                            [allowed_frame_coords_y] == ""):
                        break
                    # And choose a random button in that frame
                    # Then check random buttons until we find an empty one
                while True:
                    bot_coord_X = random.randint(0, 2)
                    bot_coord_Y = random.randint(0, 2)
                    # If the button is empty then break the loop
                    if (
                        board[allowed_frame_coords_x][allowed_frame_coords_y]
                            [bot_coord_X][bot_coord_Y] == ""):
                        break
                # Then make the bot make a move in the button

                # Make a move in the selected button
                board[allowed_frame_coords_x][allowed_frame_coords_y][
                    bot_coord_X][bot_coord_Y] = current_player
                buttons[allowed_frame_coords_x][allowed_frame_coords_y][
                    bot_coord_X][bot_coord_Y].config(text=current_player,
                                                     bg="#0000FF")
                check_winner_sub(allowed_frame_coords_x,
                                 allowed_frame_coords_y)
                check_winner_main()
                for i in range(3):
                    for r in range(3):
                        if subboard_winner[i][r] == "":
                            subboards[i][r].config(bg="#EE964B")
                current_player = "X"

                if subboard_winner[bot_coord_X][bot_coord_Y] == "":
                    # If it isn't change the allowed coords to next subboard
                    allowed_frame_coords_x = bot_coord_X
                    allowed_frame_coords_y = bot_coord_Y
                    subboards[bot_coord_X][bot_coord_Y].config(bg="#0D3B66")
                else:
                    # If it is then allow the player to move anywhere
                    allowed_frame_coords_x = ""
                    allowed_frame_coords_y = ""
                    for i in range(3):
                        for r in range(3):
                            if subboard_winner[i][r] == "":
                                subboards[i][r].config(bg="#0D3B66")
                # change allowed coords and color

        def check_winner_main():
            """Check if there is a winner in mainboard."""
            nonlocal board
            nonlocal current_player
            nonlocal subboard_winner
            nonlocal game_finished
            winning = (
                subboard_winner[0],
                subboard_winner[1],
                subboard_winner[2],  # checking the rows
                [subboard_winner[i][0] for i in range(3)],  # column one
                [subboard_winner[i][1] for i in range(3)],  # columnc 2
                [subboard_winner[i][2] for i in range(3)],  # Column 3
                [subboard_winner[i][i] for i in range(3)],  # Diagonal
                [subboard_winner[i][2 - i] for i in range(3)],
            )
            # another diagonal

            for win in winning:
                if win[0] == win[1] == win[2] != "" and win[0] != "T":
                    # If all three values in a row are the same and not empty
                    # nor tied
                    game_finished = True
                    STTT_title.config(text=f"{win[0]} wins!")
                    if win[0] == "O":
                        BTTT.config(bg="#0000FF")
                    else:
                        BTTT.config(bg="#FF0000")
                    for i in range(3):
                        for r in range(3):
                            for j in buttons[i][r]:
                                # Iterating through the list
                                for k in j:
                                    # go through and disble all buttons 1 by 1
                                    k.config(state="disabled")
                                    # Making each button
                                    # in that frame dissabled
                    return
                # prevent checking for a tie when winner is already found.
            if all(subboard_winner[i][r] != "" for i in range(3)
                   for r in range(3)):
                # If all buttons are filled but no winner
                game_finished = True
                STTT_title.config(text="Tie!!")
                for i in range(3):
                    for r in range(3):
                        for j in buttons[i][r]:  # Iterating through the list
                            for k in j:
                                # go through and disble all buttons 1 by 1
                                k.config(state="disabled")
                                # Making each button in that frame dissabled

        # Iterating through each square
        def check_winner_sub(mainrow, maincol):
            """Check if there is a winner for sub.

            These coords are used for the subboard_check var
            """
            nonlocal current_player
            nonlocal board
            nonlocal subboard_winner
            subboard_check = board[mainrow][maincol]
            # Coordinates of subboard of the button that was just clicked
            winning = (
                subboard_check[0],
                subboard_check[1],
                subboard_check[2],  # checking the rows
                [subboard_check[i][0] for i in range(3)],  # column one
                [subboard_check[i][1] for i in range(3)],  # columnc 2
                [subboard_check[i][2] for i in range(3)],  # Column 3
                [subboard_check[i][i] for i in range(3)],  # Diagonal
                [subboard_check[i][2 - i] for i in range(3)],
            )  # Diagonal2

            for win in winning:
                if win[0] == win[1] == win[2] != "":
                    # If all three values in a
                    # row are the same and not empty
                    # take note od who won the subboard in the nested list
                    subboard_winner[mainrow][maincol] = win[0]
                    # The winner is the first value out of the winning line
                    if subboard_winner[mainrow][maincol] == "X":
                        subboards[mainrow][maincol].config(bg="#FF0000")
                    else:  # Changing the colors to match the winners
                        subboards[mainrow][maincol].config(bg="#0000FF")
                    # Taking note of who won
                    for i in buttons[mainrow][maincol]:
                        # Iterating through the list
                        # Or 3rd list inside the buttons(row list)nested list
                        for r in i:
                            # Inside the list I iterate through each button
                            r.config(state="disabled")
                            # Making each button in that frame dissabled
                    return

            if all(
                subboard_check[i][r] != "" for i in range(3) for r in range(3)
            ):  # If all buttons are filled but no winner
                subboard_winner[mainrow][maincol] = "T"
                # To make confirm the board can no longer be played in
                for i in buttons[mainrow][maincol]:
                    # Iterating through the list
                    # Or 3rd list inside the buttons(row list)nested list
                    for r in i:
                        # Inside the list I iterate through each button
                        r.config(state="disabled")
                subboards[mainrow][maincol].config(bg="grey")

    friend_button = tk.Button(
        TTT,
        text="Play with a friend",
        command=Stictactoe_friend,
        font=pixel_font_buttons_hangman,
        bg="#0D3B66",
        fg="#FAF0CA",
        borderwidth=0,
    )
    bot_button = tk.Button(
        TTT,
        text="Play with a bot",
        command=Stictactoe_bot,
        font=pixel_font_buttons_hangman,
        bg="#0D3B66",
        fg="#FAF0CA",
        borderwidth=0,
    )
    friend_button.grid(row=1, column=0, pady=20, padx=20)
    bot_button.grid(row=1, column=2, pady=20, padx=20)


nums = {}


def blackjack():
    """Game of blackjack.

    Displays the BlackJack game when the corresponding button is pressed.

    """
    player_num = 0
    # I am using a tutorial by codemy.com for this blackjack game
    # the tutorial is called:
    # Build A Blackjack Card Game - Python Tkinter GUI Tutorial 208
    blackjack = tk.Toplevel(root)
    blackjack.title("BlackJack")
    blackjack.geometry("1200x800")
    blackjack.resizable(False, False)  # stop the resizing of the window
    blackjack.config(bg="#0D3B66")  # bg of window

    def back_to_menu():
        """Go back to the main menu."""
        root.lift()
        root.deiconify()

    back_button = tk.Button(blackjack, text="See\nmenu",
                            command=back_to_menu,
                            font=pixel_font_buttons_small,
                            fg="#0D3B66",
                            bg="#FAF0CA",
                            borderwidth=0,
                            padx=10,
                            pady=0)
    back_button.pack(pady=10, padx=5, anchor="ne", side="right")

    def resize_cards(card):
        """Resize the images."""
        card_image = Image.open(card).resize((135, 190))
        cardimage_resized = ImageTk.PhotoImage(card_image)
        return cardimage_resized

    # creating the deck list first
    deck = []
    # we store cards of dealer and player
    dealer = []
    player = []
    # we store points of the dealer and player
    dealer_score = []
    player_score = []
    # keep track of amount of cards being dealt out
    dealer_cards = 0
    player_cards = 0
    # SCORE THE PLAYER HAS

    cardnum = tk.Label(
        blackjack,
        text=f"Cards left in deck: 52",
        font=pixel_font_buttons_hangman,
        fg="#FAF0CA",
        bg="#0D3B66",
    )
    jack_title = tk.Label(
        blackjack,
        text=f"Welcome to BlackJack",
        font=pixel_font_buttons_hangman,
        fg="#FAF0CA",
        bg="#0D3B66",
    )
    jack_title.pack()
    cardnum.pack()

    Mframe = tk.Frame(blackjack, bg="#FAF0CA")
    Mframe.pack(pady=5)

    # where cards will be displayed
    # frame with text around border
    Dframe = tk.LabelFrame(
        Mframe,
        text="Dealer",
        bg="#FAF0CA",
        fg="#0D3B66",
        bd=0,
        font=pixel_font_buttons_small,
        pady=5,
        padx=30,
    )
    Dframe.pack(padx=20, pady=5)

    Pframe = tk.LabelFrame(
        Mframe,
        text="Player",
        bg="#FAF0CA",
        fg="#0D3B66",
        bd=0,
        font=pixel_font_buttons_small,
        pady=5,
        padx=30,
    )
    Pframe.pack(padx=20)

    def openLB():
        """Open the area to enter your score and name."""
        sb_window = tk.Toplevel(blackjack)
        sb_window.title("Blackjack scores")
        sb_window.geometry("500x500")
        sb_window.resizable(False, False)
        # stop the resizing of the window
        sb_window.configure(bg="#FAF0CA")
        # The background color of the window
        label_name = tk.Label(
            sb_window,
            text="Please enter a new name",
            fg="#0D3B66",
            bg="#FAF0CA",
            font=pixel_font_labels,
        )
        label_name.pack()
        name_enter = tk.Entry(sb_window, bg="#FAF0CA",
                              font=pixel_font_labels)
        name_enter.pack()
        name_warning = tk.Label(
            sb_window,
            text="Please enter an orginal name under 7 letters",
            fg="#0D3B66",
            bg="#FAF0CA",
            font=pixel_font_buttons_hangman,
        )
        name_warning.pack(pady=5)

        def get_name():
            """Open the leaderboard."""
            global nums
            nonlocal player_num
            # I used a tutorial by Tutorialspoint for the scroll bar
            value = name_enter.get()
            if len(value) <= 6 and value not in nums.keys():
                shuffle_button.config(state="disabled")
                confirmNamewin = tk.Toplevel(blackjack)
                confirmNamewin.title("BlackJack scores")
                confirmNamewin.geometry("400x800")
                confirmNamewin.resizable(False, False)
                confirmNamewin.grid()
                # Add the players score into the dict
                nums[value] = player_num
                # Sort the dict by value in descending order
                sortednums = dict(sorted(nums.items(),
                                         key=lambda item: item[1],
                                         reverse=True))

                # frame holding the scrollbar and canvas
                scrollframe = tk.Frame(confirmNamewin, bg="#FAF0CA")
                scrollframe.grid(row=0, column=0, sticky="nsew")

                canvasScroll = tk.Canvas(scrollframe, bg="#FAF0CA")
                # yview makes the scroll bar control canvas vertical scroll
                scrollbar = tk.Scrollbar(
                    scrollframe, orient="vertical", command=canvasScroll.yview
                )
                scrollbar.grid(row=0, column=1, sticky="ns")
                canvasScroll.configure(yscrollcommand=scrollbar.set)

                # A frame which stores all the scrollable content
                content = tk.Frame(canvasScroll, bg="#FAF0CA")
                content.grid(row=0, column=0, sticky="nsew")
                # expanding the content to fit the window
                content.rowconfigure(0, weight=1)
                content.columnconfigure(0, weight=1)

                # Allow for other widgets to be in the canvas
                canvasScroll.create_window((0, 0), window=content,
                                           anchor="nw")
                canvasScroll.grid(row=0, column=0, sticky="nsew")
                # make scroll bar expand to fit to window
                scrollframe.bind(
                    "<Configure>",
                    lambda e: canvasScroll.configure(
                        scrollregion=canvasScroll.bbox("all")
                    ),
                )

                # stop the resizing of the window
                confirmNamewin.configure(bg="#FAF0CA")
                sb_window.destroy()

                # save the scores to a dictionary with a name and score
                title_score_UN = tk.Label(
                    content,
                    text="Name",
                    font=pixel_font_labels,
                    fg="#FAF0CA",
                    bg="#0D3B66",
                )
                # spot where name is
                title_score_S = tk.Label(
                    content,
                    text="Score",
                    font=pixel_font_labels,
                    fg="#FAF0CA",
                    bg="#0D3B66",
                )
                title_score_UN.grid(row=0, column=0, padx=40, pady=5)
                title_score_S.grid(row=0, column=1, padx=40, pady=5)
                # putting them in a grid so they can stack like a leaderboard
                line = 1
                # The row the name and score are on
                for i, r in sortednums.items():
                    # putting the score and name in dict
                    # into labels so the player can see them
                    scorey = tk.Label(
                        content,
                        text=r,
                        bg="#FAF0CA",
                        fg="#0D3B66",
                        font=pixel_font_labels,
                    )
                    namey = tk.Label(
                        content,
                        text=i,
                        bg="#FAF0CA",
                        fg="#0D3B66",
                        font=pixel_font_labels,
                    )
                    scorey.grid(row=line, column=1, padx=40, pady=5)
                    namey.grid(row=line, column=0, padx=40, pady=5)
                    line += 1

                    # make it enlarge into the window
                    confirmNamewin.columnconfigure(0, weight=1)
                    confirmNamewin.rowconfigure(0, weight=1)
                    scrollframe.columnconfigure(0, weight=1)
                    scrollframe.rowconfigure(0, weight=1)
            else:
                name_warning.config(fg="#FF0000")

        confirmName = tk.Button(
            sb_window, text="Confirm name", command=get_name, bg="#0D3B66",
            fg="#FAF0CA"
        )
        confirmName.pack(pady=10)

    def gamefin():
        """Occurs when game finishes.

        creating the leaderboard
        """
        hit_button.pack_forget()
        stand_button.pack_forget()

        GEscoreLabel = tk.Label(
            button_frame,
            text=f"You have a score of {player_num}\n"
            "would you like to put your score on "
            "the leaderboard?",
            font=pixel_font_buttons_hangman,
            fg="#FAF0CA",
            bg="#0D3B66",
        )
        GEscoreLabel.pack(padx=20, pady=5)

        shuffle_button.config(text="Open Leaderboard",
                              bg="#FAF0CA",
                              fg="#0D3B66",
                              command=openLB,
                              state="normal")

    # PLAYER GET CARD
    def player_hit():
        """Player pick up cards."""
        nonlocal player_cards
        if player_cards < 5:
            # making the get card lists
            # Use these lists to keep track of what cards each person has

            # FOR PLAYER
            # getting random card using random choice out of deck
            player_card = random.choice(deck)
            # remove card from deck
            deck.remove(player_card)
            # give card to player
            player.append(player_card)
            cardnum.config(text=f"Cards left in deck: {len(deck)}",
                           fg="#FAF0CA")
            # appending the value of the card too
            # stripping the text from the card value and making it only num
            # Using split and spliting it from the first _ and then int()
            pvalue = int(player_card.split("_", 1)[0])
            if pvalue == 14:
                if sum(player_score) + 11 > 21:
                    player_score.append(1)
                else:
                    player_score.append(11)
            elif pvalue == 11 or pvalue == 12 or pvalue == 13:
                player_score.append(10)
            else:
                player_score.append(pvalue)

            # Display cards
            # seeing which cards should be displayed in which spot
            if player_cards == 0:
                # resize card
                player_image_1 = resize_cards(f"Python/{player_card}.png")
                # output card
                player_card_1.config(image=player_image_1)
                # save card
                player_card_1.image = player_image_1
                player_cards += 1

            elif player_cards == 1:
                # resize card
                player_image_2 = resize_cards(f"Python/{player_card}.png")
                # output card
                player_card_2.config(image=player_image_2)
                # save card
                player_card_2.image = player_image_2
                player_cards += 1

            elif player_cards == 2:
                # resize card
                player_image_3 = resize_cards(f"Python/{player_card}.png")
                # output card
                player_card_3.config(image=player_image_3)
                # save card
                player_card_3.image = player_image_3
                player_cards += 1

            elif player_cards == 3:
                # resize card
                player_image_4 = resize_cards(f"Python/{player_card}.png")
                # output card
                player_card_4.config(image=player_image_4)
                # save card
                player_card_4.image = player_image_4
                player_cards += 1

            elif player_cards == 4:
                # resize card
                player_image_5 = resize_cards(f"Python/{player_card}.png")
                # output card
                player_card_5.config(image=player_image_5)
                # save card
                player_card_5.image = player_image_5
                player_cards += 1
        blackjack_score("player")
        # CHECK THIS

    # DEALER GET CARD
    def dealer_hit():
        """Dealer pick up cards."""
        nonlocal dealer_cards
        # if dealer has less than 5 cards
        if dealer_cards < 5:
            # FRO DEALER
            # getting random card using random choice out of deck
            dealer_card = random.choice(deck)
            # remove card from deck
            deck.remove(dealer_card)
            # give card to dealer
            dealer.append(dealer_card)
            # appending the value of the card too
            # stripping the text from the
            # card value and making it only num
            # Using split and spliting it from the first _ and then int()
            dvalue = int(dealer_card.split("_", 1)[0])
            if dvalue == 14:
                if sum(dealer_score) + 11 > 21:
                    # If adding 11 will bust add one
                    dealer_score.append(1)
                else:
                    dealer_score.append(11)
            elif dvalue == 11 or dvalue == 12 or dvalue == 13:
                dealer_score.append(10)
            else:
                dealer_score.append(dvalue)

            cardnum.config(text=f"Cards left in deck: {len(deck)}",
                           fg="#FAF0CA")

            # Display cards
            # seeing which cards should be displayed in which spot
            if dealer_cards == 0:
                # resize card
                dealer_image_1 = resize_cards(f"Python/{dealer_card}.png")
                # dealer image backside
                dealer_back = resize_cards(f"Python/back_card.png")
                # output backside
                dealer_card_1.config(image=dealer_back)
                # save card
                dealer_card_1.image = dealer_back
                dealer_cards += 1

            elif dealer_cards == 1:
                # resize card
                dealer_image_2 = resize_cards(f"Python/{dealer_card}.png")
                # output card
                dealer_card_2.config(image=dealer_image_2)
                # save card
                dealer_card_2.image = dealer_image_2
                dealer_cards += 1

            elif dealer_cards == 2:
                # resize card
                dealer_image_3 = resize_cards(f"Python/{dealer_card}.png")
                # output card
                dealer_card_3.config(image=dealer_image_3)
                # save card
                dealer_card_3.image = dealer_image_3
                dealer_cards += 1

            elif dealer_cards == 3:
                # resize card
                dealer_image_4 = resize_cards(f"Python/{dealer_card}.png")
                # output card
                dealer_card_4.config(image=dealer_image_4)
                # save card
                dealer_card_4.image = dealer_image_4
                dealer_cards += 1

            elif dealer_cards == 4:
                # resize card
                dealer_image_5 = resize_cards(f"Python/{dealer_card}.png")
                # output card
                dealer_card_5.config(image=dealer_image_5)
                # save card
                dealer_card_5.image = dealer_image_5
                dealer_cards += 1
        if len(dealer_score) <= 2:
            # check for blackjack
            blackjack_score("dealer")
        else:
            pass

    def stand():
        """Player ends their turn and dealer can now start theirs."""
        hit_button.config(state="disabled")
        stand_button.config(state="disabled")
        if sum(dealer_score) >= 16:
            blackjack_score("dealer")
        while True:
            if sum(dealer_score) < 16:
                dealer_hit()
            else:
                stand_win()
                break

    # frame for buttons so they can be in a line
    button_frame = tk.Frame(blackjack, bg="#0D3B66")
    button_frame.pack(pady=20)

    hit_button = tk.Button(
        button_frame,
        text="Hit",
        font=pixel_font_buttons_hangman,
        command=player_hit,
        bg="#FAF0CA",
        fg="#0D3B66",
        padx=30,
        relief="flat",
    )
    hit_button.pack(pady=10, padx=10, side="right")
    stand_button = tk.Button(
        button_frame,
        text="Stand",
        command=stand,
        bg="#FAF0CA",
        fg="#0D3B66",
        font=pixel_font_buttons_hangman,
        padx=10,
        relief="flat",
    )
    stand_button.pack(pady=10, padx=10, side="left")

    # putting cards into frames
    # five cards if player gets 5 w/o busting then they win
    # only 5 as the player and dealer cannot have more than 5
    dealer_card_1 = tk.Label(Dframe, text="", bg="#FAF0CA")
    player_card_1 = tk.Label(Pframe, text="", bg="#FAF0CA")
    dealer_card_1.grid(row=0, column=0, pady=20)
    player_card_1.grid(row=1, column=0, pady=20)

    dealer_card_2 = tk.Label(Dframe, text="", bg="#FAF0CA")
    player_card_2 = tk.Label(Pframe, text="", bg="#FAF0CA")
    dealer_card_2.grid(row=0, column=1, pady=20)
    player_card_2.grid(row=1, column=1, pady=20)

    dealer_card_3 = tk.Label(Dframe, text="", bg="#FAF0CA")
    player_card_3 = tk.Label(Pframe, text="", bg="#FAF0CA")
    dealer_card_3.grid(row=0, column=2, pady=20)
    player_card_3.grid(row=1, column=2, pady=20)

    dealer_card_4 = tk.Label(Dframe, text="", bg="#FAF0CA")
    player_card_4 = tk.Label(Pframe, text="", bg="#FAF0CA")
    dealer_card_4.grid(row=0, column=3, pady=20)
    player_card_4.grid(row=1, column=3, pady=20)

    dealer_card_5 = tk.Label(Dframe, text="", bg="#FAF0CA")
    player_card_5 = tk.Label(Pframe, text="", bg="#FAF0CA")
    dealer_card_5.grid(row=0, column=4, pady=20)
    player_card_5.grid(row=1, column=4, pady=20)

    def shuffle():
        """Shuffles the cards in the deck.

        basically restarting the game.
        """
        nonlocal player_cards
        nonlocal dealer_cards
        # shuffle the cards
        deck.clear()
        # resetting the deck
        # And resetting the cards each person has
        dealer.clear()
        player.clear()
        # resetting their scores
        player_score.clear()
        dealer_score.clear()

        player_cards = 0
        dealer_cards = 0

        jack_title.config(text="Welcome to BlackJack!!")

        hit_button.config(state="normal")
        stand_button.config(state="normal")

        # resetting images of cards the player and dealer have
        dealer_card_1.config(image="")
        dealer_card_2.config(image="")
        dealer_card_3.config(image="")
        dealer_card_4.config(image="")
        dealer_card_5.config(image="")

        player_card_1.config(image="")
        player_card_2.config(image="")
        player_card_3.config(image="")
        player_card_4.config(image="")
        player_card_5.config(image="")

        # making the deck
        suits = ["diamonds", "clubs", "hearts", "spades"]
        # These values range from 2 to ace
        # ace is the 15th card
        values = range(2, 15)
        # one card value for each suit
        for i in suits:
            # i is each individual suit
            for r in values:
                # r is each value
                deck.append(f"{r}_of_{i}")
                # name them like our images
        cardnum.config(text=f"Cards left in deck: {len(deck)}",
                       fg="#FAF0CA")

        shuffle_button.config(bg="#3D5366", state="disabled")

        # at the start give 2 cards for player and dealer per blackjack rules
        dealer_hit()
        player_hit()

        dealer_hit()
        player_hit()

    shuffle_button = tk.Button(
        button_frame,
        text="Next game",
        font=pixel_font_buttons_hangman,
        command=shuffle,
        bg="#3D5366",
        fg="#0D3B66",
        padx=10,
        state="disabled",
    )
    shuffle_button.pack(pady=10, padx=10, side="left")
    # when you are finished getting cards

    # checking win after dealer moves
    def stand_win():
        """Occurs when the player presses stand.

        It checks who wins after that.
        """
        nonlocal player_num
        # DEALER WIN
        if sum(dealer_score) < 21:
            if len(dealer_score) == 5:
                jack_title.config(text="5 CARDS YOU LOSE")
                dealer_new_card = resize_cards(f"Python/{dealer[0]}.png")
                # save card
                dealer_card_1.config(image=dealer_new_card)
                dealer_card_1.image = dealer_new_card
                gamefin()
            elif sum(dealer_score) > sum(player_score):
                jack_title.config(text="YOU LOST, "
                                  " DEALER HAS A HIGHER SCORE")
                gamefin()
                # SHOW CARD
                dealer_new_card = resize_cards(f"Python/{dealer[0]}.png")
                # save card
                dealer_card_1.config(image=dealer_new_card)
                dealer_card_1.image = dealer_new_card
                # PLAYER WIN
            elif sum(dealer_score) < sum(player_score):
                jack_title.config(text="YOU WIN, YOU HAVE THE HIGHER SCORE")
                player_num += 1
                dealer_new_card = resize_cards(f"Python/{dealer[0]}.png")
                # save card
                dealer_card_1.config(image=dealer_new_card)
                dealer_card_1.image = dealer_new_card
                shuffle_button.config(bg="#FAF0CA", state="normal")
                # TIE(NO POINTS)
            else:
                jack_title.config(text="ITS A TIE")
                dealer_new_card = resize_cards(f"Python/{dealer[0]}.png")
                # save card
                dealer_card_1.config(image=dealer_new_card)
                dealer_card_1.image = dealer_new_card
                shuffle_button.config(bg="#FAF0CA", state="normal")
                # DEALER WIN
        elif sum(dealer_score) == 21:
            jack_title.config(text="BLACK JACK DEALER WINS")
            dealer_new_card = resize_cards(f"Python/{dealer[0]}.png")
            # save card
            dealer_card_1.config(image=dealer_new_card)
            dealer_card_1.image = dealer_new_card
            shuffle_button.config(bg="#3D5366", state="disabled")
            gamefin()
            # PLAYER WIN
        else:
            jack_title.config(text="ITS A BUST, YOU WIN")
            player_num += 1
            shuffle_button.config(bg="#FAF0CA", state="normal")
            dealer_new_card = resize_cards(f"Python/{dealer[0]}.png")
            # save card
            dealer_card_1.config(image=dealer_new_card)
            dealer_card_1.image = dealer_new_card

    # check for blackjack
    def blackjack_score(player):
        """Add the score of the card to the players total.

        If the player surpasses 21 they lose
        """
        nonlocal player_num
        if sum(dealer_score) == 21 and sum(player_score) == 21:
            # If both the players have blackjack
            # let player win bc im nice:)
            jack_title.config(text="BLACK JACK YOU WIN")
            player_num += 1
            hit_button.config(state="disabled")
            stand_button.config(state="disabled")
            shuffle_button.config(bg="#FAF0CA", state="normal")
            dealer_new_card = resize_cards(f"Python/{dealer[0]}.png")
            # save card
            dealer_card_1.config(image=dealer_new_card)
            dealer_card_1.image = dealer_new_card
        elif player == "dealer":
            # if cards were just chuffled
            # DEALER WIN
            if len(dealer_score) == 2:
                if dealer_score[0] + dealer_score[1] == 21:
                    jack_title.config(text="BLACK JACK, YOU LOSE")
                    hit_button.config(state="disabled")
                    stand_button.config(state="disabled")
                    shuffle_button.config(bg="#3D5366", state="disabled")
                    dealer_new_card = resize_cards(f"Python/{dealer[0]}.png")
                    # save card
                    dealer_card_1.config(image=dealer_new_card)
                    dealer_card_1.image = dealer_new_card
                    gamefin()
        elif player == "player":
            # if cards were just shuffled
            # DEALER WIN
            if sum(player_score) > 21:
                jack_title.config(text="ITS A BUST, YOU LOSE")
                hit_button.config(state="disabled")
                stand_button.config(state="disabled")
                dealer_new_card = resize_cards(f"Python/{dealer[0]}.png")
                # save card
                dealer_card_1.config(image=dealer_new_card)
                dealer_card_1.image = dealer_new_card
                gamefin()
                # PLAYER WIN
            elif sum(player_score) == 21:
                jack_title.config(text="BLACK JACK YOU WIN")
                player_num += 1
                hit_button.config(state="disabled")
                stand_button.config(state="disabled")
                shuffle_button.config(bg="#FAF0CA", state="normal")
                dealer_new_card = resize_cards(f"Python/{dealer[0]}.png")
                # save card
                dealer_card_1.config(image=dealer_new_card)
                dealer_card_1.image = dealer_new_card
                # PLAYER WIN
            else:
                if len(player_score) == 5:
                    player_num += 1
                    hit_button.config(state="disabled")
                    stand_button.config(state="disabled")
                    shuffle_button.config(bg="#FAF0CA", state="normal")
                    jack_title.config(text="5 CARDS PLAYER WINS")
                    dealer_new_card = resize_cards(f"Python/{dealer[0]}.png")
                    # save card
                    dealer_card_1.config(image=dealer_new_card)
                    dealer_card_1.image = dealer_new_card

    # add cards into the deck
    shuffle()
    # creating a deck with all the cards

    blackjack.mainloop()


def help():
    """Open the help menu."""
    help = tk.Toplevel(root)
    help.title("Help")
    help.geometry("700x1000")
    help.resizable(False, False)  # stop the resizing of the window
    help.configure(bg="#FAF0CA")  # The background color of the window
    # shows when respective help button is pressed

    def hangman_help():
        """Open help for hangman."""
        nonlocal changing_label
        changing_label.config(
            text="How to play Hangman:\n"
            "Enter the letters you think are in the word inside the "
            "text box.\n"
            "You can either enter one letter or a whole word \n"
            "BUT the letters"
            "in the word are not counted as guessed\n"
            "so consider  very carefully.\n"
            "You have 10 lives, and everytime you get a word or letter wrong,"
            "\nyou will lose a life\n"
            "and the man gets one step closer to being hanged...\n"
            "Lose all your lives and the man DIES!!!(dun dun dun)\n"
            "Guess the word correctly and you can move on to the next "
            "word!!(yay!!)\n"
            "The words are divided into 3 difficulties: easy, medium and "
            "hard.\n"
            "each difficulty gives you a different amount of points:\n"
            "easy = 1 point, medium = 2 points, hard = 3 points\n"
            "The points will then be counted and put on a leaderboard.\n"
            "Good luck and don't let the man die...",
            font=pixel_font_buttons_small,
            fg="#0D3B66",
            bg="#FAF0CA",
            justify="center",
        )

    def TTT_help():
        """Open help for Super Tic Tac Toe."""
        nonlocal changing_label
        changing_label.config(
            text="Super Tic Tac Toe is like regular Tic Tac Toe,"
            "\n but with 81 squares instead of 9 squares.\n"
            "The board is split into 9 subboards, with "
            "9 squares inide it, \n"
            "which can be played like a regular Tic Tac Toe board. \n"
            "But, the button you play in each subboard will correspond to\n"
            " the next subboard your opponent will then play in \n"
            "so make sure you choose wisely about where you move next! \n"
            "But, if you play in a button that corresponds to a \n"
            "already won or tied subboard your opponent can go anywhere, \n"
            "but the opposite can also happen. \n"
            "The subboard you will be allowed to play in will be"
            " highlighted in a dark blue colour \n"
            " once the whole board turns dark blue you"
            "can go anywhere you want. \n"
            "Once you win a subboard it will change into your"
            "corresponding colour, \n"
            "blue for “O”s and red of “X”s. \n"
            "You will win the entire game when you have won three"
            "subboards in a row.\n"
            "Feel free to play with a friend or the bot!!",
            font=pixel_font_buttons_small,
            fg="#0D3B66",
            bg="#FAF0CA",
            justify="center",
        )

    def blackjack_help():
        """Open help for Blackjack."""
        nonlocal changing_label
        changing_label.config(
            text="Blackjack is a card game that uses a poker card deck, "
            "excluding jokers.\n"
            "Each card has its own values with number cards having their "
            "value be their number, \n"
            "Ace being 11 or 1 and face cards having a value of 10.\n"
            "You will have a total score which is all the values of your "
            "cards added together.\n"
            "Your goal is to get as close to 21 as possible "
            "without going over. \n"
            "You are trying to outscore the dealer who has the same "
            "goal as you.\n"
            "You start with 2 cards and can pick up to 5 cards.\n"
            "If you reach 5 cards without going over 21 or get a score of "
            "exactly 21 cards \n"
            "or beat the dealer without going over 21 or the dealer goes "
            "over 21, you win.\n"
            "Once you are finished picking up cards you can press\n"
            " the stand button and allow the dealer to pick up cards.\n"
            "However if you go over a score of 21 or have a lower score "
            "than the dealer, \n"
            "You Lose and have to play again.\n"
            "Each round you win consecutively will give you a point, \n"
            "your goal is get the most points and therefore the highest "
            "place on the leaderboard.",
            font=pixel_font_buttons_small,
            fg="#0D3B66",
            bg="#FAF0CA",
            justify="center",
        )

    def attributiontext():
        """Open attribution."""
        nonlocal changing_label
        changing_label.config(
            text="Menu Images:\n"
            "Drawn by the amazing Yuna Ko\n"
            "\n Black Jack card image:\n"
            "from John Elders github account\n"
            "The back of the card image:\n"
            "is from Pixabay, by TJfree"
            "published on February 25, 2022 under the Pixabay license\n",
            font=pixel_font_buttons_small,
            fg="#0D3B66",
            bg="#FAF0CA",
            justify="center",
        )
    # buttons connected to the help functions
    help_label = tk.Label(
        help,
        text="What do you need help with?",
        font=pixel_font_buttons_hangman,
        fg="#0D3B66",
        bg="#FAF0CA",
    )
    changing_label = tk.Label(
        help,
        text="Click the buttons below to get help" "with each game",
        font=pixel_font_buttons_small,
        fg="#0D3B66",
        bg="#FAF0CA",
    )
    hangman_help_button = tk.Button(
        help,
        text="Hangman help?",
        command=hangman_help,
        font=pixel_font_buttons_hangman,
        fg="#FAF0CA",
        bg="#0D3B66",
        relief="flat",
        padx=25,
    )
    TTT_help_button = tk.Button(
        help,
        text="Super Tic Tac Toe help?",
        command=TTT_help,
        font=pixel_font_buttons_hangman,
        fg="#FAF0CA",
        bg="#0D3B66",
        relief="flat",
    )
    blackjack_help_button = tk.Button(
        help,
        text="Black Jack help?",
        command=blackjack_help,
        font=pixel_font_buttons_hangman,
        fg="#FAF0CA",
        bg="#0D3B66",
        relief="flat",
        padx=15,
    )
    attribution = tk.Button(
        help,
        text="See Attribution",
        command=attributiontext,
        font=pixel_font_buttons_hangman,
        fg="#FAF0CA",
        bg="#0D3B66",
        relief="flat",
        padx=15,
    )

    help_label.pack(pady=10)
    changing_label.pack(pady=10)
    TTT_help_button.pack(pady=20, padx=20)
    hangman_help_button.pack(pady=20, padx=20)
    blackjack_help_button.pack(pady=20, padx=20)
    attribution.pack(pady=20, padx=20)


root.title("Main Menu")
# button images!
hangman_image = Image.open("Python/hangmanpic.png").resize((275, 275))
hangman_image = ImageTk.PhotoImage(hangman_image)

TTT_image = Image.open("Python/TTT.jpeg.jpeg").resize((275, 275))
TTT_image = ImageTk.PhotoImage(TTT_image)

blackjackbutton_image = Image.open("Python/blacjack.jpg").resize((275, 275))
blackjackbutton_image = ImageTk.PhotoImage(blackjackbutton_image)
# menu buttons, connected to function that opens a game
help_button = tk.Button(
    root,
    text="?",
    command=help,
    font=pixel_font_buttons_small,
    fg="#FAF0CA",
    bg="#0D3B66",
    height=1,
    width=1,
).grid(row=0, column=2, sticky="ne", padx=0, pady=10)

frame_hangman = tk.Frame(
    root,
    bg="#FAF0CA",
    borderwidth=0,
)
frame_hangman.grid(row=1, column=0, rowspan=2, pady=0, padx=10)
hangman_button_image = tk.Button(
    frame_hangman,
    image=hangman_image,
    command=hangman,
    font=pixel_font_buttons,
    fg="#FAF0CA",
    borderwidth=0,
    padx=10,
    pady=10,
)
hangman_button = tk.Button(
    frame_hangman,
    text="Hangman",
    command=hangman,
    font=pixel_font_buttons,
    fg="#FAF0CA",
    bg="#0D3B66",
    borderwidth=0,
    padx=80,
    pady=0,
)
hangman_button_image.pack()
hangman_button.pack()

frame_ttt = tk.Frame(root, bg="#FAF0CA", borderwidth=0)
frame_ttt.grid(row=1, column=2, rowspan=2, pady=0, padx=0)
Stictactoe_image = tk.Button(
    frame_ttt,
    image=TTT_image,
    command=Stictactoe,
    borderwidth=0,
)
Stictactoe_image.pack()
Stictactoe_button = tk.Button(
    frame_ttt,
    text="Super Tic Tac Toe",
    command=Stictactoe,
    font=pixel_font_buttons,
    fg="#FAF0CA",
    bg="#0D3B66",
    borderwidth=0,
    pady=0,
    padx=0,
)
Stictactoe_button.pack()

blackjack_frame = tk.Frame(root, bg="#FAF0CA", borderwidth=0)
blackjack_frame.grid(row=3, column=1, rowspan=2, pady=0, padx=10)
blackjack_image = tk.Button(
    blackjack_frame,
    image=blackjackbutton_image,
    command=blackjack,
    borderwidth=0
)

blackjack_button = tk.Button(
    blackjack_frame,
    text="BlackJack",
    command=blackjack,
    font=pixel_font_buttons,
    fg="#FAF0CA",
    bg="#0D3B66",
    borderwidth=0,
    padx=70,
    pady=0,
)
blackjack_image.pack()
blackjack_button.pack()


root.mainloop()
