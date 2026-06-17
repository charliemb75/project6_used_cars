# GDPR Assessment

This document is a project-specific privacy analysis for the used-car buyer support tool. It is not legal advice, but it maps the current proof of concept to the main GDPR obligations that apply.

## 1. Personal Data Processed

### Current PoC Inputs
The current proof of concept solely asks for the following vehicle information:
* make
* model
* generation
* version description

Although these fields are not personal data by themselves, the vehicle a person currently drives, or the one they are considering purchasing, is tightly linked to their economic situation, preferences, and household needs. Therefore, they can become personal data if a user adds identifying information in free text or if the form is later linked to an account, email address, phone number, IP address, or other identifier.


### Current PoC Outputs
The generated reports mostly contain car-related technical information. They become personal data only if the user has embedded identifying information in the request or if the report is later linked to an identifiable account.

### Logs and Operational Metadata
The system may also process:
* timestamps
* execution identifiers
* file names generated from form submissions
* workflow logs
* Slack message metadata
* Google Drive file metadata
* API request / response metadata from third-party services

### Highest-Risk Data and Future Recommendation Inputs
The highest-risk processing would occur if future versions of the current system store or infer:
* user identity details
* contact (at least log-in) details
* location data
* linked usage history across multiple sessions
* free-text messages that innecesarily contain personal circumstances

A possible future feature of the tool could recommend a specific car model according to the user's needs. That would increase the privacy impact because the system would no longer process only vehicle details, but could potentially include the following information tied to a named person.
* personal preferences (makes, countries of origin, vehicle age, required equipment...)
* current vehicle and reason to change
* budget
* age
* family size
* intended use (personal, heavy-duty work, business)
* whether the user needs to transport children or elderly people
* whether the user needs to transport large objects
    * work or sports equipment
    * frequent travel with abundant luggage
    * baby stroller, chair...
    * health-related: wheelchair, walker...
* expected daily or yearly mileage
* most frequent kind of roads
* need for off-road capabilities

In that case, the project would need a stronger minimisation approach, clearer retention rules, and a renewed legal-basis review for each field collected.

## 2. Legal Basis for Each Processing Activity

### A. Generating the requested report
**Legal basis: Article 6(1)(b) GDPR - performance of a contract or pre-contractual steps**

If a user asks the system to generate a report, processing the request is necessary to deliver the service.

### B. Storing workflow logs for debugging and security
**Legal basis: Article 6(1)(f) GDPR - legitimate interests**

The project has a legitimate interest in security, fraud prevention, debugging, reliability, and service improvement.

### C. Transferring data to third-party service providers
**Legal basis: Article 6(1)(b) GDPR and Article 6(1)(f) GDPR**

Third-party services are used to run the service technically and to deliver the report output. Any optional or non-essential sharing should be minimised.

### D. Optional analytics, product improvement, or manual quality review
**Legal basis: Article 6(1)(f) GDPR - legitimate interests**

This should be limited to what is necessary for quality control and product improvement.

### E. Marketing or newsletter activity, if introduced later
**Legal basis: Article 6(1)(a) GDPR - consent**

Marketing should be opt-in and separate from the core report service.

## 3. Short DPIA

### Highest-Risk Processing Activity
The highest-risk processing activity is the storage and transfer of user-submitted request data and logs through multiple third-party services, especially if users add free-text information or if the system becomes linked to identifiable accounts.

### Why This Activity Is Sensitive
* the system may collect more information than is strictly needed for the car report
* logs can create hidden retention of personal data
* third-party providers may process data outside the immediate project environment
* future versions could link preferences, budgets, and buying intent to named users

### Risks
* unintended retention of personal data
* over-sharing with third-party processors
* accidental inclusion of sensitive details in prompts or logs
* inability to satisfy deletion or access requests across all systems
* cross-border transfer risk if providers process data outside the EEA

### Mitigations
* collect only the minimum data needed for the report
* avoid asking for names, emails, or phone numbers unless required
* redact or block sensitive free-text content where possible
* keep retention periods short and documented
* sign data-processing agreements with vendors
* restrict access to logs and report archives
* use EU data regions where available
* document deletion workflows across all processors

### Residual Risk
Residual risk should be moderate and manageable for the current PoC, provided the project remains narrowly scoped and does not begin to profile or track users extensively.

## 4. Data Subject Rights

The following rights apply when the system processes personal data:

* **Access**: users can request a copy of their data and an explanation of how it is processed.
* **Erasure**: users can request deletion where no legal reason requires retention.
* **Portability**: users can request a structured export of the data they provided.
* **Objection**: users can object to processing based on legitimate interests.

### How the System Should Support These Rights
* keep records searchable by user identifier, if one exists
* maintain a deletion workflow for logs, reports, and archived files
* provide an export format for user-provided content
* document the retention period for each data category
* explain which processing steps rely on legitimate interests
* route rights requests to a clearly identified contact point

## 5. Third-Party Data Transfers

The current workflow may transfer data to the following third-party services:

* **OpenAI API** for generation of text outputs
* **Google Drive** for storing generated report files
* **Slack** for operational notifications
* **n8n infrastructure / hosting provider** if the workflow is hosted outside the local machine

The current PoC uses Google Drive and Slack for development purposes. A further development into an MVP would replace those with downloadable reports, likely in PDF format, and notifications within the UI.

### Transfer Considerations
* data minimisation should apply before sending anything to third parties
* contracts with processors should be in place where applicable
* the project should verify where data is stored and processed
* if data is transferred outside the EEA, appropriate transfer safeguards should be documented
* vendor retention and deletion behavior should be checked and recorded

## 6. Privacy-by-Design Actions

* keep the current form small
* avoid collecting identity data by default
* separate report content from operational logs
* redact free-text fields where possible
* define retention periods for reports and logs
* prepare a rights-request workflow before launch
* review each vendor before production use

## 7. Compliance Summary

Current assessment:
* the project processes little personal data in the current PoC
* the main privacy risk comes from logs, free text, and third-party processing
* the system can be operated in a GDPR-aligned way if it keeps data minimised and its retention, transfer, and deletion rules documented
