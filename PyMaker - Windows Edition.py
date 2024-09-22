#
# This Edition best Works for Windows operating system, Created by Samar
#

import LocalDataStore
import os
from tkinter import *
from tkinter import messagebox, filedialog, colorchooser
from tkinter.filedialog import asksaveasfilename, askopenfilename
from bg_data import *
from fg_data import *
import subprocess
import time

file_path = ''
file_name = ''


def set_path(path):
    global file_path
    file_path = path


def set_file_name(path):
    global file_name
    pre = os.path.basename(path)
    string = str(pre)
    find = string.find('.')
    name = string[0:find]
    file_name = name


def save_file():
    txt = compiler.get(1.0, END)
    path = filedialog.asksaveasfilename(filetypes=[('Python file', '*.py')], defaultextension=".py")
    set_file_name(path)
    with open(path, "w") as file:
        file.write(txt)
        set_path(path)
        file.close()
        root.title("PyMaker - " + file_name)
        messagebox.showinfo("Success!", "File Saved Successfully!")


def open_file():
    open_path = filedialog.askopenfilename(filetypes=[("Python file", "*.py")])
    set_file_name(open_path)
    with open(open_path, "r") as files:
        file = files.read()
        if compiler.get(1.0, END) == file:
            messagebox.showerror("Error!", "This File is Already Opened!")
        else:
            compiler.delete(1.0, END)
            compiler.insert(INSERT, file)
            set_path(open_path)
            files.close()
            root.title("PyMaker - " + file_name)


def save():
    if file_path == "":
        save_file()
    else:
        with open(file_path, "w") as file:
            file.write("")
            file.write(compiler.get(1.0, END))
            file.close()
            root.title("PyMaker - " + file_name)


def run():
    if file_path == "":
        save()
    else:
        output.config(state=NORMAL)
        output.delete(1.0, END)
        command = f"python {file_path}"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, text=True)
        success, error = process.communicate()
        if error != "":
            if " " in file_name:
                messagebox.showerror("Error!", "Please Don't live space between file name!")
            else:
                time1 = time.strftime("%H:%M:%S")
                output.insert(1.0, "** " + error + f"\n")
                output.insert(1.0, success + f"\n")
                output.insert(s1.0, f"--- Output Shown at {str(time1)} with code '{str(process.returncode)}'" + f"\n")
        else:
            time1 = time.strftime("%H:%sM:%S")

            output.insert(1.0, error + f"\n")
            output.insert(1.0, f"--- Output Shown at {str(time1)} with code '{str(process.returncode)}'" + f"\n")
        output.config(state=DISABLED)


def create_file():
    compiler.delete(1.0, END)
    set_path("")
    root.title("PyMaker - 'Untiled File'")


def quit_app():
    save()
    quit()


def choose_bg():
    color = colorchooser.askcolor(title="Choose Background Color")[1]
    compiler.config(bg=str(color))
    save_theme(color, "bg")


def choose_fg():
    color = colorchooser.askcolor(title="Choose Foreground Color")[1]
    compiler.config(fg=str(color))
    save_theme(color, "fg")


def compile_():
    if file_path == "":
        save()
    else:
        command = f"python {file_path}"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        success, error = process.communicate()
        if error != "":
            messagebox.showinfo(f"Error Found in '{str(os.path.basename(file_path))}'!", str(error))
        else:
            messagebox.showinfo("No Error Found!", f"No Error is Found in '{str(os.path.basename(file_path))}'!")


def compile_file():
    last_path = file_path
    open_path = filedialog.askopenfilename(filetypes=[("Python file", "*.py")])
    set_path(open_path)
    compile_()
    set_path(last_path)


def save_theme(colour, which):
    if which == "bg":
        with open("bg_data.py", 'w') as file:
            file.write("bg = " + "'" + colour + "'")
            file.close()
    else:
        with open("fg_data.py", 'w') as file:
            file.write("fg = " + "'" + colour + "'")
            file.close()


def reset():
    with open("bg_data.py", 'w') as file:
        file.write("bg = ''")
        file.close()
    with open("fg_data.py", 'w') as file:
        file.write("fg = ''")
        file.close()
    messagebox.showinfo("Success!", "Your Compiler Theme have been Reset!")
    compiler.config(bg="black", fg="white")



root = Tk()
root.title("PyMaker - 'Untiled File'")
root.config(bg="black")
image = PhotoImage(file="image.png")
root.iconphoto(False, image)

frame = Frame(root, borderwidth=1)

compiler = Text(root, font=("Arial", 20), bg="black", fg="white", cursor='xterm', height=18)
compiler.pack(fill="x")

if bg == '' and fg == '':
    compiler.config(bg="black", fg="white")
elif bg == '' and fg != '':
    compiler.config(bg="black", fg=str(fg))
elif bg != '' and fg == '':
    compiler.config(bg=str(bg), fg="white")
else:
    compiler.config(bg=str(bg), fg=str(fg))

output = Text(root, font=("times", 16), bg="#37383A", fg="white", cursor="arrow", height=60)
output.config(state=DISABLED)
output.pack(fill="x")
frame.pack()

menu = Menu(root)
root.config(menu=menu)

# file
file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Create New File", command=create_file)
file_menu.add_separator()
file_menu.add_command(label=" Open...", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="Save as...", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Quit PyMaker", command=quit_app)
s
# runw
run_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Run", menu=run_menu)
run_menu.add_command(label="Run Current File", command=run)
run_menu.add_separator()
run_menu.add_command(label="Compile", command=compile_)
run_menu.add_command(label="Compile...", command=compile_file)

# theme
theme_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Theme", menu=theme_menu)
theme_menu.add_command(label="Choose Background Color...", command=choose_bg)
theme_menu.add_command(label="Choose Text Color...", command=choose_fg)
theme_menu.add_separator()
theme_menu.add_command(label="Reset Theme", command=reset)

root.mainloop()
