# Day 24: Local Files and Directories
# Main Project: Mail Merge
# From text files with names written and a starting letter with
# a muster text, the exercise is to write a python program that
# reads each of the names from the names_file and writes new
#  personalized file letters with those names.

with open('./input./letters./starting_letter.txt', mode='r') as file:
    text = file.read()

with open('./input./names./invited_names.txt', mode='r') as file:
    names_list = file.readlines()

# with open(f'./output./ReadyToSend./{}', mode='w') as file:
for name in names_list:
    name=name[:-2]
    new_text = text.replace("[name]", name)
    file = open(f'./output./ReadyToSend./{name}_letter.txt', mode='w')
    file.write(new_text)
    file.close()

