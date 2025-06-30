###################################################################
#############################Library###############################
###################################################################
import tkinter as tk
import random  # Библиотека для псевдо случайных генераций
import os  # Библиотека для работы с файловой системой
import pyglet
import sys

###################################################################
###########################Global Var##############################
###################################################################
MODE = 'dark'
MODE_COLOR = "#312727"
FONT_COLOR = '#ffffff'
COUNTER_N = 0
COUNTER_P = 0
LOOP = False
FIRST = True
PLAYER = pyglet.media.Player()

###################################################################
#############################Function##############################
###################################################################
song_list = os.listdir(path="./songs")
cover_list = os.listdir(path="./covers")
name_list = []

for name_s in song_list:
    for name_c in cover_list:
        if name_s[:-4] == name_c[:-4]:
            name_list.append(name_c[:-4])


def swith_mode():
    global MODE, MODE_COLOR, FONT_COLOR, PLAYER, LOOP
    mode = ''
    if MODE == 'dark':
        MODE = 'light'
        mode = 'dark'
    else:
        MODE = 'dark'
        mode = 'light'
    if MODE_COLOR == "#312727":
        MODE_COLOR = "#F5F6F9"
    else:
        MODE_COLOR = "#312727"
    if FONT_COLOR == '#ffffff':
        FONT_COLOR = '#292F3B'
    else:
        FONT_COLOR = '#ffffff'
    root.config(background=MODE_COLOR)
    if PLAYER.playing:
        icon_play.config(file=f'./icons/{MODE}/play.png')
    else:
        icon_play.config(file=f'./icons/{MODE}/pause.png')
    if LOOP:
        icon_loop.config(file=f'./icons/{MODE}/loop-on.png')
    else:
        icon_loop.config(file=f'./icons/{MODE}/loop-non.png')
    icon_next.config(file=f'./icons/{MODE}/next.png')
    icon_previous.config(file=f'./icons/{MODE}/previous.png')
    icon_mode.config(file=f'./icons/{MODE}/{mode}.png')
    icon_mixer.config(file=f'./icons/{MODE}/mixed.png')
    play_btn.config(background=root.cget('background'))
    next_song_btn.config(background=root.cget('background'))
    previous_song_btn.config(background=root.cget('background'))
    loop_btn.config(background=root.cget('background'))
    mixer_btn.config(background=root.cget('background'))
    mode_btn.config(background=root.cget('background'))
    song_label.config(background=root.cget(
        'background'), foreground=FONT_COLOR)


def play():
    global name_list, COUNTER_N, COUNTER_P, FIRST, PLAYER, MODE

    if FIRST:
        NAME = name_list[0]
        source = pyglet.media.load(f'./songs/{NAME}.mp3')
        PLAYER.queue(source)
        PLAYER.play()
        cover_img.config(file=f'./covers/{NAME}.png')
        song_label.config(text=NAME)
        next_song_btn.grid(column=2, row=4)
        previous_song_btn.grid(column=0, row=4)
        COUNTER_N += 1
        FIRST = False
    elif PLAYER.playing:
        PLAYER.pause()
        icon_play.config(file=f'./icons/{MODE}/pause.png')
    elif PLAYER.playing == False:
        PLAYER.play()
        icon_play.config(file=f'./icons/{MODE}/play.png')


def next_song():
    global name_list, COUNTER_N, COUNTER_P, PLAYER, LOOP
    if abs(COUNTER_N) <= len(name_list)-1:
        NAME = name_list[COUNTER_N]
        cover_img.config(file=f'./covers/{NAME}.png')
        song_label.config(text=NAME)

        source = pyglet.media.load(f'./songs/{NAME}.mp3')
        PLAYER.queue(source)
        if PLAYER.playing:
            PLAYER.next_source()
            icon_play.config(file=f'./icons/{MODE}/play.png')
        else:
            None
        LOOP = False
        icon_loop.config(file=f'./icons/{MODE}/loop-non.png')

        if abs(COUNTER_N) + 1 <= len(name_list)-1:
            if abs(COUNTER_N - COUNTER_P) == 1 or abs(COUNTER_N - COUNTER_P) == 0:
                COUNTER_P = COUNTER_N
                COUNTER_N += 1
        else:
            None
    else:
        None


def previous_song():
    global name_list, COUNTER_N, COUNTER_P, PLAYER, LOOP
    if abs(COUNTER_P) <= len(name_list)-1:
        NAME = name_list[COUNTER_P]
        cover_img.config(file=f'./covers/{NAME}.png')
        song_label.config(text=NAME)

        source = pyglet.media.load(f'./songs/{NAME}.mp3')
        PLAYER.queue(source)
        if PLAYER.playing:
            PLAYER.next_source()
            icon_play.config(file=f'./icons/{MODE}/play.png')
        else:
            None
        LOOP = False
        icon_loop.config(file=f'./icons/{MODE}/loop-non.png')

        if abs(COUNTER_P - 1) <= len(name_list)-1:
            if abs(COUNTER_N - 1) <= len(name_list):
                if abs(COUNTER_N - COUNTER_P) == 1 or abs(COUNTER_N - COUNTER_P) == 0:
                    COUNTER_N = COUNTER_P
                    COUNTER_P -= 1
                else:
                    None
            else:
                None
        else:
            None
    else:
        None


def loop():
    global LOOP, MODE
    if LOOP:
        PLAYER.loop = False
        LOOP = False
        icon_loop.config(file=f'./icons/{MODE}/loop-non.png')
    else:
        PLAYER.loop = True
        LOOP = True
        icon_loop.config(file=f'./icons/{MODE}/loop-on.png')


def mixed():
    global name_list
    mixed_list = name_list
    random.shuffle(mixed_list)
    name_list = mixed_list


def close():
    pyglet.app.exit()
    root.destroy()
    sys.exit()

###################################################################
###########################Tkinter init############################
###################################################################


root = tk.Tk()

root.geometry("400x600+100+100")  # Задаем размер окна
root.resizable(False, False)  # Запрещаем изменение размеров окна
root.title("Mp3 player")  # Задаем название страницы
# Скрываем иконку страницы и лишние кнопки
root.attributes("-toolwindow", True)
root.config(
    background=MODE_COLOR  # Задаем цвет фона используя глобальную переменную
)
# Пути к файлам для начального положения отображаемых элементов
icon_play = tk.PhotoImage(file=f'./icons/{MODE}/play.png')
icon_next = tk.PhotoImage(file=f'./icons/{MODE}/next.png')
icon_previous = tk.PhotoImage(file=f'./icons/{MODE}/previous.png')
icon_loop = tk.PhotoImage(file=f'./icons/{MODE}/loop-non.png')
icon_mode = tk.PhotoImage(file=f'./icons/{MODE}/light.png')
icon_mixer = tk.PhotoImage(file=f'./icons/{MODE}/mixed.png')
cover_img = tk.PhotoImage(file='./covers/The Record.png')

# Объявление используемых элементов
# Кнопки
play_btn = tk.Button(image=icon_play, background=root.cget(
    'background'), borderwidth=0, command=play)
next_song_btn = tk.Button(image=icon_next, background=root.cget(
    'background'), borderwidth=0, command=next_song)
previous_song_btn = tk.Button(image=icon_previous, background=root.cget(
    'background'), borderwidth=0, command=previous_song)
loop_btn = tk.Button(image=icon_loop, background=root.cget(
    'background'), borderwidth=0, command=loop)
mixer_btn = tk.Button(image=icon_mixer, background=root.cget(
    'background'), borderwidth=0, command=mixed)
mode_btn = tk.Button(image=icon_mode, background=root.cget(
    'background'), borderwidth=0, command=swith_mode)
# Надпись которая используется в качестве окна для обложки песни
img_frame = tk.Label(height=350, width=350, borderwidth=0,
                     relief="solid", image=cover_img)
# Надпись которая используеться для отображения названия песни
frame = tk.Frame(width=350, height=25)
song_label = tk.Label(frame,
                      borderwidth=2,
                      relief="solid",
                      width=30,
                      text="The Record",
                      background=root.cget('background'),
                      foreground=FONT_COLOR,
                      justify='center',
                      font=('courier', 14))

# Позиционирование элементов
play_btn.grid(column=1, row=4, pady=15)
next_song_btn.grid(column=2, row=4)
previous_song_btn.grid(column=0, row=4)
loop_btn.grid(column=0, row=5)
mixer_btn.grid(column=2, row=5, pady=15)
mode_btn.grid(column=1, row=5)
img_frame.grid(column=0, row=0, columnspan=3, padx=25)
frame.grid(column=0, row=3, columnspan=3, padx=25, pady=15)
frame.pack_propagate(False)
song_label.pack(fill='both', expand=True)

next_song_btn.grid_forget()
previous_song_btn.grid_forget()

root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
pyglet.app.run()
