#to use the LLM answering feature, uncomment the lines that run the language model and replace the model_name with your directory
import csv
from fuzzywuzzy import fuzz
#from transformers import AutoModelForQuestionAnswering, AutoTokenizer

# Read data from the CSV file
data = []
with open('SampleASMData.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        identifier, answer = row  # Split the row into identifier and answer
        data.append((identifier, answer))

# Load the language model and tokenizer
# model_name = "Models/Roberta(Squad2)"
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

def find_most_similar_intent(user_input, data):
    most_similar_intent = None
    max_similarity = 0

    for identifier, answer in data:
        similarity = fuzz.partial_ratio(user_input, identifier)
        if similarity > max_similarity:
            most_similar_intent = identifier
            max_similarity = similarity

    return most_similar_intent

# def answer_question(user_question, model, tokenizer):
#     inputs = tokenizer(user_question, return_tensors="pt", padding=True, truncation=True)
#     output = model(**inputs)
#     answer_start = output.start_logits.argmax()
#     answer_end = output.end_logits.argmax()
#     answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end + 1]))
#     return answer

user_input = input("Ask a question: ")

most_similar_intent = find_most_similar_intent(user_input, data)

if most_similar_intent:
    answer = [item[1] for item in data if item[0] == most_similar_intent][0]
    print(f"Answer: {answer}")
else:
    # answer = answer_question(user_input, model, tokenizer)
    print(f"Answer: {answer}")
