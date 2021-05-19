    # This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press Ctrl+F8 to toggle the breakpoint.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#class ConfidenceScore():
#    negative = float
#    positive = float
#    neutral = float

#class Sentence():
#    text = str
#    length = int
#    offset = int
#    compound = float
#    sentiment = str
#    confidenceScores = ConfidenceScore


#class Text():
#    sentiment = str
#    #sentences = list(Sentence)
#    confidenceScore = ConfidenceScore
from Sentence import Sentence


#def analyzeSentences():
#    sentence = Sentence("hello is it working", 55)
    #fullText = "The Wolf of Wall Street uses animals including a chimpanzee, a lion, a snake, a fish, and dogs.[51] The chimpanzee and the lion were provided by the Big Cat Habitat wildlife sanctuary in Sarasota County, Florida. The four-year-old chimpanzee Chance spent time with actor Leonardo DiCaprio and learned to roller skate over the course of three weeks. The sanctuary also provided a lion named Handsome because the film's trading company used a lion for its symbol.[52] Danny Porush denied that there were any animals in the office, although he admitted to eating an employee's goldfish.[53]"
    #sentences = fullText.split(", ")
    #analyzer = SentimentIntensityAnalyzer()
    #sentiment = analyzer.polarity_scores(sentences[5])
    #print("Text:" + sentences[5])
    #return (sentiment)


#def start():
#    analyzer = SentimentIntensityAnalyzer()
#    sentence = analyzer.polarity_scores("This plant is boring")
#    print(sentence)


# Press the green button in the gutter to run the script.
from Text import Text

if __name__ == '__main__':


    text = Text()
    text.analyzeSentences()
    text.calculateConfidenceScore()
    text.calculateSentiment()
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
