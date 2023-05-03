import requests

class DictionaryAPI:

    def __init__(self, word):
        """
        Initializes the Zen Quotes API
        args: word : str - the word that is to be defined
        returns: None
        """
        self.url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
        self.string = word

    def __str__(self) -> str:
        """
        By default returns a string
        args: None
        returns: None
        """
        return self.string

    def get(self) -> str:
        """
        Prints the definition of a word
        args: word : str - a word to be defined
        return: definition : str - definition of the word
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

    