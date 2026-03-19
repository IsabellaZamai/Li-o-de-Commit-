from http.server import HTTPServer, BaseHTTPRequestHandler

 class Servidor(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Servidor funcionando")
 HTTPServer(("0.0.0.0", 8000), Servidor).serve_forever()