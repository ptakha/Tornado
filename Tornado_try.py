import tornado.ioloop
import tornado.web
import tornado.httpserver

class MainHandler(tornado.web.RequestHandler):
    def get(self):
		form=""" <form method = "post">
		<input type="text" name="number"/>
		</form>"""
		self.write(form)
    def post(self):
		number=int(self.get_argument('number_2'))
		self.write(str(number**2))
		

def make_app():
	return tornado.web.Application([(r"/", MainHandler),])


if __name__=="__main__":
	app=make_app()
	http_server=tornado.httpserver.HTTPServer(app)
	app.listen(1024)
	tornado.ioloop.IOLoop.current().start()
