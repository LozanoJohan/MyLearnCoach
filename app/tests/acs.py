import spacy

nlp = spacy.load("es_core_news_sm")
doc = nlp("Me gusta la manzana")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
    print(ent)

    