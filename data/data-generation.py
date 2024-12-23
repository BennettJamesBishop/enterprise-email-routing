from faker import Faker
import random
import pandas as pd

# Initialize Faker
fake = Faker()

# Define categories and example templates
categories = {
    "HR": [
        {
            "subject": "Request for clarification on {topic}",
            "body": "Hi Team, I’m looking for some information regarding {topic}. Could you provide the necessary details when you get a chance? Thanks, {sender_name}"
        },
        {
            "subject": "Assistance needed for {topic}",
            "body": "Hello, I’d like to request assistance with {topic}. Let me know if there’s anything else you need from me to proceed. Best regards, {sender_name}"
        },
        {
            "subject": "Follow-up on {topic} request",
            "body": "Hi, I wanted to check on the status of my request regarding {topic}. Please let me know if further information is needed. Thanks, {sender_name}"
        },
        {
            "subject": "Question about {topic}",
            "body": "Dear Team, I have a question about {topic}. Could you clarify the process or let me know where I can find more information? Kind regards, {sender_name}"
        },
        {
            "subject": "Update needed on {topic}",
            "body": "Hello Team, Could you provide an update on the {topic} request I submitted earlier? Let me know if I should take any action. Thanks, {sender_name}"
        }
    ],
    "Finance": [
        {
            "subject": "Issue with {topic} report",
            "body": "Hi Finance, I noticed a discrepancy in the {topic} report. Could you review it and confirm the accuracy? Thanks, {sender_name}"
        },
        {
            "subject": "Approval needed for {topic}",
            "body": "Hello, Could you review and approve the {topic} for this month? Let me know if there’s anything I need to address. Best regards, {sender_name}"
        },
        {
            "subject": "Assistance required with {topic}",
            "body": "Dear Team, I need help with {topic}. Please let me know the steps to resolve this issue. Thanks, {sender_name}"
        },
        {
            "subject": "Urgent attention needed for {topic}",
            "body": "Hello Finance, This is a time-sensitive matter related to {topic}. Please prioritize this and let me know if you require additional information. Thank you, {sender_name}"
        },
        {
            "subject": "Follow-up on {topic} approval",
            "body": "Hi Team, I’m following up on the approval status for {topic}. Please let me know if it’s been processed or if further steps are required. Best, {sender_name}"
        }
    ],
    "IT Support": [
        {
            "subject": "Request for {topic} access",
            "body": "Hi Support Team, I need access to {topic} to complete my tasks. Please let me know how to proceed. Thank you, {sender_name}"
        },
        {
            "subject": "Issue with {topic}",
            "body": "Hello IT, I’m experiencing a problem with {topic}. Can you assist in resolving this issue? Thanks, {sender_name}"
        },
        {
            "subject": "Help needed for {topic}",
            "body": "Dear IT Team, I need assistance with {topic}. Please let me know the steps to address this issue. Best regards, {sender_name}"
        },
        {
            "subject": "Access problem with {topic}",
            "body": "Hello Team, I’m unable to access {topic}. Could you help troubleshoot this issue at your earliest convenience? Thank you, {sender_name}"
        },
        {
            "subject": "Follow-up on {topic} access request",
            "body": "Hi Support, I wanted to check on the status of my request for access to {topic}. Let me know if further details are needed. Best, {sender_name}"
        }
    ],
    "Marketing": [
        {
            "subject": "Ideas for {topic} campaign",
            "body": "Hi Marketing Team, I have some ideas for the {topic} campaign. Let me know when we can discuss them. Best, {sender_name}"
        },
        {
            "subject": "Feedback needed on {topic} project",
            "body": "Hello, Could you provide feedback on the {topic} project? I’d like to finalize it this week. Thanks, {sender_name}"
        },
        {
            "subject": "Analysis of {topic}",
            "body": "Dear Marketing Team, Could you analyze the data related to {topic}? Let me know the findings so we can proceed. Best regards, {sender_name}"
        },
        {
            "subject": "Request for proposal on {topic}",
            "body": "Hi Team, Could you draft a proposal for {topic}? Please share it by the end of the week. Thank you, {sender_name}"
        },
        {
            "subject": "Update on {topic} results",
            "body": "Hello Team, Can you provide an update on the results for {topic}? Let me know if you need further input. Thanks, {sender_name}"
        }
    ],
    "Customer Support": [
        {
            "subject": "Customer issue with {topic}",
            "body": "Hi Support Team, A customer has reported an issue with {topic}. Could you investigate and let me know how to resolve it? Thanks, {sender_name}"
        },
        {
            "subject": "Follow-up on {topic} complaint",
            "body": "Hello, I’m following up on the complaint about {topic}. Has there been any progress on resolving this? Thank you, {sender_name}"
        },
        {
            "subject": "Update needed on {topic} query",
            "body": "Dear Team, Could you provide an update on the {topic} query? Let me know if further details are needed. Best, {sender_name}"
        },
        {
            "subject": "Resolution for {topic} issue",
            "body": "Hi Support, Has the issue with {topic} been resolved? Please share an update as soon as possible. Thank you, {sender_name}"
        },
        {
            "subject": "Customer feedback on {topic}",
            "body": "Hello Team, We received feedback regarding {topic}. Please review it and let me know if any action is required. Best regards, {sender_name}"
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
    "compensation structure", "overtime policies", "disciplinary actions"
]

# Finance Topics
finance_topics = [
    "budget", "expense reports", "invoice processing", "tax documentation", "financial audits",
    "accounts payable", "accounts receivable", "revenue forecasts", "profit and loss statements", 
    "cost-cutting measures", "investment planning", "annual reports", "vendor payments", 
    "salary disbursements", "cash flow statements", "corporate credit cards", "debt management",
    "fraud prevention", "tax compliance", "financial reporting standards"
]

# IT Support Topics
it_topics = [
    "VPN access", "system update", "password reset", "software installation", "network issues",
    "hardware troubleshooting", "email configuration", "cybersecurity training", "server maintenance", 
    "database backups", "printer setup", "account lockout", "firewall configurations", 
    "device encryption", "antivirus updates", "cloud storage issues", "file recovery", 
    "multi-factor authentication", "application permissions", "IT policy violations"
]

# Marketing Topics
marketing_topics = [
    "campaign analytics", "content strategy", "social media engagement", "branding guidelines", 
    "email outreach", "market research", "SEO optimization", "lead generation", 
    "press releases", "web traffic analysis", "event planning", "product launch plans", 
    "advertising budgets", "partnership proposals", "influencer marketing", "customer personas", 
    "sales enablement content", "video marketing", "AB testing strategies", "brand voice development"
]

# Customer Support Topics
customer_support_topics = [
    "customer complaint", "service request", "product inquiry", "refund status", 
    "technical troubleshooting", "order delays", "account issues", "billing disputes", 
    "product returns", "warranty claims", "live chat escalations", "follow-up requests", 
    "subscription cancellations", "product replacements", "shipping problems", 
    "feedback surveys", "support ticket updates", "loyalty program questions", 
    "escalation to management", "resolution timeframes"
]


# Map categories to their specific topics
category_topics = {
    "HR": hr_topics,
    "Finance": finance_topics,
    "IT Support": it_topics,
    "Marketing": marketing_topics,
    "Customer Support": customer_support_topics
}

def generate_email_data(num_samples=100):
    data = []
    for _ in range(num_samples):
        category = fake.random_element(list(categories.keys()))
        templates = fake.random_element(categories[category])
        topic = fake.random_element(category_topics[category])  # Use category-specific topics
        sender_name = fake.name()
        
        email = {
            "subject": templates["subject"].format(topic=topic),
            "body": templates["body"].format(topic=topic, sender_name=sender_name),
            "label": category,
        }
        data.append(email)
    return data

# Generate dataset
dataset = generate_email_data(num_samples=100)

# Save to CSV
df = pd.DataFrame(dataset)
df.to_csv("email_classification_dataset.csv", index=False)
print("Dataset created and saved as 'email_classification_dataset.csv'")
