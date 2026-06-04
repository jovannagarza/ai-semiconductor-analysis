"""
AI Semiconductor Competitive Landscape Analysis
Author: Jovanna Garza
Tools: Python, Pandas, Matplotlib, Seaborn
Data: Public company 10-K filings & earnings releases (FY2022–FY2024)
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np
from data.financials import (
    REVENUE, GROSS_MARGIN, OPERATING_MARGIN, STOCK_PRICE,
    AI_REVENUE_SHARE, MARKET_CAP, REVENUE_GROWTH_FY24,
    FISCAL_YEARS, COLORS, COMPANIES
)

# ── Global style ──────────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family":      "DejaVu Sans",
    "axes.spines.top":  False,
    "axes.spines.right":False,
    "axes.grid":        True,
    "grid.color":       "#e5e5e5",
    "grid.linewidth":   0.6,
    "figure.facecolor": "white",
    "axes.facecolor":   "white",
    "axes.labelcolor":  "#333333",
    "xtick.color":      "#555555",
    "ytick.color":      "#555555",
    "font.size":        11,
})

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "charts")
os.makedirs(OUT, exist_ok=True)


# ══════════════════════════════════════════════════════════════════════════════
# CHART 1 — Revenue Trends (grouped bar)
# ══════════════════════════════════════════════════════════════════════════════
def chart1_revenue_trends():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("AI Chip Sector: Revenue Trends FY2022–FY2024",
                 fontsize=15, fontweight="bold", y=1.01, color="#1a1a1a")

    # Left: absolute revenue
    ax = axes[0]
    x = np.arange(len(FISCAL_YEARS))
    n = len(COMPANIES)
    width = 0.15
    for i, co in enumerate(COMPANIES):
        bars = ax.bar(x + i*width, REVENUE[co], width,
                      label=co, color=COLORS[co], alpha=0.92, zorder=3)
    ax.set_xticks(x + width*(n-1)/2)
    ax.set_xticklabels(FISCAL_YEARS)
    ax.set_ylabel("Revenue (USD Billions)")
    ax.set_title("Annual Revenue by Company", fontweight="bold")
    ax.legend(loc="upper left", fontsize=9)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f"${v:.0f}B"))

    # Annotate NVIDIA FY2024 bar — the outlier
    nvda_idx = COMPANIES.index("NVIDIA")
    ax.annotate("+191% YoY", xy=(2 + nvda_idx*width, REVENUE["NVIDIA"][2]),
                xytext=(2 + nvda_idx*width - 0.3, REVENUE["NVIDIA"][2] + 6),
                fontsize=8, color=COLORS["NVIDIA"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=COLORS["NVIDIA"], lw=1.2))

    # Right: YoY revenue growth FY2024
    ax2 = axes[1]
    cos = list(REVENUE_GROWTH_FY24.keys())
    vals = list(REVENUE_GROWTH_FY24.values())
    bar_colors = [COLORS[c] for c in cos]
    bars = ax2.barh(cos, vals, color=bar_colors, alpha=0.88, zorder=3)
    ax2.axvline(0, color="#aaaaaa", linewidth=1)
    ax2.set_xlabel("YoY Revenue Growth FY2024 (%)")
    ax2.set_title("Revenue Growth Rate: FY2024 vs FY2023", fontweight="bold")
    ax2.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f"{v:+.0f}%"))
    for bar, val in zip(bars, vals):
        ax2.text(val + (3 if val >= 0 else -3), bar.get_y() + bar.get_height()/2,
                 f"{val:+.1f}%", va="center", ha="left" if val >= 0 else "right",
                 fontsize=9, fontweight="bold")

    plt.tight_layout()
    path = os.path.join(OUT, "01_revenue_trends.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  ✓ Chart 1 saved → {path}")


# ══════════════════════════════════════════════════════════════════════════════
# CHART 2 — Gross & Operating Margin Comparison
# ══════════════════════════════════════════════════════════════════════════════
def chart2_margins():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Profitability Comparison: Gross & Operating Margins FY2022–FY2024",
                 fontsize=15, fontweight="bold", y=1.01, color="#1a1a1a")

    for ax, data, title, ylabel in zip(
        axes,
        [GROSS_MARGIN, OPERATING_MARGIN],
        ["Gross Margin (%)", "Operating Margin (%)"],
        ["Gross Margin (%)", "Operating Margin (%)"]
    ):
        x = np.arange(len(FISCAL_YEARS))
        n = len(COMPANIES)
        width = 0.15
        for i, co in enumerate(COMPANIES):
            ax.bar(x + i*width, data[co], width,
                   label=co, color=COLORS[co], alpha=0.88, zorder=3)
        ax.set_xticks(x + width*(n-1)/2)
        ax.set_xticklabels(FISCAL_YEARS)
        ax.set_ylabel(ylabel)
        ax.set_title(title, fontweight="bold")
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f"{v:.0f}%"))
        if ax == axes[0]:
            ax.legend(loc="lower right", fontsize=9)

    # Highlight Intel's margin collapse
    ax = axes[1]
    ax.annotate("Intel: margin\ncollapse –46pp\nover 3 years",
                xy=(2 + COMPANIES.index("Intel")*0.15, OPERATING_MARGIN["Intel"][2]),
                xytext=(1.5, -20),
                fontsize=8, color=COLORS["Intel"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=COLORS["Intel"], lw=1.2))

    plt.tight_layout()
    path = os.path.join(OUT, "02_margins.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  ✓ Chart 2 saved → {path}")


# ══════════════════════════════════════════════════════════════════════════════
# CHART 3 — AI Revenue Exposure Bubble Chart
# ══════════════════════════════════════════════════════════════════════════════
def chart3_ai_exposure_bubble():
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_title("AI Revenue Exposure vs. Market Cap (FY2024)\n"
                 "Bubble size = Total Revenue FY2024",
                 fontsize=14, fontweight="bold", color="#1a1a1a")

    for co in COMPANIES:
        x = AI_REVENUE_SHARE[co]
        y = MARKET_CAP[co]
        size = REVENUE[co][2] * 12   # scale bubble to revenue
        ax.scatter(x, y, s=size, color=COLORS[co], alpha=0.75,
                   edgecolors="white", linewidths=1.5, zorder=3)
        # Label offsets by company to avoid overlap
        offsets = {
            "NVIDIA":   (1.5,  80),
            "AMD":      (1.5, -50),
            "Intel":    (1.5, -60),
            "Qualcomm": (-14, -60),
            "TSMC":     (1.5,  60),
        }
        dx, dy = offsets[co]
        ax.annotate(f"{co}\n${y:.0f}B mkt cap",
                    xy=(x, y), xytext=(x+dx, y+dy),
                    fontsize=9, fontweight="bold", color=COLORS[co],
                    arrowprops=dict(arrowstyle="-", color=COLORS[co], lw=0.8))

    ax.set_xlabel("AI / Data Center Revenue as % of Total Revenue (FY2024)", fontsize=11)
    ax.set_ylabel("Market Capitalization (USD Billions)", fontsize=11)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f"{v:.0f}%"))
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f"${v:.0f}B"))

    # Quadrant shading
    ax.axvline(50, color="#cccccc", linestyle="--", linewidth=1)
    ax.axhline(300, color="#cccccc", linestyle="--", linewidth=1)
    ax.text(52, 50, "High AI exposure\nHigh valuation", fontsize=8,
            color="#888888", style="italic")
    ax.text(2, 50, "Low AI exposure\nLow valuation", fontsize=8,
            color="#888888", style="italic")

    # Legend for bubble size
    for rev, label in [(25, "$25B rev"), (75, "$75B rev"), (130, "$130B rev")]:
        ax.scatter([], [], s=rev*12, color="#aaaaaa", alpha=0.6,
                   edgecolors="white", label=label)
    ax.legend(title="Bubble = FY2024 Revenue", loc="upper left",
              fontsize=8, title_fontsize=8)

    plt.tight_layout()
    path = os.path.join(OUT, "03_ai_exposure_bubble.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  ✓ Chart 3 saved → {path}")


# ══════════════════════════════════════════════════════════════════════════════
# CHART 4 — Stock Price Indexed (base 100 = FY2022)
# ══════════════════════════════════════════════════════════════════════════════
def chart4_stock_indexed():
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.set_title("Indexed Stock Price Performance FY2022–FY2024\n(Base = 100 at FY2022 year-end)",
                 fontsize=14, fontweight="bold", color="#1a1a1a")

    years = [2022, 2023, 2024]
    for co in COMPANIES:
        base = STOCK_PRICE[co][0]
        indexed = [p / base * 100 for p in STOCK_PRICE[co]]
        lw = 3 if co in ("NVIDIA", "TSMC") else 1.8
        ls = "-" if co in ("NVIDIA", "TSMC", "AMD") else "--"
        ax.plot(years, indexed, marker="o", linewidth=lw, linestyle=ls,
                color=COLORS[co], label=co, zorder=3, markersize=6)
        # End label
        ax.annotate(f"{co}  {indexed[-1]:.0f}",
                    xy=(2024, indexed[-1]),
                    xytext=(2024.05, indexed[-1]),
                    fontsize=9, color=COLORS[co], fontweight="bold", va="center")

    ax.axhline(100, color="#aaaaaa", linestyle=":", linewidth=1)
    ax.set_xticks(years)
    ax.set_xticklabels(["FY2022", "FY2023", "FY2024"])
    ax.set_ylabel("Indexed Price (Base = 100)")
    ax.set_xlim(2021.8, 2025.1)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f"{v:.0f}"))
    ax.legend(loc="upper left", fontsize=9)

    plt.tight_layout()
    path = os.path.join(OUT, "04_stock_indexed.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  ✓ Chart 4 saved → {path}")


# ══════════════════════════════════════════════════════════════════════════════
# CHART 5 — Revenue per Employee (efficiency proxy)
# ══════════════════════════════════════════════════════════════════════════════
def chart5_revenue_per_employee():
    # FY2024 headcount (approx., from annual reports)
    headcount = {
        "NVIDIA":   29600,
        "AMD":      26000,
        "Intel":    108900,
        "Qualcomm": 50000,
        "TSMC":     73000,
    }
    rev_per_emp = {co: (REVENUE[co][2] * 1e9) / headcount[co] / 1e6
                   for co in COMPANIES}  # in $M per employee

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("Revenue per Employee (FY2024)\nCapital Efficiency Proxy",
                 fontsize=14, fontweight="bold", color="#1a1a1a")

    cos = sorted(rev_per_emp, key=rev_per_emp.get, reverse=True)
    vals = [rev_per_emp[c] for c in cos]
    colors = [COLORS[c] for c in cos]
    bars = ax.bar(cos, vals, color=colors, alpha=0.88, zorder=3, width=0.55)

    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
                f"${val:.2f}M", ha="center", va="bottom",
                fontsize=10, fontweight="bold")

    ax.set_ylabel("Revenue per Employee (USD Millions)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f"${v:.1f}M"))

    # Source note
    ax.text(0.99, -0.12, "Sources: Company 10-K filings, earnings releases FY2024",
            transform=ax.transAxes, fontsize=7.5, color="#888888", ha="right")

    plt.tight_layout()
    path = os.path.join(OUT, "05_revenue_per_employee.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  ✓ Chart 5 saved → {path}")


# ══════════════════════════════════════════════════════════════════════════════
# RUN ALL
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\nGenerating AI Chip Competitive Analysis charts...\n")
    chart1_revenue_trends()
    chart2_margins()
    chart3_ai_exposure_bubble()
    chart4_stock_indexed()
    chart5_revenue_per_employee()
    print("\n✓ All charts generated in /charts/\n")
