"""Basics about the justpy."""

import justpy as jp

@jp.SetRoute("/")
def home():
    wp = jp.QuasarPage(tailwind=True)
    # wp = jp.WebPage()
    main_div = jp.Div(a=wp, classes="bg-gray-200 h-screen")

    div1  = jp.Div(a=main_div, classes="grid grid-cols-3 gap-2 p-4")
    in_1 = jp.Input(a=div1, placeholder="Enter first value", classes="form-input")
    in_2 = jp.Input(a=div1, placeholder="Enter second value",classes="form-input")
    d_output = jp.Div(a=div1, text="Results goes here...", classes="text-blue-600")
    jp.Div(a=div1, text="Results goes here 2...", classes="text-blue-600")
    jp.Div(a=div1, text="Results goes here 3...", classes="text-blue-600")

    div2 = jp.Div(a=main_div, classes="grid grid-cols-2 gap-2")
    jp.QBtn(a=div2, text="Hello")
    jp.Button(a=div2, text="Calculate", click = sum_up, in1=in_1, in2=in_2,
             d = d_output,
             classes="border border-blue-500 m-10 py-1 px-4 rounded "
                     "text-blue-600 hover:bg-red-500 hover:text-white")
    jp.Div(a=div2, text="I am cool developer", mouseenter=mouse_enter, 
           mouseleave=mouse_leave, classes = "hover:bg-red-500")    
    return wp

def sum_up(widget, msg):
    print(widget.in1.value, widget.in2.value)
    sum = float(widget.in1.value) + float(widget.in2.value)
    widget.d.text = sum

def mouse_enter(widget, msg):
    widget.text = "A mouse entered the house!"

def mouse_leave(widget, msg):
    widget.text = "The mouse left."

# To start the server
jp.justpy()