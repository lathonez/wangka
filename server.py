import web

urls = (
    '/translate', 'translate',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        render = web.template.render('.')
        return render.index()
        
class translate:
    def GET(self):
        user_data = web.input()
        return user_data.number

if __name__ == "__main__":
    app.run()