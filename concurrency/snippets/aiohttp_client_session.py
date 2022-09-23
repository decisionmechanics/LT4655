import aiohttp
import asyncio

INSPIRATIONAL_QUOTES_URL = (
    "https://inspirational-quotes.azurewebsites.net/api/InspirationalQuotes"
)


async def fetch_quote():
    async with aiohttp.ClientSession() as session:
        async with session.get(INSPIRATIONAL_QUOTES_URL) as response:
            return await response.text()


async def main():
    quote = await fetch_quote()
    print(quote)


if __name__ == "__main__":
    asyncio.run(main())
