import random
from tkinter import *
from tkinter import filedialog as fd

root = Tk()
root.geometry('800x400')
img = PhotoImage(file='photo.gif')

outputText = Label(bg='white', fg='black', font=("Impact", 34))
outputText.place(relx=0.0, rely=0.0, relwidth=0.9, relheight=0.2)
generateButton = Button(text="Генерация", image=img)
generateButton.place(relx=0.9, rely=0.0, relwidth=0.1, relheight=0.2)
openFileButton = Button(text="Открыть файл")
openFileButton.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.2)


def changeSourceText(event):
    file_name = fd.askopenfilename()
    i = open(file_name, encoding="utf-8")
    o = open("input.txt", "w+", encoding="utf-8")
    temp = i.read()

    o.truncate(0)
    o.write(temp)

    i.close()
    o.close()


def readInput(inputText):
    skipLines(inputText, 1)
    temp = inputText.readline()
    return temp[:-1].split(" ")


def addConsonant(word, consonants):
    if random.randint(0, 9) == 0:
        word += consonants[random.randint(0, len(consonants) - 1)]
    return word + consonants[random.randint(0, len(consonants) - 1)]


def addVowel(word, vowels):
    return word + vowels[random.randint(0, len(vowels) - 1)]


def skipLines(inputText, linesAmount):
    for i in range(0, linesAmount):
        inputText.readline()


def generate(event):
    inputText = open("input.txt", encoding="utf-8")

    wordAmount: int = 2
    vowels = readInput(inputText)
    vowelsEnd = readInput(inputText)
    consonants = readInput(inputText)
    consonantsEnd = readInput(inputText)

    word: str = ""
    for i in range(0, wordAmount):
        temp = random.randint(2, 4)
        isFirstVowel = bool(random.getrandbits(1))

        for j in range(0, temp):
            if isFirstVowel:
                word = addVowel(word, vowels)
                word = addConsonant(word, consonants)
            else:
                word = addConsonant(word, consonants)
                word = addVowel(word, vowels)

        # Ртятяго Мугросердь, [07.03.19 22: 14] ЕСЛИ ПОСЛЕДНЯЯ БУКВА ГЛАСНАЯ ТО ГЛАСНОЕОКОНЧАНИЕ
        # ЕСЛИ ПОСЛЕДНЯЯ БУКВА СОГЛАСНАЯ ТО СОГЛАСНОЕОКОНЧАНИЕ
        # Ртятяго Мугросердь, [07.03.19 22: 14] ГДЕ ГЛАСНОЕ ОКОНЧАНИЕ ЭТО "ОКОНЧАНИЕ ДЛЯ ГЛАСНОЙ"

        if random.randint(0, 3) == 0:
            if isFirstVowel:
                word += consonantsEnd[random.randint(0, len(consonantsEnd) - 1)]
            else:
                word += vowelsEnd[random.randint(0, len(vowelsEnd) - 1)]
        word += " "
    outputText['text'] = ' '.join(word)


generateButton.bind('<Button-1>', generate)
openFileButton.bind('<Button-1>', changeSourceText)

root.mainloop()
