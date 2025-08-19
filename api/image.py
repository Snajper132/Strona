# Plik: api/image.py

import datetime

IMAGE_URL = "https://cdn.discordapp.com/attachments/1383724793731350578/1407330268355760208/Screenshot_2025-08-19-13-47-46-56_a23b203fd3aafc6dcb84e438dda678b6.jpg?ex=68a5b5f2&is=68a46472&hm=235653aa2238a45a91a06154c8541cdcee57846fea2e37cccbaef627414779ea&"

def handler(request, response):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    
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
    
    response.headers["Content-Type"] = "text/html"
    response.send(html)

