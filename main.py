
from Window import Window
from Point import Point
from Line import Line


def main():
    win = Window(800, 600)
    start_point = Point(50, 50)
    end_point = Point(350, 250)
    start_point2= Point(80, 80)
    end_point2 = Point (420, 310)
    line1 = Line(start_point, end_point)
    line2 = Line(start_point2, end_point2)
    win.draw_line(line1, "red")
    win.draw_line(line2, "black")
    win.wait_for_close()


main()