import tkinter as tk

#Global declare the expression variable
expression = ""

#Create press function in the expression_field
def press(num):
    global expression

    expression = expression+str(num)

    #update express
    equation.set(expression)

def clear():
    global expression 
    expression = ""
    equation.set("")

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("error")
        expression=""

def percent():
    try:
        global expression
        result = str(eval(expression + "/100"))
        equation.set(result)
        expression = result
    except:
        equation.set("error")
        expression = ""

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def ClearEntry():
    global expression
    expression = expression[:-3]
    equation.set(expression)


app = tk.Tk()

#Set Background color of GUI Window
app.configure(background="old lace")

#Set title
app.title("Simple Calculator")

#Set size of window
app.geometry("600x800")

equation = tk.StringVar()

#Create TexBox for expression
expression_field = tk.Entry(app, textvariable=equation, bg="snow",font=('Arial 20'),width=30,justify="right", relief="solid").grid(columnspan=4,)

#Create Button Number
btnPercent = tk.Button(app, text=" % ", bg="pale turquoise", fg="dim gray",command=lambda: percent(), height=2,width=15).grid(row=2, pady=2, column=0)
btnCE = tk.Button(app, text=" CE ", bg="pale turquoise", fg="dim gray",command=lambda: ClearEntry(), height=2,width=15).grid(row=2, pady=2, column=1)
btnC = tk.Button(app, text=" C ",command=lambda: clear(), bg="pale turquoise", fg="dim gray", height=2,width=15).grid(row=2, pady=2, column=2)
btnDelete = tk.Button(app, text=" <- ", bg="salmon", fg="dim gray",command=lambda: backspace(), height=2,width=15).grid(row=2, pady=2, column=3)

#line Number 7-9 and X
btn7 = tk.Button(app, text=" 7 ", bg="misty rose", fg="dim gray",command=lambda: press(7), height=2,width=15).grid(row=3, pady=2, column=0)
btn8 = tk.Button(app, text=" 8 ", bg="misty rose", fg="dim gray",command=lambda: press(8), height=2,width=15).grid(row=3, pady=2, column=1)
btn9 = tk.Button(app, text=" 9 ", bg="misty rose", fg="dim gray",command=lambda: press(9), height=2,width=15).grid(row=3, pady=2, column=2)
btnMultiplied = tk.Button(app, text=" * ", bg="pale turquoise", fg="dim gray",command=lambda: press('*'), height=2,width=15).grid(row=3, pady=2, column=3)

#line Number 4-6 and -
btn4 = tk.Button(app, text=" 4 ", bg="misty rose", fg="dim gray",command=lambda: press(4), height=2,width=15).grid(row=4, pady=2, column=0)
btn5 = tk.Button(app, text=" 5 ", bg="misty rose", fg="dim gray",command=lambda: press(5), height=2,width=15).grid(row=4, pady=2, column=1)
btn6 = tk.Button(app, text=" 6 ", bg="misty rose", fg="dim gray",command=lambda: press(6), height=2,width=15).grid(row=4, pady=2, column=2)
btnMinus = tk.Button(app, text=" - ", bg="pale turquoise", fg="dim gray",command=lambda: press('-'), height=2,width=15).grid(row=4, pady=2, column=3)

#line Number 1-3 and +
btn1 = tk.Button(app, text=" 1 ", bg="misty rose", fg="dim gray",command=lambda: press(1), height=2,width=15).grid(row=5, pady=2, column=0)
btn2 = tk.Button(app, text=" 2 ", bg="misty rose", fg="dim gray" ,command=lambda: press(2), height=2,width=15).grid(row=5, pady=2, column=1)
btn3 = tk.Button(app, text=" 3 ", bg="misty rose", fg="dim gray",command=lambda: press(3), height=2,width=15).grid(row=5, pady=2, column=2)
btnPlus = tk.Button(app, text=" + ", bg="pale turquoise", fg="dim gray",command=lambda: press('+'), height=2,width=15).grid(row=5, pady=2, column=3)

#line Number / and 0 and . and =
btnDivide = tk.Button(app, text=" / ", bg="pale turquoise", fg="dim gray",command=lambda: press('/'), height=2,width=15).grid(row=6, pady=2, column=0)
btn0 = tk.Button(app, text=" 0 ", bg="misty rose", fg="dim gray",command=lambda: press(0), height=2,width=15).grid(row=6, pady=2, column=1)
btnDecimal = tk.Button(app, text=" . ", bg="pale turquoise", fg="dim gray",command=lambda: press('.'), height=2,width=15).grid(row=6, pady=2, column=2)
btnEque = tk.Button(app, text=" = ", bg="pale green", fg="dim gray",command=lambda: equalpress(), height=2,width=15).grid(row=6, pady=2, column=3)


app.mainloop()