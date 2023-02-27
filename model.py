from datetime import datetime

id = None
title = None
body = None
date = None
currentNotes = []

def view_data(data):
    print(data)

def printNote(i):
    print(f"{currentNotes[i]}\n{currentNotes[i+1]}\n{currentNotes[i+2]}\n{currentNotes[i+3]}\n")

def printAll():
    i = 0
    while i < len(currentNotes):
        printNote(i)
        i += 4

def getData():
    return str(input("=> "))

def findMaxId():
    max = 0
    i = 0
    while i < len(currentNotes):
        if int(currentNotes[i]) > max: max = int(currentNotes[i])
        i += 4
    return max

def addNote():
    global id
    global title
    global body
    global date
    
    id = int(findMaxId()) + 1
    print("введите заголовок")
    title = getData()
    print("введите текст заметки")
    body = getData()
    date = datetime.now()
    currentNotes.extend([id, title, body, date])

def editNote(value):
    print(searchId(value))
    global id
    global title
    global body
    global date
    global currentNotes

    id = value
    i = searchId(value)
    print(f"текущий заголовок => {currentNotes[i + 1]}\n Введите новый заголовок или введите 's', чтобы оставить заголовок без измемнения")
    temp = getData()
    if temp == "s" or temp == "S":
        title = currentNotes[i + 1]
    else: title = temp
    print(f"текущий текст заметки => {currentNotes[i + 2]}\n Введите новый текст или введите 's', чтобы оставить заголовок без измемнения")
    temp = getData()
    if temp == "s" or temp == "S":
        body = currentNotes[i + 2]
    else: body = temp
    date = datetime.now()

    deleteNoteById(value)
    currentNotes.extend([id, title, body, date])

def importAll():
    global currentNotes
    with open("заметки.csv", "r") as file1:
        for line in file1:
            currentNotes.extend(line.strip().split(";"))
    file1.close()

def searchId(value):
    global currentNotes
    i = 0
    temp = 0
    while i < len(currentNotes):
        if currentNotes[i] == value:

            temp = i
        i = i + 4
    return temp

def searchByDate(value):
    i = 3
    while i < len(currentNotes):
        if currentNotes[i] == value:
            print(f"{currentNotes[i-3]}\n{currentNotes[i-2]}\n{currentNotes[i-1]}\n{currentNotes[i]}")
        i = i + 4

def deleteNoteById(value):
    i = 0
    while i < len(currentNotes):
        if currentNotes[i] == value:
            del currentNotes[i : i + 4]
        i = i + 4

def exportAll():
    file = open("заметки.csv", "w")
    i = 0
    while i < (len(currentNotes)):
        file.write(f"{currentNotes[i]};{currentNotes[i+1]};{currentNotes[i+2]};{currentNotes[i+3]}\n")
        i += 4
    file.close()