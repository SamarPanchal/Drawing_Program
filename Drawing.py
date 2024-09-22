from tkinter import *
from tkinter import Canvas, messagebox, colorchooser
import LocalDataStorage as storage

file = storage.LocalDataStore("png")
print(file.file_type)

brush_size = 10
is_opened = False

root = Tk()
root.geometry("1024x576")
root.title("Fun Draw - Brush")
root.resizable(False, False)

brush_selected = True
eraser_selected = False


def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    if brush_selected:
        canvas.create_oval([x1, y1, x2 + brush_size, y2 + brush_size], fill=color, outline=color)
        root.title("Fun Draw - Brush")
    else:
        canvas.create_oval([x1, y1, x2 + brush_size, y2 + brush_size], fill=bg_color, outline=bg_color)
        root.title("Fun Draw - Eraser")


canvas = Canvas(root, bg="white", height=576, width=1024)
canvas.pack()
canvas.bind("<B1-Motion>", paint)

color = "black"
bg_color = "white"


def set_brush_size(size):
    global brush_size
    brush_size = size


def set_color(b_color):
    global color
    color = b_color


def set_bg_color(g_color):
    global bg_color
    bg_color = g_color
    canvas.config(bg=bg_color)
    delete()


def set_size():
    size_b = Toplevel(height=200, width=400)
    size_b.title("Change Brush Size")
    size_b.resizable(False, False)
    int_var = DoubleVar()
    int_var.set(brush_size)

    slider = (Scale
              (size_b,
               from_=1,
               to=80,
               length=390,
               command=lambda set_value: set_brush_size(slider.get()),
               orient=HORIZONTAL))
    slider.pack()

    size_b.mainloop()


def choose_color(event):
    if is_opened:
        color_b = colorchooser.askcolor(title="Choose Brush Color")[1]
        set_color(color_b)
        color_canvas.config(bg=color)

        color_canvas = Canvas(root, height=40, width=80, borderwidth=0.5, bg="black")
        color_canvas.place(x=30, y=500)
        color_canvas.bind("<Button-1>", choose_color)


def delete():
    canvas.delete("all")
    root.title("Fun Draw")


def brush_selection():
    global brush_selected
    global eraser_selected
    brush_selected = True
    eraser_selected = False


def eraser_selection():
    global brush_selected
    global eraser_selecte
    brush_selected = False
    eraser_selected = True


def choose_bg():
    color_bg = colorchooser.askcolor(title="Choose Background Color")[1]
    set_bg_color(color_bg)


menu = Menu(root)
root.config(menu=menu)

# File
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Export as Image", command=print())

# edit
edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Clear Canvas", command=delete)
edit_menu.add_separator()
edit_menu.add_command(label="Choose Background Color...", command=choose_bg)

# tools
tools_menu = Menu(menu)
menu.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Brush", command=brush_selection)
tools_menu.add_command(label="Eraser", command=eraser_selection)

# tools
tools_p_menu = Menu(menu)
menu.add_cascade(label="Tools Preferences", menu=tools_p_menu)
tools_p_menu.add_command(label="Brush Size", command=set_size)
tools_p_menu.add_command(label="Brush Color", command=set_color)

root.mainloop()
