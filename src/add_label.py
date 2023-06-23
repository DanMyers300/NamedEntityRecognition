import spacy

MODEL_PATH = "data/custom-models/rfq_model"

nlp = spacy.blank("en")
ner = nlp.add_pipe("ner", name='rfq_ner')

ner.add_label("RFQ")

print(nlp.pipe_names)

# nlp.to_disk(MODEL_PATH)

