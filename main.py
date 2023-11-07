def boardprint(board):  #отображение игрового поля
    print (' 0 1 2')
    for i in range(len(board)):
        row=''
        for j in range(len(board[i])):
            row+=board[i][j] + ' '
        print(i,row)

def win(board,player): #выигрышные комбинации
    for i in range(3):
        if board[i][0]==board[i][1] == board[i][2] and board[i][0]!='-': #по горизонтали
            return True
        if board[0][i] == board[1][i] == board[2][i] and board[0][i]!='-': #по вертикали
            return True
        if board[0][0]==board[1][1]==board[2][2] and board[0][0]!= '-':  #по диагоналям
            return True
        if board[0][2]==board[1][1]==board[2][0] and board[0][2]!='-':
            return True
    return False
board = [['-' for _ in range(3)] for _ in range(3)]

current_player = str(input('Первый игрок должен выбрать x или o '))
while True: #основной цикл
    boardprint(board)
    print('Ход игрока ',current_player)
    row=int(input('Введите номер строки: '))
    col=int(input('Введите номер столбца: '))
    if row<0 or row>2 or col<0 or col>2:
        print('Неверные координаты строки или столбца, введите еще раз!')
        continue
    if board[row][col] != '-':
        print('Клетка уже занята, выберите другую!')
        continue
    board[row][col]=current_player

    if win(board, current_player): # проверка на победу
        boardprint(board)
        print('Игрок ', current_player, ' победил!')
        break
    if all(board[i][j]!= '-' for i in range(3) for j in range(3)): #проверка на ничью
        boardprint(board)
        print('Ничья!')
        break
    current_player = 'o' if current_player == 'x' else 'x'



