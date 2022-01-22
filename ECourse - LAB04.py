import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import Spinbox
import requests
import webbrowser


class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 10 #pozycja x
        y = y + cy + self.widget.winfo_rooty() + 10 #pozycja y
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

#===================================================================
def createToolTip( widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

win = tk.Tk()
win.title('Zdrowy Sukces - kwestionariusz')
win.iconbitmap(r'aaa.ico')

# Tab Control 
tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Tab 1")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")
tabControl.pack(expand=1, fill="both", padx=10, pady=10)
# End Tab Control

# main frame
mainFrame = ttk.LabelFrame(tab1, text='Main Label Frame')
mainFrame.grid(column=0, row=0, columnspan=3, sticky='W', padx=10, pady=10)

mainFrame2 = ttk.LabelFrame(tab2, text='Main Label Frame')
mainFrame2.grid(column=0, row=0, columnspan=3, sticky='W', padx=10, pady=10)

aLabel = ttk.Label(mainFrame, text='Zdrowy Sukces')
aLabel.grid(column=0, row=0)

def clickMe():
    action.configure(text='Witaj ' + name.get())


# Zmiana naszej label
aLabel.configure(text='Podaj Imię:')

# Dodanie TextBox
name = tk.StringVar()
nameEntered = ttk.Entry(mainFrame, width=20, textvariable=name)
nameEntered.grid(column=0, row=1)

# Adding a Button
action = ttk.Button(mainFrame, text='Start', command=clickMe)
action.grid(column=2, row=1)
nameEntered.focus()

ttk.Label(mainFrame, text='Wybierz dietę:').grid(column=1, row=0)
number = tk.StringVar
numberChosen = ttk.Combobox(
    mainFrame, width=20, textvariable=number, state='readonly')
numberChosen['values'] = ('Odchudzająca', 'Przeciwzapalna',
                          'Hormony +', 'Zdrowa Ja', 'Zapłać za nic :)')
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mainFrame2, text='Disabled',
                        variable=chVarDis, state='disable')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mainFrame2, text='UnChecked', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mainFrame2, text='Enabled', variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

#spinBox
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

spin = Spinbox(mainFrame, from_=0, to=10, width=4, command=_spin)
spin.grid(column=0, row=2, sticky=tk.W)

createToolTip(spin, "To nasz object spin")

# radioButton
Colors = ['blue', 'gold', 'red']


def radCall():
    radSel = radVar.get()
    if radSel == 0:
        win.configure(background=Colors[0])
    elif radSel == 1:
        win.configure(background=Colors[1])
    elif radSel == 2:
        win.configure(background=Colors[2])

radVar = tk.IntVar()
radVar.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(
        mainFrame, text=Colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

# Using scrolled Text Control
scrolW = 60
scrolH = 10
scr = scrolledtext.ScrolledText(
    mainFrame, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)
createToolTip(scr, 'To jest scr')

# label frame
labelsFrame = ttk.LabelFrame(mainFrame, text='--- Labels in Frame ---')
labelsFrame.grid(column=0, row=10, padx=10, pady=10, columnspan=3)

for col in range(3):
    ttk.Label(labelsFrame, text='Label' + str(col)).grid(column=col, row=0)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=10, pady=10, sticky='WE')

def _quit():
    win.quit()
    win.destroy()
    exit()

def _about():
    webbrowser.open_new_tab("https://zdrowy-sukces.pl/#o-mnie")

def _help():
    mBox.showinfo('Help', 'Zostałeś przekierowany na strone z pomocą!')
    webbrowser.open_new_tab("https://zdrowy-sukces.pl/#kontakt")

def _new():
    mBox.showerror('New', 'Funkcja jeszcze nie dodana :)')

# Menu
menuBar = Menu(win)
win.config(menu=menuBar)

# add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label='New', command=_new)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=_quit)
menuBar.add_cascade(label='File', menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label='About', command=_about)
helpMenu.add_separator()
helpMenu.add_command(label='Help', command=_help)
menuBar.add_cascade(label='Help', menu=helpMenu)


win.mainloop()