import json

def main():
    text = open("news.txt", "r").read().lower()
    subs_fptr = open("subs.json", "r")
    subs = json.load(subs_fptr)
    print(subs, type(subs))
    
    for k, v in subs.items():
        text = text.replace(k, v)
        #overrides the text
    
    fptr = open("betternews.txt", "w")
    fptr.write(text)
    fptr.close()
main()