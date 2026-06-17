## Implementation Steps And Timeline

| Step | Main activities | Duration |
|---|---|---:|
| 1. Scope and data definition | Confirm MVP features, define target users, identify required datasets, and choose the first supported car segments or markets. | 1 week |
| 2. Data collection and normalization | Gather used-car market data, depreciation data, reliability data, emissions rules, and model-specific vehicle information. Clean and structure the data. | 2-3 weeks |
| 3. Knowledge base and rules engine | Build the logic that turns model data into recommendations, red flags, and questions to ask the seller. | 2 weeks |
| 4. AI report generation | Connect the structured data with the LLM layer so it can produce clear, personalized purchase reports. | 2 weeks |
| 5. Frontend and user flow | Create a simple interface for car search, report generation, and report comparison against listings. | 2 weeks |
| 6. Testing and validation | Check accuracy, reduce hallucinations, test with real listings, and validate the output with car experts or experienced buyers. | 1-2 weeks |
| 7. Pilot launch | Release a limited beta to a small group of users or dealerships and collect feedback for iteration. | 1 week |

Total estimated MVP timeline: 9-13 weeks.

## Deployment Phases

### Phase 1: Proof of Concept
**Goal:** Prove that the workflow can generate useful buyer-support output for a limited set of car models.

**Timeframe:** Weeks 1-4

**Key milestones**
* Define the first supported market and vehicle scope
* Validate generation, variant, and report creation workflow
* Test the basic LLM prompt structure and output format
* Confirm that the current PoC can produce usable outputs end to end

**Success criteria**
* The workflow runs without manual reconstruction
* The generated output is understandable and relevant
* The team can identify the main data and logic gaps

### Phase 2: Pilot
**Goal:** Test the product with a small real user group and validate quality, trust, and usability.

**Timeframe:** Weeks 5-13

**Key milestones**
* Add a usable interface for selecting vehicle details and generating reports
* Replace development shortcuts with more stable user-facing flows
* Test with a small group of private buyers or dealerships
* Collect feedback on accuracy, usefulness, and clarity
* Introduce lightweight monitoring and a human review step for high-impact outputs

**Success criteria**
* Users complete the flow without major assistance
* Reports are judged useful by pilot users
* Major hallucinations and obvious errors are reduced
* The team understands which customer segment is most promising

### Phase 3: Full Deployment
**Goal:** Move from a pilot product to a repeatable commercial service.

**Timeframe:** Months 4-12

**Key milestones**
* Replace the PoC-style workflow with a production-ready architecture
* Introduce downloadable reports, likely PDF-based
* Add in-UI notifications and clearer report history
* Expand market and model coverage
* Formalize vendor management, privacy, support, and release processes

**Success criteria**
* The product supports recurring usage without manual firefighting
* Revenue is predictable enough to support the operating model
* The system is stable, monitored, and compliant with internal policy
* Users return and recommend the tool to others

## Stakeholder Communication

### Executives
Executives need to hear:
* the business problem and target market
* the expected ROI path and adoption assumptions
* the main risks, especially regulatory and technical ones
* whether the product should be positioned as a standalone business or as a feature inside a larger offering

### Legal
Legal needs to hear:
* how the product classifies under the EU AI Act
* what personal data is processed under GDPR
* which vendors are involved and where data is transferred
* what retention, deletion, and consent rules are planned
* when the scope changes enough to require a fresh review

### IT / Engineering
IT needs to hear:
* the target architecture for the PoC, pilot, and production phases
* integration points with LLMs, storage, and notification tools
* reliability, logging, and monitoring requirements
* the plan for handling errors, retries, and future scalability

### End-Users
End-users need to hear:
* what the tool does and does not do
* that it supports, but does not replace, human judgment
* how the report is generated and what its limits are
* how to interpret warnings, confidence levels, and source notes

## Success Metrics

### PoC Metrics
* end-to-end workflow completion rate
* internal user satisfaction with the generated output
* number of major factual errors found in testing
* time required to generate a usable report

### Pilot Metrics
* pilot user completion rate
* report usefulness score from users
* number of corrections needed per report
* number of users who return for a second report
* average support effort per user

### Full Deployment Metrics
* monthly active users
* conversion rate from visitor to report purchase or subscription
* average revenue per user
* churn or repeat usage rate
* number of escalated issues or complaints
* compliance incidents or data-handling exceptions

## Commercialisation Model

The most plausible commercialisation model is a **hybrid model**:

* **SaaS subscription for dealerships**: recurring monthly pricing for frequent use, team access, and workflow integration.
* **Per-report pricing for private buyers**: one-off purchase of a report for occasional users.
* **Consulting or setup support**: optional paid support for dealerships that want onboarding, workflow adaptation, or custom scope.

This model fits the product because:
* private buyers want low-friction, one-time value
* dealerships need repeatable usage and predictable billing
* the core capability can be offered as software, while expert support remains an optional upsell

### Recommended Rollout
* **PoC:** internal tool and learning phase
* **Pilot:** limited access, manual review, feedback-driven improvement
* **Full deployment:** SaaS plus per-report sales, with optional consulting support for larger customers

### Commercial Positioning
The product should be positioned as:
* a buyer decision-support tool
* a paid alternative to ad hoc manual research
* a lighter and cheaper complement to human inspection services

It should not be positioned as:
* a legal guarantee
* a formal vehicle inspection replacement
* a fully automated replacement for expert judgment
