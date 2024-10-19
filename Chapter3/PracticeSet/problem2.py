# name = input("Enter your full name: ")
# date = input("Enter date: ")

# letter = f'''
# Dear <|{name}|>,
# You are selected!
# <|{date}|>'''

# print(letter)


# -----------------------------------

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "Udoy").replace("<|Date|>", "10-08-2024"))