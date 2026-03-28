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

<img width="987" height="261" alt="Screenshot 1" src="https://github.com/user-attachments/assets/34cae639-bada-4e20-8af3-cce9d2d25143" />
<img width="987" height="267" alt="Screenshot 2" src="https://github.com/user-attachments/assets/ce138cc2-b9f7-409b-aa58-1f74d559fae6" />
<img width="990" height="269" alt="Screenshot 3" src="https://github.com/user-attachments/assets/ab6e030d-4807-444d-9b0d-dcfeea721470" />
<img width="985" height="283" alt="Screenshot 4" src="https://github.com/user-attachments/assets/1cebd997-eeb5-410b-8d85-79d355a0438b" />

