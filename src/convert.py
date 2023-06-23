from spacy.tokens import DocBin
import spacy
import json
from tqdm import tqdm
import random

def load_data(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data

RFQ_TRAIN = load_data("data/labeled_rfqs.json")

print(RFQ_TRAIN)
