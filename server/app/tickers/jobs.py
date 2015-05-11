import datetime
import ytickerquote
import time
import sys

from app import db
from app.tickers.models import Ticker, HistoricalPrice, TickPrice, TickPriceRaw


TRADE_TIMES = dict(
    NASDAQ = [930,1600, 12]
    )

def sync_daily_price():
    
    tickers = Ticker.query.all()
    for ticker in tickers:
        now = datetime.datetime.now()- datetime.timedelta(days=1)
        start = now.strftime('%Y-%m-%d')
        end = start
        dates = []
        records = ytickerquote.get_historical_prices(ticker.symbol, start, end)
        dates = session.query(HistoricalPrice.trading_date).filter(HistoricalPrice.ticker_id==ticker.id)

        for k, record in records.items():
            record ['Date'] = k
            price = HistoricalPrice()
            price.parse_data(ticker, record)
            db.session.add(price)
            db.session.flush()
            db.session.commit()


def sync_tick_price():
    now = datetime.datetime.now()
    current = int(now.strftime('%H%M'))
    tickers = Ticker.query.all()
    for ticker in tickers:
        s,e,d = TRADE_TIMES[ticker.exchange.upper()]
        # check stock martket time
        if (s+d)<= current and current <=(e+d):
            record = ytickerquote.get_all(ticker.symbol)
            price = TickPriceRaw()
            price.data = record
            db.session.add(price)
            db.session.flush()
            db.session.commit()
