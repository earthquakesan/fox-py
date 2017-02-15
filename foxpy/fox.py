import requests
import copy
from urllib.parse import unquote

class Fox(object):
    foxOfficialApiUri = 'http://fox-demo.aksw.org/api'
    #foxOfficialApiUri = 'http://139.18.2.164:4444/api'
    foxMyApiUri = 'http://ivanermilov.aksw.org/fox/api'
    availableNER = [
            'org.aksw.fox.nertools.NERBalie', #0
            'org.aksw.fox.nertools.NERIllinoisExtended', #1
            'org.aksw.fox.nertools.NEROpenNLP', #2 default one
            'org.aksw.fox.nertools.NERStanford', #3
            'OFF' #4
            ]
    NERBalie = 0
    NERIllinoisExtended = 1
    NEROpenNLP = 2
    NERStanford = 3
    NEROff = 4
    defaultFoxParams = {
                'input': 'Leipzig is the capital of the world!',
                'type': 'text', # text | url
                'task': 'NER',
                'output': 'JSON-LD', # JSON-LD | N3 | N-TRIPLE | RDF/{JSON | XML | XML-ABBREV} | TURTLE
                'returnHtml': 'false'#, # true | false
                #'foxlight': availableNER[NEROpenNLP]
            }

    def __init__(self, foxlight=NEROpenNLP):
        """
            foxlight param is for choosing NER method, i.e.
            0 - NERBalie
            1 - NERIllinoisExtended
            2 - NEROpenNLP
            3 - NERStanford
        """
        #self.defaultFoxParams = self._setFoxlight(foxlight)
        pass

    def _setFoxlight(self, foxlight, foxParams=None):
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
        try:
            resp = r.json()
            if (not "input" in resp) or (not "output" in resp):
                # Empty result
                raise ValueError
        except ValueError as e:
            # server failed
            resp = {'input': '', 'output': '', 'log': ''}
        return (unquote(resp['input']),
                unquote(resp['output']),
                unquote(resp['log']))

if __name__ == "__main__":
    fox = Fox()
    (text, output, log) = fox.recognizeText('Country Austria')
    print(output)
