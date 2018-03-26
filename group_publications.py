#!/usr/bin/env python3

from api import scholar
import datetime
import csv
import sys

current = datetime.datetime.now().year

if len(sys.argv) < 2:
    print("No list of people Provided")
    exit(1)

people = []
articles = []

with open(sys.argv[1], newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        length = len(row)
        assert(length >= 3)
        for name in range(length-2):
            start = current if row[length-2] == "current" else int(row[length-2])
            end = current if row[length-1] == "current" else int(row[length-1])
            people.append((row[name], start, end))

# print(people)

querier = scholar.ScholarQuerier()
for p in people:
    q = scholar.SearchScholarQuery()
    q.set_words("author:\"" + p[0].replace(" ", "+") + "\"")
    q.set_timeframe(p[1], p[2])

    querier.send_query(q)
    articles += querier.articles

unique_articles = [a for a in articles if a['title'] in {a['title'] for a in articles}]

querier.articles = articles

scholar.csv(querier, header=True, sep=',')

