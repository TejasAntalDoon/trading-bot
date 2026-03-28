from .client import BinanceClient

def place_order(client: BinanceClient, symbol: str, side: str,
                order_type: str, qty: float, price: float = None) -> dict:
    params = {"symbol": symbol, "side": side, "type": order_type, "quantity": qty}
    if order_type == "LIMIT":
        params.update({"price": price, "timeInForce": "GTC"})
    return client.post("/fapi/v1/order", params)
