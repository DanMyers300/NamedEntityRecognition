import spacy

MODEL_PATH = "data/custom-models/rfq_model"

nlp = spacy.blank("en")
ner = nlp.add_pipe("ner", name='rfq_ner')  # Use `add_pipe` directly

ner.add_label("RFQ")

nlp.to_disk(MODEL_PATH)

