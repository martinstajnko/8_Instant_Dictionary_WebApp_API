import justpy as jp
from webapp.layout import DefaultLayout
from webapp import page

class Home(page.Page):
    path ="/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = DefaultLayout(a=wp)
        
        container = jp.QPageContainer(a=lay)

        main_div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=main_div, text="This is the home page!", classes="text-4xl m-2")
        jp.Div(a=main_div, text="Tasdasfasfasfsafasfvdsgds!", classes="text-lg")
        return wp

