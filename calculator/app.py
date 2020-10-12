from tkinter import *
import parser

root = Tk()

root.resizable(width=False, height=False)
root.title("Calculator h19")


display = Entry(root, bg="grey")
display.grid(row=1, columnspan=8,sticky=W+E) #abarca todo el largo

i = 0

def get_numbers(n):
    global i 
    display.insert(i, n)
    i+=1

def get_operation(operator):
    global i 
    operator_length = len(operator) #obtengo la longitud del operador en caso de que ocupe mas de un caracter
    display.insert(i, operator)
    i+=operator_length

def clear_display():
    display.delete(0, END)

def undo(): #recorro el estado de display y inserto un nuevo estado con el restando su ultimo elemento.
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, "Error")

def calculate():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clear_display()
        display.insert(0, result)
    except expression as indentifier:
        clear_display()
        display.insert(0, "Error")

#Buttons Numeric
btn = Button(root, text="1", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_numbers(1)).grid(row=4, column=3, sticky=W+E)
Button(root, text="2", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_numbers(2)).grid(row=4, column=2, sticky=W+E)
Button(root, text="3", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_numbers(3)).grid(row=4, column=1, sticky=W+E)
Button(root, text="4", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_numbers(4)).grid(row=3, column=3, sticky=W+E)
Button(root, text="5", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_numbers(5)).grid(row=3, column=2, sticky=W+E)
Button(root, text="6", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_numbers(6)).grid(row=3, column=1, sticky=W+E)
Button(root, text="7", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_numbers(7)).grid(row=2, column=3, sticky=W+E)
Button(root, text="8", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_numbers(8)).grid(row=2, column=2, sticky=W+E)
Button(root, text="9", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_numbers(9)).grid(row=2, column=1, sticky=W+E)
Button(root, text="0", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_numbers(0)).grid(row=5, column=2, sticky=W+E)

#Buttons functions

Button(root, text="AC", bg="darkred", fg="black", activebackground="grey", activeforeground="orange", command=lambda:clear_display()).grid(row=5, column=4, sticky=W+E)
Button(root, text="%", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_operation("%")).grid(row=5, column=1, sticky=W+E)

Button(root, text="+", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_operation("+")).grid(row=4, column=4, sticky=W+E)
Button(root, text="-", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_operation("-")).grid(row=2, column=4, sticky=W+E)
Button(root, text="/", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_operation("/")).grid(row=3, column=4, sticky=W+E)
Button(root, text="=", bg="darkgreen", fg="black", activebackground="grey", activeforeground="orange",command=lambda:calculate()).grid(row=5, column=6, sticky=W+E , columnspan=2)
Button(root, text=".", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_operation(".")).grid(row=5, column=3, sticky=W+E)


Button(root, text="⇚", bg="darkred", fg="black", activebackground="grey", activeforeground="orange",command=lambda:undo()).grid(row=2, column=6, sticky=W+E)
Button(root, text="*", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_operation("*")).grid(row=2, column=7, sticky=W+E)
Button(root, text="exp", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_operation("**")).grid(row=3, column=6, sticky=W+E)
Button(root, text="^2", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_operation("**2")).grid(row=4, column=6, sticky=W+E)
Button(root, text="(", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_operation("(")).grid(row=3, column=7, sticky=W+E)
Button(root, text=")", bg="black", fg="orange", activebackground="grey", activeforeground="orange",command=lambda:get_operation(")")).grid(row=4, column=7, sticky=W+E)















root.mainloop()