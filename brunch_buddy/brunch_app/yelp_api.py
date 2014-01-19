import os
from yelpapi import YelpAPI
import argparse
import json
from pprint import pprint



class yelp_api():
    """Query Yelp API for possible restaurants"""
    def __init__(self, term, category, radius, limit):
        self.consumer_key = os.environ['YELP_CKEY']
        self.consumer_secret = os.environ['YELP_CSECRET']
        self.token = os.environ['YELP_TOKEN']
        self.token_secret = os.environ['YELP_STOKEN']

    def query(term, category, limit, location, sort):
        # create YelpAPI object
        yelp_api = YelpAPI(self.consumer_key, self.consumer_secret, self.token, self.token_secret)

        print('***** Search for brunch places in DC *****\n%s\n' % "yelp_api.search_query(category_filter='breakfast_brunch', location='washington, dc')")
        offset = 0
        response = yelp_api.search_query(term=term, category_filter=category, limit=limit, radius_filter=radius, location='washington, dc', sort=0, offset=offset)
        print('region center (lat,long): %f,%f\n' % (response['region']['center']['latitude'], response['region']['center']['longitude']))

        print 'total number of responses:', response['total']
        print 'number of returned responses:', len(response['businesses'])


        pass



if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description='Example Yelp queries using yelpy. Visit http://www.yelp.com/developers/manage_api_keys to get the necessary API keys.')
    # argparser.add_argument('consumer_key', type=str, help='Yelp v2.0 API consumer key')
    # argparser.add_argument('consumer_secret', type=str, help='Yelp v2.0 API consumer secret')
    # argparser.add_argument('token', type=str, help='Yelp v2.0 API token')
    # argparser.add_argument('token_secret', type=str, help='Yelp v2.0 API token secret')
    argparser.add_argument('--term', dest='term', type=str, default='', help='Search term (e.g. "food", "restaurants"). If term isn\'t included we search everything.')
    argparser.add_argument('--category_filter', dest='category', type=str, default='', help='Category to filter search results with. See the list of supported categories. The category filter can be a list of comma delimited categories.')
    argparser.add_argument('--radius', dest='radius', type=int, help='Search radius in meters. If the value is too large, a AREA_TOO_LARGE error may be returned. The max value is 40000 meters (25 miles).')
    argparser.add_argument('--limit', dest='limit', type=int, help='Number of business results to return')
    args = argparser.parse_args()
    term = args.term
    category = args.category
    radius = args.radius
    limit = args.limit

def main():
    print 'in main'
    print term, category, radius, limit
    

    # if args.limit is None:
    #     while offset<response['total']:
    #         offset += 20
    #         print 'fetch with offset', offset
    #         next_response = yelp_api.search_query(term=args.term, category_filter=args.category, limit=args.limit, radius_filter=args.radius, location='washington, dc', sort=0, offset=offset)
    #         print 'returned', len(next_response['businesses']), 'responses out of', next_response['total']
    #         for entry in next_response['businesses']:
    #             response['businesses'].append(entry) 
    #         print 'appending to master list for a total of', len(response['businesses']), 'responses'

    # print 'expected number:', response['total']
    # print 'actual number:', len(response['businesses'])

    # with open("data.json", "w") as outfile:
    #     json.dump(response, outfile, indent=4)

    print('\n-------------------------------------------------------------------------\n')