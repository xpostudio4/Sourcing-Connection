# This Script was taken from 
# https://github.com/mburst/burstolio/blob/master/tornadows.py

import os, sys
import django.core.handlers.wsgi
from tornado import httpserver, ioloop, wsgi, web
 
from optparse import OptionParser
parser = OptionParser()
 
parser.add_option('--port', dest='port')
 
options, args = parser.parse_args()
        
def runserver():
    app_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(os.path.dirname(app_dir))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'latech.settings'
    wsgi_app = wsgi.WSGIContainer(django.core.handlers.wsgi.WSGIHandler())
    application = web.Application([
        (r"/media/(.*)", web.StaticFileHandler, {"path": "app/latech/media"}),
        (r".*", web.FallbackHandler, dict(fallback=wsgi_app)),
    ])
 
    server = httpserver.HTTPServer(application)
    server.listen(options.port)
    try:
        ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        sys.exit(0)
 
if __name__ == '__main__':
    runserver()
