import pyttsx3
import random
from PIL import Image
b1 = b2 = b3 = b4 = b5 = b6 = b7 = pyttsx3.init()
voices = b1.getProperty('voices')
voices = b2.getProperty('voices')
voices = b3.getProperty('voices')
voices = b4.getProperty('voices')
voices = b5.getProperty('voices')
voices = b6.getProperty('voices')
voices = b7.getProperty('voices')
b1.setProperty('voice', 'ru')
b2.setProperty('voice', 'ru')
b3.setProperty('voice', 'ru')
b4.setProperty('voice', 'ru')
b5.setProperty('voice', 'ru')
b6.setProperty('voice', 'ru')
b7.setProperty('voice', 'ru')
a1 = Image.open("капусты.png")
a2 = Image.open("луки.png")
a3 = Image.open("яблоки.png")
a4 = Image.open("сыры.png")
a5 = Image.open("арбузы.png")
a6 = Image.open("кексы.png")
a7 = Image.open("бананы.png")
mas = ["капуста","лук","яблоко","сыр","арбуз","кекс","банан"]
p1 = random.randint(0,6)
p2 = random.randint(0,6)
p3 = random.randint(0,6)
if mas[p1] == "капуста" and mas[p2] == "капуста" and mas[p3] == "капуста":
    a1.show()
    b1.say('вы выиграли 100 рублей')
    b1.runAndWait()
elif mas[p1] == "лук" and mas[p2] == "лук" and mas[p3] == "лук":
    a2.show()
    b2.say('вы выиграли 200 рублей')
    b2.runAndWait()
elif mas[p1] == "яблоко" and mas[p2] == "яблоко" and mas[p3] == "яблоко":
    a3.show()
    b3.say('вы выиграли 300 рублей')
    b3.runAndWait()
elif mas[p1] == "сыр" and mas[p2] == "сыр" and mas[p3] == "сыр":
    a4.show()
    b4.say('вы выиграли 400 рублей')
    b4.runAndWait()
elif mas[p1] == "арбуз" and mas[p2] == "арбуз" and mas[p3] == "арбуз":
    a5.show()
    b5.say('вы выиграли 1.000.000 рублей')
    b5.runAndWait()
elif mas[p1] == "кекс" and mas[p2] == "кекс" and mas[p3] == "кекс":
    a6.show()
    b6.say('вы выиграли 500 рублей')
    b6.runAndWait()
elif mas[p1] == "груша" and mas[p2] == "груша" and mas[p3] == "груша":
    a7.show()
    b7.say('вы выиграли 600 рублей')
    b7.runAndWait()
else:
    print("упс... вы ничего не выиграли, попробуйте еще!")