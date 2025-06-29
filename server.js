const ws = require('ws');
const express = require('express');
const http = require('http');

const port = 0000;
const app = express();
const server = http.createServer(app);
const websocketServer = new ws.Server({ server: server });

let laptopconnected = null;

app.use(express.json());

websocketServer.on('error', function  handleerrors(error) {
    console.error("WebSocket error:", error);
})

websocketServer.on('connection', function connectionHandler(socket) {
    if (laptopconnected != null) {
        socket.close(1008, "Intrusion detected");
    }

    laptopconnected = socket;
    
    socket.send("Might want to mute your notifications.");

    socket.on('close', function () {
        console.log("Laptop disconnected");
        laptopconnected = null;
    });

    socket.on('error', function (err) {
        console.log("Socket error:", err);
        laptopconnected = null;
    });
});

websocketServer.on('listening', function serverListening() {
    console.log(`WebSocket server is listening on ws://localhost:${port}`);

});

app.get("/", function home(req, res) {
    res.sendFile(__dirname + '/index.html');
})

app.get('/status', function laptopConnectedorNot(req, res) {
    if (laptopconnected) {
        res.status(200).send("Laptop is connected");
    }
    else {
        res.status(404).send("Laptop is not connected");
    }
});

app.post('/sendMessage', function sendMessage(req, res){
    if(laptopconnected) {
        const message = req.body.message;
        laptopconnected.send(message);
        res.status(200).send("Message sent");
    }
});

server.listen(port, '0.0.0.0', () => {
    console.log(`Server is running on http://0.0.0.0:${port}`);
});
