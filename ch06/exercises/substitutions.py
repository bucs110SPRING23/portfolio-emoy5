import json

def main():
    news_ptr = open("news.txt", "r")
    subs_ptr = open("subs.json", "r")

    news = news_ptr.read()
    subs = json.load(subs_ptr)
    print(subs, type(subs))
    subs_ptr.close()

    '''
    
        for str in news:
            if news is in subs:
            


    betternews = open("betternews.txt", "w")

    json.dump(news, betternews)

    '''    
    news_ptr.close()
    #betternews.close()

main()