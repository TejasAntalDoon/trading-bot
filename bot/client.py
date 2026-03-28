import time, hmac, hashlib, requests
from urllib.parse import urlencode
from .logging_config import log

BASE_URL = "https://testnet.binancefuture.com"

class BinanceClient:
    def __init__(self, api_key: str, secret: str):
        self.secret   = secret
        self.api_key  = api_key
        self.time_offset = self._get_offset()

    def _get_offset(self) -> int:
        try:
            r  = requests.get(BASE_URL + "/fapi/v1/time", timeout=5)
            st = r.json()["serverTime"]
            lt = int(time.time() * 1000)
            offset = st - lt
            log.info(f"Server: {st} | Local: {lt} | Offset: {offset}ms")
            return offset
        except Exception as e:
            log.warning(f"Server time error: {e}")
            return 0

    def post(self, path: str, params: dict) -> dict:
        # Use server time directly — subtract 500ms safety buffer
        params["timestamp"]  = int(time.time() * 1000) + self.time_offset - 500
        params["recvWindow"] = 60000          # max allowed by Binance
        params = {k: str(v) for k, v in params.items()}
        query  = urlencode(params)
        sig    = hmac.new(self.secret.encode(), query.encode(), hashlib.sha256).hexdigest()
        body   = query + "&signature=" + sig
        log.info(f"POST {path} | body={body}")
        try:
            r = requests.post(
                BASE_URL + path,
                data=body,
                headers={
                    "X-MBX-APIKEY": self.api_key,
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                timeout=10
            )
            data = r.json()
            log.info(f"RESPONSE {r.status_code} | {data}")
            if not r.ok:
                raise ValueError(f"API Error {data.get('code')}: {data.get('msg')}")
            return data
        except requests.RequestException as e:
            log.error(f"Network error: {e}")
            raise
