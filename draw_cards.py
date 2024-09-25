import aiohttp
import asyncio
import time
start_time=time.time()
 
async def draw(value):
    async with aiohttp.ClientSession() as session:
        url=f'https://deckofcardsapi.com/api/deck/new/draw/'
        async with session.get(url) as resp:
            card=await resp.json()
            print(f'{card["cards"][0]["value"]} of {card["cards"][0]["suit"]}')
 
async def main():
    cards = [draw(i) for i in range(105)]
    await asyncio.gather(*cards)
 
asyncio.run(main())
print("time it took {}".format(time.time()-start_time))
