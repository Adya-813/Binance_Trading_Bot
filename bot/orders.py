import logging
from bot.client import get_client


def get_market_price(symbol):
    client = get_client()

    ticker = client.futures_symbol_ticker(symbol=symbol)

    price = float(ticker["price"])

    return price


def place_order(symbol, side, order_type, quantity, price=None):

    client = get_client()

    try:
        logging.info(f"Order request: {symbol} {side} {order_type}")
        # AUTO FETCH MARKET PRICE
        if order_type == "LIMIT" and price is None:

            market_price = get_market_price(symbol)

            print(f"Auto fetched market price: {market_price}")

            price = market_price

        if order_type == "MARKET":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            print("Full API Response:", order)  

        elif order_type == "LIMIT":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        elif order_type == "STOP":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP_MARKET",
                stopPrice=price,
                quantity=quantity
            )

        order_id = order.get("orderId") or order.get("algoId")
        status = order.get("status") or order.get("algoStatus")

        logging.info(f"Order Response: {{orderId: {order_id}, status: {status}}}")

        return order

    except Exception as e:

        logging.error(f"API Error: {e}")
        print("API ERROR:", e)

        raise