spam_message = ["Make a lot of money", "buy now", "subscribe this", "click this"]

user = input("Enter your message: ")

# if (user in spam_message):
#     print("Hands up! This comment is a spam message.")
# else:
#     print("Your message: ", user)


msg1 = "Make a lot of money"
msg2 = "buy now"
msg3 = "subscribe this"
msg4 = "click this"


if ((msg1 in user) or (msg2 in user) or (msg3 in user) or (msg4 in user)):
    print("This comment is a spam message.")
else:
    print("This comment is not a spam message.")