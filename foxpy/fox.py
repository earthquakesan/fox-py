import requests
import copy
import urllib

class Fox(object):
    foxOfficialApiUri = 'http://139.18.2.164:4444/api'
    defaultPayload = {
                'input': 'Leipzig is the capital of the world!',
                'type': 'text', # text | url
                'task': 'NER',
                'output': 'TURTLE', # JSONLD | N3 | N-TRIPLE | RDF/{JSON | XML | XML-ABBREV} | TURTLE
                'returnHtml': 'false', # true | false
                'foxlight': 'org.aksw.fox.nertools.NEROpenNLP'
            }

    def __init__(self):
        pass

    def recognizeText(self, text):
        """
            Input: text (any arbitrary string
            Output: recognized entities packed in tuple (input, output, log)
        """
        payload = copy.copy(self.defaultPayload)
        payload['input'] = text
        r = requests.post(self.foxOfficialApiUri, data=payload)
        resp = r.json()
        return (urllib.unquote(resp[0]['input']), 
                urllib.unquote(resp[0]['output']), 
                urllib.unquote(resp[0]['log']))

if __name__ == "__main__":
    fox = Fox()
    (text, output, log) = fox.recognizeText('Leipzig London Berlin Idaho')
