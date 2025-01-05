import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
file_path = r'C:\Users\soulr\OneDrive\Desktop\New folder\true1.csv'  # Assuming you have a dataset for reliable news
true_data = pd.read_csv(file_path)

# Expanded keyword list for reliable news
keywords = [
    # Trustworthy Sources
    "Verified", "Fact-checked", "Official", "Reliable", "Accurate", "Trusted", "Credible",
    
    # Informative Language
    "Report", "Study", "Research", "Analysis", "Data", "Evidence", "Statistics", "Information",
    
    # Neutral Tone
    "Objective", "Unbiased", "Neutral", "Fair", "Balanced", "Impartial", "Reasoned",
    
    # Health-Related
    "Health", "Medicine", "Science", "Doctor", "Expert", "Researcher", "Study", "Clinical",
    
    # Educational Content
    "Learn", "Understand", "Explain", "Teach", "Knowledge", "Insight", "Education"
]

# Initialize a dictionary for keyword counts
keyword_counts = {keyword: 0 for keyword in keywords}

# Count occurrences of each keyword in the 'text' column
for keyword in keywords:
    keyword_counts[keyword] = true_data['text'].str.contains(rf'\b{keyword}\b', case=False, na=False).sum()

# Plot the keyword occurrences
plt.figure(figsize=(14, 7))
bars = plt.bar(keyword_counts.keys(), keyword_counts.values(), color='blue')
plt.xlabel('Keywords', fontsize=14)
plt.ylabel('Occurrences', fontsize=14)
plt.title('Frequency of Common Keywords in Reliable News Articles', fontsize=16)
plt.xticks(rotation=90, fontsize=12)  # Larger x-axis labels

# Annotate the bars with values
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()
