from transformers import pipeline



if __name__ == '__main__':
    # Initialize a sentiment-analysis pipeline
    sentiment_analyzer = pipeline("sentiment-analysis")

    # Analyze sentiment of text
    result = sentiment_analyzer("")
    print(result)  # Output will show whether the sentiment is positive or negative, with a confidence score
