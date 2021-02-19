# Marc F. 
# 02/11/2021
# TypeTest: Test your accuracy and speed at typing!
...
## Import two important libraries
import random
import time

## List of words/phrases differentiated by type.
nouns = ("boy", "car", "cat", "dog", "foot", "frog",  "girl", "gorilla", "monkey", "puppy", "rabbit", "rhinosaurus", "scooter", "truck", "van" )
verbs = ("runs", "hits", "jumps", "barks", "drives", "barfs", "vomits") 
loc = ("down", "up", "towards", "rapidly towards", "rapidly from", "next to")
adv = ("crazily", "dutifully", "foolishly", "merrily", "occasionally")
adj = ("the absolutely adorable", "the spectacularly clueless", "an incredibly dirty", "the extremely odd", "the carelessly stupid", "the wonderfully irrelevant")

## Generate two sentences based off of the random words above, then combine them together.
genSentence1 = [nouns,verbs,loc,adj,nouns,adv]
genSentence2 = [nouns,adv,verbs,loc,adj,nouns]
sentence1 = ' '.join([random.choice(i) for i in genSentence1])
sentence2 = ' '.join([random.choice(i) for i in genSentence2])
text = ("The "+sentence1+". Afterwards, the incredible "+sentence2+".")

## Ask if the user is ready to begin
start = input('Hi! Welcome to Marc\'s Type Test!\n\nAre you ready to see how accurate and fast you are at typing? Hit ENTER to begin!\n\n')

## Print out the text. Begin timing and watching for the user's input.
print(text)
start_time = time.time()

## Collect the user's input and end the timer, calculating total time. Calculate the number of words.
user_text = input()
end_time = time.time()
time_typing = end_time - start_time
user_words = user_text.split(' ')
num_words = len(user_words)

## Calculate words per minute and characters per minute.
wpm = str(round((num_words / time_typing) * 60, 2))
user_chars = list(user_text)
num_chars = len(user_chars)
cpm = str(round((num_chars / time_typing) * 60, 2))

## Calculate the accuracy
text_chars = list(text)
num_text_chars = len(text_chars)
smallest_len = 0
largest_len = 0
if num_chars < num_text_chars:
    smallest_len = num_chars
    largest_len = num_text_chars
else:
    smallest_len = num_text_chars
    largest_len = num_chars
num_correct = 0
for c in range(smallest_len):
  user_c = user_chars[c]
  text_c = user_text[c]
  if user_c == text_c:
    num_correct = num_correct + 1

accuracy = str(round((num_correct / largest_len) * 100,2))

## Display the person's stats.
print("\n\nWell done! You actually kinda did it!\n\nYour Words Per Minute: "+wpm+"\nYour Characters Per Minute: "+cpm+"\nYour Accuracy: "+accuracy+"\n\nThanks for using TypeTest!")