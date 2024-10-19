words = {
    "ami":"I",
    "tumi":"You",
    "ami jabo":"I will go",
    "nam":"Nmaes",
    "tikana":"Address"
}

user = input("Enter the word you wnat to meaning of: ")

# print(words.get(user)) # it shows `None` if the word not exist in the dictionary

print(words[user]) # it shows `KeyError` if the word not exist in the dictionary