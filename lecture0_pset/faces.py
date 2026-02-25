# Making Faces - CS50P Problem Set 0
# Prompts user for input and then outputs the same input, replacing each ":)" with "🙂" and each ":(" with "🙁"

text = input()
print(text.replace(":)", "🙂").replace(":(", "🙁"))
