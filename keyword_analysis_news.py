# import matplotlib.pyplot as plt
# import pandas as pd

# # Load the dataset
# file_path = r'C:\Users\soulr\OneDrive\Desktop\New folder\false1.csv'
# false_data = pd.read_csv(file_path)

# # Expanded keyword list
# keywords = [
#     # Political Figures
#     "Trump", "Clinton", "Obama", "Biden", "Putin", "Hillary", "Pelosi",
    
#     # Social Issues
#     "Muslim", "Black", "Police", "Immigrant", "Terrorist", "Refugee", "Crime", "Race", "Equality",
    
#     # Sensational Language
#     "Scandal", "Shocking", "Secret", "Exposed", "Fraud", "Cover-up", "Lies", "Fake", "Truth",
    
#     # Conspiracy Themes
#     "Conspiracy", "Agenda", "Illuminati", "Deep State", "New World Order", "Globalist", "Hoax",
    
#     # Health-Related
#     "Covid", "Vaccine", "Cure", "Cancer", "Disease", "Infection", "Pandemic", "Lockdown",
    
#     # Clickbait Triggers
#     "Unbelievable", "You Won’t Believe", "Breaking", "Revealed", "Must See", "Top Secret", "Urgent"
# ]

# # Initialize a dictionary for keyword counts
# keyword_counts = {keyword: 0 for keyword in keywords}

# # Count occurrences of each keyword in the 'text' column
# for keyword in keywords:
#     keyword_counts[keyword] = false_data['text'].str.contains(rf'\b{keyword}\b', case=False, na=False).sum()

# # Plot the keyword occurrences
# plt.figure(figsize=(16, 8))
# plt.bar(keyword_counts.keys(), keyword_counts.values(), color='purple')
# plt.xlabel('Keywords', fontsize=14)
# plt.ylabel('Occurrences', fontsize=14)
# plt.title('Frequency of Common Keywords in False News Articles', fontsize=16)
# plt.xticks(rotation=90, fontsize=1)
# plt.annotate('Source: Kaggle Fake News Dataset', (0, 0), (0, -40), xycoords='axes fraction', textcoords='offset points', va='top', fontsize=10)
# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
file_path = r'C:\Users\soulr\OneDrive\Desktop\New folder\false1.csv'
false_data = pd.read_csv(file_path)

# Expanded keyword list
keywords = [
    # Political Figures
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
]

# Initialize a dictionary for keyword counts
keyword_counts = {keyword: 0 for keyword in keywords}

# Count occurrences of each keyword in the 'text' column
for keyword in keywords:
    keyword_counts[keyword] = false_data['text'].str.contains(rf'\b{keyword}\b', case=False, na=False).sum()

# Plot the keyword occurrences
plt.figure(figsize=(14, 7))
bars = plt.bar(keyword_counts.keys(), keyword_counts.values(), color='purple')
plt.xlabel('Keywords', fontsize=14)
plt.ylabel('Occurrences', fontsize=14)
plt.title('Frequency of Common Keywords in False News Articles', fontsize=16)
plt.xticks(rotation=90, fontsize=12)  # Larger x-axis labels

# Annotate the bars with values
for bar in bars:
    yval = bar()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()
