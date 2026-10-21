# Building a frequency counter dictionary
text_value = "apple banana apple cherry banana apple"
words_value = text_value.split()

frequency_data = {}
for word_value in words_value:
    frequency_data[word_value] = frequency_data.get(word_value, 0) + 1

print("Word Frequencies:", frequency_data)