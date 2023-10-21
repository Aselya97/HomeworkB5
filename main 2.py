game_name = "крестики-нолики"

#приветствие
print('Добро пожаловать в игру!')
print( game_name)

#создаем и игровое поле

tabel = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]
def print_doard(board):
      for row in board:
          for cell in row:
              print(cell, end=' ')
              print()


  #делаем функцию проверки победителя

def check_win(board, player):
   for row in board:
       if row.count(player) == 3:
           return  True
   for i in range(3):
       if board[0] [i] == player and board [1] [i] == player and board [2][2] == player:
           return True

   if board [0][0] == player and board [1][1] == player and board [2][0] == player:
       return True
 #проверяем по вертикали
   if board[0][2] == player and board [1][1] == player and board [2][0] == player:
       return True

#создаем игроков и начинаем саму игру
player_actual = "X"
while True:
     print_doard(tabel)
     print('ход игрока' , player_actual )
     row = int(input('Введите строку: ')) - 1
     col = int(input('Введите солбец: ')) - 1

     if tabel [row][col] != '-':
        print('Занято')
        continue

     tabel[row][col] = player_actual

     if check_win(tabel, player_actual):
           print_board(tabel)
           print(f'Игрок {player_actual} выиграл')
     if all([cell != '-' for row in tabel for cell in row]):
           print('ничья')
           print_doard()
           break

player_actual = '0' if player_actual == 'X' else 'X'
