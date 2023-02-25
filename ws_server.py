import asyncio
import logging
import websockets
import names
from websockets import WebSocketServerProtocol
from websockets.exceptions import ConnectionClosedOK

from main import exchange_chat

logging.basicConfig(level=logging.INFO)


class Server:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol):
        ws.name = names.get_full_name()
        self.clients.add(ws)
        logging.info(f'{ws.remote_address} connects')

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.remove(ws)
        logging.info(f'{ws.remote_address} disconnects')

    async def send_to_clients(self, message: str):
        if self.clients:
            [await client.send(message) for client in self.clients]

    async def ws_handler(self, ws: WebSocketServerProtocol):
        await self.register(ws)
        try:
            await self.distrubute(ws)
        except ConnectionClosedOK:
            pass
        finally:
            await self.unregister(ws)

    async def distrubute(self, ws: WebSocketServerProtocol):
        async for message in ws:
            days_exchange = valid_exchange(message)
            if days_exchange:
                await self.send_to_clients(f"{ws.name}: {await exchange_chat(days_exchange)}")
            else:
                await self.send_to_clients(f"{ws.name}: {message}")


def valid_exchange(message):
    arg = message.split(" ")
    print(arg)
    if len(arg) == 2 and arg[0].lower() in "exchange" and (0 < int(arg[1]) < 11):
        return int(arg[1])
    elif len(arg) == 1 and arg[0].lower() in "exchange":
        return 1
    else:
        return False


async def main():
    server = Server()
    async with websockets.serve(server.ws_handler, 'localhost', 8080):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())
