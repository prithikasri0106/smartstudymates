import spacy

nlp = spacy.load("en_core_web_sm")

def summarize_text(text, sentence_count=5):
    doc = nlp(text)
    sentences = list(doc.sents)
    sorted_sentences = sorted(sentences, key=lambda s: len(s), reverse=True)
    top_sentences = sorted_sentences[:sentence_count]
    summary = " ".join([sent.text.strip() for sent in top_sentences])
    return summary
