import justpy as jp
from webapp.layout import DefaultLayout
from webapp import page

class About(page.Page):
    path ="/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = DefaultLayout(a=wp)
        
        container = jp.QPageContainer(a=lay)
        main_div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=main_div, text="This is the about page!", classes="text-4xl m-2")
        jp.Div(a=main_div, text="Tasdasfasfasfsafasfvdsgds!", classes="text-lg")
        return wp