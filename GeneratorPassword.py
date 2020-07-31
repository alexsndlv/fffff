from tkinter import *
from tkinter import messagebox as mb
from random import *

class Mine:

    def __init__(self, root):

        self.label_hello = Label(root, width=20, font=75, text='Настройка пароля')
        self.label_hello.grid(row=0, column=0, sticky=W)

        self.digits_bool=BooleanVar()
        self.digits_bool.set(0)
        self.checkbox_digits = Checkbutton(text='Включать ли цифры - 0123456789?',
                               variable=self.digits_bool, onvalue=1, offvalue=0)
        self.checkbox_digits.grid(row=1, column=0, sticky=W)

        self.uppercase_letters_bool = BooleanVar()
        self.uppercase_letters_bool.set(0)
        self.checkbox_uppercase_letters = Checkbutton(text='Включать ли заглавные буквы - ABCDEFGHIJKLMNOPQRSTUVWXYZ?',
                               variable=self.uppercase_letters_bool, onvalue=1, offvalue=0)
        self.checkbox_uppercase_letters.grid(row=2, column=0, sticky=W)

        self.lowercase_letters_bool = BooleanVar()
        self.lowercase_letters_bool.set(0)
        self.checkbox_lowercase_letters = Checkbutton(text='Включать ли строчные буквы - abcdefghijklmnopqrstuvwxyz?',
                               variable=self.lowercase_letters_bool, onvalue=1, offvalue=0)
        self.checkbox_lowercase_letters.grid(row=3, column=0, sticky=W)

        self.punctuation_bool = BooleanVar()
        self.punctuation_bool.set(0)
        self.punctuation = Checkbutton(text='Включать ли символы - !#$%&*+-=?@^_ ?',
                               variable=self.punctuation_bool, onvalue=1, offvalue=0)
        self.punctuation.grid(row=4, column=0, sticky=W)

        self.entry = Entry(root)
        self.entry.grid(row=5, column=0)
        self.label_len_password = Label(root, text='Введите длинну пароля:')
        self.label_len_password.grid(row=5, column=0, sticky=W)

        self.button = Button(text='Сгенерировать',command=self.generator_password)
        self.button.grid(row=6, column=0, sticky=W)

        self.label_password = Label(root, text='Ваш пароль:')
        self.label_password.grid(row=7, sticky=W)
        
    def generator_password(self):
        ''' Generator password '''
        try:
            # var
            password = ''
            self.len_password = self.entry.get()
            self.count = int(self.len_password)

            
            # const
            self.digits = '0123456789'
            self.lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
            self.uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            self.punctuation = '!#$%&*+-=?@^_'
            
            # arr
            self.lst = [self.digits_bool, self.uppercase_letters_bool, self.lowercase_letters_bool, self.punctuation_bool]
            self.lst1 = [self.digits, self.uppercase_letters, self.lowercase_letters, self.punctuation]

            while self.count > 0:
                self.random_num = randint(0, 3)
    
                if self.lst[self.random_num].get():
                    self.f = self.lst1[self.random_num]
                    password += self.f[randint(0, len(self.lst1[self.random_num]) - 1)]
                    self.count -= 1

            self.label_password.configure(text=f'Ваш пароль: {password}')

        except ValueError:
            mb.showerror('Ошибка', 'Вы ввели неправильную длинну пароля')

root = Tk()
root.title('Генератор паролей')
root.geometry('400x200+200+100')
root.resizable(width=False, height=False)

q=Mine(root)

root.mainloop()
