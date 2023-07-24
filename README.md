# marketwatchdata


[![pypi](https://img.shields.io/pypi/v/marketwatchdata.svg)](https://pypi.org/project/marketwatchdata/)
[![downloads](https://pepy.tech/badge/marketwatchdata)](https://pepy.tech/project/marketwatchdata)
[![documentation status](https://readthedocs.org/projects/marketwatchdata/badge/?version=latest)](https://marketwatchdata.readthedocs.io/en/latest/?badge=latest)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![actions status](https://github.com/yacper/marketwatchdata/actions/workflows/check.yml/badge.svg)](https://github.com/yacper/marketwatchdata/actions)
[![mit licence](https://camo.githubusercontent.com/14a9abb7e83098f2949f26d2190e04fb1bd52c06/68747470733a2f2f626c61636b2e72656164746865646f63732e696f2f656e2f737461626c652f5f7374617469632f6c6963656e73652e737667)](https://github.com/yacper/marketwatchdata/blob/main/license)

## overview

[marketwathdata](https://github.com/yacper/marketwatchdata) retrieve datas from marketwatch.com.

- documentation: [文档](https://marketwatchdata.readthedocs.io/)


## installation

### general

```shell
pip install marketwatchdata --upgrade
```

### china

```shell
pip install marketwatchdata -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com  --upgrade
```
#### test

```python
import marketwatchdata as mw

print(mw.__version__)
```

## usage

### data

code

```python
import marketwatchdata as mw

df = mw.ohlc('stock/us/xnas/aapl', 'p1d', 'p1y')
print(df)
```

output

```
                open     high      low   close       volume
date
2022-07-25  154.010  155.040  152.280  152.95   53623953.0
2022-07-26  152.265  153.085  150.800  151.60   55138688.0
2022-07-27  152.580  157.330  152.160  156.79   78620688.0
2022-07-28  156.980  157.640  154.410  157.35   81378727.0
2022-07-29  161.240  163.630  159.500  162.51  101786898.0
...             ...      ...      ...     ...          ...
2023-07-17  191.900  194.320  191.810  193.99   50520160.0
2023-07-18  193.350  194.330  192.415  193.73   48353770.0
2023-07-19  193.100  198.230  192.650  195.10   80507320.0
2023-07-20  195.090  196.470  192.495  193.13   59581199.0
2023-07-21  194.100  194.970  191.230  191.94   71951683.0

[250 rows x 5 columns]
```

### plot

code

```python
import marketwatchdata as mw
import mplfinance as mpf  # please install mplfinance as follows: pip install mplfinance

df = mw.ohlc('stock/us/xnas/aapl', 'p1d', 'p1y')
mpf.plot(df, type='candle', mav=(3, 6, 9), volume=true, show_nontrading=false)
```

output

![](https://user-images.githubusercontent.com/668255/255549764-1665d2e5-f50d-462d-a4a6-ed04e7f7517a.png)

## acknowledgement

thanks for the data provided by [marketwatch](http://www.marketwatch.com/);