import tkinter as tk
from tkinter import ttk
from tkinter.font import Font#So I can use fonts in the games and menu
import random#For hangman and blackjack

current_player = "X"#X is the current player
#I am using a tutorial by Alina Chudnova but I modified it to make it super
#I used codingspots ultimate tictactoe video for the nested list board
TTT = tk.Tk()
TTT.title("Tic Tac Toes")
TTT.geometry("805x875")
TTT.configure(bg="#FAF0CA")#The background color of the window

#Giving our board a value
board = [[[["" for i in range(3)] for r in range (3)] 
          for j in range(3)] for k in range(3)]
#I creates the first row, r creates the first subboard, 
# j creates the first row of subboards, k creates the bigger board
subboard_winner = [["" for i in range(3)] for r in range(3)]
#Creating a way to store all the winners of the subboard
#These subboards function as a section in tic tac toe

pixel_font_title = Font(family = "VT323", size = 70)
pixel_font_buttons = Font(family = "VT323", size = 26)
pixel_font_labels = Font(family = "VT323", size = 40)
pixel_font_buttons_hangman = Font(family = "VT323", size = 20)
scary_font_label = Font(family = "Nosifer", size = 20)

game_finished = False

allowed_frame_coords_x = ""
allowed_frame_coords_y = ""#The coordinates of the only frame the user is able
#To move in

STTT_title = tk.Label(TTT, text = "Super Tic Tac Toe, with a bot", 
                      font = pixel_font_labels, 
                      fg = "#0D3B66", bg = "#FAF0CA")
STTT_title.grid(row = 0, column = 0, columnspan = 3, pady = 10)

def make_move(mainrow, maincol, subrow, subcol):
    #the code so the player can click a button to make a move
    global current_player
    global board
    global buttons
    global allowed_frame_coords_x
    global allowed_frame_coords_y
    global subboard_winner
    #The the mainrow maincol determines which frame the button picked is
    #The subrow subcol determines which button inside the frame was clicked
    if allowed_frame_coords_x == "" and allowed_frame_coords_y == "" and board[mainrow][maincol][subrow][subcol] == "":
        board[mainrow][maincol][subrow][subcol] = current_player
        #Turning all the subboards blue except those that are won
        #or the one that we are moving in
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
        check_winner_sub(mainrow, maincol)#check if subboard wins using the coordinates
        check_winner_main()#Check if main board wins
        #Then change the button the whatever the current player is
        if current_player == "O":#Changing the color of the square
            buttons[mainrow][maincol][subrow][subcol].config(text=current_player, bg = "blue")
        else:
            buttons[mainrow][maincol][subrow][subcol].config(text=current_player, bg = "red")
        #changing the text of the button to the current player
        if current_player == "X":#Changing the current player after each turn
            current_player = "O"
            if game_finished == False:
            #The bot making a move if its O
                TTT.after(100, TTT_bot_move, allowed_frame_coords_x, allowed_frame_coords_y)
                #delaying the bot by 0.1 secconds to make it seem more natural
                #and give the winning function to calculate the winner before
                #the bot makes a move
        else:
            current_player = "X"


            #First check if the button is empty
            #Then check if the button is in the allowed frame
    elif board[mainrow][maincol][subrow][subcol] == "" and allowed_frame_coords_x == mainrow and allowed_frame_coords_y == maincol:
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
        #Check if the next subboard is won
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
            buttons[mainrow][maincol][subrow][subcol].config(text=current_player, bg = "blue")
        else:
            buttons[mainrow][maincol][subrow][subcol].config(text=current_player, bg = "red")
        #changing the text of the button to the current player
        check_winner_sub(mainrow, maincol)
        #check if the subboard fo these coords wins
        check_winner_main()#Check if main board wins
        if current_player == "X":#Changing the current player after each turn
            current_player = "O"
            if game_finished == False:
            #The bot only moves if its O
               TTT.after(100, TTT_bot_move, allowed_frame_coords_x, \
                         allowed_frame_coords_y)#Make the bot move
               #delay to the bots movements
        else:
            current_player = "X"

def TTT_bot_move(bot_allowed_frame_coords_x, bot_allowed_frame_coords_y):
    global board
    global current_player
    bot_coord_X = random.randint(0,2)
    bot_coord_Y = random.randint(0,2)
    global buttons
    global subboards
    global subboard_winner
    global allowed_frame_coords_x
    global allowed_frame_coords_y
    if allowed_frame_coords_x != "" and allowed_frame_coords_y != "":
        while board[allowed_frame_coords_x][allowed_frame_coords_y][bot_coord_X][bot_coord_Y] != "":
            bot_coord_X = random.randint(0,2)
            bot_coord_Y = random.randint(0,2)
            #Rabdomise the coords until we find an empty button
        if board[allowed_frame_coords_x][allowed_frame_coords_y][bot_coord_X][bot_coord_Y] == "":
            #Change the button to the current player or whatever player the but is
            board[allowed_frame_coords_x][allowed_frame_coords_y][bot_coord_X][bot_coord_Y] = current_player
            #Changing the color of the square depedning on the player
            buttons[allowed_frame_coords_x][allowed_frame_coords_y][bot_coord_X][bot_coord_Y].config(text=current_player, bg = "blue")
            for i in range(3):
                for r in range(3):
                    if subboard_winner[i][r] == "":
                        subboards[i][r].config(bg = "#EE964B")
            check_winner_sub(allowed_frame_coords_x, allowed_frame_coords_y)
            check_winner_main()
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
        while subboard_winner[allowed_frame_coords_x][allowed_frame_coords_y] != "":
            allowed_frame_coords_x = random.randint(0,2)
            allowed_frame_coords_y = random.randint(0,2)
            #If the frame isn't won then break the loop
            if subboard_winner[allowed_frame_coords_x][allowed_frame_coords_y] == "":
                break
            #And choose a random button in that frame
            #Then check random buttons until we find an empty one
        while board[allowed_frame_coords_x][allowed_frame_coords_y][bot_coord_X][bot_coord_Y] != "":
            bot_coord_X = random.randint(0,2)
            bot_coord_Y = random.randint(0,2)
            #If the button is empty then break the loop
            if board[allowed_frame_coords_x][allowed_frame_coords_y][bot_coord_X][bot_coord_Y] == "":
                break
        #Then make the bot make a move in the button
        
        #Make a move in the selected button
        board[allowed_frame_coords_x][allowed_frame_coords_y][bot_coord_X][bot_coord_Y] = current_player
        buttons[allowed_frame_coords_x][allowed_frame_coords_y][bot_coord_X][bot_coord_Y].config(text=current_player, bg = "blue")
        check_winner_sub(allowed_frame_coords_x, allowed_frame_coords_y)
        check_winner_main() 
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
    global board
    global current_player
    global subboard_winner
    global game_finished
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
            print(current_player)
            game_finished = True
            print("I love chicken nuggets")
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
        print("Tie")
#Iterating through each square
def check_winner_sub(mainrow, maincol):#Checking if there is a winner for sub
    #These coords are used for the subboard_check var
    global current_player
    global board
    global subboard_winner
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
            print("win")
            subboard_winner[mainrow][maincol] = win[0]
            #The winner is the first value out of the winning line
            if subboard_winner[mainrow][maincol] == "X":
                subboards[mainrow][maincol].config(bg = "red")
            else:#Changing the colors to match the winners
                subboards[mainrow][maincol].config(bg = "blue")
            #Taking note of who won
            for i in buttons[mainrow][maincol]:#Iterating through the list
                #Or 3rd list inside the buttons(row list)nested list
                for r in i:#Inside the list I iterate through each button
                    r.config(state = "disabled")
                    #Making each button in that frame dissabled
            return
        
    if all(subboard_check[i][r] != "" for i in range(3) for r in range(3)):#If all buttons are filled but no winner
        print("Tie")
        subboard_winner[mainrow][maincol] = "T"
        #To make confirm the board can no longer be played in
        for i in buttons[mainrow][maincol]:#Iterating through the list
            #Or 3rd list inside the buttons(row list)nested list
            for r in i:#Inside the list I iterate through each button
                r.config(state = "disabled")
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
        subboard_frame = tk.Frame(TTT, bg = "#EE964B",)
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
                                    font = pixel_font_buttons, 
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


TTT.mainloop()
