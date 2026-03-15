from rouge_score import rouge_scorer
from nltk.translate.meteor_score import meteor_score

def rouge_eval(reference, generated):

    scorer = rouge_scorer.RougeScorer(["rouge1","rouge2","rougeL"], use_stemmer=True)

    return scorer.score(reference, generated)

def meteor_eval(reference, generated):

    return meteor_score([reference], generated)