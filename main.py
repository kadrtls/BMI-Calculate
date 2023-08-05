from  tkinter import *

window=Tk()
window.title("BMI Calculate")
window.minsize(width=300,height=250)

def calculate_BMI():
    weight=weight_entry.get()
    height=height_entry.get()

    if weight=="" or height=="":
        label_result.config(text="Enter both weight and height")
    elif type(weight)!=int or type(height)!=int:
        label_result.config(text="Please enter a valid value")
    else:
        bmı_indeks=float(weight) / (float(height)/100) **2
        bmı_indeks=round(bmı_indeks,2)
        if bmı_indeks<18.5:
            label_result.config(text=f"Your bmı is {bmı_indeks},you are a under weight")
        elif 18<=bmı_indeks<24.9:
            label_result.config(text=f"Your bmı is {bmı_indeks},you are a normal weight")
        elif 25 <= bmı_indeks <29.9:
            label_result.config(text=f"Your bmı is {bmı_indeks},you are a overweight")
        elif 30 <= bmı_indeks <34.9:
            label_result.config(text=f"Your bmı is {bmı_indeks},you are a obese class 1")
        elif 35<=bmı_indeks<39.9:
            label_result.config(text=f"Your bmı is {bmı_indeks}you are a obese class 2")
        else:
            label_result.config(text=f"Your bmı is {bmı_indeks},you are a obese class 3")

label_kg = Label(text="Enter your weight (kg)")
label_kg.config(pady=10)
label_kg.pack()

weight_entry = Entry(width=20)
weight_entry.pack()

label_height = Label(text="Enter your height (cm)")
label_height.config(pady=10)
label_height.pack()

height_entry = Entry(width=20)
height_entry.pack()


#def bmı_value():
    # if bmı_indeks<18.5:
    #     print(f"Your bmı is {bmı_indeks},you are a under weight")
    # elif 18<=bmı_indeks<24.9:
    #     print(f"Your bmı is {bmı_indeks},you are a normal weight")
    # elif 25 <= bmı_indeks <29.9:
    #     print(f"Your bmı is {bmı_indeks},you are a overweight")
    # elif 30 <= bmı_indeks <34.9:
    #     print(f"Your bmı is {bmı_indeks},you are a obese class 1")
    # elif 35<=bmı_indeks<39.9:
    #     print(f"Your bmı is {bmı_indeks}you are a obese class 2")
    # else:
    #     print(f"Your bmı is {bmı_indeks},you are a obese class 3")


calculate_button = Button(text="Calculate",command=calculate_BMI)
calculate_button.pack()

label_result=Label()
label_result.pack()

window.mainloop()