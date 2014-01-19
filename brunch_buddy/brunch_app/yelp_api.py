import os
import sys
from yelpapi import YelpAPI
import argparse
import json
from pprint import pprint



class yelp_api():
    """Query Yelp API for possible restaurants"""
    def __init__(self):
        self.consumer_key = os.environ['YELP_CKEY']
        self.consumer_secret = os.environ['YELP_CSECRET']
        self.token = os.environ['YELP_TOKEN']
        self.token_secret = os.environ['YELP_STOKEN']

    def full_query(self, term, limit=5, category='', radius=None, location='washington, dc', sort=0):
        '''A full query that passes back the full JSON response from Yelp. For more information on 
        seacch and response values see http://www.yelp.com/developers/documentation/v2/search_api'''
        # create YelpAPI object
        yelp_api = YelpAPI(self.consumer_key, self.consumer_secret, self.token, self.token_secret)

        category=''
        limit=5
        radius=None
        offset = 0
        response = yelp_api.search_query(term=term, category_filter=category, limit=limit, radius_filter=radius, location=location, sort=sort, offset=offset)
        return response

    def min_query(self, term, limit=5, category='', radius=None, location='washington, dc', sort=0, offset=0):
        '''A minimal query that returns a simple dictionary with the following key values. Every value is a string except for categories, which is a list. 
        The values returned include name, phone, display phone, location, categories, yelp rating, yelp review count, a rating image url, yelp url, and yelp mobile url
        To simplify/minimize location, we return the neighborhood if available, else we return the city.'''
        # create YelpAPI object
        yelp_api = YelpAPI(self.consumer_key, self.consumer_secret, self.token, self.token_secret)

        response = yelp_api.search_query(term=term, category_filter=category, limit=limit, radius_filter=radius, location=location, sort=sort, offset=offset)
        min_response = []
        for entry in response['businesses']:
            if 'neighborhoods' in entry['location'].keys():
                location = entry['location']['neighborhoods'][0]
            elif 'city' in entry['location']:
                location = entry['location']['city']
            else:
                location = 'No neighborhood or city listed :('
            tmp_dict = {'name':entry['name'], 'phone':entry['phone'], 'display_phone':entry['display_phone'], 'location':location, 'categories':entry['categories'], 'rating':entry['rating'], 'review_count':entry['review_count'], 'rating_img_url':entry['rating_img_url'], 'url':entry['url'], 'mobile_url':entry['mobile_url']}
            min_response.append(tmp_dict)
        return min_response        


def main():
    test = yelp_api()
    print 'Test 1:'

    response = test.full_query('Teds')
    print('region center (lat,long): %f,%f\n' % (response['region']['center']['latitude'], response['region']['center']['longitude']))
    print 'total number of responses:', response['total']
    print 'number of returned responses:', len(response['businesses'])
    for entry in response['businesses']:
        print entry['name']
        for key in entry.keys():
            print '\t', key, '\t\t\t\t', entry[key]

    print '\n\nTest 2:'
    response = test.min_query('Teds')
    for entry in response:
        print entry['name']
        for key in entry:
            print '  ', key, '\t\t', entry[key]


if __name__ == "__main__":
    sys.exit(main())