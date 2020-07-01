from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

#default parameter is noun
#if you have word that is not a noun, pass pos tag

print(lemmatizer.lemmatize('better', pos='a'))
print(lemmatizer.lemmatize('best', 'a'))
print(lemmatizer.lemmatize('run', 'n'))
print(lemmatizer.lemmatize('run', 'v'))
