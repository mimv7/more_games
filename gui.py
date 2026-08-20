from tkinter import *

root = Tk()
root.title('hello')
root.geometry('200x85')

# Создаем фрейм (контейнер) для виджетов
app = Frame(root)
app.grid()

# Создаем и размещаем кнопку
btn1 = Button(app, text='useless')

btn1.grid()

# Запускаем окно ОДИН раз в самом конце кода
root.mainloop()
