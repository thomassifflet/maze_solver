from tkinter import Tk, BOTH, Canvas
from Line import Line

class Window:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.canvas = Canvas(self.root_widget, width = self.width, height = self.height)
        self.canvas.pack()
        self.window_is_running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()


    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
        

    def wait_for_close(self):
        self.window_is_running = True
        while self.window_is_running:
            self.redraw()

    def close(self):
        self.window_is_running = False