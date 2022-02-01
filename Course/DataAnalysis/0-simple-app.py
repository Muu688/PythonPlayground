import justpy as jp

# The main webpage
def app():
    wp = jp.QuasarPage()

    # Write elements for the Wep Page
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h1 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-body1")
    
    return wp

jp.justpy(app)