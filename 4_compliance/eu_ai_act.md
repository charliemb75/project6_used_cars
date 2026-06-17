# EU AI Act Assessment

This document is a project-specific compliance analysis for the used-car buyer support tool. It is not legal advice, but it is intended to give the project a clear working classification and a compliance checklist.

## 1. Risk Classification

### Classification Result
**Provisional classification: Minimal Risk**

### Reasoning Step by Step
1. The system supports used-car buyers by generating informational reports and recommendations.
2. It does not make or automate decisions that determine access to employment, law enforcement, services such as education, credit, healthcare; or other Annex III high-risk domains.
3. It does not perform biometric identification, social scoring, manipulation, or another prohibited use case.
4. It is not a safety component of a regulated product.

In its current version, the system is a consumer decision-support tool. Because of that, the system sits outside the unacceptable-risk and high-risk categories and is best classified as minimal risk.

### When the Classification Could Change
The system should be reclassified if a future version:
* starts making automated approval / rejection decisions
* scores people for financing, insurance, or similar access decisions
* becomes part of a regulated vehicle safety function
* begins to rely on sensitive personal-data profiling at scale

## 2. If the System Were High-Risk

If the product were later reclassified as high-risk, the main mandatory obligations would include:

* **Data governance**: training, validation, and testing data must be relevant, representative, sufficiently complete, and properly managed.
* **Human oversight**: a human must be able to monitor, understand, and intervene when needed.
* **Transparency**: users must receive clear information about the system, its purpose, limitations, and expected use.
* **Accuracy**: the system should achieve an appropriate level of accuracy and should be tested for known failure modes.
* **Robustness**: the system should be resilient to errors, misuse, and reasonably foreseeable attacks.
* **Logging and traceability**: key events and outputs should be recordable so the system can be audited.
* **Risk management**: the provider should maintain a lifecycle risk-management process.
* **Conformity assessment**: the system would need a formal assessment before being placed on the market or put into service.

## 3. Conformity Assessment Summary

### What the System Does
The system asks the user for vehicle details, retrieves or generates structured used-car knowledge, and produces a buyer-oriented report about model generations, variants, maintenance concerns, and practical buying guidance.

### Risk Class
**Minimal risk**

### Obligations That Apply
For the current MVP, no high-risk conformity assessment is required.

The project should still apply good practice obligations:
* provide clear user-facing transparency about what the system does
* keep a human review step for important outputs during the pilot phase
* monitor hallucinations, bias, and factual drift
* keep records of inputs and outputs so the team can debug issues

### Obligations That Would Apply If Reclassified as High-Risk
* data governance and dataset controls
* documented risk management
* human oversight controls
* transparency notices
* accuracy, robustness, and cybersecurity testing
* quality management and post-market monitoring
* formal conformity assessment and technical documentation

## 4. Technical Documentation Outline

### 1. System Overview
* product name and purpose
* intended users
* intended use and prohibited use
* operating environment

### 2. Risk Classification
* classification conclusion
* reasoning and boundary cases
* triggers for future reclassification

### 3. System Architecture
* workflow diagram
* model providers and services used
* prompts, rules, and retrieval logic
* human review points

### 4. Data and Knowledge Sources
* source types
* update process
* validation process
* known data gaps and limitations

### 5. Training, Prompting, and Evaluation
* model configuration
* prompt templates
* evaluation tests
* regression testing approach

### 6. Accuracy, Robustness, and Safety
* known failure modes
* hallucination controls
* fallback behavior
* abuse / misuse considerations

### 7. Human Oversight
* review workflow
* escalation rules
* override and correction process

### 8. Logging and Traceability
* what is logged
* retention periods
* access control
* audit trail

### 9. User Transparency
* disclosure text
* limitations
* source references
* confidence/warning indicators

### 10. Incident Handling
* issue reporting
* correction workflow
* severity definitions
* post-incident review

### 11. Deployment and Monitoring
* release process
* monitoring metrics
* update cadence
* rollback plan

### 12. Compliance Appendices
* supplier list
* legal and contractual notes
* policy references
* review approvals
