# Day 26: List and Dictionary Comprehensions
# From the attached csv file containing letters and their
# corresponding codes, the goal is to create a python dictionary,
# in which the keys are the letters, and the values, the codes,
# using dictionary comprehension.
# Secondly, it must be created a list of the phonetic code words
# from a word that the use inputs, using list comprehension.

import pandas

csv_file = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row["letter"]: row["code"] for index, row in csv_file.iterrows()}
print(nato_dict)

word = input("Enter a word: ").upper()
code_words = [nato_dict[letter] for letter in word]
print(code_words)


