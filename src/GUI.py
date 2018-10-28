import tkinter
import View
import Timer


class Gui(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.view = View.View()
        self.root = tkinter.Tk()
        self.root.title('Game of Life')
        self.round_label = tkinter.Label(self.root, text='round:0')
        self.alive_label = tkinter.Label(self.root, text='Alive Cell:0')
        self.update()
        self.alive = 0
        self.cell = tkinter.Label(self.root, width=5, height=2, bd=1)
        self.s_btn = tkinter.Button(self.root, width=8, height=2, text='start', command= self.start)
        self.p_btn = tkinter.Button(self.root, width=8, height=2, text='pause', command= self.pause)
        self.s_btn.grid(row=self.rows + 1, column=0, columnspan=2)
        self.p_btn.grid(row=self.rows + 1, column=2, columnspan=2)
        self.round_label.grid(row=self.rows + 1, column=12, columnspan=2)
        self.alive_label.grid(row=self.rows + 1, column=16, columnspan=3)
        
        tkinter.mainloop()
        
    def judge(self):
        self.alive = 0     #活细胞数目
        for row in range(self.rows):
            for col in range(self.cols):
                if self.view.map[row][col] == 1:      #活细胞进行黑色填充
                    self.alive += 1
                    self.cell = tkinter.Listbox(self.root, width=5, height=2, bd=0.1, bg='#000')
                else:      #死细胞不进行填充
                    self.cell = tkinter.Listbox(self.root, width=5, height=2, bd=0.1)
                self.cell.grid(row=row, column=col)
                
    def update(self):
        self.round_label.config(text='round:'+str(self.view.round))
        self.view.update()
        self.judge()
        self.alive_label.config(text='Alive Cell:'+str(self.alive))
       
        

    def start(self):
        self.timer=Timer.Timer(2, self.update)
        self.timer.start()
        
    def hold(self):
        self.judge()
        
    def pause(self):
        self.timer.pause()
        self.hold()


def main():
    gui = Gui(15, 25)


if __name__ == "__main__":
    main()