import ystockquote as ysq

"""
An alternative method for get_all such using a dynamic 
mapping that doesn't hardcode indexes. The format string
is generated dynamically, thus we can get back to the values
without such cruft.

This currently suffers from Yahoo's CSV format errors.

Not a clean drop-in because currently value names are not
backwardly compatible.
"""

def get_all(symbol):
    ids = ''.join([x[1] for x in CODES])
    raw = ysq._request(symbol, ids)
    values = raw.split(',')
    #assert len(ids) == len(values), "Diff # fields came back than queried."
    labels = [x[0] for x in CODES]
    #print ("\n".join([str(v) for v in zip(labels, values)]))
    return dict(zip(labels, values))


CODES = [
    ('AfterHoursChangeRealtime', 'c8'),
    ('AnnualizedGain', 'g3'),
    ('Ask', 'a0'),
    ('AskRealtime', 'b2'),
    ('AverageDailyVolume', 'a2'),
    ('Bid', 'b0'),
    ('BidRealtime', 'b3'),
    ('BookValuePerShare', 'b4'),
    ('Change', 'c1'),
    ('Change_ChangeInPercent', 'c0'),
    ('ChangeFromFiftydayMovingAverage', 'm7'),
    ('ChangeFromTwoHundreddayMovingAverage', 'm5'),
    ('ChangeFromYearHigh', 'k4'),
    ('ChangeFromYearLow', 'j5'),
    ('ChangeInPercent', 'p2'),
    ('ChangeInPercentRealtime', 'k2'),
    ('ChangeRealtime', 'c6'),
    ('Commission', 'c3'),
    ('Currency', 'c4'),
    ('DaysHigh', 'h0'),
    ('DaysLow', 'g0'),
    ('DaysRange', 'm0'),
    ('DaysRangeRealtime', 'm2'),
    ('DaysValueChange', 'w1'),
    ('DaysValueChangeRealtime', 'w4'),
    ('DividendPayDate', 'r1'),
    ('TrailingAnnualDividendYield', 'd0'),
    ('TrailingAnnualDividendYieldInPercent', 'y0'),
    ('DilutedEPS', 'e0'),
    ('EBITDA', 'j4'),
    ('EPSEstimateCurrentYear', 'e7'),
    ('EPSEstimateNextQuarter', 'e9'),
    ('EPSEstimateNextYear', 'e8'),
    ('ExDividendDate', 'q0'),
    ('FiftydayMovingAverage', 'm3'),
    ('HighLimit', 'l2'),
    ('HoldingsGain', 'g4'),
    ('HoldingsGainPercent', 'g1'),
    ('HoldingsGainPercentRealtime', 'g5'),
    ('HoldingsGainRealtime', 'g6'),
    ('HoldingsValue', 'v1'),
    ('HoldingsValueRealtime', 'v7'),
    ('LastTradeDate', 'd1'),
    ('LastTradePriceOnly', 'l1'),
    ('LastTradeRealtimeWithTime', 'k1'),
    ('LastTradeTime', 't1'),
    ('LastTradeWithTime', 'l0'),
    ('LowLimit', 'l3'),
    ('MarketCapitalization', 'j1'),
    ('MarketCapRealtime', 'j3'),
    ('MoreInfo', 'i0'),
    ('Name', 'n0'),
    ('Notes', 'n4'),
    ('OneyrTargetPrice', 't8'),
    ('Open', 'o0'),
    ('OrderBookRealtime', 'i5'),
    ('PEGRatio', 'r5'),
    ('PERatio', 'r0'),
    ('PERatioRealtime', 'r2'),
    ('PercentChangeFromFiftydayMovingAverage', 'm8'),
    ('PercentChangeFromTwoHundreddayMovingAverage', 'm6'),
    ('ChangeInPercentFromYearHigh', 'k5'),
    ('PercentChangeFromYearLow', 'j6'),
    ('PreviousClose', 'p0'),
    ('PriceBook', 'p6'),
    ('PriceEPSEstimateCurrentYear', 'r6'),
    ('PriceEPSEstimateNextYear', 'r7'),
    ('PricePaid', 'p1'),
    ('PriceSales', 'p5'),
    ('Revenue', 's6'),
    ('SharesOwned', 's1'),
    ('ShortRatio', 's7'),
    ('StockExchange', 'x0'),
    ('Symbol', 's0'),
    ('TickerTrend', 't7'),
    ('TradeDate', 'd2'),
    ('TradeLinks', 't6'),
    ('TradeLinksAdditional', 'f0'),
    ('TwoHundreddayMovingAverage', 'm4'),
    ('Volume', 'v0'),
    ('YearHigh', 'k0'),
    ('YearLow', 'j0'),
    ('YearRange', 'w0'),
    # Suspect fields moved to end to not screw up the rest.
    ('AskSize', 'a5'),
    ('BidSize', 'b6'),
    ('LastTradeSize', 'k3'),
    ('SharesFloat', 'f6'),
    ('SharesOutstanding', 'j2'),
    ]

CODE_MAP = dict(CODES)

REV_CODE_MAP = dict([(x[1].replace('0', ''), x[0]) for x in CODES])
