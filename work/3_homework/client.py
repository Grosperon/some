import pickle
import asyncio

from common import ADDR

async def main():
    reader, writer = await asyncio.open_connection(*ADDR)
    data = await reader.read(4096)
    Tee = pickle.loads(data)

    Tee.tea_party()

    writer.close()
    await writer.wait_closed()

asyncio.run(main())