# AI Semiconductor Competitive Landscape Analysis
### AMD · NVIDIA · Intel · Qualcomm · TSMC — FY2022–FY2024

**Author:** Jovanna Garza · [linkedin.com/in/jovannagarza](https://linkedin.com/in/jovannagarza) · [github.com/jovannagarza](https://github.com/jovannagarza)  
**Tools:** Python, Pandas, Matplotlib  
**Data:** Public 10-K filings, earnings releases, company annual reports (FY2022–FY2024)

---

## Overview

This project analyzes the competitive dynamics of the AI semiconductor industry across five companies that collectively define the hardware stack powering modern AI infrastructure. The analysis covers financial performance, margin trajectories, AI revenue exposure, stock returns, and capital efficiency — structured as an analyst memo rather than an academic exercise.

The central question: **who is winning in AI chips, and is it durable?**

---

## Project Structure

```
ai_chip_analysis/
├── analysis.py              # Main script — runs all charts
├── data/
│   └── financials.py        # Verified financial data (sourced from filings)
├── charts/
│   ├── 01_revenue_trends.png
│   ├── 02_margins.png
│   ├── 03_ai_exposure_bubble.png
│   ├── 04_stock_indexed.png
│   └── 05_revenue_per_employee.png
└── README.md
```

---

## How to Run

```bash
git clone https://github.com/jovannagarza/ai-chip-analysis
cd ai-chip-analysis
pip install pandas matplotlib numpy
python analysis.py
```

Charts are saved to `/charts/`. No API keys or external data fetches required — all financial data is embedded in `data/financials.py` with sources cited inline.

---

## Company Positioning

| Company | AI Chip Role | Key Product |
|---|---|---|
| **NVIDIA** | Dominant AI accelerator supplier | H100 / H200 / GB200 GPUs; CUDA ecosystem |
| **AMD** | Primary GPU challenger | MI300X; ROCm software stack |
| **Intel** | Legacy CPU leader, AI transition | Gaudi 3 accelerator; Xeon for inference |
| **Qualcomm** | Edge AI and mobile inference | Snapdragon X Elite; Oryon NPU |
| **TSMC** | Foundry — manufactures chips for all above | 3nm / 5nm advanced nodes; CoWoS packaging |

---

## Charts

### 1. Revenue Trends & Growth Rates
![Revenue Trends](charts/01_revenue_trends.png)

NVIDIA's FY2024 revenue of $130.5B represents a 191% YoY increase — the most dramatic single-year revenue expansion in semiconductor history. Every other company grew modestly or declined. Intel's 2.1% contraction reflects accelerating market share loss in the data center CPU segment.

---

### 2. Gross & Operating Margins
![Margins](charts/02_margins.png)

NVIDIA's gross margin expanded to **75%** in FY2024 — a figure more consistent with software companies than hardware manufacturers — driven by inelastic demand and H100 pricing power ($25,000–$40,000 per GPU). Intel's operating margin turned deeply negative (–2.2%), reflecting both restructuring charges and the cost of competing foundry investment without commensurate revenue.

---

### 3. AI Revenue Exposure vs. Market Cap
![AI Exposure Bubble](charts/03_ai_exposure_bubble.png)

NVIDIA derives ~88% of revenue from data center and AI workloads; its $3.3T market cap prices in continued dominance. TSMC sits in an unusual position: 52% AI/HPC exposure but valued at a fraction of NVIDIA despite being the irreplaceable manufacturing layer beneath every AI chip in this analysis. This divergence reflects the market's view that TSMC's pricing power is capped by customer concentration risk (Apple + NVIDIA = ~35% of revenue).

---

### 4. Indexed Stock Performance
![Stock Indexed](charts/04_stock_indexed.png)

From a FY2022 base of 100: NVIDIA reached **~928** by FY2024 year-end. TSMC reached **~241** — the second-best performer, rewarded for being the picks-and-shovels play with less demand concentration risk than NVIDIA. Intel fell to **~76**, the only company in this group to destroy shareholder value over the period.

---

### 5. Revenue per Employee
![Revenue per Employee](charts/05_revenue_per_employee.png)

NVIDIA generates **$4.41M revenue per employee** — more than 12x Intel's $0.49M. This is the clearest expression of NVIDIA's business model advantage: it designs chips and builds software, then outsources fabrication entirely to TSMC. Intel both designs and manufactures, carrying ~109,000 employees and the full cost of running fabs. AMD's $0.99M/employee reflects a design-only model that is capital-light but not yet as leveraged as NVIDIA.

---

## Strategic Analysis

### Who Is Winning, and Why It's Not Just the Hardware

NVIDIA's FY2024 results are not the story of a better chip — they are the story of a better **ecosystem**. CUDA, NVIDIA's proprietary GPU programming framework, has been in continuous development since 2007. The result is 17+ years of library integrations, developer tooling, and model optimizations that run natively on NVIDIA hardware. AMD's ROCm framework is technically capable but lacks this integration depth. When a machine learning researcher defaults to CUDA without considering alternatives, that is not a product decision — it is a switching cost embedded in institutional muscle memory.

This distinction matters enormously for competitive analysis. Hardware generations cycle every 18–24 months. Software ecosystems do not. Intel learned this in the CPU market: by the time AMD's Zen architecture caught up on transistor density, Intel's developer relationships had already eroded. The same dynamic is playing out in AI accelerators — AMD's MI300X is a competitive product on benchmarks, but it ships into a market where most enterprise MLOps teams have built toolchains, deployment pipelines, and optimization workflows around CUDA assumptions.

### The TSMC Dependency Risk Is the Industry's Most Underpriced Vulnerability

Every chip in this analysis — NVIDIA's H100, AMD's MI300, Qualcomm's Snapdragon — depends on TSMC's advanced nodes for production. Intel is the only company with its own leading-edge fab, and it has spent five years and over $40B trying to compete with TSMC at 3nm without reaching yield parity. This creates a structural concentration risk that does not appear in any company's income statement: a TSMC disruption (geopolitical, natural disaster, or technical) would simultaneously impair NVIDIA, AMD, and Qualcomm production with no near-term alternative. The U.S. CHIPS Act and Intel Foundry Services exist precisely to reduce this dependency — but neither is close to offering the advanced packaging and node density TSMC provides today.

### What This Means for Investment and Industry Structure

The market has priced NVIDIA's CUDA moat into a $3.3T valuation while leaving TSMC — the enabling infrastructure beneath all of it — at roughly $1T. If you believe NVIDIA's AI revenue growth is durable, you are implicitly betting on TSMC's continued operational excellence. But TSMC trades at a material discount to NVIDIA on an EV/Revenue basis (~4x vs. ~25x), suggesting either that the market undervalues TSMC's strategic position or that it is correctly pricing the geopolitical and customer-concentration risks that make TSMC structurally cheap. For companies building AI infrastructure today, the strategic implication is clear: any serious supply chain or vendor strategy needs to treat TSMC continuity as a first-order risk variable, not a commodity assumption.

---

## Data Sources

| Company | Source |
|---|---|
| NVIDIA | 10-K FY2024 (Jan 2024); earnings releases Q4 FY2024 |
| AMD | 10-K FY2024 (Dec 2023); Q4 2024 earnings |
| Intel | 10-K FY2024 (Dec 2023); Q4 2024 earnings |
| Qualcomm | 10-K FY2024 (Sep 2024); fiscal year ends September |
| TSMC | Annual Report 2024; USD figures converted from TWD at average annual rate |

Stock prices are approximate fiscal year-end adjusted closes sourced from public market data.  
All financial figures in USD billions unless noted.

---

*This analysis was produced as a portfolio project demonstrating applied economics, financial data analysis, and Python visualization. It is not investment advice.*
