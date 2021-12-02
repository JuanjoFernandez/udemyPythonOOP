import justpy as jp
from justpy.htmlcomponents import WebPage

class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage()

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)        

        drawer = jp.QDrawer(a=layout, show_if_above=True, v_model="left",
                            bordered="True")
        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu",
                click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the home page", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        Lorem Ipsum es simplemente el texto de relleno de las imprentas
            y archivos de texto. Lorem Ipsum ha sido el texto de relleno 
            estándar de las industrias desde el año 1500, cuando un impresor 
            (N. del T. persona que se dedica a la imprenta) desconocido usó 
            una galería de textos y los mezcló de tal manera que logró hacer 
            un libro de textos especimen. No sólo sobrevivió 500 años, 
            sino que tambien ingresó como texto de relleno en documentos 
            electrónicos, quedando esencialmente igual al original. 
            Fue popularizado en los 60s con la creación de las hojas "Letraset", 
            las cuales contenian pasajes de Lorem Ipsum, y más recientemente con
            software de autoedición, como por ejemplo Aldus PageMaker, el cual 
            incluye versiones de Lorem Ipsum.
        """, classes="text-lg")

        return wp
  
    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else: 
            widget.drawer.value = True