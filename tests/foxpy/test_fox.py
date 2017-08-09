"""Tests for fox.py"""

from foxpy.fox import Fox

FOX = Fox()

PARAMS = {
    'input': 'Leipzig is the capital of the world!',
    'foxlight': 'org.aksw.fox.nertools.NERBalie',
    'task': 'ner',
    'output': 'JSON-LD',
    'type': 'text',
    'lang': 'en'
}

def test_setFoxlight():
    new_params = FOX._setFoxlight(0, foxParams=None)
    print(new_params)
    assert new_params == PARAMS

def test_recognizeText():
    json_ld = FOX.recognizeText("country Austria")
    assert "@graph" in json_ld
    assert "@context" in json_ld

def test_annotateEntities():
    test_1 = FOX.annotateEntities("country Austria is not country Australia")
    assert test_1 == "country <entity>Austria</entity> is not country <entity>Australia</entity>"
    test_2 = FOX.annotateEntities("country Austria is not country Australia with George Bush and McDonalds")
    assert test_2 == "country <entity>Austria</entity> is not country <entity>Australia</entity> with <entity>George Bush</entity> and <entity>McDonalds</entity>"
    test_3 = FOX.annotateEntities("Los Angeles country Austria is not Wikipedia country Australia with George Bush and McDonalds")
    assert test_3 == "<entity>Los Angeles</entity> country <entity>Austria</entity> is not <entity>Wikipedia</entity> country <entity>Australia</entity> with <entity>George Bush</entity> and <entity>McDonalds</entity>"

def test_case_london_airport():
    test_string = "1. london heathrow airport {hillingdon|greater london|england|united kingdom} lhr/egll 40239190 NULL 0.8%"
    annotated_string = FOX.annotateEntities(test_string)
    import ipdb; ipdb.set_trace()
