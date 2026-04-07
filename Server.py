from fastapi import FastAPI, WebSocket
from Connect4 import Connect4, Status

app = FastAPI()

connections = []
players = {}
game = Connect4()


async def broadcast(message):
    for conn in connections:
        await conn.send_json(message)

async def sendToPlayerTurn(message):
    for conn in connections:
        if players[conn] == game.current_player:
            await conn.send_json(message)

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()

    # Assign player
    if len(connections) >= 2:
        await websocket.send_json({
            "type": "error",
            "message": "Game is full"
        })
        await websocket.close()
        return

    connections.append(websocket)

    if len(connections) == 1:
        players[websocket] = Status.YELLOW
        await websocket.send_json({
            "type": "waiting",
            "message": "Waiting for another player..."
        })

    elif len(connections) == 2:
        players[websocket] = Status.RED

        # Start match
        await broadcast({
            "type": "start",
            "message": "Match starting",
            "current_player": game.current_player.value,
            "board": game.serialize()["board"]
        })
        await sendToPlayerTurn({"type": "state"})
    try:
        while True:
            data = await websocket.receive_json()

            if data["type"] == "move":
                player = players[websocket]

                # Enforce turn
                if player != game.current_player:
                    await websocket.send_json({
                        "type": "error",
                        "message": "Not your turn"
                    })
                    continue

                column = data["column"]
                valid = game.drop(column)

                if not valid:
                    await websocket.send_json({
                        "type": "error",
                        "message": "Invalid move"
                    })
                    continue

                finished = game.isFinisehd()

                await broadcast({
                    "type": "state",
                    **game.serialize(),
                    "finished": finished
                })

                if finished:
                    await broadcast({
                        "type": "game_over",
                        "winner": player.value
                    })

    except Exception as e:
        print("Disconnected:", e)

        connections.remove(websocket)
        players.pop(websocket, None)