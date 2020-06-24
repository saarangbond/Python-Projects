import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import ne_chunk, pos_tag

text = 'hello world this is a simple test. Mr. Jack and Ms. Jill went up the hill'

sents = sent_tokenize(text)
print(sents)


words = word_tokenize(text)
print(words)
print(nltk.wordpunct_tokenize(text))
print(nltk.pos_tag(words))

def entities(text):
    return ne_chunk(
        pos_tag(
            word_tokenize(text)
        )
    )

tree = entities('New York Gov. Andrew Cuomo, New Jersey Gov. Phil Murphy and Connecticut Gov. Ned Lamont said the travel advisory applies to anyone coming from a state with a transmission rate above 10 per 100,000 people on a seven-day rolling average or 10 percent of the total population testing positive on a seven-day rolling average.')
tree.pprint()
tree.draw()
