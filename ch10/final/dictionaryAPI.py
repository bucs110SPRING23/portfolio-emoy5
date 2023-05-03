import requests

class DictionaryAPI:

    def __init__(self, word):
        self.url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'

    def get(self) -> str:
        """
        Prints the definition of a word
        args: None
        return: quote : str - definition 
        """
        r = requests.get(self.url)
        response = r.json()
        
        
        if response[0]["meanings"] == "":
            return "Definition not found"
        else:
            meanings = response[0]["meanings"]
            definitions = meanings[0]["definitions"]
            definition = definitions[0]["definition"]
            return definition

    