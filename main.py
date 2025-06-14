import websocket
from win10toast import ToastNotifier

toaster = ToastNotifier()

def on_message(ws, message):
    print("[📥] New message received!")
    toaster.show_toast("New Message", message, duration=3, threaded=True)

def on_open(ws):
    print("[✓] Connected to the WebSocket server")

def on_error(ws, error):
    print(f"[!] Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"[✖] Disconnected. Code: {close_status_code}, Reason: {close_msg}")

if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        "ws://melo.wisp.uno:12227/",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )

    ws.run_forever()
