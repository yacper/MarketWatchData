#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Date: 2023/7/21 18:16
Desc: To test intention, just write test code here!
"""
# from marketwatchdata.MarketWatch import ohlc
from marketwatchdata.MarketWatch import ohlc


def test_ohlc():
    """
    just for test aim
    :return: assert result
    :rtype: assert
    """
    df = ohlc('TMUBMUSD03M', 'P1D', 'P1Y')
    assert df.shape[0] > 0


if __name__ == "__main__":
    test_ohlc()
