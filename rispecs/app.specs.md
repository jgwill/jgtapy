# JGTapy Application Specification

> Master specification for the JGT Technical Indicators Library

**Specification Version**: 1.0  
**RISE Framework Compliance**: Full  
**Last Updated**: 2026-01-31

---

## Desired Outcome Definition

**What Users Create**: Rich technical indicator calculations on pandas DataFrames, with native support for Bill Williams' 5 Dimensions methodology that powers the entire JGT trading ecosystem.

**Achievement Indicator**: Users can load any OHLCV DataFrame and add Williams indicators (Alligator, AO, AC, Fractals, MFI) with single method calls, producing analysis-ready data.

**Value Proposition**: Pure pandas-based indicator calculations with no external dependencies beyond numpy, providing the mathematical foundation for all JGT signal detection.

---

## Application Overview

JGTapy is a Python library that:
1. Calculates technical indicators on pandas DataFrames
2. Implements complete Bill Williams indicator suite
3. Supports multi-dimensional fractal detection (2,3,5,8,13,21,34,55,89 bars)
4. Provides standard indicators (SMA, EMA, Bollinger, etc.)
5. Used by jgtpy/JGTIDS.py to generate indicator data

---

## Structural Tension

**Current Reality**: Raw OHLCV price data lacks the derived indicators needed for trading analysis.

**Desired State**: DataFrames enriched with Alligator, AO, AC, Fractals, MFI and other indicators ready for signal detection.

**Natural Progression**: jgtapy transforms price data into analysis-ready DataFrames that flow to JGTIDS, JGTCDS, and ultimately trading signals.

---

## Core API

### Basic Usage

```python
import pandas as pd
from jgtapy import Indicators

# Load price data
df = pd.read_csv('EURUSD60.csv')

# Create indicator calculator
i = Indicators(df)

# Add Williams indicators
i.alligator()                    # Adds jaw, teeth, lips columns
i.awesome_oscillator('ao')        # Adds ao column
i.accelerator_oscillator('ac')    # Adds ac column
i.fractals(column_name_high='fh', column_name_low='fl')
i.bw_mfi('mfi')                  # Market Facilitation Index

# Get enriched DataFrame
df_with_indicators = i.df
```

### Fractal Dimensions

```python
# Standard 5-bar fractals
i.fractals(column_name_high='fh', column_name_low='fl')

# Multi-dimensional fractals
i.fractals3(column_name_high='fb3', column_name_low='fs3')
i.fractals5(column_name_high='fb5', column_name_low='fs5')
i.fractals8(column_name_high='fb8', column_name_low='fs8')
i.fractals13(column_name_high='fb13', column_name_low='fs13')
i.fractals21(column_name_high='fb21', column_name_low='fs21')
i.fractals34(column_name_high='fb34', column_name_low='fs34')
i.fractals55(column_name_high='fb55', column_name_low='fs55')
i.fractals89(column_name_high='fb89', column_name_low='fs89')
```

---

## Williams Indicator Specifications

### Alligator 🐊

**Purpose**: Identify trends and their direction using three smoothed moving averages

**Formula**:
- Jaw (Blue): SMMA(Median, 13) shifted 8 bars forward
- Teeth (Red): SMMA(Median, 8) shifted 5 bars forward  
- Lips (Green): SMMA(Median, 5) shifted 3 bars forward

**Output Columns**: `jaw`, `teeth`, `lips`

**Trading Interpretation**:
- Lines intertwined = "Alligator sleeping" = no trade
- Lines separating = "Alligator awakening" = trend starting
- Lines spread apart = "Alligator feeding" = trending market

### Awesome Oscillator (AO) 🌟

**Purpose**: Measure market momentum

**Formula**: SMA(Median, 5) - SMA(Median, 34)

**Output Column**: `ao`

**Trading Interpretation**:
- Zero line crossings indicate momentum shifts
- Green bars (rising) = bullish momentum
- Red bars (falling) = bearish momentum

### Accelerator Oscillator (AC) 🚀

**Purpose**: Measure acceleration/deceleration of momentum

**Formula**: AO - SMA(AO, 5)

**Output Column**: `ac`

**Trading Interpretation**:
- Measures the "speed of the speed"
- Color changes before AO direction changes
- Confirmation signal for entries

### Fractals 🌀

**Purpose**: Identify potential reversal points

**Formula** (5-bar):
- Bullish Fractal: Middle bar has highest high, two lower highs each side
- Bearish Fractal: Middle bar has lowest low, two higher lows each side

**Output Columns**: `fh` (high fractal), `fl` (low fractal)

**Dimensions**: 2, 3, 5, 8, 13, 21, 34, 55, 89 bars

### Market Facilitation Index (MFI) 📈

**Purpose**: Measure price movement efficiency per unit of volume

**Formula**: (High - Low) / Volume

**Output Column**: `mfi`

**Bar Types**:
- Green (high MFI, high Vol) - Strong trend
- Squat (low MFI, high Vol) - Potential reversal
- Fade (high MFI, low Vol) - Low participation
- Fake (low MFI, low Vol) - Market indecision

---

## Type Definitions

```python
from typing import Optional
import pandas as pd

class Indicators:
    def __init__(self, df: pd.DataFrame) -> None: ...
    
    # Williams Indicators
    def alligator(
        self,
        period_jaws: int = 13,
        period_teeth: int = 8,
        period_lips: int = 5,
        shift_jaws: int = 8,
        shift_teeth: int = 5,
        shift_lips: int = 3,
        column_name_jaws: str = 'jaw',
        column_name_teeth: str = 'teeth',
        column_name_lips: str = 'lips'
    ) -> None: ...
    
    def awesome_oscillator(
        self,
        column_name: str = 'ao'
    ) -> None: ...
    
    def accelerator_oscillator(
        self,
        column_name: str = 'ac'
    ) -> None: ...
    
    def fractals(
        self,
        column_name_high: str = 'fh',
        column_name_low: str = 'fl'
    ) -> None: ...
    
    def bw_mfi(
        self,
        column_name: str = 'mfi'
    ) -> None: ...
    
    # Standard Indicators
    def sma(
        self,
        period: int = 5,
        column_name: str = 'sma'
    ) -> None: ...
    
    def ema(
        self,
        period: int = 5,
        column_name: str = 'ema'
    ) -> None: ...
    
    def bollinger_bands(
        self,
        period: int = 20,
        deviation: int = 2
    ) -> None: ...
    
    @property
    def df(self) -> pd.DataFrame: ...
```

---

## Creative Advancement Scenarios

### Scenario: Generate IDS Data

**Desired Outcome**: Convert raw PDS to indicator-enriched IDS

**Current Reality**: Have OHLCV DataFrame, need Williams indicators

**Natural Progression**:
1. Load PDS: `df = pd.read_csv('pds.csv')`
2. Create indicators: `i = Indicators(df)`
3. Add Alligator: `i.alligator()`
4. Add AO/AC: `i.awesome_oscillator(); i.accelerator_oscillator()`
5. Add Fractals: `i.fractals()`
6. Get result: `ids_df = i.df`

**Resolution**: IDS DataFrame with all Williams columns ready for JGTCDS

### Scenario: Multi-Timeframe Fractal Analysis

**Desired Outcome**: Identify fractals at multiple scales simultaneously

**Current Reality**: Single-dimension fractals miss larger patterns

**Natural Progression**:
1. Add standard fractals: `i.fractals()`
2. Add higher dimensions: `i.fractals13(); i.fractals34()`
3. Analyze confluence: where multiple fractal dimensions align

**Resolution**: Multi-scale fractal map revealing major support/resistance

---

## Module Structure

```
jgtapy/
├── __init__.py           # Package exports
├── indicators.py         # Main Indicators class
└── utils.py              # Utility functions
```

---

## Integration with JGT Ecosystem

```
jgtapy (this package)
    ↓ provides indicator calculations
jgtpy/JGTIDS.py
    ↓ uses indicators to create IDS
jgtpy/JGTCDS.py
    ↓ adds signals on top of indicators
jgtml
    ↓ analyzes signal patterns
jgt-data-server
    ↓ serves indicators via API
jgt-code
    ↓ displays analysis in terminal
```

---

## Quality Criteria

✅ **Pure Pandas**: No external dependencies beyond numpy  
✅ **Williams Complete**: Full 5 Dimensions implementation  
✅ **Multi-Dimensional Fractals**: 2-89 bar fractal support  
✅ **Column Naming**: Customizable output column names  
✅ **Method Chaining**: Fluent API for adding indicators
