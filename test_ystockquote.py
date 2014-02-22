#!/usr/bin/env python
#
#  Copyright (c) 2013, Corey Goldberg (cgoldberg@gmail.com)
#
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#  Requires: Python 2.7/3.3+


import unittest

import pep8
from testscenarios import generate_scenarios, TestWithScenarios

import ystockquote
import quote_properties


class Pep8ConformanceTestCase(unittest.TestCase):
    """Test that all code conforms to PEP8!"""

    def test_pep8_conformance(self):
        self.pep8style = pep8.StyleGuide(show_source=True)
        files = ('ystockquote.py', 'test_ystockquote.py')
        self.pep8style.check_files(files)
        self.assertEqual(self.pep8style.options.report.total_errors, 0)


class YStockQuoteTestCase(TestWithScenarios):

    def test_get_all(self):
        symbol = 'GOOG'
        all_info = ystockquote.get_all(symbol)
        self.assertIsInstance(all_info, dict)
        pc = all_info['previous_close']
        self.assertNotEqual(pc, 'N/A')
        self.assertGreater(float(pc), 0)

    def test_get_historical_prices(self):
        symbol = 'GOOG'
        start_date = '2013-01-02'
        end_date = '2013-01-15'
        prices = ystockquote.get_historical_prices(
            symbol, start_date, end_date)
        self.assertIsInstance(prices, dict)
        self.assertEqual(len(prices), 10)
        self.assertEqual(sorted(prices.keys())[0], '2013-01-02')
        self.assertEqual(sorted(prices.keys())[-1], end_date)
        self.assertGreater(float(prices[start_date]['Open']), 0.0)
        self.assertGreater(float(prices[start_date]['High']), 0.0)
        self.assertGreater(float(prices[start_date]['Low']), 0.0)
        self.assertGreater(float(prices[start_date]['Close']), 0.0)
        self.assertGreater(float(prices[start_date]['Volume']), 0.0)
        self.assertGreater(float(prices[start_date]['Adj Close']), 0.0)
        self.assertGreater(float(prices[end_date]['Open']), 0.0)
        self.assertGreater(float(prices[end_date]['High']), 0.0)
        self.assertGreater(float(prices[end_date]['Low']), 0.0)
        self.assertGreater(float(prices[end_date]['Close']), 0.0)
        self.assertGreater(float(prices[end_date]['Volume']), 0.0)
        self.assertGreater(float(prices[end_date]['Adj Close']), 0.0)

    def test_get_all_alignment(self):
        """ Compare bulk 'all_info' values to individual values.
        Currently broken due to misalignment from invalid CSV in
        fields: f6, k3, and maybe j2, a5, b6.
        """
        symbol = 'GOOG'
        all_info = ystockquote.get_all(symbol)
        self.assertIsInstance(all_info, dict)
        self.assertEquals(
            all_info['previous_close'],
            ystockquote.get_previous_close(symbol))
        self.assertEquals(
            all_info['volume'],
            ystockquote.get_volume(symbol))
        self.assertEquals(
            all_info['bid_realtime'],
            ystockquote.get_bid_realtime(symbol))
        self.assertEquals(
            all_info['ask_realtime'],
            ystockquote.get_ask_realtime(symbol))
        self.assertEquals(
            all_info['last_trade_price'],
            ystockquote.get_last_trade_price(symbol))
        self.assertEquals(
            all_info['today_open'],
            ystockquote.get_today_open(symbol))
        self.assertEquals(
            all_info['todays_high'],
            ystockquote.get_todays_high(symbol))
        self.assertEquals(
            all_info['last_trade_date'],
            ystockquote.get_last_trade_date(symbol))

    def test_get_all_alignment_new(self):
        """ Compare bulk 'all_info' values to individual values.
        Currently broken due to misalignment from invalid CSV in
        fields: f6, k3, and maybe j2, a5, b6.
        """
        symbol = 'GOOG'
        all_info = quote_properties.get_all(symbol)
        self.assertIsInstance(all_info, dict)
        self.assertEquals(
            all_info['PreviousClose'],
            ystockquote.get_previous_close(symbol))
        self.assertEquals(
            all_info['Volume'],
            ystockquote.get_volume(symbol))
        self.assertEquals(
            all_info['BidRealtime'],
            ystockquote.get_bid_realtime(symbol))
        self.assertEquals(
            all_info['AskRealtime'],
            ystockquote.get_ask_realtime(symbol))
        self.assertEquals(
            all_info['LastTradePriceOnly'],
            ystockquote.get_last_trade_price(symbol))
        self.assertEquals(
            all_info['Open'],
            ystockquote.get_today_open(symbol))
        self.assertEquals(
            all_info['DaysHigh'],
            ystockquote.get_todays_high(symbol))
        self.assertEquals(
            all_info['LastTradeDate'],
            ystockquote.get_last_trade_date(symbol))


if __name__ == '__main__':
    unittest.main()
