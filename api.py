import aiohttp


async def get_info(symbol):
    link = f'https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}'

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as response:
                data = await response.json()
                return data
    except Exception as e:
        print(f'Error! {e}' )
        


