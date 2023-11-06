import aiohttp
from .flags import Flags
from .exceptions import ProxyCheckDenied, ProxyCheckError
from .ip import IP
import logging

class Client:
    def __init__(self, api_key: str = None):
        self.api_key: str = api_key
        self.base_url: str = "https://proxycheck.io/v2/"
        self.session = aiohttp.ClientSession()

    async def __aenter__(self):
        if not self.session:
            self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if not self.session.closed:
            await self.session.close()
        self.session = None

    async def ip(self, ip: str, flags: Flags = None):
        if not flags:
            flags = Flags.default()
        params = flags.to_dict()
        response = await self._get(f"{self.base_url}{ip}", params=params)
        ip_info = response.get(ip)
        return IP(ip, **ip_info)

    async def _request(self, url: str, params: dict = None, headers: dict = None, method: str = "GET"):
        if not params:
            params = {}
        if not headers:
            headers = {}
        if self.api_key:
            params.update({"key": self.api_key})
        try:
            async with self.session.request(method, url, params=params, headers=headers) as resp:
                if 300 > resp.status >= 200:
                    if not resp.status == 200:
                        logging.warning(f"{resp.status} {resp.reason}")
                    return await resp.json()

                if resp.status == 403:
                    raise ProxyCheckDenied(await resp.text())
                elif resp.status == 400:
                    raise ProxyCheckError(await resp.text())

        except aiohttp.ClientError as e:
            raise ProxyCheckError(str(e))

    async def _get(self, url: str, params: dict = None, headers: dict = None):
        return await self._request(url, params, headers, "GET")

