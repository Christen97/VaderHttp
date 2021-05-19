from flask import Flask, request
from Text import Text
from Sentence import Sentence

app = Flask(__name__)


@app.route('/sentiment', methods=['POST'])
def dictionary():
    inputText = request.form.get('text')
    text = Text(inputText)
    text.analyzeSentences()
    text.calculateConfidenceScore()
    text.calculateSentiment()
    sentences = []
    for sentence in text.sentences:
        sentences.append({
            'text': sentence.text,
            'length': sentence.length,
            'offset': sentence.offset,
            'sentiment': text.sentiment,
            'confidenceScores': {
                'positive': round(sentence.confidenceScores.positive, 3),
                'neutral': round(sentence.confidenceScores.neutral, 3),
                'negative': round(sentence.confidenceScores.negative, 3)
            }
        })
    s1 = Sentence(inputText, 0)
    return {
        'text': {
            'confidenceScores': {
                'positive': round(text.confidenceScore.positive, 3),
                'neutral': round(text.confidenceScore.neutral, 3),
                'negative': round(text.confidenceScore.negative, 3),
            },
            'sentences': sentences

        }}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
