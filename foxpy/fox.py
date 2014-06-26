import requests
import copy
import urllib

class Fox(object):
    foxOfficialApiUri = 'http://139.18.2.164:4444/api'
    defaultFoxParams = {
                'input': 'Leipzig is the capital of the world!',
                'type': 'text', # text | url
                'task': 'NER',
                'output': 'TURTLE', # JSONLD | N3 | N-TRIPLE | RDF/{JSON | XML | XML-ABBREV} | TURTLE
                'returnHtml': 'false', # true | false
                'foxlight': 'OFF'
            }
    availableNER = [
            'org.aksw.fox.nertools.NERBalie', #0
            'org.aksw.fox.nertools.NERIllinoisExtended', #1
            'org.aksw.fox.nertools.NEROpenNLP', #2 default one
            'org.aksw.fox.nertools.NERStanford' #3
            ]
    NERBalie = 0
    NERIllinoisExtended = 1
    NEROpenNLP = 2
    NERStanford = 3

    def __init__(self, foxlight=NEROpenNLP):
        """
            foxlight param is for choosing NER method, i.e.
            0 - NERBalie
            1 - NERIllinoisExtended
            2 - NEROpenNLP
            3 - NERStanford
        """
        self.defaultFoxParams = self.setFoxlight(foxlight)

    def setFoxlight(self, foxlight, foxParams=None):
        if(foxParams==None):
            foxParamsNew = copy.copy(self.defaultFoxParams)
        else:
            foxParamsNew = copy.copy(foxParams)
        foxParamsNew['foxlight'] = self.availableNER[foxlight]
        return foxParamsNew

    def recognizeText(self, text):
        """
            Input: text (any arbitrary string
            Output: recognized entities packed in tuple (input, output, log)
        """
        payload = copy.copy(self.defaultFoxParams)
        payload['input'] = text
        r = requests.post(self.foxOfficialApiUri, data=payload)
        resp = r.json()
        return (urllib.unquote(resp[0]['input']), 
                urllib.unquote(resp[0]['output']), 
                urllib.unquote(resp[0]['log']))

if __name__ == "__main__":
    fox = Fox()
    (text, output, log) = fox.recognizeText('Leipzig London Berlin Idaho')
