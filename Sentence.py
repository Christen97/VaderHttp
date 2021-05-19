from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from ConfidenceScore import ConfidenceScore


class Sentence:
    def __init__(self, text, offset):
        self.text = text.strip()
        self.offset = offset
        self.length = len(text)
        sentimentAnalyzer = SentimentIntensityAnalyzer()
        analyzedText = sentimentAnalyzer.polarity_scores(self.text)
        self.compound = analyzedText['compound']
        self.confidenceScores = ConfidenceScore(analyzedText['pos'], analyzedText['neg'], analyzedText['neu'])
        self.sentiment = ""
        if self.confidenceScores.positive >= 0.4 and self.confidenceScores.negative >= 0.4:
            self.sentiment = "neutral"
        elif self.confidenceScores.neutral >= 0.6:
            self.sentiment = "neutral"
        elif self.confidenceScores.positive >= 0.5 and self.confidenceScores.negative <= 0.2:
            self.sentiment = "positive"
        elif self.confidenceScores.negative >= 0.5 and self.confidenceScores.positive <= 0.2:
            self.sentiment = "negative"