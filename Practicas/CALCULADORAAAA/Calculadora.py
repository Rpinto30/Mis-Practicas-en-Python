from tkinter import *
import re
from buttons_calc import *

#-----------------------------------------CREACION DE LA APLICACIÓN-----------------------------------------

root = Tk()
root.resizable(0,0)
root.title("Calculadora")

#Frames

frm_head = Frame(root)
frm_head.config(width=300, height=100, bg = "blue")
frm_head.pack(fill = X)

frm_buttons = Frame(root)
frm_buttons.config(width=300, height=300, bg = "red", )
frm_buttons.pack()

#Encabezado

entry_width = 20 
entry_data = "0"

ans_font = "Arial 20"
ans_width = 18

cal_text = Label(frm_head, text= "Calculadora",  font=('Arial', 25, 'bold'), background= "blue")

cal_text.config()

cal_text.config(justify= LEFT)
cal_text.grid(row= 0, column= 0, sticky=W)

entry = Entry(frm_head, width= entry_width, font= ("Arial", 20), textvariable= entry_data, text = "asdasd")
entry.grid(row=1, column= 0, columnspan = 2, padx= 10, pady= 5)

ans_text = Label(frm_head, text= "=", width= ans_width, font= ans_font, justify= RIGHT)
ans_text.grid(row=2, column= 0, columnspan = 2, padx= 10, pady= 5, sticky= E)

#------------------------------------------------BOTONES-------------------------------------------------

button_size = [5, 2]
buttons_pad = [5, 2]
button_font = ("Arial 10")

def set_value_entry(value = StringVar()):
    entry.insert(len(str(entry.get())) +1, value)

def set_button(button = Button, grid_pos= [0,0]):
    button.config(width= button_size[0], height = button_size[1], font= button_font)
    button.grid(row= grid_pos[0], column= grid_pos[1], padx= buttons_pad[0], pady= buttons_pad[1])

def create_button_number(num = IntVar, grid_pos = [0,0]):

    if num != 0:
        Button(frm_buttons, text= str(num), font= button_font, width= button_size[0], height= button_size[1],
           command= lambda: set_value_entry(str(num))).grid(
            row = grid_pos[0], column= grid_pos[1], padx= buttons_pad[0], pady= buttons_pad[1])
    else: 

        #   CERO

        Button(frm_buttons, text= str(num), font= button_font, width= button_size[0]*2, height= button_size[1],
           command= lambda: set_value_entry(str(num))).grid(
            row = 4, column= 2, padx= buttons_pad[0], pady= buttons_pad[1], columnspan= 2)



#-----------------------------------------------Numeros------------------------------------------------
buttons = []

i = -1
new_button = None
while i < 9:  
    u = i+1
    if i == -1: new_button = create_button_number(num= i +1, grid_pos= [4,2])

    if i < 3 and i > -1:
        new_button = create_button_number(num= i +1, grid_pos= [3, u])
    if i < 6 and i > 2:
        new_button = create_button_number(num= i +1, grid_pos= [2, u-3])
    if i < 9 and i > 5:
        new_button = create_button_number(num= i +1, grid_pos= [1, u-6])
    
    # Test 
    # print("i = " + str(i) + ";" + "u= " + str(u))

    buttons.insert(i ,new_button)
    i+=1


symbols = ["+", "-", "*", "/"]

#Operar los numeros
def set_operation():
    
    nums_ = []
    signs = []
    
    digit_first = 0
    digit_second = digit_first + 1
    data = entry.get()

    #Buscar y separar los números y simbolos
    num_finds = re.findall(r'[-+]?\d*\.?\d+', entry.get())
    sings_finds = re.findall(r'[-+*/]', entry.get())

    for numero in num_finds: nums_.append(float(numero))
    for signo in sings_finds: signs.append(signo)

    #Bucle de operaciones
    #try:
    while len(nums_) > 1:
        print("----------------Inicio bucle----------------")
        print(str(signs) + ": Start")
        print(str(nums_) + ": Start")
        data = 0
        if len(signs) > 0:

            for num in signs:
                if(num == "*" or num == "/"): 
                    digit_first = signs.index(num)
                    print("multiplica") 
                    break
                elif (num == "+" or num == "-"): 
                    if(signs.index(num) == len(signs) -1):
                        print("Sumaaa")
                        digit_first = signs.index(num) 
                    else: 
                        continue

            print(str(digit_first))

            if(signs[digit_first] == "/"):
                if(nums_[digit_second] != 0):
                    data = nums_[digit_first] / nums_[digit_second]
                else: 
                    print("NOOOOOOOOOOO")
                    nums_.clear()
                    
                if (digit_second < len(signs) and signs[digit_second] != None):
                    if(signs[digit_second] == "/"):
                        print("divideee2")
                        del nums_[digit_second]
                        del nums_[digit_first]
                        nums_.insert(0,data)
                        signs.append("+")
                        print(str(nums_) + ": before change")

                        data = nums_[digit_first] / nums_[digit_second]
                        print(str(nums_[digit_first]) + "/"+str(nums_[digit_second]) + ":change")
                        print(str(nums_) + ": after change")
                    else:
                        nums_.append(data)
                        signs.append("+")

                del signs[digit_first]
                
            elif(signs[digit_first] == "*"):
                data = nums_[digit_first] * nums_[digit_second]
                nums_.append(data)
                signs.append("+")
                del signs[digit_first]
            elif(signs[digit_first] == "+" or signs[digit_first] == "-"):
                data = nums_[digit_first] + nums_[digit_second]
                nums_.append(data)
                signs.append("+")
                del signs[0]
        
            del nums_[digit_second]
            del nums_[digit_first]
            if (digit_first + 1 < len(signs) and signs[digit_first + 1] != None):
                del signs[digit_first]

            digit_first = 0
            print(str(signs) + ": End")
            print(str(nums_) + ": End")
    else: 
        if(entry.get() == ""): 
            data = "Por favor, introduce una operación"
            ans_text.config(width= 30, font=("Arial", 10))
        else: 
            ans_text.config(font= ans_font, width=ans_width)
    #except: data = "Sintax Error"

    ans_text.config(text= data)  



#-----------------------------------------Symbols-----------------------------------------
sum_button = Button(frm_buttons, text= symbols[0])
sum_button.config(command= lambda: set_value_entry(symbols[0]))
set_button(button= sum_button, grid_pos= [3,4])

rest_button = Button(frm_buttons, text= symbols[1])
rest_button.config(command= lambda: set_value_entry(symbols[1]))
set_button(button= rest_button, grid_pos= [2,4])

mult_button = Button(frm_buttons, text= symbols[2])
mult_button.config(command= lambda: set_value_entry(symbols[2]))
set_button(button= mult_button, grid_pos= [1,4])

div_button = Button(frm_buttons, text= symbols[3])
div_button.config(command= lambda: set_value_entry(symbols[3]))
set_button(button= div_button, grid_pos= [0,4])


num_equal = Button(frm_buttons, text= "=")
num_equal.config(command= lambda: set_operation())
set_button(button= num_equal, grid_pos= [4,4])

dot_button = Button(frm_buttons, text= ".")
dot_button.config(command= lambda: set_value_entry("."))
set_button(button= dot_button, grid_pos= [4,1])


#-----------------------------------------Extras-----------------------------------------
def clear_entry(): entry.delete(0, END)
clear_button = Button(frm_buttons, text= "C", command= clear_entry)
set_button(button= clear_button, grid_pos= [0,1])


def delete_entry(): entry.delete(entry.index("end") - 1)
delete_button = Button(frm_buttons, text= "Delete", command= delete_entry)
set_button(button= delete_button, grid_pos= [0,2])

more_button = Button(frm_buttons, text= "f(x)")
set_button(button= more_button, grid_pos= [0,0])


root.mainloop()