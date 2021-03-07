import asyncio
from collections import namedtuple

import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

services = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    # Service('ip-api', 'https://ip-api.com/json', 'query')
)


async def get_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_ip(service):
    print(f'Fetching IP from {service.name}')

    json_response = await get_json(service.url)
    ip = json_response[service.ip_attr]
    return f'{service.name} finished with result: {ip}'


