from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QBoxLayout, QListWidget, QPushButton, QLineEdit
import json

app = QApplixation([])
window = QWidget()

song_names = QListWidget()
songs_text = QTextEdit()
songs_line = QLineEdit()
songs_line.setPlaceholderText('Введите Песню....')
add_song_button = QPushButton('Добавить Песню')
edit_song_button = QPushButton('Изменить Песню')
del_song_button = QPushButton('Удалить Песню')

layout_main = QHBoxLayout()

layout_v = QVBoxLaout()
layout_v.addWidget(songs_text)
layout_v.addWidget(songs_line)

layout_line_buttons = QHBoxLayout()
layout_line_buttons.addWidget(add_song_button)
layout_line_buttons.addWidget(edit_song_button)
layout_line_buttons.addWidget(del_song_button)

layout_v.addLayout(layout_line_buttons)

layout_main.addWidget(song_names)
layout_main.addLayout(layout_v)

with open('songs.json', 'r', encoding='utf-8') as file:
    songs = json.load(file)
    songs_names.addItems(songs)

'''Функции'''

def add_song():
    song = songs_line.text()
    with open('songs.json', 'r', encoding='utf-8') as file:
        songs = json.load(file)
    songs[song] = ''
    with open('songs.json', 'w', encoding='utf-8') as file:
        json.dump(songs, file)
    songs_names.clear()
    songs_names.addItems(songs)

def info_song():
    song = songs_names.selectedItems()[0].txt()
    with open('songs.json', 'r', encoding='utf-8') as file:
        songs = json.load(file)
    songs_text.setText(songs[song])

def edit_song():
    if songs_names.selectedItems():
        text_song = songs_text.toPlainText()
        song = s_song.selectedItems()[0].text()
        with open('songs.json', 'r', encoding='utf-8') as file:
        songs = json.load(file)
    songs[song] = text_song
    with open('songs.json', 'w', encoding='utf-8') as file:
        json.dump(songs, file)
    songs_names.clear()
    songs_text.clear()
    songs_names.addItems(songs)

def del_song():
    if songs_names.selectedItems():
        song = songs_names.selectedItems()[0].text()
        with open('songs.json', 'r', encoding='utf-8') as file:
        songs = json.load(file)
    del songs[game]
    with open('songs.json', 'w', encoding='utf-8') as file:
        json.dump(songs, file)
    songs_names.clear()
    songs_text.clear()
    songs_names.addItems(songs)


    add_song_button.clicked.connect(add_song)
    songs_names.itemClicked.connect(info_songs)
    edit_song_button.clicked.connect(edit_song)
    del_song_button.clicked.connect(del_song)

    window.setLayout(layout_main)
    window.show()
    app.exec()

