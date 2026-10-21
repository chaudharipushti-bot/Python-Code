# 2.5 String Reverse & Palindrome
def reverse_string_value(text_value):
    return text_value[::-1]

def is_palindrome_value(text_value):
    cleaned_s_value = text_value.lower().replace(" ", "")
    return cleaned_s_value == reverse_string_value(cleaned_s_value)

test_strings_value = ["madam", "racecar", "Aarav", "Ahmedabad"]

for renamed_8 in test_strings_value:
    rev_value = reverse_string_value(renamed_8)
    palindrome_flag_value = "Yes" if is_palindrome_value(renamed_8) else "No"
    print(f"String: '{renamed_8}' | Reversed: '{rev_value}' | Palindrome: {palindrome_flag_value}")