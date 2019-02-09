#! /bin/python3
#an app to pick a random quote of the day and put it in /Web/index.html file
from requests import get
from json import loads
from random import randint
import os

quotes = loads(get("http://dojodevopschallenge.s3-website-eu-west-1.amazonaws.com/fortune_of_the_day.json").text)

QofDay = quotes[randint(0, len(quotes) - 1 )]

Index = open('/Web/index.html', 'w+')
Index.truncate(0)
Index.write(QofDay["message"])
Index.close()
