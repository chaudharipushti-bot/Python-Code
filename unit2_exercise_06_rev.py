# Vowel Counter & Character Frequency

def count_vowels_value(text_value):
    vowel_chars = "aeiouAEIOU"
    item_count = 0

    for current_char in text_value:
    # for char in s(paramter: given input)
        if current_char in vowel_chars:
        #  if char in vowels
            item_count += 1
            # make 0 += 1 increament by 1

    return item_count
    # return given count

# ------------------------- check occurrence of characters
def char_frequency_value(text_value):
    frequency_data = {}
    # empty dictonary

    for current_char in text_value:
    # for char in s(paramter: given input)
        if current_char in frequency_data:
        # if char in looped dictonary
            frequency_data[current_char] += 1
            # If yes, increase its count by 1 
        else:
            frequency_data[current_char] = 1
            # Add the character with an initial count of 1

    return frequency_data


sample_sentence = "momo"

print("Sentence:", sample_sentence)
print("Total Vowels:", count_vowels_value(sample_sentence))
print("Character Frequency:", char_frequency_value(sample_sentence))