import csv
from app.tickers.models import Ticker
from app import db
reader = csv.reader(open('data/NASDAQ.csv'))
next(reader)
for row in reader:
    ticker = Ticker()
    ticker.symbol = row[0]
    ticker.name = row[1]
    if row[2] != 'n/a':
        ticker.last_sale = float(row[2])
    if row[3] != 'n/a':
        ticker.market_cap = float(row[3])
    if row[4] != 'n/a':
        ticker.tso = int(row[4])
    if row[5] != 'n/a':
        ticker.ipo_year = int(row[5])
    ticker.sector = row[6]
    ticker.industry = row[7]
    ticker.exchange = row[8]
    db.session.add(ticker)
    db.session.commit()