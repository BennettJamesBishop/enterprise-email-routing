import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv("full_dataset.csv")

# Check for missing values and drop them if necessary
df = df.dropna(subset=["request", "label", "topic"])

# Combine 'label' and 'topic' into a single column for stratification
df['stratify_col'] = df['label'] + "__" + df['topic']

# Split the dataset into training and testing sets
train_data, test_data = train_test_split(
    df, test_size=0.2, random_state=42, stratify=df['stratify_col']
)

# Drop the temporary stratification column
train_data = train_data.drop(columns=["stratify_col"])
test_data = test_data.drop(columns=["stratify_col"])

# Print summary of the split
print(f"Train dataset size: {len(train_data)}")
print(f"Test dataset size: {len(test_data)}")
print("Train dataset label counts:")
print(train_data['label'].value_counts())
print("\nTest dataset label counts:")
print(test_data['label'].value_counts())

print("Train dataset topic counts:")
print(train_data['topic'].value_counts())
print("\nTest dataset topic counts:")
print(test_data['topic'].value_counts())

# Drop the topics column, as it is unwanted for training and testing
train_data = train_data.drop(columns=["topic"])
test_data = test_data.drop(columns=["topic"])

# Save the train and test datasets to CSV files
train_data.to_csv("data/train_dataset.csv", index=False)
test_data.to_csv("data/test_dataset.csv", index=False)

