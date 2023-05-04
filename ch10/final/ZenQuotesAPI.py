import requests

class ZenQuotesAPI:

    def __init__(self):
        """
        Initializes the Zen Quotes API
        args: quote : str - the quote that it returns
        returns: None
        """
        self.url = f'https://zenquotes.io/api/random'
    
    def __str__(self) -> str:
        """
        By default returns a string
        args: None
        returns: None
        """
        return self.string

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
        
    
    