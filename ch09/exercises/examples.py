""" 
Network Programming

- Building a program that asks trivia questions - getting questions and answers elsewhere

Server: any computer listening for network connections
    - technically all phones and computers themselves are servers

Request: incoming connections that asks for some resource from the server
    - images, videos, music
    - media files
    - text
    - JSON
    - HTML

Types of requests
    - GET: read operation
        - visiting a page, downloading a file
    - PUT: write operation - requires a security
        - login, deleting a file

Headers
    - sent with request and response
        - Status codes
            200: ok, everything works
            400: resource couldn't be delivered
            500: bad code - server
        - IP addresses
        - system information (geolocation)

Using the Request Library

"""

import requests
import random

class TriviaProxyAPI:
    def __init__(self) -> None:
        self.url = "https://opentdb.com/api.php?"
        self.varstr = "amount=2&category=18"

    def get(self):
        url = self.url + self.varstr 
        response = requests.get(url)
        data = response.json()
        return data['results']


def main():
    tp = TriviaProxyAPI()
    #print(response.status_code)
    #print(response.headers)
    #print(response.text)
    results = tp.get()

    for r in results:
        print(r['question'])
        possibles = [r["correct_answer"] + r["incorrect_answers"]]
        random.shuffle(possibles)
        print("Make your selection")
        for i, p in enumerate(possibles):
            print(f"{i}) {p}")

        selection = int(input(": "))
        if possibles[selection] == r["correct_answer"]:
            print("You are correct")
        else:
            print(f"You need to study more. The correct asnwer is: {r['correct_answer']}")

main()

"""
API - Application Programmer's Interface

APIs can return data in any format-> usually in JSON 
- go for ones that don't need authorization

URL Parameters
? and &
    binghamton.edu/cs?
    - anything after ? are variables
        binghamton.edu/cs?var=100
    - mulitple variables
        binghamton.edu/cs?var=100&var2=1000
There's something about changing the quotes for the results file but idk how to do it
"""