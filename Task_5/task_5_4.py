# 1 - Создайте программу для игры в ""Крестики-нолики"".

class Board:
    DECODE_MARK = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}

    def __init__(self):
        self.board_plate = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def __str__(self):
        return str(self.board_plate)

    def show_board(self):
        for i, v in enumerate(self.board_plate):
            print(f'  {v[0]} | {v[1]} | {v[2]}  ')
            print(' ___ ___ ___' if i < 2 else '')

    def change_board(self, number, mark):
        decode_num = Board.DECODE_MARK[number]
        while self.board_plate[decode_num[0]][decode_num[1]] in ('X', 'O'):
            print('Sorry this field is already occupied')
            decode_num = Board.DECODE_MARK[int(input('Please enter the field number: '))]
        self.board_plate[decode_num[0]][decode_num[1]] = mark

    def check_win(self):
        # if self.board_plate.count[0](self.board_plate[0][0]) == len(self.board_plate.count[0]):
        for i in range(3):
            if self.board_plate[i].count(self.board_plate[i][0]) == len(self.board_plate[i]):
                return True
        for i in range(3):
            if self.board_plate[0][i] == self.board_plate[1][i] == self.board_plate[2][i]:
                return True
        




l = Board()

l.show_board()
l.change_board(9, 'X')
l.show_board()
l.change_board(6, 'O')
l.show_board()
l.change_board(6, 'O')
l.show_board()

# def board(*args):
#     board_plate = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     for i in args:
