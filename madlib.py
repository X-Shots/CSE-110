print("Please enter a word belonging to the following categories: ")
print()
words = ["adjective", "animal","verb", "exclamation", "verb", "verb", "favorite politician"]

i = 0
for x in words:
    words[i] = input(f"{words[i]}: ")
    i = i + 1

words[6] = (words[6].casefold()).capitalize()
words[3] = (words[3].casefold()).capitalize()


print()
print("your story is:")
print()

print("The other day, I was really in trouble. It all started when I saw a very")
print(f'{words[0]} {words[1]} {words[2]} down the hallway. "{words[3]}!" I yelled. But all')
print(f"I could think to do was to {words[4]} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {words[5]}")
print(f"right in front of {words[6]}. Well how about that {words[6]} mumbled.")