import asyncio
import websockets
import json

async def main():
    uri = "ws://127.0.0.1:8000/ws/1"

    async with websockets.connect(uri) as ws:
        print("Connected to room")

        async for message in ws:
            data = json.loads(message)
            print("SERVER:", data)

            if data["type"] == "waiting":
                # Do nothing, just wait
                continue

            if data["type"] == "start":
                print("Game started!")

            if data["type"] == "state":
                if data.get("finished"):
                    print("Game finished!")
                    break

                # Ask user for move
                col = input("Your move (0-6): ")

                await ws.send(json.dumps({
                    "type": "move",
                    "column": int(col)
                }))

            if data["type"] == "error":
                print("Error:", data["message"])

asyncio.run(main())