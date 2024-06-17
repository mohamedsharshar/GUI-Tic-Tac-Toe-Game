Program Description
This Python program is a graphical user interface (GUI) implementation of the classic game Tic Tac Toe, built using the Tkinter library. The program sets up a window where two players can take turns to play the game. The game board consists of a 3x3 grid of buttons that players can click to place their respective marks ("X" or "O"). The program includes functionality to check for a win or a draw, and it can reset the game once a win or draw is detected.

Key Components:
Imports and Window Setup:

Tkinter is imported to create the GUI.
messagebox is used to display pop-up messages for win or draw notifications.
The main application window (app) is created and configured with a title, size, and background color.
Game State Variables:

current_player: Tracks whose turn it is ("X" or "O").
board: A list representing the game board state, initialized with empty strings to denote empty spaces.
Button Click Handling:

myclick(index): This function handles a button click. It updates the button text and the board state if the clicked space is empty, checks for a win or a draw, and switches the current player.
Win Check Function:

check_win(): Checks the board state for any winning combinations. Returns True if a win is detected, otherwise returns False.
Winning combinations are defined in the checker list, which contains tuples of indices that need to match for a win.
Game Restart Function:

restart_game(): Resets the game by clearing the board state and button texts, and sets the current player back to "X".
GUI Layout:

A Frame widget is used to contain the game buttons, placed at the center of the main window.
A loop creates nine buttons for the 3x3 grid, each with a command to call myclick(index) with the appropriate index.
A copyright label is added at the bottom of the window.
Main Application Loop:

app.mainloop(): Starts the Tkinter event loop, which waits for user interaction.
Detailed GUI Setup:
Main Window:

Title: "Tic Tac Toe"
Size: 400x400 pixels
Background color: #850F8D (a shade of purple)
Game Board:

A Frame widget centered in the main window.
Nine buttons arranged in a 3x3 grid, each button is initially blank.
Button appearance: light purple background (#E49BFF), white text, bold font.
Game Logic:

Button clicks update the text on the button and the board list.
After each click, the program checks if there is a winner or if the board is full (draw).
A message box notifies the players of a win or draw.
The game resets automatically after a win or draw.
User Interaction:
Start the Game:
Run the program to open the Tic Tac Toe window.
Playing the Game:
Players take turns clicking on empty buttons to place their mark ("X" or "O").
The program automatically switches turns between "X" and "O".
Win/Draw Detection:
When a player gets three of their marks in a row (horizontally, vertically, or diagonally), a message box announces the win.
If all buttons are filled without a winner, a message box announces a draw.
Restarting the Game:
The game board resets automatically after a win or draw, allowing the players to start a new game immediately.
