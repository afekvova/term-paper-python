from tkinter import *
from tkinter import messagebox

from pymongo import MongoClient

global connect_main, window

def book_list_view():
    temp_window = default_window()

    label_frame = Frame(temp_window, bg='yellow')
    label_frame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

    lst = [('ID', 'Назва', 'Автор', 'Статус')]

    try:
        for i in connect_main.find():
            lst.append((i['bid'], i['title'], i['author'], i['status']))
    except:
        messagebox.showinfo("Не вдалося отримати документи з бази даних")

    total_rows = len(lst)
    total_columns = len(lst[0])

    for i in range(total_rows):
        for j in range(total_columns):
            e = Entry(label_frame, width=14, fg='blue')

            e.grid(row=i, column=j)
            e.insert(END, lst[i][j])

    quit_button = Button(temp_window, text="Вийти", bg='white', fg='black', command=temp_window.destroy)
    quit_button.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    temp_window.mainloop()

def status_book_button(root, bid_info, status_info):
    bid = bid_info.get()
    status = status_info.get()

    if not bid or not status:
        messagebox.showinfo('Помилка', "Ви не заповнили поле")
        return

    myquery = {"bid": bid}
    try:
        if connect_main.count_documents(myquery) != 0:
            newvalues = {"$set": {"status": status}}
            connect_main.update_one(myquery, newvalues)
            messagebox.showinfo("Успіх", "Ви успішно змінили статус")
        else:
            messagebox.showinfo("Помилка", "ID книги відсутній")
    except:
        messagebox.showinfo("Помилка", "Не вдається отримати ID книги")

    root.destroy()

def status_book():
    temp_window = default_window()

    label_frame = Frame(temp_window, bg='yellow')
    label_frame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

    book_id_label = Label(label_frame, text="ID книги: ", bg='white', fg='black')
    book_id_label.place(relx=0.05, rely=0.2)

    book_id_info = Entry(label_frame)
    book_id_info.place(relx=0.3, rely=0.2, relwidth=0.62)

    book_status_label = Label(label_frame, text="Статус: ", bg='white', fg='black')
    book_status_label.place(relx=0.05, rely=0.4)

    book_status_info = Entry(label_frame)
    book_status_info.place(relx=0.3, rely=0.4, relwidth=0.62)

    issue_button = Button(temp_window, text="Змінити статус", bg='white', fg='black',  command=lambda: status_book_button(temp_window, book_id_info, book_status_info))
    issue_button.place(relx=0.18, rely=0.9, relwidth=0.4, relheight=0.08)

    quit_button = Button(temp_window, text="Вийти", bg='white', fg='black', command=temp_window.destroy)
    quit_button.place(relx=0.63, rely=0.9, relwidth=0.18, relheight=0.08)

    temp_window.mainloop()


def info_about_book_button(root, bid_info):
    bid = bid_info.get()

    if not bid:
        messagebox.showinfo('Помилка', "Ви не заповнили поле")
        return

    root.destroy()

    myquery = {"bid": bid}
    try:
        if connect_main.count_documents(myquery) != 0:
            temp_window = default_window()

            label_frame = Frame(temp_window, bg='yellow')
            label_frame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

            lst = [('ID', 'Назва', 'Автор', 'Статус')]

            try:
                document = connect_main.find_one(myquery)
                lst.append((document['bid'], document['title'], document['author'], document['status']))
            except:
                messagebox.showinfo("Не вдалося отримати документи з бази даних")

            total_rows = len(lst)
            total_columns = len(lst[0])

            for i in range(total_rows):
                for j in range(total_columns):
                    e = Entry(label_frame, width=14, fg='blue')

                    e.grid(row=i, column=j)
                    e.insert(END, lst[i][j])

            quit_button = Button(temp_window, text="Вийти", bg='white', fg='black', command=temp_window.destroy)
            quit_button.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

            temp_window.mainloop()
        else:
            messagebox.showinfo("Помилка", "ID книги відсутній")
    except:
        messagebox.showinfo("Помилка", "Не вдається отримати ID книги")

def info_about_book():
    temp_window = default_window()

    label_frame = Frame(temp_window, bg='yellow')
    label_frame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

    book_id_label = Label(label_frame, text="ID книги: ", bg='white', fg='black')
    book_id_label.place(relx=0.05, rely=0.2)

    book_id_info = Entry(label_frame)
    book_id_info.place(relx=0.3, rely=0.2, relwidth=0.62)

    issue_button = Button(temp_window, text="Дізнатися інформацію", bg='white', fg='black',  command=lambda: info_about_book_button(temp_window, book_id_info))
    issue_button.place(relx=0.18, rely=0.9, relwidth=0.4, relheight=0.08)

    quit_button = Button(temp_window, text="Вийти", bg='white', fg='black', command=temp_window.destroy)
    quit_button.place(relx=0.63, rely=0.9, relwidth=0.18, relheight=0.08)

    temp_window.mainloop()


def delete_book_button(root, book_title_info):
    bid = book_title_info.get()

    if not bid:
        messagebox.showinfo('Помилка', "Ви не заповнили поле")
        return

    myquery = {"bid": bid}

    try:
        connect_main.delete_one(myquery)
        messagebox.showinfo('Успіх', "Ви успішно видалили книгу")
    except:
        messagebox.showinfo("Перевірте ID книги")

    root.destroy()


def delete_book():
    temp_window = default_window()

    label_frame = Frame(temp_window, bg='yellow')
    label_frame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

    book_id_label = Label(label_frame, text="ID книги: ", bg='white', fg='black')
    book_id_label.place(relx=0.05, rely=0.5)

    book_title_info = Entry(label_frame)
    book_title_info.place(relx=0.3, rely=0.5, relwidth=0.62)

    submit_button = Button(temp_window, text="Видалити", bg='white', fg='black',
                           command=lambda: delete_book_button(window, book_title_info))
    submit_button.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quit_button = Button(temp_window, text="Вийти", bg='white', fg='black', command=temp_window.destroy)
    quit_button.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    temp_window.mainloop()


def new_book_register(root, book_bid_info, book_title_info, book_author_info, book_status_info):
    bid = book_bid_info.get()
    title = book_title_info.get()
    author = book_author_info.get()
    status = book_status_info.get().lower()

    if not bid or not title or not author or not status:
        messagebox.showinfo('Помилка', "Ви не заповнили одне з поль")
        return

    new_book = {
        "bid": bid,
        "title": title,
        "author": author,
        "status": status
    }

    try:
        connect_main.insert_one(new_book)
        messagebox.showinfo('Успіх', "Книгу успішно додано!")
    except:
        messagebox.showinfo("Помилка", "Неможливо додати дані в базу даних")

    root.destroy()


def add_new_book():
    temp_window = default_window()

    label_frame = Frame(temp_window, bg='yellow')
    label_frame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

    book_id_label = Label(label_frame, text="ID книги: ", bg='white', fg='black')
    book_id_label.place(relx=0.05, rely=0.2, relheight=0.08)

    book_id_info = Entry(label_frame)
    book_id_info.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    book_title_label = Label(label_frame, text="Назва: ", bg='white', fg='black')
    book_title_label.place(relx=0.05, rely=0.35, relheight=0.08)

    book_title_info = Entry(label_frame)
    book_title_info.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    book_author_label = Label(label_frame, text="Автор: ", bg='white', fg='black')
    book_author_label.place(relx=0.05, rely=0.50, relheight=0.08)

    book_author_info = Entry(label_frame)
    book_author_info.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    book_status_label = Label(label_frame, text="Статус: ", bg='white', fg='black')
    book_status_label.place(relx=0.05, rely=0.65, relheight=0.08)

    book_status_info = Entry(label_frame)
    book_status_info.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    submit_button = Button(temp_window, text="Добавити", bg='white', fg='black',
                           command=lambda: new_book_register(temp_window, book_id_info, book_title_info, book_author_info,
                                                             book_status_info))
    submit_button.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quit_button = Button(temp_window, text="Вийти", bg='white', fg='black', command=temp_window.destroy)
    quit_button.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    temp_window.mainloop()


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def initialize_buttons(window):
    add_book_button = Button(window, text="Добавити книгу", bg='white', fg='black', command=add_new_book)
    add_book_button.place(relx=0.28, rely=0.1, relwidth=0.45, relheight=0.1)

    delete_book_button = Button(window, text="Видалити книгу", bg='white', fg='black', command=delete_book)
    delete_book_button.place(relx=0.28, rely=0.2, relwidth=0.45, relheight=0.1)

    book_list_button = Button(window, text="Показати список книг", bg='white', fg='black', command=book_list_view)
    book_list_button.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

    set_status_book_button = Button(window, text="Задати статус", bg='white', fg='black', command=status_book)
    set_status_book_button.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    info_book_button = Button(window, text="Дізнатися інформацію", bg='white', fg='black', command=info_about_book)
    info_book_button.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    quit_book = Button(window, text="Вийти", bg='white', fg='black', command=window.destroy)
    quit_book.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)


def default_window():
    root = Tk()
    root.title("Система управління бібліотекою")
    root.minsize(width=400, height=600)
    root.resizable(0, 0)
    center(root)
    return root


window = default_window()
initialize_buttons(window)

CONNECTION_STRING = "mongodb+srv://afekvova:4267242672AfeK@cluster.3kqic.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(CONNECTION_STRING)
database = client['university']
connect_main = database['library']

window.mainloop()

# Спроба використати PyQt6
# from PyQt6.QtCore import Qt
# from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QPushButton, QWidget
#
# app = QApplication([])
# window = QWidget()
# window.setFixedWidth(400)
# window.setFixedHeight(600)
# window.setWindowTitle("Система управління бібліотекою")
# layout = QVBoxLayout()
#
# art_alb = QLabel()
# art_alb.setText("michael buble - christmas")
# layout.addWidget(art_alb, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
#
# layout.addWidget(QPushButton('Top'))
# layout.addWidget(QPushButton('Bottom'))
# window.setLayout(layout)
#
# window.show()
# app.exec()
