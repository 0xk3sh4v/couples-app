import websocket
from win10toast import ToastNotifier
from plyer import notification
import time

# add to startup folder to run on boot
# pyinstaller --onefile --noconsole --hidden-import=plyer.platforms.win.notification main.py

def on_message(ws, message):
    notification.notify(
        title="New Message",
        message=message,
        timeout=5
    )

def on_open(ws):
    print("[✓] Connected to the WebSocket server")

def on_error(ws, error):
    print(f"[!] Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"[✖] Disconnected. Code: {close_status_code}, Reason: {close_msg}")

ws = websocket.WebSocketApp(
    "ws://ip:port/",
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)

while True:
    ws.run_forever(ping_interval=30, ping_timeout=10)
