from transformers import AutoTokenizer, TFAutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = TFAutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "I would like to ride bike after my math class"

ner_results = nlp(example)

for answer in ner_results:
    print(answer['word'])

print(ner_results)
