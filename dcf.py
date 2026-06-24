from data import get_financials
from data import get_shares_outstanding

def project_fcf(base_fcf, growth_rate, years=5):
    fcf_list = []
    for t in range(1, years + 1):
        fcf = base_fcf * (1 + growth_rate) ** t
        fcf_list.append(fcf)
    return fcf_list

def terminal_value(final_fcf, terminal_growth, wacc):
    return (final_fcf * (1 + terminal_growth)) / (wacc - terminal_growth)

def discount_cashflows(cashflows, terminal_val, wacc):
    discounted = []
    for t, cf in enumerate(cashflows):
        pv = cf / (1 + wacc) ** (t + 1)
        discounted.append(pv)
    discounted_tv = terminal_val / (1 + wacc) ** len(cashflows)
    return discounted

def run_dcf(base_fcf, fcf_growth, terminal_growth, wacc, shares):
    projected = project_fcf(base_fcf, fcf_growth)
    tv = terminal_value(projected[-1], terminal_growth, wacc)
    discounted = discount_cashflows(projected, tv, wacc)
    discounted_tv = tv / (1 + wacc) ** 5
    enterprise_value = sum(discounted) + discounted_tv
    price_per_share = enterprise_value / shares
    return {
        "Projected FCFs": [round(x, 2) for x in projected],
        "Terminal Value": round(tv, 2),
        "Enterprise Value": round(enterprise_value, 2),
        "Price Per Share": round(price_per_share, 2)
    }
