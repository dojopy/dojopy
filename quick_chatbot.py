
""" quick chatbot by Dojopy """
import spacy
from textdistance import cosine

def tokenizar(text): #limpieza de texto
    doc = nlp(text.strip())
    doc = [i.lemma_ for i in doc]
    return ' '.join(doc)

training_reponse = {
    tokenizar('comprar zapatos rojos'): 'Hola!, mira estos zapatos rojos: https://myshop.com/zapatos',
    tokenizar('comprar botines verdes'): 'Hola!, mira estos botines verdes: https://myshop.com/botines',
}

def similary_text(text1, text2):
    rate = cosine.normalized_similarity(text1, text2)
    if rate >= 0.6:  # si el umbral es mayor al 60% se considera similar ;)
        return True
    else:
        return False

def quick_chatbot(user_query):
    my_query = tokenizar(user_query)
    for train in training_reponse.keys():
        if similary_text(my_query, train):
            return training_reponse[train]



quick_chatbot('buenos días, hay zapatos rojos?')
#'Hola!, mira estos zapatos rojos: https://myshop.com/zapatos'
