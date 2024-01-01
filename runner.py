import time
from tkinter import *
from tkinter import ttk
import datetime
import calendar
from PyQt6 import QtGui
import timetable as TTable

timetable = {
    'Monday': TTable.get_monday(),
    'Tuesday': TTable.get_tuesday()
}


def action(win, val):

    global root

    if val:
        win.destroy()
        root.destroy()


def alert_window(message):

    global root

    win = Toplevel()
    win.withdraw()
    win.update_idletasks()

    app = QtGui.QGuiApplication([])
    screen_width = app.primaryScreen().geometry().width()
    screen_height = app.primaryScreen().geometry().height()

    size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
    x = screen_width / 2 - size[0] / 2
    y = screen_height / 2 - size[1] / 2

    win.geometry("+%d+%d" % (x, y))
    win.deiconify()

    win.title('CRITICAL!!! ATTENTION!!!')

    ttk.Label(win, text="                              ").grid(column=1, row=1)
    ttk.Label(win, text="                              ").grid(column=2, row=1)
    ttk.Label(win, text="                              ").grid(column=3, row=1)
    ttk.Label(win, text="                              ").grid(column=1, row=2)
    ttk.Label(win, text=message).grid(column=2, row=2)
    ttk.Label(win, text="                              ").grid(column=3, row=2)
    ttk.Label(win, text="                              ").grid(column=1, row=3)
    ttk.Label(win, text="                              ").grid(column=2, row=3)
    ttk.Label(win, text="                              ").grid(column=3, row=3)
    ack_btn = ttk.Button(win, text="GOCHCHA!", command=lambda: action(win, True))
    ttk.Label(win, text="                              ").grid(column=1, row=4)
    ack_btn.grid(column=2, row=4)
    ttk.Label(win, text="                              ").grid(column=3, row=4)
    ttk.Label(win, text="                              ").grid(column=1, row=5)
    ttk.Label(win, text="                              ").grid(column=2, row=5)
    ttk.Label(win, text="                              ").grid(column=3, row=5)

    win.lift()
    win.attributes('-topmost', True)


def timetable_func():
    # get current day
    today = calendar.day_name[datetime.date.today().weekday()]

    # get day's schedule
    today_tasks = timetable.get(today)

    # start the timetabler
    for task in today_tasks:

        now = datetime.datetime.now()

        task_time = now.replace(hour=task.get('taskHour'), minute=task.get('taskMinute'))

        if now == task_time:

            root.withdraw()
            alert_window(task.get('taskName'))
            root.mainloop()

        else:

            print('nothing now')


root = Tk()
timetable_func()
