import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
#corpora - body of text
#lexicon - words and their meanings in specific contexts

example_text = 'Hello Mr. Smith, how are you doing today? The weather is great and python is awesome. The sky is pinkish-blue. You should not eat cardboard.'

print(sent_tokenize(example_text))
print()
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)