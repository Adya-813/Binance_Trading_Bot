# Binance Futures Testnet Trading Bot

Python CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

## Features

- Market Orders
- Limit Orders
- Stop Orders (Bonus)
- CLI Input
- Logging
- Error Handling

## Setup

Install dependencies

pip install -r requirements.txt

## Environment Variables

export BINANCE_API_KEY=your_key
export BINANCE_API_SECRET=your_secret

## Run Examples

Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 50000

Stop Order

python cli.py --symbol BTCUSDT --side BUY --type STOP --quantity 0.01 --price 48000

Logs will be stored in:

logs/trading_bot.log

Assumptions:
->Users have a Binance Futures Testnet account.
->Valid API keys are generated and configured in the client file.
->Testnet wallet has sufficient funds for placing orders.
->The bot interacts only with the Binance Futures Testnet environment