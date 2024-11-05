from transformers import pipeline


if __name__ == '__main__':


    classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

    text = "This movie was excellent!"
    classification = classifier(text)
    print(classification)
