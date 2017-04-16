import web
import wangka

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
        number = int(user_data.number)
        result = wangka.wangka().get_wangka_number(int(user_data.number))
        render = web.template.render('.')
        return render.translated(number, result)

if __name__ == "__main__":
    app.run()