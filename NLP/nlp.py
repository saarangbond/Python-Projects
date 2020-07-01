import nltk
import urllib.request as urlreq
from bs4 import BeautifulSoup as beausoup
from nltk.corpus import stopwords as sw

response = urlreq.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()
soup = beausoup(html, 'html5lib')
text = soup.get_text(strip = True)
tokens = [t for t in text.split()]
sr = sw.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in sw.words('english'):
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)
for key, val in freq.items():
    print(str(key) + ':' + str(val))

freq.plot(20, cumulative=False)
