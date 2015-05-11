import sys
from app.tickers.jobs import sync_daily_price, sync_tick_price


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'update_daily_prices':
        sync_daily_price()
    elif cmd == 'update_realtime_prices':
        sync_tick_price()

