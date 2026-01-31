# jgtapy Indicators Specification

> Core Williams Trading System Indicator Library

**Specification Version**: 1.0  
**Module**: `jgtapy/indicators.py`  
**RISE Framework Compliance**: Full  
**Last Updated**: 2026-01-31

---

## Desired Outcome Definition

**What Users Create**: Technical indicator calculations using the Indicators class - a pandas-native library for adding Bill Williams and standard indicators to any OHLCV DataFrame.

**Achievement Indicator**: Given DataFrame with OHLCV, produces:
- Alligator lines (jaw, teeth, lips)
- Awesome Oscillator (AO)
- Accelerator Oscillator (AC)
- Fractals (highs and lows)
- All standard moving averages

**Value Proposition**: Single class to add any Williams indicator with consistent pandas integration.

---

## Structural Tension

**Current Reality**: Raw OHLCV DataFrame with no analytical power.

**Desired State**: DataFrame enriched with all Williams Trading System indicators.

**Natural Progression**: Create Indicators(df) → Call methods → Access df.

---

## Core Class: Indicators

```python
class Indicators:
    """
    Add technical indicators to a pandas DataFrame.
    
    Example:
        >>> import pandas as pd
        >>> from jgtapy import Indicators
        >>> df = pd.read_csv('EURUSD60.csv')
        >>> i = Indicators(df)
        >>> i.accelerator_oscillator(column_name='AC')
        >>> i.awesome_oscillator(column_name='ao')
        >>> i.alligator()
        >>> result = i.df  # DataFrame with indicators
    """
    
    def __init__(
        self,
        df: pd.DataFrame,
        open_col: str = "Open",
        high_col: str = "High",
        low_col: str = "Low",
        close_col: str = "Close",
        volume_col: str = "Volume",
        median_col: str = "Median",
        index_column_name: str = "Date"
    ):
        """
        Initialize Indicators with OHLCV DataFrame.
        
        Args:
            df: DataFrame with OHLCV columns
            open_col: Name of Open column
            high_col: Name of High column
            low_col: Name of Low column
            close_col: Name of Close column
            volume_col: Name of Volume column
            median_col: Name of Median column (optional)
            index_column_name: Index column name
        """
```

---

## Moving Averages

### Simple Moving Average (SMA)

```python
def sma(
    self,
    period: int = 5,
    column_name: str = "sma",
    apply_to: str = "Close"
) -> None:
    """
    Simple Moving Average.
    
    Formula:
        SMA = sum(price[i-period:i]) / period
    
    Args:
        period: Number of periods (default: 5)
        column_name: Output column name
        apply_to: Price column to use
    """
```

### Smoothed Moving Average (SMMA)

```python
def smma(
    self,
    period: int = 5,
    column_name: str = "smma",
    apply_to: str = "Close"
) -> None:
    """
    Smoothed Moving Average (used by Alligator).
    
    Formula:
        First: SMMA[0] = SMA(period)
        Then: SMMA[i] = (SMMA[i-1] * (period-1) + price[i]) / period
    
    This creates a smoother line than SMA with less lag than EMA.
    """
```

### Exponential Moving Average (EMA)

```python
def ema(
    self,
    period: int = 5,
    column_name: str = "ema",
    apply_to: str = "Close"
) -> None:
    """
    Exponential Moving Average.
    
    Formula:
        EMA = price * k + EMA[i-1] * (1-k)
        where k = 2 / (period + 1)
    """
```

---

## Alligator Family

### Standard Alligator (5-8-13)

```python
def alligator(
    self,
    period_jaws: int = 13,
    period_teeth: int = 8,
    period_lips: int = 5,
    shift_jaws: int = 8,
    shift_teeth: int = 5,
    shift_lips: int = 3,
    column_name_jaws: str = "jaw",
    column_name_teeth: str = "teeth",
    column_name_lips: str = "lips"
) -> None:
    """
    Bill Williams Alligator indicator.
    
    Components:
        Jaw (Blue): SMMA(13) shifted 8 bars forward
        Teeth (Red): SMMA(8) shifted 5 bars forward
        Lips (Green): SMMA(5) shifted 3 bars forward
    
    Applied to: Median price (High + Low) / 2
    
    Interpretation:
        - Lines intertwined: Alligator sleeping, no trade
        - Lines separating: Alligator awakening, prepare
        - Lines spread apart: Alligator feeding, trend active
        - Lines converging: Alligator sated, take profits
    """
```

### Big Alligator (34-55-89)

```python
def big_alligator(
    self,
    period_jaws: int = 89,
    period_teeth: int = 55,
    period_lips: int = 34,
    shift_jaws: int = 8,
    shift_teeth: int = 5,
    shift_lips: int = 3,
    column_name_jaws: str = "bjaw",
    column_name_teeth: str = "bteeth",
    column_name_lips: str = "blips"
) -> None:
    """
    Big Alligator for intermediate trends.
    
    Same SMMA calculation with longer periods.
    Used for swing trading and position entries.
    """
```

### Tide Alligator (144-233-377)

```python
def tide_alligator(
    self,
    period_jaws: int = 377,
    period_teeth: int = 233,
    period_lips: int = 144,
    shift_jaws: int = 8,
    shift_teeth: int = 5,
    shift_lips: int = 3,
    column_name_jaws: str = "tjaw",
    column_name_teeth: str = "tteeth",
    column_name_lips: str = "tlips"
) -> None:
    """
    Tide Alligator for macro trends.
    
    Fibonacci-derived periods for long-term analysis.
    Used for position trading and major trend identification.
    """
```

---

## Oscillators

### Awesome Oscillator (AO)

```python
def awesome_oscillator(
    self,
    column_name: str = "ao"
) -> None:
    """
    Awesome Oscillator - Momentum indicator.
    
    Formula:
        Median = (High + Low) / 2
        AO = SMA(Median, 5) - SMA(Median, 34)
    
    Interpretation:
        - AO > 0: Bullish momentum
        - AO < 0: Bearish momentum
        - AO increasing: Momentum strengthening
        - AO decreasing: Momentum weakening
    
    Color (typically added separately):
        Green: AO[i] > AO[i-1]
        Red: AO[i] < AO[i-1]
    """
```

### Accelerator Oscillator (AC)

```python
def accelerator_oscillator(
    self,
    column_name: str = "ac"
) -> None:
    """
    Accelerator Oscillator - Momentum acceleration.
    
    Formula:
        AC = AO - SMA(AO, 5)
    
    Interpretation:
        - AC > 0: Bullish acceleration
        - AC < 0: Bearish acceleration
        - AC changes sign before AO does
        - Leading indicator for AO
    
    Trading Rules:
        - Buy only with green AC (2 green bars above zero, 3 below)
        - Sell only with red AC (2 red bars below zero, 3 above)
    """
```

### Gator Oscillator

```python
def gator_oscillator(
    self,
    column_name_upper: str = "gator_upper",
    column_name_lower: str = "gator_lower"
) -> None:
    """
    Gator Oscillator - Visualizes Alligator convergence/divergence.
    
    Formula:
        Upper = abs(Jaw - Teeth)  (displayed positive)
        Lower = abs(Teeth - Lips) (displayed negative)
    
    Phases:
        Sleeping: Both bars shrinking (red)
        Awakening: One growing, one shrinking
        Feeding: Both bars growing (green)
        Sated: Both bars beginning to shrink
    """
```

---

## Fractals

```python
def fractals(
    self,
    period: int = 5,
    column_name_high: str = "fh",
    column_name_low: str = "fl"
) -> None:
    """
    Williams Fractals - Key reversal points.
    
    Fractal High:
        High[i] is highest among High[i-2:i+3] (5-bar default)
        Marked 1 if true, 0 otherwise
    
    Fractal Low:
        Low[i] is lowest among Low[i-2:i+3] (5-bar default)
        Marked 1 if true, 0 otherwise
    
    Usage:
        - Entry above fractal high = buy signal confirmation
        - Entry below fractal low = sell signal confirmation
        - Used with Alligator for FDB signals
    """
```

---

## Market Facilitation Index

```python
def market_facilitation_index(
    self,
    column_name: str = "mfi"
) -> None:
    """
    Market Facilitation Index.
    
    Formula:
        MFI = (High - Low) / Volume
    
    Classification (comparing to previous bar):
        Green (+MFI, +Volume): Strong trend
        Fade (-MFI, -Volume): Trend exhaustion
        Squat (-MFI, +Volume): Battle, potential reversal
        Fake (+MFI, -Volume): False move
    """
```

---

## Support Functions

```python
# In jgtapy/utils.py

def calculate_ao(
    df: pd.DataFrame,
    column_name: str = "ao"
) -> None:
    """Calculate Awesome Oscillator."""

def calculate_sma(
    df: pd.DataFrame,
    period: int,
    column_name: str,
    apply_to: str
) -> None:
    """Calculate Simple Moving Average."""

def calculate_smma(
    df: pd.DataFrame,
    period: int,
    column_name: str,
    apply_to: str
) -> pd.DataFrame:
    """
    Calculate Smoothed Moving Average.
    
    Returns new DataFrame to merge with original.
    """

def mad(series: pd.Series) -> float:
    """Calculate Mean Absolute Deviation."""
```

---

## Usage Pattern

```python
import pandas as pd
from jgtapy import Indicators

# Load price data
df = pd.read_csv('EUR-USD_H1.csv')

# Create Indicators instance
ind = Indicators(df)

# Add Williams indicators
ind.alligator()
ind.awesome_oscillator()
ind.accelerator_oscillator()
ind.fractals()

# Add Big Alligator
ind.big_alligator()

# Get enriched DataFrame
result = ind.df

# Columns now include:
# jaw, teeth, lips, bjaw, bteeth, blips, ao, ac, fh, fl
```

---

## Dependencies

```python
import pandas as pd
import numpy as np
from .utils import calculate_ao, calculate_sma, calculate_smma, mad
```

---

## Quality Criteria

✅ **Pandas Native**: Direct DataFrame integration  
✅ **Williams Complete**: All 5 dimensions available  
✅ **Alligator Variants**: Regular, Big, Tide  
✅ **Configurable Periods**: Customizable for any strategy  
✅ **Proper Shifts**: Alligator lines shifted correctly  
✅ **SMMA Implementation**: Correct smoothed average formula

---

## Version

Current version: **1.9.22**
