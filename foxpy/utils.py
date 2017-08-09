"""Utils for foxpy."""

def extractNifPhrases(json_ld):
    if "@graph" in json_ld:
        graph = json_ld["@graph"]
        return list(filter(lambda x: x["@type"] == "nif:Phrase", graph))
    else:
        return []

def insertCharacterAtPosition(string, char, position):
    return string[:position] + char + string[position:]
