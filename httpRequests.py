import socket as s


"""
Script connectes with wikipedia.org and httpbin.org 
tries to send http request and get response
then writes recived date to files for each request
"""

WIKI = 'wikipedia.org'
HTTPBIN = 'httpbin.org'
BUFF_SIZE = 4096

WIKI_REQUEST = """GET /wiki/Main_Page HTTP/1.1\r\n
Host: en.wikipedia.org\r\n
User-Agent: Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509\r\n
Firefox/3.0b5\r\n
Accept: text/html\r\n
Connection: close\r\n\r\n\r\n"""

HB_REQUESTS = ["""GET /ip HTTP/1.1\r\n
Host: httpbin.org\r\n
Accept: */*\r\n""",

"""GET /get?foo=bar&1=2&2/0&error=True HTTP/1.1\r\n
Host: httpbin.org\r\n
Accept: */*\r\n""",

"""POST /post HTTP/1.1\r\n
Host: httpbin.org\r\n
Accept: */*\r\n
Content-Length: 35\r\n
Content-Type: application/x-www-form-urlencoded\r\n
\r\n
\r\n
\r\n
foo=bar&1=2&2%2F0=&error=True\r\n
"""
,
"""GET /cookies/set?country=Ru HTTP/1.1\r\n
Host: httpbin.org\r\n
Accept: */*\r\n"""
,

"""GET /cookies HTTP/1.1\r\n
Host: httpbin.org\r\n
Accept: */*\r\n"""
,
"""GET /redirect/4 HTTP/1.1\r\n
Host: httpbin.org\r\n
Accept: */*\r\n"""]

def fullRecive(socket):
    res = ""
    buff = ""
    buff=socket.recv(BUFF_SIZE)
    while buff:
        res = res + buff
        buff = socket.recv(BUFF_SIZE)
    return res


if __name__ == "__main__":

    try:
        sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        sock.connect((WIKI,80))
        sock.send(WIKI_REQUEST)
        sock.send('\r\n')
        data = fullRecive(sock)
        sock.close()
        fd = open("wikipedia.html",'w')
        fd.write(data)
        fd.close()
        
        i = 0
        for request in HB_REQUESTS:
            sock = s.socket(s.AF_INET, s.SOCK_STREAM)
            sock.connect((HTTPBIN,80))
            sock.send(request)
            sock.send('\r\n')
            data =fullRecive(sock)
            sock.close()
            fd = open("httpbin"+str(i)+".html",'w')
            fd.write(data)
            fd.close()
            i = i + 1
    except Exception:
        print "some web sites are not awailable, please try to run this script again later"
    
    
    
