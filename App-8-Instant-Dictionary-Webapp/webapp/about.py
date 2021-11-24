import justpy as jp

class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage()
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the about page", classes="text-4xl m-2")
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
    
jp.Route(About.path, About.serve)
jp.justpy()