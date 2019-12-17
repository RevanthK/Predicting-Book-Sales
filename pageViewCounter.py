'''
Revanth Korrapolu
December 12, 2019
TODO:
Add columns:

F_tot: Cumulative wiki views of Author
t_F: Longevity of Authors views
f_tot: Normalized AuthCumViews
F_rec: pageviews of author a month before the publication of the book
'''

import pandas as pd
import requests
from mwviews.api import PageviewsClient
import json
import time
import csv


def getWikiPageViewsDeprecated(book_info):
    p = PageviewsClient(user_agent="<person@organization.org> Selfie, Cat, and Dog analysis")

    for ind in range(0, len(book_info)):
        Title = book_info["Title_NY"].tolist()[ind]
        Title = Title.replace(" ", "_")
        print(Title)
        try:
            temp = p.article_views('en.wikipedia', [Title], granularity='monthly', start='20080101',
                                  end='20161231')
            print(temp)
        except Exception:
            print("failed")

def getWikiPageViews(book_info):
    pageViews = {}
    # print(len(book_info))
    for ind in range(0, len(book_info)):
    # for ind in range(0, 50):
        Title = str(book_info["Title_NY"].tolist()[ind])
        Title = Title.title()
        Title = Title.replace(" ", "_")
        TitleNovel = Title + "_(novel)"
        TitleBook = Title + "_(book)"
        Titles = [TitleBook, TitleNovel, Title]

        for title in Titles:
            req = requests.get(
                'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/' + title + '/monthly/20080101/20161231')
            prepared = req.json()
            # prepared = json.dumps(prepared)

            if "title" in prepared and prepared["title"] == "Not found.":
                    continue
            else:
                pageViews[title] = prepared
                break

    with open('DATA/pageview.csv', 'w') as f:
        for key in pageViews.keys():
            f.write("%s,%s\n" % (key, pageViews[key]))


def main():

    book_info = pd.read_csv("DATA/isbnToInfo.csv")

    # 1. Preprocessing - Data Collection + aggregation

    # 1.1 - get WikipageViews
    # start = time.time()
    # print("test")
    # getWikiPageViews(book_info)
    # end = time.time()
    # print(end - start)




if __name__ == "__main__":
    main()




