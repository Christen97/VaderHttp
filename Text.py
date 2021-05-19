from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from ConfidenceScore import ConfidenceScore
from Sentence import Sentence


class Text:
    def __init__(self, text):
        self.text = text
        self.sentences = []
        self.sentiment = ""
        self.confidenceScore = None

    def calculateConfidenceScore(self):
        negative = 0
        positive = 0
        neutral = 0
        for sentence in self.sentences:
            negative += sentence.confidenceScores.negative
            positive += sentence.confidenceScores.positive
            neutral += sentence.confidenceScores.neutral
        negative /= len(self.sentences)
        positive /= len(self.sentences)
        neutral /= len(self.sentences)
        self.confidenceScore = ConfidenceScore(positive, negative, neutral)

    def calculateSentiment(self):
        if self.confidenceScore.positive >= 0.6 and self.confidenceScore.negative <= 0.2:
            self.sentiment = "positive"
        elif self.confidenceScore.negative >= 0.6 and self.confidenceScore.positive <= 0.2:
            self.sentiment = "negative"
        elif self.confidenceScore.neutral >= 0.5:
            self.sentiment = "neutral"
        elif self.confidenceScore.positive >= 0.4 and self.confidenceScore.negative >= 0.4:
            self.sentiment = "mixed"



    def analyzeSentences(self):
        entireText = self.text
        #textTrimmed = entireText.strip()
        splitText = entireText.split(".")
        offset = 0
        for sentence in splitText:
            #sentence.strip()
            values = Sentence(sentence, offset)
            offset += len(sentence)
            self.sentences.append(values)