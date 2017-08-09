"""Tests for foxpy.utils"""

from foxpy.fox import Fox
from foxpy.utils import extractNifPhrases, insertCharacterAtPosition

FOX = Fox()

def test_extractEntities():
    json_ld = FOX.recognizeText("Country Austria and George Bush")
    nif_phrases = extractNifPhrases(json_ld)
    assert len(nif_phrases) == 2
    assert nif_phrases[0]["anchorOf"] == "George Bush"

def test_insertCharacterAtPosition():
    _string = "fast fox jump over bla"
    _character = "<entity>"
    _new_string = insertCharacterAtPosition(_string, _character, 4)
    assert _new_string == "fast<entity> fox jump over bla"
