import flair
import csv
from tqdm import tqdm



flair_sentiment = flair.models.TextClassifier.load('en-sentiment')
row_number = 0

with open("IMDB-Dataset.100.csv", newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='"') 
  # skip column names
  next(reader)
  polarities=dict()
  for row in reader:
    row_number += 1
    # if row_number >= 15:
    #   break
    s = flair.data.Sentence(row[0])
    flair_sentiment.predict(s)
    sentence_score=s.labels[0].score
    for label in s.get_labels():
      print(label.score, label.value)
#     sent=[tok.text for tok in s]
#     for pos in tqdm(range(0, len(s.tokens))):
#       word=s[pos].text
#       substracted=flair.data.Sentence(" ".join(word for word in sent[:pos]+sent[pos+1:]))
#       flair_sentiment.predict(substracted)
#       substracted_score=substracted.labels[0].score
#       delta=sentence_score-substracted_score
#       if word not in polarities:
#         polarities[word]=delta
#       else:
#         polarities[word]=+delta
#       sorted_polarities=dict(sorted(polarities.items(), key=lambda item: item[1]))
# for word, polarity in sorted_polarities.items():
#   print(word, round(polarity,3))