import datetime

from sqlalchemy.dialects.postgresql import JSON
from app import db
from utils import clean_value

class Ticker(db.Model):
    
    __tablename__ = 'tickers'

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String)
    name = db.Column(db.String)
    last_sale = db.Column(db.Float)
    market_cap = db.Column(db.Float)
    tso = db.Column(db.Integer, nullable=True)
    ipo_year = db.Column(db.Integer, nullable=True)
    sector = db.Column(db.String, nullable=True)
    industry = db.Column(db.String, nullable=True)
    exchange = db.Column(db.String)

    status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def parse_data(self, exchange, data):
        if market in ['NASDAQ', 'NYSE', 'AMEX']:
            self.symbol = data[0]
            self.name = data[1]
            self.last_sale = clean_value(float, data[2])
            self.market_cap = clean_value(float, data[3])
            self.tso = clean_value(int, data[4])
            self.ipo_year = clean_value(int, data[5])
            self.sector = data[6]
            self.industry = data[7]
            self.exchange = exchange

    def as_json(self):
        return dict(
            symbol=self.symbol,
            exchange=self.exchange,
            type=self.type,
            is_daily_sync=self.is_daily_sync,
            is_realtime_sync=self.is_realtime_sync
        )


class HistoricalPrice(db.Model):
    
    __tablename__ = 'historical_prices'

    id = db.Column(db.Integer, primary_key=True)
    ticker_id = db.Column(db.Integer, db.ForeignKey('tickers.id'))
    trading_date = db.Column(db.Date)
    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    volume = db.Column(db.Float)
    adj_close = db.Column(db.Float, nullable=True)

    ticker = db.relationship("Ticker")

    status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def parse_data(self, ticker, data):
        import datetime
        self.ticker_id =  ticker.id
        self.trading_date =  datetime.datetime.strptime(data['Date'], '%Y-%m-%d')
        self.open = clean_value(float, data['Open'])
        self.high = clean_value(float, data['High'])
        self.low = clean_value(float, data['Low'])
        self.close = clean_value(float, data['Close'])
        self.volume = clean_value(float, data['Volume'])
        self.adj_close = clean_value(float, data['Adj Close'])

    def as_json(self):
        return dict(
            symbol=self.ticker.symbol,
            exchange=self.ticker.exchange,
            trading_date=self.date.isoformat(' '),
            open=self.open,
            high=self.high,
            low=self.low,
            close=self.close,
            volume=self.volume,
            adj_close=self.adj_close
        )

class TickPrice(db.Model):
    
    __tablename__ = 'tick_prices'

    id = db.Column(db.Integer, primary_key=True)
    ticker_id = db.Column(db.Integer, db.ForeignKey('tickers.id'))
    trading_time = db.Column(db.DateTime)
    avg_daily_volume = db.Column(db.Float)
    book_value = db.Column(db.Float)
    change = db.Column(db.Integer)
    dividend_per_share = db.Column(db.Float)
    dividend_yield = db.Column(db.Float)
    earnings_per_share = db.Column(db.Float)
    ebitda = db.Column(db.Float)
    fifty_day_moving_avg = db.Column(db.Float)
    fifty_two_week_high = db.Column(db.Float)
    fifty_two_week_low = db.Column(db.Float)
    market_cap = db.Column(db.Float)
    price = db.Column(db.Float)
    price_book_ratio = db.Column(db.Float)
    price_earnings_growth_ratio = db.Column(db.Float)
    price_earnings_ratio = db.Column(db.Float)
    price_sales_ratio = db.Column(db.Float)
    short_ratio = db.Column(db.Float)
    two_hundred_day_moving_avg = db.Column(db.Float)
    volume = db.Column(db.Float)
    
    ticker = db.relationship("Ticker")
    
    status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def parse_data(self, ticker, data):
        import datetime
        self.ticker_id =  ticker.id
        self.trading_time = datetime.datetime.now()
        self.avg_daily_volume = clean(float, data['avg_daily_volume'])
        self.book_value = clean(float, data['book_value'])
        self.change = clean(float, data['change'])
        self.dividend_per_share = clean(float, data['dividend_per_share'])
        self.dividend_yield = clean(float, data['dividend_yield'])
        self.earnings_per_share = clean(float, data['earnings_per_share'])
        self.ebitda = clean(float, data['ebitda'])
        self.fifty_day_moving_avg = clean(float, data['fifty_day_moving_avg'])
        self.fifty_two_week_high = clean(float, data['fifty_two_week_high'])
        self.fifty_two_week_low = clean(float, data['fifty_two_week_low'])
        self.market_cap = clean(float, data['market_cap'])
        self.price = clean(float, data['price'])
        self.price_book_ratio = clean(float, data['price_book_ratio'])
        self.price_earnings_growth_ratio = clean(float, data['price_earnings_growth_ratio'])
        self.price_earnings_ratio = clean(float, data['price_earnings_ratio'])
        self.price_sales_ratio = clean(float, data['price_sales_ratio'])
        self.short_ratio = clean(float, data['short_ratio'])
        self.two_hundred_day_moving_avg = clean(float, data['two_hundred_day_moving_avg'])
        self.volume = clean(float, data['volume'])


    def as_json(self):
       return dict(
        trading_time=self.trading_time.isoformat(' '),
        avg_daily_volume=self.avg_daily_volume,
        book_value=self.book_value,
        change=self.change,
        dividend_per_share=self.dividend_per_share,
        dividend_yield=self.dividend_yield,
        earnings_per_share=self.earnings_per_share,
        ebitda=self.ebitda,
        fifty_day_moving_avg=self.fifty_day_moving_avg,
        fifty_two_week_high=self.fifty_two_week_high,
        fifty_two_week_low=self.fifty_two_week_low,
        market_cap=self.market_cap,
        price=self.price,
        price_book_ratio=self.price_book_ratio,
        price_earnings_growth_ratio=self.price_earnings_growth_ratio,
        price_earnings_ratio=self.price_earnings_ratio,
        price_sales_ratio=self.price_sales_ratio,
        short_ratio=self.short_ratio,
        two_hundred_day_moving_avg=self.two_hundred_day_moving_avg,
        volume=self.volume
       )



class TickPriceRaw(db.Model):
    
    __tablename__ = 'tick_price_raw'

    id = db.Column(db.Integer, primary_key=True)
    ticker_id = db.Column(db.Integer, db.ForeignKey('tickers.id'))
    data = db.Column(JSON)

    status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    
    ticker = db.relationship("Ticker")