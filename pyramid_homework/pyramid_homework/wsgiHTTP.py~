"""
author mrequ
all right reserved 2015!!!


script runs paste httpServer on localhost with wsgi app, that 
renders jinja2 templates
"""

import selector
from jinja2 import Environment,FileSystemLoader

status = '200 OK'
http_headers = [('Content-Type', 'text/html; charset=UTF-8')]
ABOUTME_LINK = """<a href="about/about.html">LINK TO aboutme.html</a>"""
INDEX_LINK = """<a href="../index.html">LINK TO INDEX.HTML</a>"""


class BaseApp(object):

    def __init__(self,environ,start_response,link,template):
        self.env = environ
        self.start_response = start_response
        self.teplates  = Environment(loader=FileSystemLoader('templates'))
        self.template = template
        self.link = link

    def __iter__(self):
        self.start_response(status,http_headers)
        template = self.teplates.get_template(self.template)
        yield template.render(link=self.link)
             
class IndexApp(BaseApp):
    def __init__(self,environ,start_response):
        BaseApp.__init__(self, environ, start_response, ABOUTME_LINK, "index.html")

class AboutApp(BaseApp):
    def __init__(self,environ,start_responce):
        BaseApp.__init__(self,environ,start_responce,INDEX_LINK,"about.html")

def init():
    disp =  selector.Selector()
    disp.add("/index.html",GET=IndexApp)
    disp.add("/about/about.html",GET=AboutApp)
    return disp



if __name__=="__main__":
    from paste.httpserver import serve
    app = init()
    serve( app, host='localhost', port=8000)
