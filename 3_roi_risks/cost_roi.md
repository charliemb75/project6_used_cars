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

## Indicative Price Per Report

Based on the research, the tool should be priced well below human inspection-style services, which are often around 300 EUR per vehicle, while still leaving room to cover AI usage, support, and product maintenance.

The suggestion is a hybrid pricing model:
* **Occasional/private users:** 14.99-29.99 EUR per report, or 4.99-9.99 EUR per report if the report page includes advertising or sponsored placements
* **Dealerships:** 4.99-12.99 EUR per report at volume, or a monthly subscription for frequent use, at around 99.99 EUR
* Premium reports with deeper listing comparison or more detailed model coverage could be priced above this range

As a starting point, 19.99 EUR per report is a reasonable MVP price for private users without ads, because it is low enough to feel accessible but high enough to signal value and support operating costs.

## Quantified Business Value

The business value should be estimated in three parts:
* **Time saved** from replacing manual car research and comparison
* **Revenue gained** from report sales and subscriptions
* **Cost avoided** from reducing bad recommendations, duplicated research, and outsourced advisory work

The following scenario assumptions are intentionally simple and conservative:
* Average time saved per report: 30 minutes
* Imputed value of time: 20 EUR / hour
* Effective private report revenue: 15 EUR per report
* Dealership subscription revenue: 150 EUR per dealership per month at the 12-month horizon, increasing with adoption and account depth by 36 months
* Cost avoided: scales with support load, repeated research, and advisory effort as the product matures

| Value stream | Conservative 12m | Conservative 36m | Realistic 12m | Realistic 36m | Optimistic 12m | Optimistic 36m |
|---|---:|---:|---:|---:|---:|---:|
| Time saved | 200 EUR / month | 600 EUR / month | 1,000 EUR / month | 4,000 EUR / month | 3,000 EUR / month | 12,000 EUR / month |
| Revenue gained | 450 EUR / month | 1,500 EUR / month | 2,250 EUR / month | 8,700 EUR / month | 6,750 EUR / month | 25,500 EUR / month |
| Cost avoided | 100 EUR / month | 250 EUR / month | 400 EUR / month | 900 EUR / month | 1,000 EUR / month | 3,000 EUR / month |
| **Total business value** | **750 EUR / month** | **2,350 EUR / month** | **3,650 EUR / month** | **13,600 EUR / month** | **10,750 EUR / month** | **40,500 EUR / month** |

Annualized, this corresponds to:
* Conservative: 9,000 EUR / year at 12 months, 28,200 EUR / year at 36 months
* Realistic: 43,800 EUR / year at 12 months, 163,200 EUR / year at 36 months
* Optimistic: 129,000 EUR / year at 12 months, 486,000 EUR / year at 36 months

## ROI Calculation

Simple ROI is calculated as:

`ROI = (Total Value - Total Cost) / Total Cost`

The table below uses the monthly run-rates above and annualizes them over each horizon.

| Scenario | 12-month cost | 12-month value | 12-month ROI | 36-month cost | 36-month value | 36-month ROI |
|---|---:|---:|---:|---:|---:|---:|
| Conservative | 82,800 EUR | 9,000 EUR | -89.1% | 153,600 EUR | 84,600 EUR | -44.9% |
| Realistic | 69,600 EUR | 43,800 EUR | -37.1% | 208,800 EUR | 489,600 EUR | 134.5% |
| Optimistic | 76,000 EUR | 129,000 EUR | 69.7% | 338,800 EUR | 1,458,000 EUR | 330.3% |

## Possible Next Steps

1. Validate the highest-value target segment: private buyers, dealerships, or both.
2. Build a small prototype, test the output with real listings and compare recommendations against expert judgment.
3. Estimate monetization more precisely, especially subscription pricing for dealerships and per-report pricing for private users.
4. If the prototype performs well, prepare a pilot with a limited user group and measure conversion, usage, and trust.
