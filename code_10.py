from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from yelpapi import YelpAPI

api_key ="hozg-LayZzs2urdoJR_rJpOWWQ8iDNnaEtURht0wP0w-JAM_bdigBpsXm04V3CddmS5E6aO_-h4i3UhkuYySETkINWtLPirwiwq0ILmd-S9uHhDMIlMkvgDCVElMZXYx"

yelp_api = YelpAPI(api_key)
s_term = 'Tacos'
analyzer = SentimentIntensityAnalyzer()
loc = 'El Paso, TX'
df = pd.DataFrame()
alias = []
revtext =[]
data = yelp_api.search_query(s_term=s_term,
                             location=loc,
                             limit=20)
for item in data['businesses']:
    review_response = yelp_api.reviews_query(id=item.get('alias'))
    for review in review_response['reviews']:
        alias.append(item.get('alias'))
        revtext.append(review.get('text'))

data = {"Alias":alias,'Review':revtext}
df = pd.DataFrame(pd.DataFrame.from_dict(data))

for review in df['Review']:
    print (review)
    sen_score = analyzer.polarity_scores(review)
    print(sen_score)