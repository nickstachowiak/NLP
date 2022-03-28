from time import timezone
from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

#print(blob)

sentences = blob.sentences

#print(sentences)

words = blob.words

#print(words)

#print(blob.tags)

#print(blob.noun_phrases)

#print(blob.sentiment) #between -1 and 1
#print(blob.sentiment.polarity)
#print(blob.sentiment.subjectivity)

for sentence in sentences:
    print(round(sentence.sentiment.polarity, 3))

from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)

#spanish = blob.translate(to="es")
#print(spanish)

#chinese = blob.translate(to="zh")
#print(chinese)

#french = blob.translate(to="fr")
#print(french)

#hindi = blob.translate(to="hi")
#print(hindi)

from textblob import Word

index = Word('index')
cacti = Word('cacti')

print(index.pluralize())
print(cacti.singularize())

animals = TextBlob('dog cat fish bird').words
print(animals.pluralize())

#Spell check and correction

word = Word('theyr')

print(word.spellcheck())

print(word.correct())


word1 = Word('studies')
word2 = Word('varieties')

print(word1.stem())
print(word2.stem())

#print(word1.lemmatize())
#print(word2.lemmatize())

# definitions, synonyms, antonyms

happy = Word('happy')

#print(happy.definitions)
#print(happy.synsets)

