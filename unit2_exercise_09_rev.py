# 3.9 Anagram Checker
# contains exact same words(chars)
# apple
# a p p l e

# pappl
# p a p p l
def is_anagram_value(s1_value, s2_value):
    # Convert both strings to lowercase and remove spaces
    str1_value = s1_value.lower().replace(" ", "")
    str2_value = s2_value.lower().replace(" ", "")
    
    # Sort the characters of both strings and compare them
    return sorted(str1_value) == sorted(str2_value)

pairs_value = [
    ("listen", "silent"),
    ("triangle", "integral"),
    ("apple", "pappl"),
    ("hello", "world")
]
"""
Index 0 → ("listen", "silent")
Index 1 → ("triangle", "integral")
Index 2 → ("apple", "pappl")
Index 3 → ("hello", "world")
"""

for s1_value, s2_value in pairs_value:
# Python goes through each tuple one by one.
    result_value = "Anagrams" if is_anagram_value(s1_value, s2_value) else "Not Anagrams"
    """
    same as:
    if is_anagram(s1, s2):
        result = "Anagrams"
    else:
        result = "Not Anagrams"
    """
    print(f"'{s1_value:<9}' and '{s2_value:<9}' -> {result_value}")
