import tkinter
from tkinter import messagebox

from TICTACTOE import TictactoeGameEngine

class Tictactoe:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
    def play(self):
        #show board
        print(self.game_engine)
        while True:
        #무한반복
            #row, col 입력받자
            row = int(input('row: '))
            col = int(input('col: '))
            #말을 놓자
            self.game_engine.set(row,col)
            #show board
            # print(self.game_engine)
            #만약에 승자가 있으면, 무승부이면 끝
            winner = self.game_engine.check_winner
            if winner == 'O' or winner == 'X' or winner == 'd':
                break
        #결과 출력하자
        if winner =='O':
            print("O승리")
        elif winner == 'X':
            print("X승리")
        elif winner == 'd':
            print("무승부")

class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()

        CANVAS_SIZE =300
        self.TITLE_SIZE = CANVAS_SIZE/3

        self.root = tkinter.Tk()
        self.root.geometry(str(CANVAS_SIZE)+'x'+str(CANVAS_SIZE))
        self.root.title('틱 택 토')
        self.root.resizable(width=False, height=False)
        self.canvas = tkinter.Canvas(self.root, bg='white', width=CANVAS_SIZE, height=CANVAS_SIZE)
        self.canvas.pack()

        self.images = {}
        self.images['O'] = tkinter.PhotoImage(file='O.gif')
        self.images['X'] = tkinter.PhotoImage(file='X.gif')

        self.canvas.bind('<Button-1>', self.click_handler)

    def click_handler(self, event):
        x = event.x
        y = event.y
        col = x//100+1
        row = y//100+1
        self.game_engine.set(row, col)
        # print(self.game_engine)
        self.draw_board()
        if self.game_engine.check_winner == 'O':
            messagebox.showinfo('Game Over','O 이김')
            self.root.quit()
        elif self.game_engine.check_winner == 'X':
            messagebox.showinfo('Game Over','X 이김')
            self.root.quit()
        elif self.game_engine.check_winner == 'd':
            messagebox.showinfo('Game Over','무승부')
            self.root.quit()

    def draw_board(self):
        x=0
        y=0
        for i,v in enumerate(self.game_engine.board):#->얘를 바탕으로 그림을 그린당!
            if v =='X':
                self.canvas.create_image(x, y, anchor='nw', image=self.images['X'])
            elif v =='O':
                self.canvas.create_image(x, y, anchor='nw', image=self.images['O'])
            # elif v !='.':
            #     self.canvas.create_image(x, y, anchor='nw', image=self.images[v])
            x += self.TITLE_SIZE
            if i%3==2:
                x=0
                y +=self.TITLE_SIZE

    def play(self):
        # self.canvas.create_image(0,100, anchor='nw', image=self.images['O'])
        # self.canvas.create_image(200, 100, anchor='nw', image=self.images['O'])
        # self.canvas.create_image(100, 200, anchor='nw', image=self.images['O'])
        # self.canvas.create_image(200, 0, anchor='nw', image=self.images['X'])
        # self.canvas.create_image(0,0, anchor='nw', image=self.images['X'])
        self.root.mainloop()

if __name__=='__main__':
    ttt = TictactoeGUI()
    ttt.play()