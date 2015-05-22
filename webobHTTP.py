"""
author mrequ
all right reserver 2015!!!

Script connectes with wikipedia.org and httpbin.org
tries to send http request using the webob pack and get response
then writes recived date for each request
to files into current directory"""

from webob import Request,Response 
WIKI = 'wikipedia.org'
HTTPBIN = 'httpbin.org'
BUFF_SIZE = 4096

#zapros poluchayet glavnuyu stranicu sayta wikipedia
reqWiki = Request.blank("wiki/Main_Page")
reqWiki.host = WIKI
reqWiki.environ["SERVER_NAME"] = WIKI
reqWiki.accept = "text/html"
reqWiki.user_agent = "User-Agent: Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509 Firefox/3.0b5"


#zapros poluchayet ip adres kliyenta
reqH1 = Request.blank("ip")
reqH1.host = HTTPBIN
reqH1.environ["SERVER_NAME"] = WIKI
reqH1.accept = '*/*'

#zapros posylayet severu informachiyu s pomoshyu metoda get 
#poluchayet otvet v vide spiska peredannyh parametrov
reqH2 = Request.blank("get?foo=bar&1=2&2/0&error=True")
reqH2.host = HTTPBIN
reqH2.environ["SERVER_NAME"] = HTTPBIN
reqH2.accept = '*/*'

#zapros posylayet severu informachiyu s pomoshyu metoda post 
#poluchayet otvet v vide spiska peredannyh parametrov
reqH3 = Request.blank("post")
reqH3.host = HTTPBIN
reqH3.environ["SERVER_NAME"] = HTTPBIN
reqH3.method = 'POST'
reqH3.content_length = 35
reqH3.content_type = "application/x-www-form-urlencoded"
reqH3.body = "foo=bar&1=2&2%2F0=&error=True"

#zapros ustanavlivayet cookie
reqH4 = Request.blank('cookies/set?country=Ru')
reqH4.host = HTTPBIN
reqH4.environ["SERVER_NAME"] = HTTPBIN
reqH4.accept = '*/*'

#zapros poluchayet cookie
reqH5 = Request.blank("cookies")
reqH5.host = HTTPBIN
reqH5.environ["SERVER_NAME"] = HTTPBIN
reqH5.accept = '*/*'
 
#zapros posylayet 'redirect/4'
#v otvet poluchayet ssylku na perenapravleniye
reqH6 = Request.blank('redirect/4')
reqH6.host = HTTPBIN
reqH6.environ["SERVER_NAME"] = HTTPBIN
reqH6.accept = '*/*'

#ZADANIYE 4
#zapros posylayet severu informachiyu s pomoshyu metoda post 
#poluchayet otvet v vide spiska peredannyh parametrov
reqExtra = Request.blank("post")
reqExtra.host = HTTPBIN
reqExtra.environ["SERVER_NAME"] = HTTPBIN
reqExtra.method = 'POST'
post_body = "firstname=Alex&lastname=Macedonian&group=fo321001&message=helloWorld"
reqExtra.content_length = len(post_body)
reqExtra.content_type = "application/x-www-form-urlencoded"
reqExtra.body = post_body


requests = [reqWiki,reqH1,reqH2,reqH3,reqH4,reqH5,reqH6,reqExtra]

i=0
for req in requests:
    res = req.get_response()
    f = open(req.host+str(i)+".html",'w')
    f.write(res.body)
    f.close();
    i=i+1
