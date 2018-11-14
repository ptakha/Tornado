#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This is second try"""
import os
import random
import ssl
import json
import tornado.web
import tornado.httpserver
import tornado.ioloop

ssl_ctx=ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_ctx.load_cert_chain("CA_test/localhost.cert.pem", "CA_test/localhost.key.pem")
ssl_ctx.load_verify_locations("CA_test/ca.cert.pem")
ssl_ctx.load_verify_locations("test/ca_client.cert.pem")
ssl_ctx.verify_mode = ssl.CERT_REQUIRED


# pylint: disable = W0223, invalid-name, arguments-differ

class MainHandler(tornado.web.RequestHandler):
    """Request handler for the main page of the app localhost:1025"""
    def get(self):
        """Information about server which returns with  HTTP Get"""
        self.render("MainPage.html")
    def post(self):
        """Post function"""
        if self.get_argument('User') == "U" and self.get_argument('Password') == "R":
            self.write("Ok")
            self.redirect("https://localhost:1027/random")
        else:
            self.write("Nope")

class MathHandler(tornado.web.RequestHandler):
    """Request handler for random page"""
    def get(self):
        """get function"""
        self.write("Random !!!")
        self.write("\n")
        self.write(str(random.randint(0, 1000)))
    def post(self):
        """Post function"""
        self.write(str(random.randint(0, 1000)))
class JsonHandler(tornado.web.RequestHandler):
    """Request handler for json messages"""
    def initialize(self):
        """Auth by cert"""
        client_cert = self.request.get_ssl_certificate()
        cert_dict = {}
        for i in range(len(client_cert['subject'])):
            cert_dict.update(dict(client_cert['subject'][i]))
        self.client_dn = cert_dict
        if self.client_dn['organizationName'] != 'Some_organization':
            self.write('Acces denied')
            self.finish()
    def get(self):
        """get function of jsonhandler"""
        self.write(self.client_dn)
    def post(self):
        """post function of json handler"""
        self.write(self.request.get_ssl_certificate())
        json_message = json.loads(self.request.body.decode('string-escape').strip('"'))
        #json.loads(json.loads(self.request.body)) #you can try with this too ^^
        if json_message["source"] == "InstallDIRAC":
            self.write("\nSource is correct")
def make_app():
    """Make app with two pages main and random"""
    return tornado.web.Application([(r"/", MainHandler), (r"/random", MathHandler),
                                    (r"/json", JsonHandler)])

if __name__ == "__main__":
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app, ssl_options=ssl_ctx)
    http_server.listen(1027)
    tornado.ioloop.IOLoop.current().start()
    print(entry)
