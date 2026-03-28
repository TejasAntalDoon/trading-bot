def validate(symbol, side, order_type, qty, price):
    errors = []
    if not symbol:                              errors.append("Symbol is required.")
    if side not in ("BUY", "SELL"):             errors.append("Side must be BUY or SELL.")
    if order_type not in ("MARKET", "LIMIT"):   errors.append("Type must be MARKET or LIMIT.")
    if qty <= 0:                                errors.append("Quantity must be > 0.")
    if order_type == "LIMIT" and not price:     errors.append("Price required for LIMIT orders.")
    if errors:
        raise ValueError("\n".join(errors))
