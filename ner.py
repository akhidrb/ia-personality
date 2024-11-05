from transformers import pipeline


if __name__ == '__main__':
    ner_pipeline = pipeline("ner", grouped_entities=True)
    text = "Apple is looking at buying U.K. startup for $1 billion"
    entities = ner_pipeline(text)
    print(entities)
