# Risk Assessment Matrix

This document summarizes the main project risks for the used-car buyer support tool. The matrix uses a simple 1-5 scale:

* **Likelihood**: 1 = very unlikely, 5 = very likely
* **Impact**: 1 = low impact, 5 = very high impact
* **Risk score**: likelihood x impact

The goal is not to eliminate all risk, but to identify the most likely failure modes early and define practical mitigations for the MVP.

## Risk Matrix

| Category | Main risk | Likelihood (1-5) | Impact (1-5) | Risk score | Why it matters | Mitigation strategy |
|---|---|---:|---:|---:|---|---|
| Regulatory | AI Act or GDPR non-compliance if the product expands into more personal profiling, higher-risk decision support, or poorly documented data processing | 3 | 5 | 15 | This could delay launch, create legal exposure, and damage trust | Keep the MVP narrowly scoped, maintain compliance documentation, minimise personal data, review vendors, and re-assess if the product scope changes |
| Technical | Model hallucinations, omission of relevant issues, or inaccurate model/variant data | 5 | 5 | 25 | Incorrect advice can lead to bad car purchases, repair costs, and reputational damage | Use structured outputs, validation checks, human review for critical outputs, and regression testing against known models |
| Technical | Integration failures between the LLM, n8n workflow, Google Drive, Slack, or future UI/reporting components | 3 | 3 | 9 | Broken automation can interrupt the workflow and reduce user confidence | Add monitoring, retries, fallback paths, clear error handling, and remove unnecessary dependencies in the MVP |
| Ethical | Bias across brands, countries of origin, fuel types, or technologies | 3 | 5 | 15 | Biased advice can unfairly discourage good options or overstate risks for certain segments | Use balanced prompts, test across categories, review outputs manually, and document known biases and limitations |
| Ethical | Misuse of the system as a replacement for expert inspection or as an overly authoritative recommendation engine | 3 | 4 | 12 | Users may over-trust the system and make expensive decisions based on incomplete information | Make the advisory nature explicit, include confidence limits, and avoid language that suggests certainty where none exists |
| Operational | Adoption risk: buyers may prefer traditional search, and dealerships may be slow to change workflows | 3 | 3 | 9 | Low adoption reduces revenue and weakens the business case | Start with a narrow user segment, keep the interface simple, and validate value with pilot users early |
| Operational | Change management risk when the product moves from PoC to MVP and later to a production workflow | 3 | 3 | 9 | Scope creep can increase cost and slow delivery | Define release stages clearly, freeze MVP scope, maintain a change log, and separate development-only shortcuts from production design |
| Operational | Support burden from user questions, corrections, and content updates | 4 | 3 | 12 | Manual support can grow faster than expected and erode margins | Document support flows, define update responsibilities, and automate repetitive responses where possible |

## Detailed Notes

### 1. Regulatory Risks
The main regulatory risk is not the current PoC itself, but future scope creep. If the tool begins to collect more personal information, infer user preferences in detail, or influence financial or access decisions, the compliance burden will increase quickly. For that reason, the current MVP should remain focused on buyer decision support and should keep the compliance and vendor documentation up to date.

### 2. Technical Risks
Technical risk is the most immediate risk category. The most important failure modes are hallucinated issues, missing common faults, incorrect generation or variant identification, and broken integrations. Because the product is meant to help users make expensive purchase decisions, factual precision matters more than creative language. The system should therefore prefer structured outputs, explicit source references where possible, and a human review step during the pilot phase.

### 3. Ethical Risks
The biggest ethical concerns are bias and over-trust. A model can easily overgeneralize across brands, fuel types, regions, or drivetrains, and users may treat the report as more authoritative than it really is. The product should clearly state that it supports, but does not replace, human judgment and inspection. It should also be tested against a diverse set of vehicle types and market segments.

### 4. Operational Risks
Operational risk is mostly about adoption and change management. Even if the product works technically, it still has to fit into how buyers and dealerships actually search for and evaluate cars. If the workflow feels too slow or too manual, users may not return. The MVP should therefore keep the interaction lightweight, reduce unnecessary steps, and make the output easy to understand and share.

## Priority Actions

1. Keep the MVP scope narrow and well documented.
2. Add human review for the highest-impact outputs.
3. Test the system on multiple brands, fuel types, and vehicle segments.
4. Reduce reliance on development-only tools before production.
5. Monitor user feedback and update the risk matrix as the product evolves.
