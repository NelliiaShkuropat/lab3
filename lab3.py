import tkinter as tk
from tkinter import messagebox
import random
from string import ascii_uppercase
import winsound


def generate_key():
    word = word_entry.get()
    word = word.upper()
    if len(word) != 6 or word.isalpha() is False or any(letter not in ascii_uppercase for letter in word):
        messagebox.showerror('Ошибка', 'Введите слово из 6 латинских букв')
        return 0
    digits = ''.join(str(ascii_uppercase.index(letter) + 1)[-1] for letter in word)
    letters = ''.join(random.sample(word, len(word))) #list
    key = f'{letters[:3]}-{digits}-{letters[3:]}'
    key_entry.delete(0, 'end')
    key_entry.insert(0, key)


def animate_title(step=0):
    title.config(fg=colors[step])
    next_step = (step + 1) % len(colors)
    window.after(90, animate_title, next_step)


window = tk.Tk()
window.title('The Elder Scrolls V: Skyrim')
window.geometry('1000x750')
window.resizable(0,0)

winsound.PlaySound('Skyrim-8-Bit-Theme.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

bg_img = tk.PhotoImage(file='game.png')
label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

title = tk.Label(window, text='THE ELDER SCROLLS V: SKYRIM',
                 font=('Georgia', 26, 'bold'),
                 fg='#d8cfae', bg='#0d1014')
title.place(relx=0.5, y=15, anchor='n')

frame = tk.Frame(window, bg='#17181c', bd=2, relief='ridge') #hex, borderwidth
frame.place(relx=0.5, y=450, width=560, height=185, anchor='n') #центр на середине окна с точкой привязки сверху фрейма и отступом сверху 350

instruction = tk.Label(frame, text='Введите слово из 6 латинских букв:',
                       font=('Verdana', 12),
                       fg='#d8cfae', bg='#17181c')
instruction.place(relx=0.5, y=15, anchor='n')

word_entry = tk.Entry(frame,
                      width=10,
                      font=('Verdana', 16),
                      justify='center',
                      bg='#f0e9d2', fg='#1c1a14')
word_entry.place(relx=0.32, y=48, anchor='n')
word_entry.insert(0, 'MASTER')

button = tk.Button(frame, text='Сгенерировать ключ', width=20,
                   font=('Verdana', 12, 'bold'),
                   bg='#4a4d55', fg='#e8e0c8',
                   activebackground='#6a6d75', activeforeground='#ffffff',
                   command=generate_key)
button.place(relx=0.72, y=48, anchor='n')

key_label = tk.Label(frame,
                     text='Ваш ключ:',
                     font=('Verdana', 12),
                     fg='#d8cfae', bg='#17181c')
key_label.place(relx=0.5, y=105, anchor='n')

key_entry = tk.Entry(frame,
                     width=16,
                     font=('Verdana', 18, 'bold'),
                     justify='center',
                     bg='#f0e9d2', fg='#1c1a14')
key_entry.place(relx=0.5, y=133, anchor='n')

colors = ['#8c826b', '#a69b80', '#bfb395', '#d8cfae',
    '#f0e6c5', '#fff8e0', '#f0e6c5', '#d8cfae', '#bfb395', '#a69b80']


animate_title()

window.mainloop()