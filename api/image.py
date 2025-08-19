from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime

# URL obrazka do wyświetlenia
IMAGE_URL = "https://strona-blue.vercel.app/api/image"

class ImageServer(BaseHTTPRequestHandler):
    def handleRequest(self):
        try:
            # Pobieramy aktualną godzinę
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            
            # Tworzymy prostą stronę HTML z obrazem
            html = f"""
            <html>
                <head><title>Testowy Serwer</title></head>
                <body>
                    <h1>Testowy komunikat</h1>
                    <p>Aktualna godzina: {current_time}</p>
                    <img src="{IMAGE_URL}" alt="Obraz testowy" style="max-width:100%;height:auto;">
                </body>
            </html>
            """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode())
        
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f"500 - Internal Server Error<br>{str(e)}".encode())

    do_GET = handleRequest
    do_POST = handleRequest

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, ImageServer)
    print("Serwer działa na http://localhost:8000")
    httpd.serve_forever()
