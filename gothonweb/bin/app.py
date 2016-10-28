import web

urls = ('/','index')

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
    def GET(self):
        greeting = "Hello World"
        return render.my_html()

if __name__ == "__main__":
    app.run()