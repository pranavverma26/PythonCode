from textblob import TextBlob
import spacy
import text2emotion as te
class API:

    def sentiment_analysis(self, text):

        blob = TextBlob(text)

        polarity = blob.sentiment.polarity

        if polarity > 0:
            return "Positive"
        elif polarity < 0:
            return "Negative"
        else:
            return "Neutral"

    # In Named Entity Recognition (NER), an entity refers to a specific real-world object or concept mentioned in the text that has a clear identity.
    def NER(self,text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        entities = {}
        for ent in doc.ents:
            if ent.label_ not in entities:
                entities[ent.label_] = []
            entities[ent.label_].append(ent.text)
        return entities
    
    def emotion_prediction(self,text):
        emotion = te.get_emotion(text)
        return emotion



        
