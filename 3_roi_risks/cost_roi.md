# ROI Estimation

Overall, the research suggests a strong opportunity for an AI assistant that helps used-car buyers compare listings, understand risks, and ask the right questions before purchase. The combination of market scale, buyer uncertainty, rising emissions pressure, and the lack of personalized buyer-side tools makes this a timely use case.

It is recommended to build this tool as an MVP first, because the market signal is strong, the use case is clear, and the initial scope can be kept focused.

## Assumptions

* The tool generates decision support, **not a legally binding** inspection or guarantee.
* The estimate is based on a **Germany-first, EU-facing used-car buyer market**.
* The first release is English-only.
* The product is assumed to start as an **MVP** operated by a **small startup-style team**, with some **outsourced or freelance support**.
* The first release is assumed to be **English-only**.
* Hosting, logging, and storage are assumed to be **GDPR-compliant** and located in an **EU region**.
* The customer base is assumed to consist of **private buyers** and **dealerships**, with gradual adoption over time rather than immediate mass-market scale.
* The ROI scenarios are directional planning estimates, not a financial forecast.

## Demand Evolution

The cost and revenue estimates below are based on an assumed adoption curve for two customer groups:
* **Private customers**, who are likely to use the tool for one-off purchase decisions
* **Dealerships**, who can use it repeatedly and therefore generate recurring demand

Demand is expected to start modestly and then grow as the product gains trust, more model coverage, and repeat usage in dealership workflows.

| Scenario | Private reports / month at 12 months | Active dealerships at 12 months | Private reports / month at 36 months | Active dealerships at 36 months |
|---|---:|---:|---:|---:|
| Conservative | 20 | 1 | 60 | 4 |
| Realistic | 100 | 5 | 400 | 18 |
| Optimistic | 300 | 15 | 1,200 | 50 |

How this feeds the business case:
* Private demand drives most of the one-off revenue.
* Dealership adoption drives recurring subscription revenue and support effort.
* Higher report volume also increases API usage and validation workload, so it affects ongoing costs as well as revenue.
* The 36-month scenario assumes stronger repeat usage, wider model coverage, and higher dealership penetration than the 12-month baseline.
* The cost and value tables below are expressed as monthly run-rates at the 12-month and 36-month horizon, and the ROI table annualizes them to the relevant horizon.

## Cost Estimate

### Upfront Costs

| Cost item | Conservative | Realistic | Optimistic |
|---|---:|---:|---:|
| Product discovery and planning | 4,000 EUR | 3,000 EUR | 2,000 EUR |
| Data acquisition and preparation | 10,000 EUR | 6,000 EUR | 3,000 EUR |
| Development | 28,000 EUR | 18,000 EUR | 10,000 EUR |
| Testing and validation | 8,000 EUR | 5,000 EUR | 3,000 EUR |
| Licences and tools setup | 5,000 EUR | 2,000 EUR | 2,000 EUR |
| Training and expert review | 2,000 EUR | 1,000 EUR | 1,000 EUR |
| Infrastructure setup | 3,000 EUR | 1,000 EUR | 1,000 EUR |
| **Total upfront** | **60,000 EUR** | **36,000 EUR** | **22,000 EUR** |

### Ongoing Costs

| Cost item | Conservative 12m | Conservative 36m | Realistic 12m | Realistic 36m | Optimistic 12m | Optimistic 36m |
|---|---:|---:|---:|---:|---:|---:|
| Hosting and operations | 600 EUR / month | 800 EUR / month | 700 EUR / month | 1,200 EUR / month | 1,000 EUR / month | 1,800 EUR / month |
| Maintenance and content updates | 800 EUR / month | 1,100 EUR / month | 1,100 EUR / month | 1,900 EUR / month | 1,800 EUR / month | 3,500 EUR / month |
| API fees | 400 EUR / month | 500 EUR / month | 700 EUR / month | 1,200 EUR / month | 1,200 EUR / month | 2,300 EUR / month |
| Customer support and admin | 100 EUR / month | 200 EUR / month | 300 EUR / month | 500 EUR / month | 500 EUR / month | 1,200 EUR / month |
| **Total ongoing** | **1,900 EUR / month** | **2,600 EUR / month** | **2,800 EUR / month** | **4,800 EUR / month** | **4,500 EUR / month** | **8,800 EUR / month** |

For a more polished commercial version with stronger automation, broader model coverage, and continuous content maintenance, both upfront and ongoing costs would be higher than these MVP-level numbers.

## Business Value for Customers

The customer value should be estimated in two parts:
* **Time saved** from replacing manual car research and comparison
* **Cost avoided** from reducing bad recommendations, duplicated research, and outsourced advisory work

The following scenario assumptions are intentionally simple and conservative:
* Average time saved per report: 30 minutes
* Imputed value of time: 20 EUR / hour
* Cost avoided: scales with support load, repeated research, and advisory effort as the product matures

| Value stream | Conservative 12m | Conservative 36m | Realistic 12m | Realistic 36m | Optimistic 12m | Optimistic 36m |
|---|---:|---:|---:|---:|---:|---:|
| Time saved | 200 EUR / month | 600 EUR / month | 1,000 EUR / month | 4,000 EUR / month | 3,000 EUR / month | 12,000 EUR / month |
| Cost avoided | 100 EUR / month | 250 EUR / month | 400 EUR / month | 900 EUR / month | 1,000 EUR / month | 3,000 EUR / month |
| **Total customer value** | **300 EUR / month** | **850 EUR / month** | **1,400 EUR / month** | **4,900 EUR / month** | **4,000 EUR / month** | **15,000 EUR / month** |

Annualized customer value:
* Conservative: 3,600 EUR / year at 12 months, 10,200 EUR / year at 36 months
* Realistic: 16,800 EUR / year at 12 months, 58,800 EUR / year at 36 months
* Optimistic: 48,000 EUR / year at 12 months, 180,000 EUR / year at 36 months

## Price Per Report

Based on the research, the tool should be priced well below human inspection-style services, which are often around 300 EUR per vehicle, while still leaving room to cover AI usage, support, and product maintenance. It should be low enough to feel accessible but high enough to signal value and support operating costs.

The suggestion is a hybrid pricing model:
* **Occasional/private users:** 15-30 EUR per report, or 5-10 EUR per report if the report page includes advertising or sponsored placements
* **Dealerships:** 5-15 EUR per report at volume, or a monthly subscription for frequent use, at around 100 EUR
* Premium reports with deeper listing comparison or more detailed model coverage could be priced above this range

For the revenue model below, the initial estimation uses round numbers and a baseline private report price of **15 EUR per report**. The monthly dealership fee remains **100 EUR**, because a recurring subscription is easier to justify for frequent use than per-report billing.

This pricing is plausible because:
* the report can save time and reduce the chance of a bad purchase decision
* even a small reduction in search effort or repair risk can justify a price above a basic consumer subscription
* dealership users are likely to generate repeated value, so a monthly fee remains well below the potential benefit

## Developer Revenue

Developer revenue should be estimated from the demand forecast and the chosen price points, not from the customer value table.

The revenue assumptions are:
* Private report price: 15 EUR
* Dealership subscription price: 100 EUR per month

To follow the demand curve above, revenue is calculated as a gradual ramp:
* **12-month revenue** assumes a linear ramp from zero to the 12-month demand level across the first 12 months.
* **36-month revenue** assumes a linear ramp from zero to the 12-month demand level across months 1-12, and then a linear ramp from the 12-month level to the 36-month level across months 13-36.

| Revenue stream | Conservative 12m | Conservative 36m | Realistic 12m | Realistic 36m | Optimistic 12m | Optimistic 36m |
|---|---:|---:|---:|---:|---:|---:|
| Private report revenue | 1,800.00 EUR | 16,200.00 EUR | 9,000.00 EUR | 99,000.00 EUR | 27,000.00 EUR | 297,000.00 EUR |
| Dealership subscription revenue | 600.00 EUR | 6,600.00 EUR | 3,000.00 EUR | 30,600.00 EUR | 9,000.00 EUR | 87,000.00 EUR |
| **Total developer revenue** | **2,400.00 EUR** | **22,800.00 EUR** | **12,000.00 EUR** | **129,600.00 EUR** | **36,000.00 EUR** | **384,000.00 EUR** |

## ROI Calculation

Simple ROI is calculated as:

`ROI = (Total Revenue - Total Cost) / Total Cost`

The table below uses the developer revenue estimates above and the cost estimates in this document.

| Scenario | 12-month cost | 12-month revenue | 12-month ROI | 36-month cost | 36-month revenue | 36-month ROI |
|---|---:|---:|---:|---:|---:|---:|
| Conservative | 71,400 EUR | 2,400.00 EUR | -96.6% | 125,400 EUR | 22,800.00 EUR | -81.8% |
| Realistic | 52,800 EUR | 12,000.00 EUR | -77.3% | 144,000 EUR | 129,600.00 EUR | -10.0% |
| Optimistic | 49,000 EUR | 36,000.00 EUR | -26.5% | 208,600 EUR | 384,000.00 EUR | 84.1% |

## Possible Next Steps

1. Validate the highest-value target segment: private buyers, dealerships, or both.
2. Build a small prototype, test the output with real listings and compare recommendations against expert judgment.
3. Estimate monetization more precisely, especially subscription pricing for dealerships and per-report pricing for private users.
4. If the prototype performs well, prepare a pilot with a limited user group and measure conversion, usage, and trust.
