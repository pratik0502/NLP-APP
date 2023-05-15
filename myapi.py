import paralleldots

class Api:

    def __init__(self):
        paralleldots.set_api_key('P7GlwLKlmzFGoCsiF1pwWSzS3ayJwgWsr5nqr2WASN8')

    def sentiment_analysis(self,text):
        responce = paralleldots.sentiment(text)
        return responce

    def ner(self,text):
        responce = paralleldots.ner(text)
        return responce

    def emotion_prediction(self,text):
        responce = paralleldots.emotion(text)
        return responce

