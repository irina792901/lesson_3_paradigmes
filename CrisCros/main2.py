Инициализация игрового поля размером 3x3
board = [" "] * 9

Функция для отображения игрового поля
def display_board():
for i in range(0, 9, 3):
# Отображение каждой строки игрового поля
print(board[i], "|", board[i+1], "|", board[i+2])

Функция для проверки условий победы
def check_win():
# Возможные комбинации победы на игровом поле 3x3
win_combinations = [
(0,1,2), (3,4,5), (6,7,8), # Горизонтали
(0,3,6), (1,4,7), (2,5,8), # Вертикали
(0,4,8), (2,4,6) # Диагонали
]
for combo in win_combinations:
# Если все три ячейки в одной из победных комбинаций содержат один и тот же символ и не пусты, то есть победитель
if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
return True
return False

Начало игры с первым игроком
player = "X"

Основной игровой цикл
for _ in range(9): # 9 ходов (максимальное количество ходов в игре)
display_board()
pos = int(input(f"{player}'s turn. Choose position (0-8): "))

# Проверка, свободна ли выбранная ячейка
if board[pos] == " ":
    # Заполнение выбранной ячейки символом текущего игрока
    board[pos] = player

    # Проверка на победу после каждого хода
    if check_win():
        display_board()
        print(f"{player} wins!")
        break

    # Смена игрока после каждого хода
    player = "O" if player == "X" else "X"
else:
    print("Position occupied! Try again.")
else:
# Если все 9 ходов сделаны и никто не выиграл
display_board()
print("It's a draw!")
