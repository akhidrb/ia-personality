from transformers import pipeline


if __name__ == '__main__':

    qa_pipeline = pipeline("question-answering")

    context = "Kobe, Jordan, and Lebron are one of the best basketball players in the NBA"
    question = "Who is the best basketball player in the NBA ?"

    answer = qa_pipeline(question=question, context=context)
    print(answer)

