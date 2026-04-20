# Wemos D1 Mini LED Control Web Server

A simple MicroPython project for the Wemos D1 Mini (ESP8266) board that creates a Wi-Fi access point and serves a web page to control the built-in LED.

## Features

- Creates a Wi-Fi access point (AP mode)
- Runs a basic HTTP web server on port 80
- Provides a web interface to toggle the built-in LED
- Displays current LED status (ON/OFF) with color-coded button

## Hardware Requirements

- Wemos D1 Mini (ESP8266-based board)
- USB cable for programming and power

## Software Requirements

- MicroPython firmware installed on the Wemos D1 Mini
- `mpremote` tool for uploading files to the device
- Python 3.x on your development machine

## Installation

1. **Install MicroPython on your Wemos D1 Mini:**
   - Download the latest MicroPython firmware for ESP8266 from [micropython.org](https://micropython.org/download/esp8266/)
   - Flash the firmware using esptool or your preferred flashing tool

2. **Clone or download this repository:**
   ```bash
   git clone https://github.com/FehTeh/led-toggle-wemos-d1-mini.git
   cd led-toggle-wemos-d1-mini
   ```

3. **Configure Wi-Fi settings:**
   - Edit `config.py` to set your desired SSID and password:
     ```python
     WIFI_SSID = "YourAPName"
     WIFI_PASSWORD = "YourPassword"
     ```

4. **Upload files to the device:**
   ```bash
   mpremote cp config.py :config.py
   mpremote cp main.py :main.py
   mpremote cp boot.py :boot.py
   ```

## Usage

1. Power on the Wemos D1 Mini
2. The device will create a Wi-Fi access point with the configured SSID
3. Connect to the access point using the configured password
4. Open a web browser and navigate to `http://192.168.4.1` (default AP IP)
5. Use the "TOGGLE LED" button to turn the built-in LED on/off
6. The page will refresh to show the current status

## File Structure

- `main.py`: Main application code - sets up Wi-Fi AP and web server
- `config.py`: Configuration file for Wi-Fi SSID and password
- `boot.py`: Boot script (runs on device startup)

## Troubleshooting

- **Can't connect to the access point:** Ensure the correct password is set in `config.py`
- **Web page not loading:** Check that the device is powered on and the server is running (check serial output)
- **LED not responding:** Verify the LED pin (GPIO 2) is correctly configured
- **Upload issues:** Make sure `mpremote` is installed and the device is connected via USB

## Development

To modify the code:
1. Edit the Python files locally
2. Upload changes using `mpremote cp <file> :<file>`
3. Reset the device to apply changes

## License

This project is open source. Feel free to modify and distribute.