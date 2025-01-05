import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r'C:\Users\soulr\OneDrive\Desktop\New folder\testing_data.csv'
df = pd.read_csv(file_path)

# Define the keywords to search for
keywords = [
    "Trump", "Clinton", "Obama", "Biden", "Putin", "Hillary", "Pelosi",
    # Social Issues
    "Muslim", "Black", "Police", "Immigrant", "Terrorist", "Refugee", "Crime", "Race", "Equality",
    # Sensational Language
    "Scandal", "Shocking", "Secret", "Exposed", "Fraud", "Cover-up", "Lies", "Fake", "Truth",
    # Conspiracy Themes
    "Conspiracy", "Agenda", "Illuminati", "Deep State", "New World Order", "Globalist", "Hoax",
    # Health-Related
    "Covid", "Vaccine", "Cure", "Cancer", "Disease", "Infection", "Pandemic", "Lockdown",
    # Clickbait Triggers
    "Unbelievable", "You Won’t Believe", "Breaking", "Revealed", "Must See", "Top Secret", "Urgent"
]  # Add your keywords here

# Initialize a dictionary to store keyword occurrences
keyword_counts = {keyword: 0 for keyword in keywords}

# Count occurrences of each keyword in the text column
for text in df['text']:
    for keyword in keywords:
        if keyword in text:
            keyword_counts[keyword] += 1

# Filter out keywords with zero occurrences
keyword_counts = {k: v for k, v in keyword_counts.items() if v > 0}

# Plot the number of occurrences of each keyword
plt.figure(figsize=(10, 5))
bars = plt.bar(keyword_counts.keys(), keyword_counts.values())
plt.xlabel('Keywords')
plt.ylabel('Number of Occurrences')
plt.title('Keyword Occurrences in Text Column')
plt.xticks(rotation=90, ha='center')

# Add annotations
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, int(yval), ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Filter and plot text values with label column value of 1
label_1_texts = df[df['label'] == 1]['text']

label_1_keyword_counts = {keyword: 0 for keyword in keywords}
for text in label_1_texts:
    for keyword in keywords:
        if keyword in text:
            label_1_keyword_counts[keyword] += 1

# Filter out keywords with zero occurrences for label 1 texts
label_1_keyword_counts = {k: v for k, v in label_1_keyword_counts.items() if v > 0}

plt.figure(figsize=(10, 5))
bars = plt.bar(label_1_keyword_counts.keys(), label_1_keyword_counts.values())
plt.xlabel('Keywords')
plt.ylabel('Number of Occurrences')
plt.title('Keyword Occurrences in Tweets with misinformative label')
plt.xticks(rotation=90, ha='center')

# Add annotations
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, int(yval), ha='center', va='bottom')
plt.annotate('Source: HuggingFace Tweets Dataset', (0, 0), (0, -40), xycoords='axes fraction', textcoords='offset points', va='top', fontsize=10)
plt.tight_layout()
plt.show()
