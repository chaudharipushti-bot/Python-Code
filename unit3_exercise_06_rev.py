# 3.6 Word Frequency Counter
import re

text_value = """
Python is an amazing programming language. Python is flexible, clean,
and python syntax is clean and readable.
"""

# Clean and tokenize words
words_value = re.findall(r'\b\w+\b', text_value.lower())

# Count frequency
frequency_data = {}
for word_value in words_value:
    frequency_data[word_value] = frequency_data.get(word_value, 0) + 1

# Sort by frequency (most common first)
sorted_freq_value = sorted(frequency_data.items(), key=lambda item_value: item_value[1], reverse=True)

print(f"{'Word':<15} | {'Frequency':<10}")
print("-" * 28)
for word_value, item_count in sorted_freq_value:
    print(f"{word_value:<15} | {item_count:<10}")