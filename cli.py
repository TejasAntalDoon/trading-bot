"""
Binance Futures Testnet Trading Bot — CLI Entry Point

Usage:
  python cli.py --symbol BTCUSDT --side BUY  --type MARKET --qty 0.001
  python cli.py --symbol BTCUSDT --side SELL --type LIMIT  --qty 0.001 --price 80000

Credentials via env vars (recommended):
  export BINANCE_API_KEY=<your_key>
  export BINANCE_API_SECRET=<your_secret>
Or pass directly:
  python cli.py --api-key KEY --api-secret SECRET ...
"""
import argparse, os
from bot.client     import BinanceClient
from bot.orders     import place_order
from bot.validators import validate
from bot.logging_config import log

def parse():
    p = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    p.add_argument("--api-key",    default=os.getenv("BINANCE_API_KEY"))
    p.add_argument("--api-secret", default=os.getenv("BINANCE_API_SECRET"))
    p.add_argument("--symbol",     required=True)
    p.add_argument("--side",       required=True, type=str.upper)
    p.add_argument("--type",       required=True, type=str.upper, dest="order_type")
    p.add_argument("--qty",        required=True, type=float)
    p.add_argument("--price",      type=float, default=None)
    return p.parse_args()

def display(args, order: dict):
    sep = "=" * 42
    print(f"\n{sep}\n  REQUEST SUMMARY\n{sep}")
    print(f"  Symbol : {args.symbol}  |  Side : {args.side}")
    print(f"  Type   : {args.order_type}  |  Qty  : {args.qty}")
    if args.order_type == "LIMIT": print(f"  Price  : {args.price}")
    print(f"\n{sep}\n  ORDER RESPONSE\n{sep}")
    print(f"  Order ID    : {order.get('orderId')}")
    print(f"  Status      : {order.get('status')}")
    print(f"  Executed Qty: {order.get('executedQty')}")
    print(f"  Avg Price   : {order.get('avgPrice', 'N/A')}")
    print(f"{sep}\n  ✅ Order placed successfully!\n")

def main():
    args = parse()
    if not args.api_key or not args.api_secret:
        print("❌ API credentials missing. Use --api-key/--api-secret or env vars."); return
    try:
        validate(args.symbol, args.side, args.order_type, args.qty, args.price)
        client = BinanceClient(args.api_key, args.api_secret)
        order  = place_order(client, args.symbol, args.side, args.order_type, args.qty, args.price)
        display(args, order)
    except ValueError as e:
        log.error(e); print(f"\n❌ {e}\n")
    except Exception as e:
        log.error(e); print(f"\n❌ Unexpected error: {e}\n")

if __name__ == "__main__":
    main()
