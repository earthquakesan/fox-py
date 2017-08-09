import copy
import urllib.parse

import requests

from foxpy.utils import extractNifPhrases, insertCharacterAtPosition

class Fox(object):
    foxOfficialNERUri = 'http://fox.cs.uni-paderborn.de:4444/call/ner/entities'
    foxOfficialApiUri = 'http://fox.cs.uni-paderborn.de:4444/fox'
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
                'lang': 'en',
                'type': 'text', # text | url
                'task': 'ner',
                'output': 'JSON-LD', # JSON-LD | N3 | N-TRIPLE | RDF/{JSON | XML | XML-ABBREV} |
            }
    defaultFoxHeaders = {
                "charset": "utf-8",
                "Content-Type": "application/json"
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
        r = requests.post(self.foxOfficialApiUri, json=payload, headers=self.defaultFoxHeaders)
        r.raise_for_status()
        try:
            resp = r.json()
        except ValueError as e:
            #server failed
            resp = {}
        return resp

    def annotateEntities(self, text):
        """
            Input: text (string)
                e.g. "Country Austria"
            Output: annotated text (string)
                e.g. "Country <entity>Austria</entity>"
        """
        json_ld = self.recognizeText(text)
        nif_phrases = extractNifPhrases(json_ld)
        if len(nif_phrases) < 1:
            return text

        nif_phrases = sorted(nif_phrases, key=lambda t: t["endIndex"], reverse=True)

        for nif_phrase in nif_phrases:
            text = insertCharacterAtPosition(text, "</entity>", int(nif_phrase["endIndex"]))
            text = insertCharacterAtPosition(text, "<entity>", int(nif_phrase["beginIndex"]))
        return text
