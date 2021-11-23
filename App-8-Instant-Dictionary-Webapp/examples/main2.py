import justpy as jp

@jp.SetRoute('/home')
def home():
    wp = jp.WebPage()
    jp.Div(a=wp, text="Hello World!")
    jp.Div(a=wp, text="Hello again!")
    return wp

@jp.SetRoute('/about')
def about():
    wp = jp.WebPage()
    jp.Div(a=wp, text="Hi World!")
    jp.Div(a=wp, text="Hey again!")
    return wp

jp.justpy()