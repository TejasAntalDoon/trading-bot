# Binance Futures Testnet Trading Bot

## Setup

```bash
pip install -r requirements.txt
export BINANCE_API_KEY=x1DLQYQllM67DLBePCcWy1TZzvS6HhQhKtat6YJr9tKNqZiYBxxzXlGvcFth86c6
export BINANCE_API_SE CRET=UvKvosmMig70dVvXyq2m6XXZjqBXWeqCff8s3GaexiYGbHfjxlEr1FqF14DNFd7C
```

## Usage

```bash
# Market order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

# Limit order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 80000
```

## Project Structure

```
trading_bot/
  bot/
    __init__.py        # Package marker
    client.py          # HMAC signing + HTTP requests
    orders.py          # Order payload builder
    validators.py      # Input validation
    logging_config.py  # File + console logging
  cli.py               # CLI entry point (argparse)
  requirements.txt
  README.md
```

## Logs

All API requests, responses, and errors are saved to `trading_bot.log`.
