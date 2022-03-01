import code
urls = (
'/input', 'index'
)
class index:
    def GET(self):
        i = code.input(name=None)
        return render.index(i.name)
if __name__ == "__main__":
    app = code.application(urls, globals())
    app.run()
render = code.template.render('templates/')