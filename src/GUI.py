import tkinter
import View
import Timer


class Gui(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.alive = 0
        self.timer = Timer.Timer(1, self.g_update)
        self.view = View.View(0.2, rows, cols)
        self.root = tkinter.Tk()
        self.root.title('Game of Life')
        self.root.geometry('600x640')
        self.canvas = tkinter.Canvas(self.root, bg='white', width=560, height=560)
        self.canvas.place(x=20, y=20)
        self.p_btn = tkinter.Button(self.root, width=8, text='pause', command=self.pause)
        self.p_btn.place(x=100, y=596)
        self.round_label = tkinter.Label(self.root, text='round:0')
        self.round_label.place(x=220, y=596)
        self.alive_label = tkinter.Label(self.root, text='Alive Cell:0')
        self.alive_label.place(x=300, y=596)
        self.start_button = tkinter.Button(self.root, text='start', width=8, command=self.start)
        self.start_button.place(x=20, y=596)
        
    def draw(self):
        width = float(self.canvas['width'])
        height = float(self.canvas['height'])
        p_width = width/self.cols
        p_height = height/self.rows
        self.alive = 0
        self.canvas.create_rectangle(0, 0, width, height, fill="#fff", outline="#fff")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.view.map[row][col] == 1:
                    self.alive += 1
                    self.canvas.create_rectangle(p_width*col, p_height*row, p_width*(1+col), p_height*(1+row), fill='#000', outline='#fff')
        self.alive_label.config(text='Alive Cell:' + str(self.alive))
        tkinter.mainloop()

    def g_update(self):
        self.round_label.config(text='round:'+str(self.view.round))
        self.view.update()
        self.draw()

    def start(self):
        self.timer = Timer.Timer(1, self.g_update)
        self.timer.start()
        
    def pause(self):
        self.timer.pause()



def main():
    gui = Gui(25, 25)


if __name__ == "__main__":
    main()