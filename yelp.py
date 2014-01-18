from yelpapi import YelpAPI
import argparse
import json
from pprint import pprint

argparser = argparse.ArgumentParser(description='Example Yelp queries using yelpy. Visit http://www.yelp.com/developers/manage_api_keys to get the necessary API keys.')
argparser.add_argument('consumer_key', type=str, help='Yelp v2.0 API consumer key')
argparser.add_argument('consumer_secret', type=str, help='Yelp v2.0 API consumer secret')
argparser.add_argument('token', type=str, help='Yelp v2.0 API token')
argparser.add_argument('token_secret', type=str, help='Yelp v2.0 API token secret')
argparser.add_argument('--term', dest='term', type=str, default='', help='Search term (e.g. "food", "restaurants"). If term isn\'t included we search everything.')
argparser.add_argument('--category_filter', dest='category', type=str, default='', help='Category to filter search results with. See the list of supported categories. The category filter can be a list of comma delimited categories.')
argparser.add_argument('--radius', dest='radius', type=int, help='Search radius in meters. If the value is too large, a AREA_TOO_LARGE error may be returned. The max value is 40000 meters (25 miles).')
argparser.add_argument('--limit', dest='limit', type=int, help='Number of business results to return')
args = argparser.parse_args()

yelp_api = YelpAPI(args.consumer_key, args.consumer_secret, args.token, args.token_secret)



"""
        Example search by location text and term. Take a look at http://www.yelp.com/developers/documentation/v2/search_api for
        the various options available.
"""
print('***** Search for brunch places in DC *****\n%s\n' % "yelp_api.search_query(category_filter='breakfast_brunch', location='washington, dc')")
offset = 0
response = yelp_api.search_query(term=args.term, category_filter=args.category, limit=args.limit, radius_filter=args.radius, location='washington, dc', sort=0, offset=offset)
print('region center (lat,long): %f,%f\n' % (response['region']['center']['latitude'], response['region']['center']['longitude']))

# for business in response['businesses']:
#         print('%s\n\tYelp ID: %s\n\trating: %g (%d reviews)\n\taddress: %s' % (business['name'], business['id'], business['rating'], \
#                 business['review_count'], ', '.join(business['location']['display_address'])))

print 'total number of responses:', response['total']
print 'number of returned responses:', len(response['businesses'])



if args.limit is None:
    while offset<response['total']:
        offset += 20
        print 'fetch with offset', offset
        next_response = yelp_api.search_query(term=args.term, category_filter=args.category, limit=args.limit, radius_filter=args.radius, location='washington, dc', sort=0, offset=offset)
        print 'returned', len(next_response['businesses']), 'responses out of', next_response['total']
        response['businesses'].append(next_response['businesses']) 
        print next_response['businesses']
        print 'appending to master list for a total of', len(response['businesses']), 'responses'

print 'expected number:', response['total']
print 'actual number:', len(response['businesses'])

with open("data.json", "w") as outfile:
    json.dump(response, outfile, indent=4)

# i = 1
# for business in response['businesses']:
#     try:
#         location = business["location"]["neighborhoods"][0]
#     except:
#         #print business["location"]
#         location = business["location"]["display_address"][0]
#     print i, " ", business['name'], " - ", location
#     pprint business
#     i += 1
        

print('\n-------------------------------------------------------------------------\n')

