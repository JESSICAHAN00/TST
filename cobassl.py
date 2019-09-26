from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

httpd = HTTPServer(('localhost', 7373), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='C:/Users/Luke/Desktop/TST/ca.crt',keyfile='C:/Users/Luke/Desktop/TST/ca.key', server_side=True)
httpd.serve_forever()