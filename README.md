# Couples App 💞

A minimalist real-time messaging app for couples.

---

## Quick Start

```bash
git clone https://github.com/0xk3sh4v/couples-app.git
cd couples-app
npm install
node server.js
```

Open your browser at `http://localhost:3000` and start chatting.

---

## Project Structure

```
.
├── server.js        # Node.js WebSocket server
├── index.html       # Frontend UI
├── winClient.py     # The app that should be deployed on Windows
└── README.md        # This file
```

---

## Features

- Real-time messaging via WebSockets
- Simple front-end with no build tools
- No dependencies except `ws` (lightweight)
- Works in browser and any WebSocket client

---

## How It Works

1. `server.js` starts a WebSocket server on the setup port using `ws`.
2. Frontend (website) connects to the server and sends messages.
3. Server broadcasts messages to all allowed clients (limit is set to 1) 
4. The windows client (written in Python) connects to the server and throws a Windows Toast Notification with the contents of the message
5. No database or user accounts, just instant one way messages between 2 people

---

## Use Cases

- Private one way message
- Running locally or on LAN using configured ports
- Great for quick heads up notifications in an office where you need to announce something to a large group of people connected on a local network. This can be achieved by changing the connection limit in the server code
- General use case is for a couple where one wants to remind the other about something while they are busy working.

---

## Tech Stack

![Node.js](https://img.shields.io/badge/Made%20with-Node.js-339933?style=flat&logo=node.js) ![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat&logo=python)

- Node.js
- ws (WebSocket lib)
- Vanilla HTML/JS frontend
- Python (Windows API)

---

## Future Plans

- [ ] Support for rooms or multiple pairs
- [ ] Make this into a 2 way chatapp
