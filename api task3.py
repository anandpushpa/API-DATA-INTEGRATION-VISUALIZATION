import nltk
from nltk.chat.util import Chat, reflections
from collections import Counter
import matplotlib.pyplot as plt

nltk.download('punkt')

# Chatbot patterns
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!"]],
    [r"what is your name ?", ["I am an AI Chatbot using NLP."]],
    [r"how are you ?", ["I am fine, thank you!"]],
    [r"what can you do ?", ["I can answer simple questions."]],
    [r"bye|exit", ["Bye! Have a nice day."]],
    [r"(.*)", ["Sorry, I didn't understand that."]]
]

chatbot = Chat(pairs, reflections)

print("🤖 AI Chatbot (type 'exit' to quit)")

user_inputs = []

while True:
    user_input = input("> ")
    if user_input.lower() in ["exit", "bye"]:
        print("Bye! 👋")
        break
    user_inputs.append(user_input)
    print(chatbot.respond(user_input))

# -------- GRAPH PART --------
# Tokenize words
words = []
for sentence in user_inputs:
    words.extend(nltk.word_tokenize(sentence.lower()))

# Count word frequency
word_freq = Counter(words)
common_words = word_freq.most_common(5)

# Separate words and counts
labels = [item[0] for item in common_words]
counts = [item[1] for item in common_words]

# Plot graph
plt.bar(labels, counts)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Most Common User Words in Chatbot")
plt.show()