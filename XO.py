from tkinter import *
from tkinter import messagebox  

app = Tk()
app.title("Tic Tac Toe")
app.geometry("400x400")
# app.iconbitmap("tic-tac-toe_39453.ico")
app.config(bg="#850F8D")
current_player = "X"
board = [""] * 9

def myclick(index):
    global current_player
    if buttons[index]['text'] == "" and board[index] == "":
        buttons[index]["text"] = current_player
        board[index] = current_player
        if check_win():
            messagebox.showinfo("Tic Tac Toe", f"{current_player} wins")
            restart_game()
        elif "" not in board:
            messagebox.showinfo("Tic Tac Toe", "It's a draw")
            restart_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def check_win():
    checker = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
               (0, 3, 6), (1, 4, 7), (2, 5, 8),
               (0, 4, 8), (2, 4, 6)]
    for i in checker:
        if board[i[0]] == board[i[1]] == board[i[2]] != "":
            return True
    return False

def restart_game():
    global board, current_player
    board = [""] * 9
    for button in buttons:
        button['text'] = ""
    current_player = "X"

frame = Frame(app, bg="#850F8D")
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

buttons = []
for i in range(9):
    button = Button(frame, text="", padx=20, pady=10, bg="#E49BFF", fg="#fff",font="bold",
                    command=lambda i=i: myclick(i))
    button.grid(row=i // 3, column=i % 3, padx=15, pady=5)
    buttons.append(button)
copyright=Label(app,text="Made By SHAR SHAR",bg="#850F8D",font="bold",fg="#fff",anchor=CENTER)
copyright.grid(row=3,column=1,padx=118,pady=20)
app.mainloop()
