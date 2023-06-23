"""
Use the model that was previously created
"""
import spacy

nlp = spacy.load("data/custom-models/model-best")

def open_file(input_file):
    "Open a text file"
    with open(input_file, "r", encoding="utf-8") as opened_file:
        open_text = opened_file.read()
    return open_text
text = open_file("data/rfq_dump.txt")

doc = nlp(text)
for ent in doc.ents:
    print (ent.text, ent.label_)
