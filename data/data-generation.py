from faker import Faker
import random
import pandas as pd

# Initialize Faker
fake = Faker()

# Define categories and example templates
categories = {
    "HR": [
        {
            "request": "I’m looking for some information regarding {topic}. Could you provide the necessary details when you get a chance?"
        },
        {
            "request": "I’d like to request assistance with {topic}. Let me know if there’s anything else you need from me to proceed."
        },
        {
            "request": "I wanted to check on the status of my request regarding {topic}. Please let me know if further information is needed."
        },
        {
            "request": "I have a question about {topic}. Could you clarify the process or let me know where I can find more information?"
        },
        {
            "request": "Could you provide an update on the {topic} request I submitted earlier? Let me know if I should take any action."
        },
        {
            "request": "I’m gathering details about {topic} and was hoping you could provide some insight. Let me know if you need further specifics from me."
        },
        {
            "request": "I need your guidance on handling {topic}. Please share the necessary steps or resources to proceed."
        },
    {
        "request": "Can you confirm the steps for handling {topic}? I want to ensure I’m following the correct procedure."
    },
    {
        "request": "What’s the latest update on the {topic}? I need it for my report."
    },
    {
        "request": "I’m confused about the {topic} policy. Can someone clarify it for me?"
    },
    {
        "request": "Please send me the information about {topic} as soon as possible."
    },
    {
        "request": "Where can I find the document related to {topic}? I’ve looked but can’t locate it."
    },
    {
        "request": "What’s the deadline for submitting {topic} forms? I don’t want to miss it."
    },
    {
        "request": "Do you have the latest version of the {topic} handbook? I need it for a new hire orientation."
    },
    {
        "request": "Can you clarify the process for requesting {topic}? I need this done today."
    },
        {
        "request": "Need details about {topic}."
    },
    {
        "request": "Update on {topic} request?"
    },
    ],


    "Finance": [
        {
            "request": "I noticed a discrepancy in the {topic} report. Could you review it and confirm the accuracy?"
        },
        {
            "request": "Could you review and approve the {topic} for this month? Let me know if there’s anything I need to address."
        },
        {
            "request": "I need help with {topic}. Please let me know the steps to resolve this issue."
        },
        {
            "request": "This is a time-sensitive matter related to {topic}. Please prioritize this and let me know if you require additional information."
        },
        {
            "request": "I’m following up on the approval status for {topic}. Please let me know if it’s been processed or if further steps are required."
        },
        {
            "request": "Could you clarify the details about {topic}? I want to ensure I’m proceeding correctly."
        },
        {
            "request": "I’m dealing with a challenge regarding {topic}. Could you provide guidance on resolving this issue?"
        },
    {
        "request": "I need assistance with {topic}. Could you outline the steps I should take to resolve this issue?"
    },
    {
        "request": "This is a time-sensitive matter related to {topic}. Please prioritize this and let me know if you require any additional input from my side."
    },
    {
        "request": "I’m following up on the approval status for {topic}. Could you confirm if it’s been processed or if further steps are required from me?"
    },
    {
        "request": "Could you clarify the process for {topic}? I want to ensure all the necessary details are accurate before proceeding."
    },
    {
        "request": "I’m dealing with a challenge regarding {topic}. Could you provide specific guidance or share any relevant resources to help resolve it?"
    },
    {
        "request": "What’s the timeline for resolving the {topic} issue? Please share an update so I can plan accordingly."
    },
    {
        "request": "I need to ensure compliance with the guidelines for {topic}. Could you provide a detailed breakdown of the requirements?"
    },
    {
        "request": "Could you provide a summary of the {topic} report? I need it for a presentation this week."
    },
    {
        "request": "Can you confirm the reimbursement amount for {topic}? I want to verify it aligns with the submitted documents."
    },
    {
        "request": "Could you provide a detailed explanation of how the {topic} was calculated? I want to double-check the figures."
    },
    {
        "request": "I’m preparing the budget for next quarter and need data on {topic}. Could you share this information by end of day?"
    },
    {
        "request": "What’s the status of the payment for {topic}? I need this cleared before the vendor’s deadline."
    },
    {
        "request": "I’m unable to access the system to update {topic}. Could you assist in resolving this issue so I can proceed?"
    },
    {
        "request": "Can you confirm the timeline for fixing {topic}? This is time-sensitive."
    },
        {
        "request": "Discrepancy in {topic}. Fix it."
    },
    {
        "request": "Need approval for {topic}. Required as soon as possible."
    },
    {
        "request": "Check {topic} and update me."
    },
    ],
    "IT Support": [
        {
            "request": "I need access to {topic} to complete my tasks. Please let me know how to proceed."
        },
        {
            "request": "I’m experiencing a problem with {topic}. Can you assist in resolving this issue?"
        },
        {
            "request": "I need assistance with {topic}. Please let me know the steps to address this issue."
        },
        {
            "request": "I’m unable to access {topic}. Could you help troubleshoot this issue at your earliest convenience?"
        },
        {
            "request": "I wanted to check on the status of my request for access to {topic}. Let me know if further details are needed."
        },
        {
            "request": "Could you explain the setup process for {topic}? I want to ensure it’s configured correctly."
        },
        {
            "request": "I’m currently facing a challenge with {topic}. Please share the best way to resolve this."
        },
            {
        "request": "I need access to {topic} to complete my tasks. Could you guide me on how to proceed and what steps are required?"
    },
    {
        "request": "I’m experiencing an issue with {topic}. Can you assist in diagnosing and resolving the problem as soon as possible?"
    },
    {
        "request": "I require assistance with {topic}. Could you provide detailed steps or resources to address this effectively?"
    },
    {
        "request": "I’m unable to access {topic}. Could you troubleshoot this and let me know once the issue is resolved?"
    },
    {
        "request": "Could you update me on the current status of my access request for {topic}? Let me know if you need any additional details."
    },
    {
        "request": "I need clarification on the setup process for {topic}. Could you provide a step-by-step explanation to ensure it’s configured correctly?"
    },
    {
        "request": "I’m encountering a challenge with {topic}. Could you share the best way to resolve this, or connect me with someone who can assist?"
    },
    {
        "request": "Could you confirm if {topic} has been updated or maintained recently? I need this information to ensure system stability."
    },
    {
        "request": "I’m noticing inconsistent behavior with {topic}. Could you investigate and provide a resolution or workaround?"
    },
    {
        "request": "I need help troubleshooting {topic}. It’s affecting my ability to complete essential tasks on time."
    },
    {
        "request": "Can you verify the permissions for {topic}? I’m unable to access certain features that should be available."
    },
    {
        "request": "Could you guide me through the process of resetting {topic}? I want to ensure I follow the correct procedure."
    },
    {
        "request": "I suspect there may be a security issue with {topic}. Could you investigate this and let me know the findings?"
    },
    {
        "request": "I need support deploying {topic} for my team. Could you help set this up or provide the necessary tools?"
    },
    {
        "request": "What’s the estimated resolution time for the {topic} issue I reported? Please keep me updated if there are delays."
    },
        {
        "request": "Need access to {topic}."
    },
    {
        "request": "Fix {topic} problem."
    },
    {
        "request": "What’s going on with {topic}? Update me."
    },
    {
        "request": "{topic} access?"
    },
    ],
    "Marketing": [
        {
            "request": "I have some ideas for the {topic} campaign. Let me know when we can discuss them."
        },
        {
            "request": "Could you provide feedback on the {topic} project? I’d like to finalize it this week."
        },
        {
            "request": "Could you analyze the data related to {topic}? Let me know the findings so we can proceed."
        },
        {
            "request": "Could you draft a proposal for {topic}? Please share it by the end of the week."
        },
        {
            "request": "Can you provide an update on the results for {topic}? Let me know if you need further input."
        },
        {
            "request": "Could you share insights on the performance of {topic}? This will help guide our next steps."
        },
        {
            "request": "I need help with managing {topic}. Please provide your recommendations or feedback."
        },
            {
        "request": "I have some creative ideas for the {topic} campaign. Could we schedule a brainstorming session to discuss them?"
    },
    {
        "request": "Could you provide detailed feedback on the {topic} project? I need to address any changes before finalizing it this week."
    },
    {
        "request": "Can you analyze the data related to {topic} and summarize the key takeaways? This will help inform our next steps."
    },
    {
        "request": "Could you draft a comprehensive proposal for {topic}? Please include timelines and share it by the end of the week."
    },
    {
        "request": "Can you provide an update on the progress and results of the {topic} initiative? Let me know if there are any blockers."
    },
    {
        "request": "Could you share detailed insights on the performance metrics for {topic}? I’d like to use this data for our planning."
    },
    {
        "request": "I’m seeking your recommendations on managing {topic}. Please provide any strategies or resources you think would be effective."
    },
    {
        "request": "Could you create a brief for the {topic} strategy? I need a clear direction for execution."
    },
    {
        "request": "Can you prepare a performance report for {topic}? Let me know if you require additional inputs from my end."
    },
    {
        "request": "Could you outline the steps to optimize our {topic} approach? Any case studies or examples would be helpful."
    },
        {
        "request": "Insights on {topic} performance needed."
    },
    {
        "request": "Draft proposal for {topic}."
    },
    {
        "request": "Please send over recent {topic}. I need this as soon as possible."
    },
    {
        "request": "Feedback on {topic}?"
    },
    {
        "request": "Help with {topic} plan."
    },
    {
        "request": "Status on {topic} results?"
    }
    ],
    # Facilities Management Templates
"Facilities Management": [
    {
        "request": "I’d like to request maintenance for {topic}. Please let me know when it can be addressed."
    },
    {
        "request": "There’s an issue with {topic}. Could you arrange for a resolution at the earliest convenience?"
    },
    {
        "request": "Could you provide an update on the status of the {topic} request I submitted? Let me know if further input is needed."
    },
    {
        "request": "I need assistance with arranging {topic}. Please provide the details or next steps."
    },
    {
        "request": "Could you confirm the availability of {topic}? I’d like to proceed with scheduling."
    },
    {
        "request": "There’s a concern about {topic} that requires attention. Please share the steps to address it."
    },
    {
        "request": "I’m planning an event that requires {topic}. Could you provide support or necessary arrangements?"
    },
      {
        "request": "Could you schedule maintenance for {topic}? Please let me know the estimated timeline for completion."
    },
    {
        "request": "There seems to be an issue with {topic}. Could you prioritize resolving it and share the expected timeframe?"
    },
    {
        "request": "Can you provide an update on the progress of the {topic} request? Let me know if any further details are needed from my side."
    },
    {
        "request": "I need help coordinating {topic}. Could you share the required steps or confirm the next actions?"
    },
    {
        "request": "Could you confirm if {topic} is available for use? I’d like to finalize my scheduling plans accordingly."
    },
    {
        "request": "There’s an ongoing concern with {topic}. Could you provide recommendations or outline the process to resolve it?"
    },
    {
        "request": "I’m organizing an event and require assistance with {topic}. Please let me know what support is available."
    },
    {
        "request": "Can you assess the condition of {topic} and advise if repairs or replacements are needed? Let me know the next steps."
    },
    {
        "request": "Could you facilitate arrangements for {topic}? This is time-sensitive, so an update on scheduling would be helpful."
    },
    {
        "request": "I’ve noticed a recurring issue with {topic}. Could you investigate and let me know the resolution plan?"
    },
        {
        "request": "Fix {topic}. Need timeline."
    },
    {
        "request": "Issue with {topic}. Resolve as soon as possible."
    },
    {
        "request": "When will {topic} be fixed?"
    },
    {
        "request": "{topic} issue—update?"
    },
    {
        "request": "Maintenance: {topic}"
    },
    {
        "request": "Help with {topic} setup."
    }
]
}



# Category-specific topics
# HR Topics
hr_topics = [
    "payroll", "leave policy", "employee handbook", "job application", "benefits enrollment",
    "401(k) plans", "time-off requests", "performance reviews", "hiring process", "onboarding materials",
    "termination procedures", "training sessions", "health insurance plans", "promotion guidelines", 
    "diversity and inclusion policies", "workplace safety", "employee assistance programs", 
    "compensation structure", "overtime policies", "disciplinary actions",
    "relocation assistance", "retirement planning resources", "employee recognition programs",
    "team-building activities", "conflict resolution support", "equal employment opportunity concerns",
    "mental health resources", "tuition reimbursement programs", "exit interview scheduling",
    "compliance with labor laws", "travel expense policies", "background check procedures",
    "job role reassignments", "annual bonus criteria", "holiday schedules", 
    "guidelines for remote work", "flexible work arrangements", "employee referral programs",
    "internal promotion opportunities", "internship program details", "pay stub discrepancies",
    "mandatory training sessions",  "workforce planning strategies", "employee engagement initiatives", "diversity training sessions", 
    "internal job posting system", "confidential grievance handling", "succession planning resources", 
    "leadership development programs", "access to payroll history", "benefits comparison for new hires", 
    "accommodation requests for disabilities", "parental leave policies", "volunteer time-off programs", 
    "rewards for long-term employees", "performance improvement plans", "attendance tracking tools"
]


# Finance Topics
finance_topics = [
    "budget", "expense reports", "invoice processing", "tax documentation", "financial audits",
    "accounts payable", "accounts receivable", "revenue forecasts", "profit and loss statements", 
    "cost-cutting measures", "investment planning", "annual reports", "vendor payments", 
    "salary disbursements", "cash flow statements", "corporate credit cards", "debt management",
    "fraud prevention", "tax compliance", "financial reporting standards", 
    "forecasting expenses for new projects", "compliance with international financial regulations",
    "currency exchange rate analysis", "employee reimbursement processing", "budget variance analysis",
    "audit preparation checklists", "procurement approvals", "corporate expense policies",
    "investment risk assessments", "revenue recognition compliance", "payroll tax adjustments",
    "emergency funding requests", "cost-benefit analysis for new projects", 
    "capital expenditure approvals", "vendor contract negotiations", "tax credits and deductions",
    "depreciation schedules for assets", "foreign transaction fees", "real-time budget updates",
    "bank reconciliation issues", "travel expense audits", "automating invoicing processes",
    "financial compliance training", "profit margin projections", "subscription service tracking"
]

# IT Support Topics
it_topics = [
    "VPN access", "system update", "password reset", "software installation", "network issues",
    "hardware troubleshooting", "email configuration", "cybersecurity training", "server maintenance", 
    "database backups", "printer setup", "account lockout", "firewall configurations", 
    "device encryption", "antivirus updates", "cloud storage issues", "file recovery", 
    "multi-factor authentication", "application permissions", "IT policy violations",
    "incident response for cybersecurity breaches", "deployment of new software tools",
    "system-wide performance monitoring", "server downtime notifications", 
    "user training for enterprise applications", "technical specifications for hardware upgrades", 
    "data center migrations", "implementation of zero-trust security models", 
    "access provisioning for new hires", "support for legacy systems", "VPN troubleshooting",
    "phishing email reporting", "hardware return and replacement", "data encryption policies",
    "system-wide patch updates", "monitoring bandwidth usage", "storage capacity planning",
    "request for custom software integration", "access to archived emails", 
    "managing software licenses", "device compatibility issues", "firewall exception requests",
    "server access logs", "remote desktop setup", "cyberattack incident response"
]

# Marketing Topics
marketing_topics = [
    "campaign analytics", "content strategy", "social media engagement", "branding guidelines", 
    "email outreach", "market research", "SEO optimization", "lead generation", 
    "press releases", "web traffic analysis", "event planning", "product launch plans", 
    "advertising budgets", "partnership proposals", "influencer marketing", "customer personas", 
    "sales enablement content", "video marketing", "AB testing strategies", "brand voice development",
    "customer retention strategies", "competitor market analysis", "designing customer surveys",
    "ROI tracking for ad campaigns", "preparing marketing collateral", 
    "exploring new target demographics", "brand awareness initiatives", 
    "crisis communication strategies", "setting KPIs for campaigns", "monitoring online reputation",
    "designing banner ads", "keyword research for PPC campaigns", "competitive analysis reports",
    "content for email drip campaigns", "launching retargeting ads", "product placement strategies",
    "customer journey mapping", "localized marketing campaigns", "automating social media posts",
    "trend analysis for viral content", "feedback collection from focus groups", 
    "scripting for video advertisements", "email click-through rate analysis", 
    "seasonal campaign planning", "building affiliate partnerships"
]

# Facilities Topics
facilities_topics = [
    "office lighting repair", "air conditioning maintenance", "desk relocation", "conference room booking",
    "cleaning services", "furniture assembly", "power outage", "HVAC system issues", "security system installation",
    "office renovations", "safety inspections", "pest control", "water dispenser refill", "trash disposal schedule",
    "elevator maintenance", "fire extinguisher servicing", "parking space allocation", "facility access cards",
    "event setup and teardown", "office space reconfiguration",
    "solar panel maintenance", "window repair and cleaning", "landscaping and outdoor maintenance",
    "relocation of office equipment", "ergonomic workspace assessments", "setting up temporary workstations",
    "storage space optimization", "installation of soundproofing", "conference room AV setup",
    "energy efficiency upgrades", "breakroom equipment repair", "flood cleanup support", "emergency evacuation drills",
    "setting up standing desks", "temperature regulation complaints", "recycling bin placement",
    "compliance with fire codes", "coordination of office moves", "workspace noise reduction",
    "parking lot repaving", "emergency generator checks", "air quality assessments", 
    "restroom plumbing issues", "sanitization protocols for shared areas"
]



# Map categories to their specific topics
category_topics = {
    "HR": hr_topics,
    "Finance": finance_topics,
    "IT Support": it_topics,
    "Marketing": marketing_topics,
    "Facilities Management": facilities_topics,
}


# Initialize an empty list to store the data
data = []

# Generate the dataset using a for loop
for category, templates in categories.items():
    topics = category_topics[category]  # Get the topics for the current category
    for template in templates:
        for topic in topics:
            # Format the request with the current topic
            request_text = template["request"].format(topic=topic)
            
            # Append the request and category (label) to the data list
            data.append({"request": request_text, "label": category})

# Convert the list of dictionaries into a DataFrame
df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv("full_dataset.csv", index=False)