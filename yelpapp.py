from yelpapi import YelpAPI
import pandas as pd

api_key ="hozg-LayZzs2urdoJR_rJpOWWQ8iDNnaEtURht0wP0w-JAM_bdigBpsXm04V3CddmS5E6aO_-h4i3UhkuYySETkINWtLPirwiwq0ILmd-S9uHhDMIlMkvgDCVElMZXYx"

yelp_api_instance = YelpAPI(api_key)
search_term = 'burger'
location_term = 'El Paso, TX'

search_results = yelp_api_instance.search_query(
    term=search_term, location= location_term,
    sort_by='rating', limit = 20
)

# print(search_results)

for business in search_results['businesses']:
    print('\n')
    print(business)



id_for_reviews = 'burger-bros-el-paso'

reviews_response = yelp_api_instance.reviews_query(id= id_for_reviews)

for review in reviews_response['reviews']:
    print("\n")
    print(review)


result_df =  pd.DataFrame.from_dict(search_results['businesses'])
print(result_df)
result_df.to_csv('api_result.csv',index=False)


# for review in data:
#     sen_score = analyzer.poparity_score(review)
#     print(review)
#     print(sen_score)