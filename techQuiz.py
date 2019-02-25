import html as html
import random as random

import requests as request
from requests.exceptions import ConnectionError


def print_options(wrong_options, correct_option, index):
    i=1
    if wrong_options == "" and (correct_option == "True" or correct_option == "False"):
        print("--> True\n--> False")
        return
    for option in wrong_options:
        if index == i:
            print("--> " + correct_option)
            i+=1
        print("--> " + option)
        i+=1
    return


URL = "https://opentdb.com/api.php?amount=10&category=18&difficulty=hard"
response = ""

try:
    response = request.get(url=URL).json()
except ConnectionError:
    print("What do u need for cool tech questions? Network Connection? You don't have it")

correct = 0
i = 1
try:
    if response != "":
        for a in response["results"]:
            status = 0
            print("Question " + str(i) + ": " + html.unescape(a["question"]))
            incorrect_answers = html.unescape(a["incorrect_answers"])
            correct_answer = html.unescape(a["correct_answer"])
            print_options(incorrect_answers, correct_answer, random.randint(1, 4))
            your_answer = input("Your Answer: ")
            if your_answer.lower() == correct_answer.lower():
                correct += 1
                status = 1
            if status == 1:
                print("Awesome!! You are correct")
            print("\tCorrect Answer: " + html.unescape(a["correct_answer"]) + "\n\n")
            i += 1
except (KeyboardInterrupt, SystemExit):
    print("Ctrl+c is a bad wat to quit :)")
finally:
    if i < 10:
        print("Winners never quit and quitters never win!! Let's c how u did? ")
    if correct / i == 1:
        print("Awesome!! Pure Tech Blood found!! :D ")
    elif correct / i > 0.7:
        print("Great!! You have skills but not a pure one. :)")
    elif correct / i > 0.5:
        print("Cool!! You have long way to go. Better retry !! :| ")
    elif correct / i > 0.25:
        print("Hi Newbie! Better luck next time!! :(")
    else:
        print("Are u even realated to Computers? I don't think so.. :P ")
