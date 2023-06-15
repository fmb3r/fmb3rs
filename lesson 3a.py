from tkinter import *

window = Tk()
window.geometry('800x600')

canvas = Canvas(window, width = 800, height = 600, bg = 'white')
canvas.pack()

canvas.create_polygon(175, 120, 190, 65, 205, 120, fill = 'yellow', outline = '')
canvas.create_polygon(190, 110, 190, 135, 245, 120, fill = 'yellow', outline = '')
canvas.create_polygon(190, 110, 190, 135, 135, 120, fill = 'yellow', outline = '')
canvas.create_polygon(195, 110, 175, 135, 235, 175, fill = 'yellow', outline = '')
canvas.create_polygon(180, 110, 200, 135, 150, 175, fill = 'yellow', outline = '')

class Star:
    def __init__(self, tri1_color, tri2_color, tri3_color, tri4_color, tri5_color ):
        self.tri1_color = tri1_color
        self.tri2_color = tri2_color
        self.tri3_color = tri3_color
        self.tri4_color = tri4_color
        self.tri5_color = tri5_color

    def print_star(self):
        canvas.create_polygon(175, 120, 190, 65, 205, 120, fill=self.tri1_color, outline='')
        canvas.create_polygon(190, 110, 190, 135, 245, 120, fill=self.tri2_color, outline='')
        canvas.create_polygon(190, 110, 190, 135, 135, 120, fill=self.tri3_color, outline='')
        canvas.create_polygon(195, 110, 175, 135, 235, 175, fill=self.tri4_color, outline='')
        canvas.create_polygon(180, 110, 200, 135, 150, 175, fill=self.tri5_color, outline='')

star1 = Star('red', 'yellow', 'green', 'blue', 'pink')
star1.print_star()