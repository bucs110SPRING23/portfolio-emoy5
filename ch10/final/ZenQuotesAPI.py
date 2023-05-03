import requests

class ZenQuotesAPI:

    def __init__(self):
        self.url = f'https://zenquotes.io/api/random'

    def get(self) -> str:
        """
        Prints a random quote from the Zen Quotes API
        args: None
        return: quote : str - generated random quote 
        """
        r = requests.get(self.url)
        response = r.json()

        quote = (response[0]["q"] + " -" + response[0]["a"])

        return str(quote)
        
    
    