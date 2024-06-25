import tkinter as tk
from tkinter import simpledialog, messagebox

# Создаем окно игры
window = tk.Tk()
window.title("Крестики-нолики")

# Запрашиваем имена игроков
player1_name = simpledialog.askstring("Имя игрока", "Введите имя игрока X:")
player2_name = simpledialog.askstring("Имя игрока", "Введите имя игрока O:")

# Словарь для хранения имени игроков
player_names = {"X": player1_name, "O": player2_name}

# Создаем переменную для хранения текущего игрока
current_player = "X"

# Функция для проверки победителя


def check_winner(player):
    # Проверяем диагонали
    if (buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == player) or (buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] == player):
        return True

    # Проверяем строки и столбцы
    for i in range(3):
        if (buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] == player) or (buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] == player):
            return True

    return False

# Функция для проверки ничьи


def check_draw():
    for row in buttons:
        for button in row:
            if button["text"] == " ":
                return False
    return True

# Функция для обработки хода игрока


def make_move(button):
    global current_player

    if button["text"] == " " and not check_winner("X") and not check_winner("O"):
        button["text"] = current_player

        if check_winner(current_player):
            winner_name = player_names[current_player]
            messagebox.showinfo("Победа!", f"Игрок {
                                winner_name} ({current_player}) победил!")
            window.quit()
        elif check_draw():
            messagebox.showinfo("Ничья!", "Игра закончилась ничьей!")
            window.quit()
        else:
            current_player = "O" if current_player == "X" else "X"


# Создаем кнопки для игрового поля
buttons = [[None, None, None], [None, None, None], [None, None, None]]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(window, text=" ", font=("Arial", 20), width=5, height=2,
                                  command=lambda i=i, j=j: make_move(buttons[i][j]))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

# Запускаем игровой цикл
window.mainloop()
