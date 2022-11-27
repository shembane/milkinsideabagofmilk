from tkinter import *
import webbrowser

window = Tk()
window.geometry('600x800')
window.resizable(False, False)
window.title('dIE wItH rEgREts')
window.configure(bg= 'skyblue')



def rickroll():
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

def menu():
    webbrowser.open('https://pizza-shemesh.co.il/%D7%A4%D7%99%D7%A6%D7%94-%D7%A9%D7%9E%D7%A9')


Title = Label(window, text= 'Welcome To: \n Die With Regrets', height= 10, width= 25, bg= 'lightblue', fg = 'dark red')
Title.config(font= ('Comic Sans MS', 25))
Title.pack(side= TOP)

rick = Button(window, text='Rick', height=20, width= 42, command = rickroll, bg= 'green', fg = 'white')
rick.pack(side = LEFT)

food = Button(window, text='menu', height=20, width= 42, command = menu, bg = 'red', fg = 'white')
food.pack(side = RIGHT)
window.mainloop()