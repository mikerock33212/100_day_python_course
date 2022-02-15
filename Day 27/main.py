import tkinter

window = tkinter.Tk()
window.title('Mile to KM Converter')
window.minsize(width=400, height=300)
window.config(padx=20, pady=20)

# lable
label = tkinter.Label(text='is equal to: ', font=('Arial', 14, 'bold'))
# label.pack(side='left')
label.place(x=0, y=120)

label_1 = tkinter.Label(text='Miles', font=('Arial', 20, 'bold'))
label_1.place(x=270, y=50)

label_2 = tkinter.Label(text='Km', font=('Arial', 20, 'bold'))
label_2.place(x=270, y=115)

label_3 = tkinter.Label(text='', font=('Arial', 20, 'bold'))
label_3.place(x=165, y=115)

label.config()

#Entry
input_1 = tkinter.Entry(width=10)
input_1.place(x=130, y=50)
# button


def button_clicked():
    new_input = input_1.get()
    new_num = round(int(new_input) * 1.609344, 2)
    label_3.config(text=new_num)


button = tkinter.Button(text='Calculate', command=button_clicked)
button.place(x=135, y=180)
# button.pack()



window.mainloop()








# * is the unlimited positional arguments


# def add (*num):
#     result = 0
#     for n in num:
#         result += n
#     print(result)
#
# add(1)

# ** unlimited keyword arguments


# def calculate(n, **kwargs):
#     n += kwargs.get('add')
#     n *= kwargs.get('multiply')
#     n /= kwargs.get('divide')
#     print(n)
#
#
# calculate(5, add=10, multiply=10, divide=2)


# class Car:
#
#     def __init__(self, **kwargs):
#         self.make = kwargs.get('make')
#         self.model = kwargs.get('model')
#         self.year = kwargs.get('year')
#
#
# my_car = Car(make='Nissan', model='GTR')
# print(my_car.year)


