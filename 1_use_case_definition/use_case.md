# Use Case Definition

**This project is an AI-powered decision support tool for used-car buyers. It helps users evaluate a vehicle before purchase, understand the main risks, and ask the right questions to the seller.**

## Business Problem
The business problem is that used-car buyers face a high-risk, information-heavy purchase with limited expert support. Most buyers do not have enough technical knowledge to assess a listing properly, compare model-year risks, or ask the right questions before buying. This creates a gap between buyer confidence and the actual complexity of the market, which can lead to bad purchases, unexpected repair costs, and low trust in the buying process.

## Proposed AI-Powered Solution
The proposed solution is an AI assistant that generates structured used-car purchase reports for a specific model, covering:

**PoC**
* Typical maintenance needs and common failure points
* Known reliability concerns and how to estimate whether they are likely to affect the specific vehicle
* Features, model years, trims, and equipment to prefer or avoid

**Expansion**
* Comparison of a concrete listing against the known model risks and strengths
* Practical questions to ask the seller before buying
* Checklist generation for in-person inspection or test drive

The tool supports, but does not replace, the buyer's final decision.

## Key Stakeholders
The main target users are:
* Private buyers who want affordable, trustworthy guidance before making a one-off purchase 
* Dealerships that want to minimize the risk in their purchases and have a repeatable advisory tool for sales staff or customer support
* The product development team, who need the system to be reliable, explainable, and scalable
* Data providers and source owners, whose information quality directly affects the output. The current PoC is purely LLM-based, but verified knowledge could be added via RAG in the future.

## Success Criteria
This works if the tool consistently helps users make safer and more confident buying decisions. In practice, success would look like:
* Users receive clear, structured, and explainable reports for a specific car model
* The output highlights realistic risks, relevant maintenance concerns, and useful questions for the seller
* Users feel more confident comparing vehicles and narrowing down their options
* The system avoids obvious hallucinations and keeps a transparent relationship with its sources
* It should include confidence levels or clear warnings when the data is incomplete
* Human feedback (given by market experts, pilot users or early testers) considers the advice as useful enough to rely on during the buying process

## Introduction to the conducted research
The data used for this analysis includes:
* Used-car market structure and transaction volumes
* Reliability and aftersales claim statistics
* Vehicle availability by age and mileage
* Depreciation trends
* Emissions rules and low-emission-zone restrictions that affect vehicle usability

Why this use case is timely:
* Low Emission Zones are forcing vehicle replacement in many European cities
* A large share of buyers still lacks confidence in car knowledge and buying processes
* The market is fragmented, making expert-style guidance valuable and difficult to scale manually
* AI can make personalized purchase support much cheaper than traditional inspection or advisory services