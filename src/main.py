#main.py
"""
Main module to control ESP8266 via Web.
This script sets up the ESP8266 as a Wi-Fi access point and runs a simple web server.
The web server serves an HTML page that allows the user to toggle the built-in LED on and off.
"""

import gc
import socket
import network # pylint: disable=import-error
from machine import Pin # pylint: disable=import-error
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

def get_html_from_file(status):
    """Reads index.html and replaces status placeholder."""
    try:
        with open('www/index.html', 'r', encoding='utf-8') as f:
            html = f.read()
        return html.replace('{{status}}', status)
    except OSError as e:
        print('Get HTML Error:', e)
        return "<h1>Error: www/index.html not found</h1>"

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

        status_text = "ON" if led.value() == 0 else "OFF"

        # Get the template and process it
        response = get_html_from_file(status_text)

        conn.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
        conn.sendall(response)
        conn.close()
        gc.collect()
    except OSError as e:
        print("Error:", e)
        if 'conn' in locals():
            conn.close()
