import time, hmac, hashlib, requests
from urllib.parse import urlencode

BASE_URL   = "https://testnet.binancefuture.com"
API_KEY    = "x1DLQYQllM67DLBePCcWy1TZzvS6HhQhKtat6YJr9tKNqZiYBxxzXlGvcFth86c6"       # paste your actual key
API_SECRET = "UvKvosmMig70dVvXyq2m6XXZjqBXWeqCff8s3GaexiYGbHfjxlEr1FqF14DNFd7C"    # paste your actual secret

# Get server time offset
send_time   = int(time.time() * 1000)
r           = requests.get(BASE_URL + "/fapi/v1/time")
recv_time   = int(time.time() * 1000)
server_time = r.json()["serverTime"]
offset      = server_time - recv_time + (recv_time - send_time) // 2
print(f"Offset: {offset}ms")

# Build params
params = {
    "symbol"     : "BTCUSDT",
    "side"       : "BUY",
    "type"       : "MARKET",
    "quantity"   : "0.001",            # string, not float
    "timestamp"  : int(time.time() * 1000) + offset,
    "recvWindow" : 10000,
}

# Sign
query     = urlencode(params)
signature = hmac.new(API_SECRET.encode("utf-8"), query.encode("utf-8"), hashlib.sha256).hexdigest()
query    += "&signature=" + signature

print(f"Query string: {query}")
print(f"Signature: {signature}")

# Send
r = requests.post(
    BASE_URL + "/fapi/v1/order",
    data=query,
    headers={
        "X-MBX-APIKEY": API_KEY,
        "Content-Type": "application/x-www-form-urlencoded"
    }
)
print(f"Status : {r.status_code}")
print(f"Response: {r.json()}")