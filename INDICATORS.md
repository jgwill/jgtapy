# Technical Indicators Documentation

## Alligator 🐊

The Alligator indicator is a combination of three smoothed moving averages with different periods and shifts. It is used to identify trends and their direction. The three lines are called the Jaw, Teeth, and Lips. The implementation can be found in the `alligator` method in `jgtapy/indicators.py`.

### Usage Example
```python
import pandas as pd
from jgtapy import Indicators

df = pd.read_csv('EURUSD60.csv')
i = Indicators(df)
i.alligator(period_jaws=13, period_teeth=8, period_lips=5, shift_jaws=8, shift_teeth=5, shift_lips=3, column_name_jaws='alligator_jaws', column_name_teeth='alligator_teeth', column_name_lips='alligator_lips')
df = i.df
print(df.tail())
```

## Awesome Oscillator (AO) 🌟

The Awesome Oscillator is a momentum indicator that compares the 5-period simple moving average (SMA) with the 34-period SMA. It helps to identify market momentum. The implementation can be found in the `awesome_oscillator` method in `jgtapy/indicators.py`.

### Usage Example
```python
import pandas as pd
from jgtapy import Indicators

df = pd.read_csv('EURUSD60.csv')
i = Indicators(df)
i.awesome_oscillator(column_name='ao')
df = i.df
print(df.tail())
```

## Accelerator Oscillator (AC) 🚀

The Accelerator Oscillator measures the acceleration or deceleration of the current market driving force. It is derived from the Awesome Oscillator by subtracting a 5-period SMA of the AO from the AO itself. The implementation can be found in the `accelerator_oscillator` method in `jgtapy/indicators.py`.

### Usage Example
```python
import pandas as pd
from jgtapy import Indicators

df = pd.read_csv('EURUSD60.csv')
i = Indicators(df)
i.accelerator_oscillator(column_name='ac')
df = i.df
print(df.tail())
```

## Fractals 🌀

Fractals are used to identify potential reversal points in the market. They consist of a series of at least five bars, with the highest high in the middle and two lower highs on each side for a bullish fractal, or the lowest low in the middle and two higher lows on each side for a bearish fractal. The implementation can be found in the `fractals` method and its variations in `jgtapy/indicators.py`.

### Usage Example
```python
import pandas as pd
from jgtapy import Indicators

df = pd.read_csv('EURUSD60.csv')
i = Indicators(df)
i.fractals(column_name_high='fractals_high', column_name_low='fractals_low')
df = i.df
print(df.tail())
```

## Market Facilitation Index (MFI) 📈

The Market Facilitation Index measures the efficiency of price movement by comparing the range of price movement to the volume. It helps to identify potential market trends and reversals. The implementation can be found in the `bw_mfi` method in `jgtapy/indicators.py`.

### Usage Example
```python
import pandas as pd
from jgtapy import Indicators

df = pd.read_csv('EURUSD60.csv')
i = Indicators(df)
i.bw_mfi(column_name='bw_mfi')
df = i.df
print(df.tail())
```
