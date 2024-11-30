#!/usr/bin/env python
# coding: utf-8

# In[9]:


def luhn_check(card_number):
    card_number = ''.join(filter(str.isdigit, card_number))
    digits = [int(d) for d in card_number[::-1]]
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    total_sum = sum(digits)
    return total_sum % 10 == 0
card_number = "4539 1488 0343 6467"
is_valid = luhn_check(card_number)
print(f"The card number {card_number} is {'valid' if is_valid else 'invalid'}.")


# In[1]:


# remove punctuation
punctuation_marks = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
def remove_punctuations(input_string):
    result = ""
    for char in input_string:
        if char not in punctuation_marks:
            result += char
    return result
user_input = input("Enter a string: ")
print("Original string:", user_input)
result = remove_punctuations(user_input)
print("String without punctuations:", result)


# In[1]:


def bubble_sort(input_string):
    char_list = list(input_string)
    n = len(char_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if char_list[j] > char_list[j + 1]:
                char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]
    return ''.join(char_list)
input = input("Enter a word: ")
sorted_string = bubble_sort(input)
print("Sorted word:", sorted_string)


# In[ ]:





# In[ ]:




