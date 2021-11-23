import justpy as jp
from pandas.core.dtypes.common import classes

@jp.SetRoute('/home')
def home():
    wp = jp.WebPage()
    div = jp.Div(a=wp, classes="bg-gray-200 h-screen")

    div1 = jp.Div(a=div, classes="grid grid-cols-3 gap-4")
    jp.Input(a=div1, placeholder="Enter first value", classes="form-input")
    jp.Input(a=div1, placeholder="Enter second value", classes="form-input")
    jp.Div(a=div1, text="Result goes here...", classes="text-gray-600")
    jp.Div(a=div1, text="One div", classes="text-gray-600")
    jp.Div(a=div1, text="Another div", classes="text-gray-600")
    
    div2 = jp.Div(a=div, classes="grid grid-cols-2 gap-4")
    jp.Button(a=div2, text="Calculate",
              classes="border border-blue-500 m-2 py-1 px-4 rounded "
                      "text-blue-600 hover:bg-blue-900 hover:text-white")

    jp.Div(a=div2, text="I am a cool interactive div!")
    return wp

jp.justpy()