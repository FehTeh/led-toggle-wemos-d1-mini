import network
import socket
from machine import Pin
import config

# 1. Hardware Setup (Built-in LED on Wemos D1 Mini is GPIO 2)
# Note: On ESP8266, the internal LED uses inverted logic (0=ON, 1=OFF)
led = Pin(2, Pin.OUT)
led.value(1) # Start with LED turned OFF

# 2. Wi-Fi Configuration (Access Point Mode)
ap = network.WLAN(network.AP_IF)
ap.config(essid=config.WIFI_SSID, password=config.WIFI_PASSWORD)
ap.active(True)

print('Access Point Active. IP Address:', ap.ifconfig()[0])

def get_html(status):
    color = "red" if status == "ON" else "green"
    return """<!DOCTYPE html>
    <html>
        <body>
            <h1>Wemos Control</h1>
            <p>Status: <b>""" + status + """</b></p>
            <form method="POST">
                <input type="submit" value="TOGGLE LED" style="height:100px; width:200px; background:""" + color + """; color:white;">
            </form>
        </body>
    </html>"""

# 3. Web Server Setup
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

print('Server running on port 80...')

while True:
    try:
        conn, addr = s.accept()
        request = conn.recv(1024).decode('utf-8')
        
        if "POST /" in request:
            led.value(not led.value())
        
        # Force a small delay to ensure buffer is ready
        status_text = "ON" if led.value() == 0 else "OFF"
        response = get_html(status_text)
        
        # Send in one go
        conn.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
        conn.sendall(response) # sendall ensures the whole string goes out
        conn.close()
    except Exception as e:
        print("Error:", e)
        if 'conn' in locals(): conn.close()