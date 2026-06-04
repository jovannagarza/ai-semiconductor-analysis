"""
AI Semiconductor Financial Data
Sources: Company 10-K filings, earnings releases (FY2022-FY2024)
All revenue figures in USD billions. Margins as decimals.
"""

# Annual Revenue (USD Billions) — FY2022, FY2023, FY2024
REVENUE = {
    "NVIDIA": [26.97, 44.87, 130.50],   # FY ends Jan; FY24=CY2023, FY25=CY2024
    "AMD":    [23.60, 22.68, 25.79],
    "Intel":  [63.05, 54.23, 53.10],
    "Qualcomm":[44.20, 35.82, 38.96],
    "TSMC":   [75.88, 69.30, 88.36],    # USD, converted from TWD at avg rate
}

# Fiscal years mapped to calendar context
FISCAL_YEARS = ["FY2022", "FY2023", "FY2024"]

# Gross Margin % — FY2022, FY2023, FY2024
GROSS_MARGIN = {
    "NVIDIA":   [64.9, 66.8, 75.0],
    "AMD":      [48.0, 46.1, 49.1],
    "Intel":    [45.8, 42.6, 32.7],
    "Qualcomm": [55.7, 55.8, 56.3],
    "TSMC":     [59.6, 54.4, 57.1],
}

# Operating Margin % — FY2022, FY2023, FY2024
OPERATING_MARGIN = {
    "NVIDIA":   [37.3, 29.0, 61.1],
    "AMD":      [5.5,  -4.1, 4.9],
    "Intel":    [3.7,  -13.0,-2.2],
    "Qualcomm": [29.0, 24.3, 28.4],
    "TSMC":     [45.2, 38.7, 47.3],
}

# Stock price at fiscal year-end (approximate, adjusted close, USD)
STOCK_PRICE = {
    "NVIDIA":   [14.6,  49.5,  135.6],
    "AMD":      [65.5,  147.4, 168.2],
    "Intel":    [26.4,  46.9,  20.0],
    "Qualcomm": [110.0, 130.5, 155.8],
    "TSMC":     [78.5,  102.3, 189.4],
}

# Data Center / AI-related revenue as % of total (FY2024 estimates)
AI_REVENUE_SHARE = {
    "NVIDIA":   88,   # Data center segment
    "AMD":      32,   # Data Center segment (MI300 ramp)
    "Intel":    25,   # DCAI + Gaudi (rough)
    "Qualcomm": 8,    # Cloud/Edge AI, nascent
    "TSMC":     52,   # HPC (includes AI chips) as % of wafer revenue
}

# Market cap USD billions (approx. end of FY2024 / early 2025)
MARKET_CAP = {
    "NVIDIA":   3300,
    "AMD":      258,
    "Intel":    88,
    "Qualcomm": 170,
    "TSMC":     1000,
}

# YoY revenue growth FY2024 vs FY2023
REVENUE_GROWTH_FY24 = {
    "NVIDIA":   +190.9,
    "AMD":      +13.7,
    "Intel":    -2.1,
    "Qualcomm": +8.8,
    "TSMC":     +27.6,
}

# Colors per company (consistent across charts)
COLORS = {
    "NVIDIA":   "#76b900",   # NVIDIA green
    "AMD":      "#ed1c24",   # AMD red
    "Intel":    "#0071c5",   # Intel blue
    "Qualcomm": "#3253DC",   # Qualcomm blue
    "TSMC":     "#FF6B35",   # TSMC orange
}

COMPANIES = list(REVENUE.keys())
