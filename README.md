# DCF Valuation Model
A Python-based Discounted Cash Flow (DCF) valuation tool that pulls live financial data from Yahoo Finance and estimates the intrinsic value per share of any publicly listed company.
Built as a first-year Mathematics student to develop practical Python skills and apply core finance concepts from first principles.

## How it works
1. Fetches the company's most recent Free Cash Flow and shares outstanding directly from Yahoo Finance using the yfinance API.
2. Projects Free Cash Flows forward over 5 years using a user-defined compound growth rate.
3. Calculates a Terminal Value using the Gordon Growth Model, assuming stable perpetual growth after year 5.
4. Discounts all future cash flows back to present value using WACC as the discount rate.
5. Outputs Enterprise Value and intrinsic Price Per Share via an interactive Streamlit web app

## How to run

```
pip install pandas numpy yfinance streamlit
streamlit run app.py
```
## Inputs
| Parameter | Description | Default |
|---|---|---|
| Ticker | Any listed stock on yfinance | NVDA |
| FCF Growth Rate | Annual projected FCF growth over 5 years | 10% |
| Terminal Growth Rate | Long-term constant growth rate after 5 years | 2.5% |
| WACC | Weighted average cost of capital, used as discount rate | 9% |

## Tech stack
Python, pandas, numpy, yfinance, Streamlit
