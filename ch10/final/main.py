from ZenQuotesAPI import ZenQuotesAPI
from dictionaryAPI import DictionaryAPI

def main():
    
    generate_quote = ZenQuotesAPI()
    quote = generate_quote.get()
    words_in_quote = separating_words(quote)
    
    print(quote)
    print("\n")
    print(words_in_quote)

    for word in range(len(words_in_quote)):
        generate_definition = DictionaryAPI(words_in_quote[word])
        definition = generate_definition.get()
        
        print("\n")
        print("'"+words_in_quote[word]+"'" + " is defined as:")
        print(definition)

def separating_words(quote):
    """
    Creates a list of words in the quote before any punctation
    args: quote : str - the quote
    return: words : list - words in the quote before any punctuation
    """
    lowercase = str(quote.lower())

    author_removed = lowercase.split(" -")
    no_author = str(author_removed[0])
        
    period_separated = no_author.split(".")
    first_sent = str(period_separated[0])
    
    comma_split = first_sent.split(", ")
    first_frag = str(comma_split[0])
    
    quote_split = first_frag.split()
    for element in range(len(quote_split)):
        if element == ";":
            quote_split.remove(quote_split[element])
        else:
            None
        return quote_split

main()