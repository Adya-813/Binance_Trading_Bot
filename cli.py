import argparse
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

parser.add_argument("--symbol", required=True, help="Trading pair e.g BTCUSDT")
parser.add_argument("--side", required=True, help="BUY or SELL")
parser.add_argument("--type", required=True, help="MARKET / LIMIT / STOP")
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float,help="Price for LIMIT or STOP orders")


args = parser.parse_args()

try:

    validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

    print("\nOrder Request Summary")
    print("---------------------")
    print("Symbol:", args.symbol)
    print("Side:", args.side)
    print("Type:", args.type)
    print("Quantity:", args.quantity)
    print("Price:", args.price)

    order = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\nOrder Response")
    print("---------------------")

     # Different order types return different IDs
    order_id = order.get("orderId") or order.get("algoId")

    # Different statuses depending on order type
    status = order.get("status") or order.get("algoStatus")

    print("Order ID:", order_id)
    print("Status:", status)
    print("Executed Qty:", order.get("executedQty", "0"))
    print("Avg Price:", order.get("avgPrice", "N/A"))

    print("\nOrder placed successfully")
   

except Exception as e:

    print("\nOrder Failed")
    print("Error:", e)