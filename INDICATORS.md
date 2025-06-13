# Technical Indicators Documentation for JGT Platform

## JGT Platform Core Indicators (Used in Production)

The JGT platform focuses on Bill Williams indicators for systematic trading analysis. These indicators are actively used in jgtpy.JGTIDS and jgtapyhelper for signal generation.

### Alligator 🐊

The Alligator indicator is central to JGT platform analysis, used in multiple degrees for multi-timeframe confluence.

**JGT Implementation**: Three smoothed moving averages representing market phases:
- **Jaw** (Blue Line) - Long-term trend
- **Teeth** (Red Line) - Medium-term momentum  
- **Lips** (Green Line) - Short-term direction

**JGT Usage Patterns**:
```python
import pandas as pd
from jgtapy import Indicators

df = pd.read_csv('EURUSD60.csv')
i = Indicators(df)

# Regular Alligator (Primary analysis)
i.alligator(period_jaws=13, period_teeth=8, period_lips=5, 
           shift_jaws=8, shift_teeth=5, shift_lips=3,
           column_name_jaws='jaw', column_name_teeth='teeth', column_name_lips='lips')

# Big Alligator (Higher timeframe context) 
i.alligator(period_jaws=89, period_teeth=55, period_lips=34,
           shift_jaws=55, shift_teeth=34, shift_lips=21,
           column_name_jaws='bjaw', column_name_teeth='bteeth', column_name_lips='blips')

# Tide Alligator (Macro trend analysis)
i.alligator(period_jaws=377, period_teeth=233, period_lips=144,
           shift_jaws=233, shift_teeth=144, shift_lips=89,
           column_name_jaws='tjaw', column_name_teeth='tteeth', column_name_lips='tlips')
```

**Output Columns**: `jaw`, `teeth`, `lips` (+ variants for big/tide)

### Awesome Oscillator (AO) 🌟

Core momentum indicator used for FDB signal detection and ZLC (Zero Line Cross) analysis.

**JGT Implementation**: Difference between 5-period and 34-period SMA of median price
**JGT Usage**: Primary component of FDB (Fractal Divergent Bar) signals and momentum analysis

```python
i.ao_ac_oscillator(column_name_ao='ao', column_name_ac='ac')
```

**Output Columns**: `ao`

### Accelerator Oscillator (AC) 🚀

Measures momentum acceleration/deceleration, used for signal confirmation in JGT platform.

**JGT Implementation**: AO minus 5-period SMA of AO  
**JGT Usage**: Signal confirmation and momentum validation in conjunction with AO

```python
# Combined with AO in single call
i.ao_ac_oscillator(column_name_ao='ao', column_name_ac='ac')
```

**Output Columns**: `ac`

### Fractals 🌀

Multi-degree fractal analysis for support/resistance identification across timeframes.

**JGT Implementation**: Pattern recognition for potential reversal points
**JGT Usage**: Multiple degrees for comprehensive support/resistance mapping

```python
# Standard fractals (5-bar pattern)
i.fractals(column_name_high='fh', column_name_low='fl')

# Progressive degrees for multi-timeframe analysis
i.fractals3(column_name_high='fh3', column_name_low='fl3')
i.fractals5(column_name_high='fh5', column_name_low='fl5')
i.fractals8(column_name_high='fh8', column_name_low='fl8')
i.fractals13(column_name_high='fh13', column_name_low='fl13')
i.fractals21(column_name_high='fh21', column_name_low='fl21')
i.fractals34(column_name_high='fh34', column_name_low='fl34')
i.fractals55(column_name_high='fh55', column_name_low='fl55')
i.fractals89(column_name_high='fh89', column_name_low='fl89')
```

**Output Columns**: `fh`, `fl` (high/low fractals with degree suffixes)

### Market Facilitation Index (MFI) 📈

Bill Williams' MFI for volume efficiency analysis and signal quality assessment.

**JGT Implementation**: Measures efficiency of price movement relative to volume
**JGT Usage**: Signal quality assessment through Squat, Green, Fade, and Fake patterns

```python
i.bw_mfi(column_name='mfi')
```

**Output Columns**: `mfi`

**JGT Signal Patterns**:
- **Squat (+-)**`: High volume, lower MFI - Preparation phase
- **Green (++)**`: High volume, higher MFI - Bullish momentum  
- **Fade (--)**: Low volume, lower MFI - Weakness
- **Fake (-+)**: Low volume, higher MFI - False move

### Gator Oscillator (Optional)

Alligator phase analysis for market structure identification.

**JGT Implementation**: Histogram showing Alligator line convergence/divergence
**JGT Usage**: Market phase identification (sleeping, awakening, eating, sated)

```python
i.gator(period_jaws=13, period_teeth=8, period_lips=5,
        shift_jaws=8, shift_teeth=5, shift_lips=3,
        column_name_val1='gl', column_name_val2='gh')
```

**Output Columns**: `gl`, `gh`

## JGT Platform Integration

### Data Flow Pipeline
```
Market Data → jgtapy Indicators → jgtpy.JGTIDS → jgtml Signal Detection → Trading Decisions
```

### Column Naming Standards
The JGT platform uses standardized column names for indicator integration:

```python
# Standard naming convention
from jgtutils.jgtconstants import (
    JAW, TEETH, LIPS,           # Regular Alligator
    BJAW, BTEETH, BLIPS,        # Big Alligator  
    TJAW, TTEETH, TLIPS,        # Tide Alligator
    AO, AC,                     # Oscillators
    FH, FL, FH3, FL3, # ... ,   # Fractals
    MFI                         # Market Facilitation Index
)
```

### Configuration Control
Indicator usage is controlled through JGTIDSRequest objects:

```python
from jgtpy.JGTIDSRequest import JGTIDSRequest

rq = JGTIDSRequest()
rq.mfi_flag = True              # Enable MFI calculation
rq.gator_oscillator_flag = False # Disable Gator (optional)
rq.balligator_flag = True       # Enable Big Alligator
rq.talligator_flag = True       # Enable Tide Alligator
```

---

## Other Available Indicators (Not Used in JGT Platform)

The jgtapy package includes many additional indicators that are not currently used in the JGT platform's core trading logic:

### Trend Indicators
- **Simple Moving Average (SMA)**
- **Exponential Moving Average (EMA)**  
- **Smoothed Moving Average (SMMA)**

### Momentum Indicators
- **MACD (Moving Average Convergence/Divergence)**
- **Momentum**
- **Money Flow Index (MFI)** - Different from Bill Williams MFI

### Volatility Indicators
- **Bollinger Bands**
- **Average True Range (ATR)**

### Volume Indicators
- **Accumulation/Distribution (A/D)**
- **Force Index (FRC)**

### Oscillators
- **Commodity Channel Index (CCI)**
- **DeMarker (DeM)**
- **Bears Power**
- **Bulls Power**

### Example Usage (Available but Unused)
```python
# These work but are not part of JGT platform logic
i.sma(period=20, column_name='sma20')
i.bollinger_bands(period=20, column_name='bb')
i.macd(column_name='macd')
```

### Why Not Used in JGT Platform

The JGT platform focuses exclusively on Bill Williams indicators because:

1. **Methodological Coherence** - All indicators work together as an integrated system
2. **Multi-Timeframe Scaling** - Bill Williams indicators scale naturally across timeframes
3. **Signal Integration** - Natural confluence between AO, AC, Alligator, and Fractals
4. **Proven Track Record** - Battle-tested methodology in live trading
5. **Reduced Complexity** - Focused approach prevents indicator overload

---

## Development Guidelines

### Adding New Indicators to JGT Platform

If considering adding indicators to JGT platform usage:

1. **Methodological Fit** - Must integrate with Bill Williams approach
2. **Multi-Timeframe Compatibility** - Should work across all timeframes
3. **Signal Integration** - Must provide unique value not covered by existing indicators
4. **Testing Required** - Extensive backtesting and forward testing needed

### Modifying Existing Indicators

When modifying JGT-used indicators:

1. **Backward Compatibility** - Maintain existing column names and parameters
2. **Configuration Control** - Use JGTIDSRequest flags for new features
3. **Testing Required** - Verify impact on existing signal detection
4. **Documentation Update** - Update both jgtapy and jgtpy documentation

*This documentation reflects the actual usage patterns within the JGT platform. For experimental or research purposes, the full range of jgtapy indicators remains available.*
