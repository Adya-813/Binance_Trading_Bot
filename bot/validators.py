def validate_order(symbol, side, order_type, quantity, price):

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT", "STOP"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    # LIMIT price optional (auto-fetch)
    if order_type == "STOP" and price is None:
        raise ValueError("STOP orders require trigger price")