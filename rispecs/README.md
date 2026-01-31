# JGTapy RISE Specifications

> Reverse-engineer → Intent-extract → Specify → Export

This directory contains RISE-compliant specifications for JGTapy - the technical indicators library for pandas DataFrames, implementing Bill Williams' trading indicators.

## Quick Start

1. **Start Here**: [`app.specs.md`](./app.specs.md) - Master specification
2. **Indicators**: [`indicators.spec.md`](./indicators.spec.md) - All indicator implementations

## Specification Map

```
app.specs.md                    ← Master specification (start here)
├── indicators.spec.md          ← Indicator implementations
│   ├── alligator.spec.md       ← Alligator (Jaw/Teeth/Lips)
│   ├── ao-ac.spec.md           ← Awesome Oscillator & Accelerator
│   ├── fractals.spec.md        ← Fractal detection (multi-dimension)
│   └── mfi.spec.md             ← Market Facilitation Index
└── utils.spec.md               ← Utility functions
```

## RISE Framework Compliance

✅ **Desired Outcome Definition** - What users CREATE, not problems to solve  
✅ **Structural Tension** - Current reality vs desired state drives progression  
✅ **Natural Advancement** - Clear flow from current to desired  
✅ **Autonomous Specification** - Another LLM could implement from spec alone

## Key Concepts

### Williams 5 Dimensions
1. **Fractals** - Reversal patterns (5-bar, 3-bar, multi-dimension)
2. **Momentum (AO)** - Awesome Oscillator
3. **Acceleration (AC)** - Accelerator Oscillator
4. **Zone Trading** - Green/Red zone confluence
5. **Balance Line** - Alligator indicator

### Available Indicators
- Alligator (Jaw/Teeth/Lips)
- Awesome Oscillator (AO)
- Accelerator Oscillator (AC)
- Fractals (2,3,5,8,13,21,34,55,89 dimensions)
- Market Facilitation Index (MFI)
- Gator Oscillator
- Plus: SMA, EMA, SMMA, Bollinger, CCI, ATR, MACD, etc.

## Specification Version

- **Version**: 1.0
- **Framework**: RISE
- **Created**: 2026-01-31
